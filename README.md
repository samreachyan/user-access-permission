# Dev Stream API

A best-practice FastAPI project with PostgreSQL, JWT authentication, role-based access (admin, manager, user), and multi-language API responses (en/km/vn).

## Project Structure
```
dev-stream-api/
│
├── app/
│   ├── main.py                # FastAPI app entrypoint
│   ├── core/                  # Core config, security, messages
│   ├── db/                    # Database base and session
│   ├── models/                # SQLAlchemy models (User, etc.)
│   ├── schemas/               # Pydantic schemas (request/response)
│   ├── api/                   # API routers, dependencies
│   │   └── v1/                # Versioned API endpoints
│   ├── services/              # Business logic/services
│   └── utils/                 # Utilities (response formatting, etc.)
│
├── requirements.txt
├── docker-compose.yml
├── README.md
└── .env
```

## Prerequisites
- Python 3.8+
- Docker & Docker Compose

## Setup & Running
1. **Clone the repository:**
    ```sh
    git clone <your-repo-url>
    cd dev-stream-api
    ```
2. **Start PostgreSQL with Docker Compose:**
    ```sh
    docker-compose up -d
    ```
3. **Create and activate a virtual environment:**
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```
4. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
5. **Run the FastAPI application:**
    ```sh
    uvicorn app.main:app --reload
    ```
    The API will be available at: http://127.0.0.1:8000

## API Endpoints & Access Control
- **/api/v1/auth/register**: Register a new user (choose role: admin, manager, user)
- **/api/v1/auth/login**: Login and get JWT token
- **/api/v1/users/admin-only**: Admin access only
- **/api/v1/users/manager-or-admin**: Manager or Admin access
- **/api/v1/users/user-access**: Any authenticated user

All endpoints return responses in a consistent format:
```json
{
  "success": true,
  "message": "...",
  "data": { ... },
  "error_code": null
}
```

## Multi-language Support
- API responses support English (en), Khmer (km), Vietnamese (vn)
- Set the `Accept-Language` header in your requests:
    - `Accept-Language: en` (default)
    - `Accept-Language: km`
    - `Accept-Language: vn`

## Interactive API Docs
Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.

---
For production, use Alembic for migrations and update `.env` for secure secrets.
