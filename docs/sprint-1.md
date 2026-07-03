# Sprint 1 Review: User authentication

## Sprint Goal

Build the first user authentication system for AI Cryto Copilot.
By the end of Sprint 1, the backend can register users, log users in, create access tokens, and return the current authenticated user.

## Completed Tasks

### 1. Project Configuration

I moved the API metadata into "backend/core/config.py"
The project now has shared configuration values such as:
- 'APP_NAME'
- 'API_VERSION'
- 'API_DESCRIPTION'
- 'DATABASE_URL'
- 'SECRET_KEY'
- 'ALGORITHM'
- 'ACCESS_TOKEN_EXPIRE_MINUTES'
This makes backend easier to maintain because important settings are stored in one place.

### 2. Database Setup

I added SQLAlchemy and database session management.
The backend now has:
- 'backend/db/session.py'
- 'backend/db/base.py'
- 'backend/db/init_db.py'
- 'ai_crypto_copilot.db'
For local development, the project uses SQLite as a simple database.
I also added '*.db' to '.gitignore' so local database files will not be uploaded to GitHub.

### 3. User Model

I created the first database model for users.
The user model is stored in:
- 'backend/models/user.py'
The 'User' model includes:
- 'id'
- 'email'
- 'hashed_password'
- 'is_active'

### 4. Auth Schemas

I added Pydantic schemas for authentication requests and responses.
The auth schemas are stored in:
- 'backend/schemas/auth.py'
The project now has:
- 'UserCreate'
- 'UserLogin'
- 'Token'
These schemas define the data shape for registration, login, and token responses.

### 5. Password Security

I added password hashing utilities in:
- 'backend/core/security.py'
The project uses Passlib and bcrypt to hash and verify passwords.
The backend now has:
- 'get_password_hash()'
- 'verify_password()'
This means the project does not store plain text password in the database.

Problem I encounterd:
I saw a bcrypt-related error during password hashing. The password I tested was short, but the installed bcrypt version caused compatibility issues with Passlib.
Then I fixed it by installing a compatible bcrypt version and updating 'requirements.txt'.

### 6. Authentication Endpoints

I built the first authentication API endpoints.
The project now has:
- 'POST /auth/register'
- 'POST /auth/login'
- 'GET /auth/me'
'/auth/register' creates a new user.
'/auth/login' checks the user's email and password, then returns and access token.
'/auth/me' uses the access token to return the current authenticated user.

### 7. JWT Access Token

I added JWT sccess token support.
After a successful login, the backend creates an access token with the user's email stored in 'sub' field.
The project has:
- 'create_access_token()'
- 'decode_access_token()'
The access token is used to sccess protected API endpoints such as 'GET /auth/me'.

## Testing

I tested the authentication flow with FastAPI Swagger UI and curl.
I verified that:
- A new user and register successfully.
- Registering a same email again returns a '400 Bad Request'.
- A user can log in with the correct email and password.
- Logging in with a wrong credentials returns a '401 Unauthorized'.
- The login endpoint returns an access token.
- 'GET /auth/me' returns the current user when the valid token is provided.
- 'GET /auth/me' returns '401 Unauthorized' when no token or an invalid token is provided.

## Problems I Encountered

### 1. Bcrypt Compatibility Issues

When I tested password hashing, I met a bcrypt-related error that the password was short but the installed bcrypt version was not compatible with Passlib.
I fixed this issue by installing a compatible bcrypt version and updating 'requirements.txt'.

### 2. Swagger 0Auth2 Authorization Issues
There's a 'Authorize' form in Swagger UI when I tested the protected endpoint.
The Swagger 'Authorize' form is designed for 0Auth2 password flow but my current '/auth/login' endpoint uses a JSON request body.
So I tested the protected endpoint with curl by sending the token in the 'Authorization' header.

### 3. Invalid Token Issue

When I tested 'GET /auth/me' with an old sccess token the backend returned 'Invalid token'.
That's means a token must match the current 'SECURITY_KEY' and token format.
After logging in again and using a refresh token, 'GET /auth/me' returned the current user successfully.

## What I Learned

### 1. Authentication and Authorization

Authentication means verifying who the user is.
Authorization means deciding what the user is allowed to access.
In this sprint, login is the authentication step, and 'GET /auth/me' is a protect endpoint that requires authorization.

### 2. Password Hashing

Password hashing protects user password and instead of storing plain text passwords, the backend stores hashed passwords.
During login, the backend verifies the input password against the stored password hash.

### 3. Database Models and Schemas

A database model describes how data is stored in the database and a schema describes the data shape used by API requests and responses.
In this sprint, the 'User' model represents the 'users' table while 'UserCreate', 'UserLogin' and 'Token' define the API data shape.

### 4.Dependency Injection

FastAPI dependency injection lets and dempoint receive shared resources sutomatically.
In this sprint, I used dependencied to provide a database session and the current authenticated user.
The 'get_db()' dependency opens a database session, yeilds it to the endpoint, and closes it after the request is finished.

### 5. JWT Access Tokens

A JWT access token is a signed token used to prove user identity.
The backend creates a token after login and stores the user's email in the 'sub' field.
Protected endpoint can decode the token, find the user and return user-specific data.

## Commands I Practiced

'''bash
python -m backend.db.init_db
uvicorn backend.main:app --reload
git status
git add .
git commit -m "..."
git push

## English Notes

authentication: verifying who the user is
authorization: deciding what the user can access
credentials: login information such as email and password
endpoint: an API address
schema: the data shape for requests and responses
dependency: something a function needs in order to work
token: a digital access pass
protected endpoint: and API endpoint that requires authentication
invalid token: a token that cannot be trusted or decoded
compatibility issue: a problem caused by two tools not working well together

## Sprint 1 Result

By the end of Sprint 1, the backend has a working user authentication foundation
The project can now:
- Register a new user
- Store hashed passwords
- Log in with email and password
- Generate JWT access tokens
- Decode JWT access tokens
- Protect an API endpoint
- Return the current authenticated user

This sprint turned the project from a basic FastAPI backend into the first version of a real user system
