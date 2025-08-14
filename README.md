# AI Interview Platform Backend

A Flask-based backend service that powers an AI-driven interview platform. This system facilitates automated interviews, user management, and AI-powered analytics. [Demo Video](https://www.loom.com/share/fe7175954d924d62be659587a5b3cf27?sid=6c6ec4b7-d65e-4195-894f-db882ca1d56f)

Deployed app: https://ai-interview.replit.app/

## Features

- **Authentication System**
  - User registration and login
  - OAuth integration with Google
  - Password reset functionality
  - JWT-based authentication

- **Interview Management**
  - Create and manage interview sessions
  - Real-time interview interactions using WebSocket
  - AI-powered response analysis
  - Follow-up question generation

- **Product Management**
  - Product creation and management
  - Category organization
  - Product-specific interview customization

- **Invitation System**
  - Generate and manage interview invitations
  - Track participant responses
  - Automated email notifications

- **Analytics**
  - Interview response analysis
  - AI-powered insights

- **AI Integration**
  - Google Gemini Pro integration
  - Real-time response processing
  - Dynamic conversation handling

## Technical Stack

- **Framework**: Flask 3.1.0
- **Database**: SQLAlchemy with Flask-SQLAlchemy
- **Authentication**: Flask-JWT-Extended
- **Real-time Communication**: Flask-SocketIO
- **Documentation**: Swagger/OpenAPI
- **Email Service**: SendGrid
- **AI Models**: Google Gemini Pro

## Project Structure

```
backend/
├── api/                   # Main application package
│   ├── models/            # Database models
│   ├── services/          # Business logic and routes
│   ├── templates/         # HTML templates
│   ├── static/            # Static files
│   └── utils/             # Utility functions
├── migrations/            # Database migrations
├── tests/                 # Test suite
└── config.py              # Configuration settings
```
```
backend/
├── api/
│   ├── models/
│   │   ├── agent/
│   │   │   ├── __init__.py
│   │   │   └── conversation.py
│   │   ├── interviews/
│   │   │   ├── __init__.py
│   │   │   ├── interview.py
│   │   │   ├── participant.py
│   │   │   └── question.py
│   │   ├── invitations/
│   │   │   ├── __init__.py
│   │   │   └── invitation.py
│   │   ├── products/
│   │   │   ├── __init__.py
│   │   │   └── product.py
│   │   ├── responses/
│   │   │   ├── __init__.py
│   │   │   └── response.py
│   │   ├── users/
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   ├── __init__.py
│   │   └── base.py
│   ├── services/
│   │   ├── ai_integration/
│   │   │   ├── __init__.py
│   │   │   ├── logic.py
│   │   │   ├── routes.py
│   │   │   ├── schemas.py
│   │   │   └── websocket.py
│   │   ├── analytics/
│   │   │   ├── __init__.py
│   │   │   ├── logic.py
│   │   │   ├── routes.py
│   │   │   └── schemas.py
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   ├── logic.py
│   │   │   ├── routes.py
│   │   │   └── schemas.py
│   │   ├── interview/
│   │   │   ├── __init__.py
│   │   │   ├── logic.py
│   │   │   ├── routes.py
│   │   │   └── schemas.py
│   │   ├── invitation/
│   │   │   ├── __init__.py
│   │   │   ├── logic.py
│   │   │   ├── routes.py
│   │   │   └── schemas.py
│   │   └── product/
│   │       ├── __init__.py
│   │       ├── logic.py
│   │       ├── routes.py
│   │       └── schemas.py
│   ├── static/
│   │   └── swagger.yaml
│   ├── templates/
│   │   ├── auth/
│   │   │   ├── forgot_password.html
│   │   │   ├── login.html
│   │   │   ├── profile.html
│   │   │   ├── register.html
│   │   │   └── reset_password.html
│   │   ├── interview/
│   │   │   ├── participate.html
│   │   │   ├── portal.html
│   │   │   ├── questions.html
│   │   │   └── responses.html
│   │   ├── invitation/
│   │   │   └── manage.html
│   │   ├── product/
│   │   │   ├── create.html
│   │   │   ├── edit.html
│   │   │   └── portal.html
│   │   ├── base.html
│   │   └── index.html
│   ├── utils/
│   │   ├── __init__.py
│   │   └── email.py
│   ├── __init__.py
│   ├── errors.py
│   └── extensions.py
├── migrations/
├── tests/
├── .env
├── .gitignore
├── README.md
├── config.py
├── requirements.txt
├── reset_db.py
└── run.py
```
## Setup and Installation

1. Clone the repo
```python
git clone https://github.com/minerva-university/cs162-ai-interviewer
cd cs162-ai-interviewer/backend
```

2. Create and activate a virtual environment (recommended)
```python
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables in `.env`:
```env
DATABASE_URI=sqlite:///app.db
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret
JWT_REFRESH_SECRET_KEY=your-jwt-refresh-secret-key
SENDGRID_API_KEY=your-sendgrid-key
SENDER_EMAIL=your-email-you-set-up-with-sendgrid-api
SUPPORT_EMAIL=support-email
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GEMINI_API_KEY=your-gemini-api-key
```
You can run the file `generate_keys.py` in the scripts folder to generate the secret keys for JWT. To generate the API keys for Google Authentication, Sendgrid, and Gemini, please follow these official tutorials:
- [Google OAuth 2.0](https://support.google.com/googleapi/answer/6158849?hl=en)
- [SendGrid Gmail Sending](https://sendgrid.com/en-us/solutions/email-api)
- [Gemini API](https://ai.google.dev/gemini-api/docs/api-key)

5. Initialize the database:
```bash
python reset_db.py
```

6. Run the application:
```bash
python run.py
```

## API Documentation

The API documentation is available at `/docs` endpoint using Swagger UI. Key endpoints include:

- `/auth/*` - Authentication endpoints
- `/interview/*` - Interview management
- `/product/*` - Product management
- `/invitation/*` - Invitation handling
- `/analytics/*` - Analytics and reporting
- `/ai_integration/*` - AI interaction endpoints

## Error Handling

The application implements comprehensive error handling with:
- Custom error classes
- Standardized error responses
- Detailed logging
- Transaction management

## WebSocket Integration

Real-time features are implemented using Flask-SocketIO:
- Connection management
- Error handling
- Event broadcasting
- Client synchronization

## Security Features

- JWT-based authentication
- Password hashing
- CORS protection
- OAuth 2.0 integration
- Rate limiting
- Input validation

## Database Models

- User: Authentication and profile management
- Interview: Interview session management
- Product: Product information storage
- Invitation: Interview invitation tracking
- Conversation: AI interaction history
- Response: Interview response storage

## Testing

The backend system is designed with robust testing:

**1. Model Testing**
- Validates the behavior of all database models.
- Includes tests for field constraints, default values, relationships, and utility methods.

**2. Service Testing**
- Covers business logic implemented in the services/ package.
- Tests the functionality of services such as interview creation, question management, response analysis, and AI-powered features.

**3. Template Testing**
- Ensures HTML templates render properly with the expected content.
- Includes both static elements and dynamic content based on session states and data.

**4. API Testing**
- Tests all RESTful API endpoints for correctness, including authentication, interview management, product handling, and invitation generation.
- Verifies status codes, response structures, and error handling.

**5. WebSocket Testing**
- Covers real-time features such as connection handling and message synchronization using Flask-SocketIO.
- Ensures WebSocket events like connect, disconnect, and user_response are handled without errors and trigger appropriate server-side actions.

**6. Error Handling Testing**
- Validates custom error classes and ensures standardized responses are returned for common issues like invalid input, authentication failures, and missing resources.

## Testing Setup

To run the tests:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Error Codes

Common error codes returned by the API:
- `AUTH_ERROR`: Authentication-related errors
- `INVALID_REQUEST`: Invalid input data
- `NOT_FOUND`: Resource not found
- `INTERACTION_ERROR`: AI interaction failures
- `CONFIG_ERROR`: Configuration issues

## Future Plans
Implement the frontend using React to follow the industry standards and improve loading time by loading only components instead of the whole page.
