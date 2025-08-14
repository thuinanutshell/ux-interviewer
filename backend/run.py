from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO
from api.services.auth.routes import auth_bp
from api.services.product.routes import product_bp 
from api.services.interview.routes import interview_bp
from api.services.analytics.routes import analytics_bp
from api.services.ai_integration.routes import ai_integration_bp
from api.services.invitation.routes import invitation_bp
from api.extensions import db, jwt, oauth
from api.models.users import User
from config import Config
import os
from dotenv import load_dotenv
from api.utils.email import EmailService
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Create a single SocketIO instance
socketio = SocketIO(
    cors_allowed_origins="*",
    async_mode='threading',
    logger=True,
    engineio_logger=True,
    ping_timeout=60,
    ping_interval=25
)

def configure_websocket(app):
    """Configure WebSocket error handlers and event listeners"""
    
    @socketio.on_error()
    def error_handler(e):
        logger.error(f"WebSocket error: {str(e)}")
        
    @socketio.on_error_default
    def default_error_handler(e):
        logger.error(f"WebSocket default error: {str(e)}")
        
    @socketio.on('connect')
    def handle_connect():
        logger.info("Client connected to WebSocket")
        
    @socketio.on('disconnect')
    def handle_disconnect():
        logger.info("Client disconnected from WebSocket")

def create_app(config_class=Config):
    """Create and configure the Flask application with WebSocket support"""
    app = Flask(__name__,
        template_folder='api/templates',
        static_folder='api/static'
    )
    
    # Load configuration
    app.config.from_object(config_class)
    
    # Ensure secret key is set
    if not app.config.get('SECRET_KEY'):
        raise ValueError("No SECRET_KEY set for Flask application")
    
    # Initialize extensions with enhanced error handling
    try:
        CORS(app, resources={r"/*": {"origins": "*"}})
        db.init_app(app)
        jwt.init_app(app)
        socketio.init_app(app, message_queue='redis://')
        
        # Configure WebSocket
        configure_websocket(app)
        
        # Configure OAuth with Google
        oauth.init_app(app)
        oauth.register(
            name='google',
            client_id=os.getenv('GOOGLE_CLIENT_ID'),
            client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
            server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
            client_kwargs={
                'scope': 'openid email profile',
                'prompt': 'select_account'
            }
        )
    except Exception as e:
        logger.error(f"Error initializing extensions: {str(e)}")
        raise
    
    # Register blueprints with error handling
    try:
        app.register_blueprint(auth_bp, url_prefix='/auth')
        app.register_blueprint(product_bp, url_prefix='/product')
        app.register_blueprint(interview_bp, url_prefix='/interview')
        app.register_blueprint(analytics_bp, url_prefix='/analytics')
        app.register_blueprint(ai_integration_bp, url_prefix='/ai_integration')
        app.register_blueprint(invitation_bp, url_prefix='/invitation')
    except Exception as e:
        logger.error(f"Error registering blueprints: {str(e)}")
        raise
    
    # Add root route
    @app.route('/')
    def home():
        return render_template('index.html')
    
    # Initialize email service
    try:
        app.email_service = EmailService(app)
    except Exception as e:
        logger.error(f"Error initializing email service: {str(e)}")
        raise
    
    return app

def initialize_database(app):
    """Initialize database with proper error handling"""
    with app.app_context():
        try:
            db.create_all()
            logger.info("Database tables created successfully!")
        except Exception as e:
            logger.error(f"Error creating database tables: {str(e)}")
            raise

# Application initialization
app = create_app()

if __name__ == '__main__':
    try:
        # Initialize database
        initialize_database(app)
        
        # Start the application with SocketIO support
        socketio.run(
            app,
            host='0.0.0.0',
            port=int(os.getenv('PORT', 5001)),
            debug=True,
            allow_unsafe_werkzeug=True,  # Only for development
            use_reloader=True
        )
    except Exception as e:
        logger.error(f"Application startup error: {str(e)}")
        raise