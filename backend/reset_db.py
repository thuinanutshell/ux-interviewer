# backend/reset_db.py

from flask import Flask
from api import create_app
from api.extensions import db
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def reset_database():
    """
    Performs a complete reset of the database environment by:
    1. Removing the existing instance folder and its contents
    2. Creating a fresh database with the current schema
    3. Ensuring all necessary directories exist
    """
    logger.info("Starting fresh database setup...")
    
    app = create_app()
    
    with app.app_context():
        try:
            # Remove the entire instance directory if it exists
            if os.path.exists('instance'):
                import shutil
                shutil.rmtree('instance')
                logger.info("✓ Removed existing instance directory")
            
            # Create a new instance directory
            os.makedirs('instance')
            logger.info("✓ Created fresh instance directory")
            
            # Create all database tables based on current models
            db.create_all()
            logger.info("✓ Created new database with current schema")
            
            logger.info("\nDatabase setup completed successfully!")
            logger.info("You can now start your application with a fresh database.")
            
        except Exception as e:
            logger.error(f"\n❌ Error during database setup: {str(e)}")
            raise

if __name__ == "__main__":
    reset_database()