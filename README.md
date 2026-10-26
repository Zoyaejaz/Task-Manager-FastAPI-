# Task Management System | FastAPI

A backend-only Task Management System built using **FastAPI and Python**, featuring user registration, authentication, authorization, task CRUD operations, and automated email confirmation. The application provides RESTful APIs for managing users and their tasks securely.

## 🚀 Features

### 👤 User Management
- **User Registration:** Register new users with validated information.
- **Email Confirmation:** Automatically send a registration confirmation email after user registration.
- **Authentication:** Authenticate users before granting access to protected endpoints.
- **Authorization:** Restrict access to resources based on user permissions.
- **Account Deletion:** Allow users to delete their registered accounts.

### ✅ Task Management
- **Create Tasks:** Add new tasks.
- **Retrieve Tasks:** Fetch task details.
- **Update Tasks:** Modify existing tasks.
- **Delete Tasks:** Remove tasks when they are no longer required.
- **User-Specific Access:** Allow users to manage their own tasks according to authorization rules.

### 🧪 API Testing
- **Postman:** Tested API endpoints using Postman to validate request handling, responses, and application functionality.
- **Swagger UI:** Explore and interact with API endpoints through FastAPI's automatically generated documentation.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API development |
| Pydantic | Data validation |
| FastAPI-Mail | Email notifications |
| SMTP | Email delivery |
| Uvicorn | ASGI server |
| Postman | API testing |
| Git & GitHub | Version control |

## ⚡ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Zoyaejaz/Task-Manager-FastAPI-.git
cd "Task Management System"
```



### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and configure the email credentials required by your application.

Example for Gmail SMTP:

```env
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
```

Use a Gmail App Password if you use Gmail SMTP. Never commit your `.env` file or credentials to GitHub.

### 5. Run the Application

If your FastAPI instance is named `app` in `src/main.py`, run:

```bash
uvicorn src.main:app --reload
```

The development server will be available at:

`http://127.0.0.1:8000`

### 6. Explore the API Documentation

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## 🔄 Application Workflow

1. A user registers through the registration API.
2. The backend validates the submitted data and creates the user account.
3. A registration confirmation email is sent through the configured email service.
4. The user authenticates to access protected endpoints.
5. Authorized users create, retrieve, update, and delete their tasks.
6. Users can delete their accounts through the account-management API.

## 🔐 Security Considerations

- Validate incoming request data.
- Protect private endpoints with authentication.
- Enforce authorization checks for user-specific resources.
- Store sensitive credentials in environment variables.
- Avoid exposing passwords, tokens, and other secrets in source control.

## 🧪 Testing

The APIs have been tested using **Postman** to verify endpoint behavior and responses.

Key test scenarios include:

- User registration and input validation.
- Registration confirmation email functionality.
- Authentication and access to protected endpoints.
- Creating, retrieving, updating, and deleting tasks.
- Authorization checks for user-specific resources.
- Account deletion.

FastAPI's Swagger UI can also be used to explore and test the available endpoints.

## 🔮 Future Improvements

- Add automated unit and integration tests.
- Introduce task priorities, deadlines, and status tracking.
- Implement pagination, filtering, and sorting.
- Improve logging and error handling.
- Containerize the application using Docker.
- Deploy the API to a cloud platform.
- Develop a frontend for interacting with the backend.

## 👩‍💻 Author

**Zoya Ejaz**

GitHub: [@Zoyaejaz](https://github.com/Zoyaejaz)

---

If you find this project useful, consider giving the repository a ⭐.
