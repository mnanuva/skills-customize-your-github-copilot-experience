from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# Initialize the FastAPI application
app = FastAPI()

# Define a Pydantic model for student data
class Student(BaseModel):
    name: str
    grade: str

# Sample data: list of students
students = [
    {"id": 1, "name": "Alice", "grade": "A"},
    {"id": 2, "name": "Bob", "grade": "B"},
    {"id": 3, "name": "Diana", "grade": "A"}
]

# Task 1: Create your first API endpoints
# TODO: Implement a root endpoint "/" that returns a welcome message

# TODO: Implement a "/students" GET endpoint that returns the list of students


# Task 2: Add dynamic endpoints with path parameters
# TODO: Implement a "/students/{student_id}" GET endpoint to retrieve a specific student


# Task 3: Implement POST endpoint to create data
# TODO: Implement a POST "/students" endpoint that accepts a Student object


if __name__ == "__main__":
    # Run the server with: uvicorn starter-code:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)
