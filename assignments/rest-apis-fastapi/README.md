# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using the FastAPI framework. You'll create endpoints that handle HTTP requests and return JSON responses, understanding the fundamentals of web API development.

## 📝 Tasks

### 🛠️ Create Your First API Endpoints

#### Description
Set up a basic FastAPI application with simple GET endpoints that return static data.

#### Requirements
Completed program should:

- Import and initialize FastAPI
- Create a root endpoint (`/`) that returns a welcome message in JSON format
- Create a `/students` endpoint that returns a list of students with their names and grades
- Run the server using `uvicorn` and test the endpoints locally
- Example response for `/students`:
  ```json
  [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"}
  ]
  ```

### 🛠️ Add Dynamic Endpoints with Path Parameters

#### Description
Create endpoints that accept dynamic parameters from the URL path to return specific data.

#### Requirements
Completed program should:

- Add a `/students/{student_id}` endpoint that retrieves a specific student by ID
- Return the student's details including name, grade, and ID
- Handle cases where a student ID doesn't exist (return an appropriate error message)
- Example response for `/students/1`:
  ```json
  {"id": 1, "name": "Alice", "grade": "A"}
  ```

### 🛠️ Implement POST Endpoint to Create Data

#### Description
Create an endpoint that accepts POST requests with JSON data to add new students.

#### Requirements
Completed program should:

- Define a request model using Pydantic to specify the structure of incoming data
- Create a POST `/students` endpoint that accepts a student object with name and grade
- Add the new student to the student list and return the created student with an assigned ID
- Return appropriate HTTP status codes (201 for created, 400 for invalid data)
- Example request body:
  ```json
  {"name": "Charlie", "grade": "A"}
  ```
