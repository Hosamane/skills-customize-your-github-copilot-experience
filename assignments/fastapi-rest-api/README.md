# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple, well-structured REST API using the FastAPI framework. Students will create endpoints, define request/response models, validate input, and explore automatic API docs.

## 📝 Tasks

### 🛠️ Project Setup & Hello World

#### Description
Install FastAPI and an ASGI server, scaffold a minimal application, and run a basic endpoint that returns a greeting.

#### Requirements
Completed project should:

- Use `fastapi` and `uvicorn` (or another ASGI server) in a minimal app
- Expose a `GET /` endpoint that returns a JSON greeting like `{ "message": "Hello, FastAPI!" }`
- Include brief run instructions (commands) in the README

Example run commands:

```
pip install fastapi uvicorn
uvicorn main:app --reload
```


### 🛠️ CRUD Endpoints for a Resource

#### Description
Implement Create, Read, Update, and Delete endpoints for a simple resource (e.g., `Item` with `id`, `name`, `description`, `price`).

#### Requirements
Completed project should:

- Implement endpoints: `GET /items`, `GET /items/{id}`, `POST /items`, `PUT /items/{id}`, `DELETE /items/{id}`
- Use an in-memory store (list or dict) for data persistence during runtime
- Return appropriate HTTP status codes (201 for create, 404 for not found, etc.)
- Include sample `curl` or `HTTP` requests and expected responses for each endpoint

Example `POST /items` request/response:

```
POST /items
{
  "name": "Notebook",
  "description": "A ruled notebook",
  "price": 4.99
}

Response 201
{
  "id": 1,
  "name": "Notebook",
  "description": "A ruled notebook",
  "price": 4.99
}
```


### 🛠️ Data Validation & Pydantic Models

#### Description
Use Pydantic models to declare request and response schemas, and validate incoming data.

#### Requirements
Completed project should:

- Define Pydantic `BaseModel` classes for requests and responses
- Validate required fields and types (e.g., `price` must be a positive number)
- Demonstrate handling of invalid input with proper error responses


### 🛠️ API Docs and Basic Testing

#### Description
Explore FastAPI's automatic documentation (Swagger UI and Redoc) and add a few tests or manual checks to verify endpoints.

#### Requirements
Completed project should:

- Confirm interactive docs are available at `/docs` (Swagger) or `/redoc`
- Provide at least two example tests or `curl` checks that validate core functionality (e.g., create and retrieve an item)
- Include brief notes on how to run tests or perform the checks

---

Optional extensions (not required but encouraged):

- Add query parameters for filtering or pagination on `GET /items`
- Persist data to a lightweight database (SQLite) using `databases` or `SQLModel`
- Add authentication for protected endpoints
