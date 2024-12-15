
#### Documentation

Update 

README.md

:

```markdown
# Task Management API

## API Endpoints

### 1. GET /api/tasks/?userId=<USER_ID>

- **Description**: Retrieves a list of all tasks for a specific user.
- **Input**:
  - **userId** (Query Parameter): The ID of the user whose tasks are to be fetched.
- **Output**:
  ```json
  {
    "tasks": [
      {
        "id": "UUID",
        "title": "string",
        "description": "text",
        "deadline": "datetime",
        "priority": "enum (high/medium/low)",
        "status": "enum (working/done/pending)"
      }
    ]
  }
  ```

### 2. POST /api/tasks/add/

- **Description**: Adds a new task to the database.
- **Input**:
  ```json
  {
    "userId": "UUID",
    "title": "string",
    "description": "text",
    "deadline": "datetime",
    "priority": "enum (high/medium/low)",
    "estimated_time": "integer",
    "remainder_sound": "string",
    "Reminder_duration": "integer"
  }
  ```
- **Output**:
  ```json
  {
    "success": true,
    "task_id": "UUID"
  }
  ```

### 3. PUT /api/tasks/edit/<task_id>/

- **Description**: Updates an existing task.
- **Input**:
  ```json
  {
    "title": "string",
    "description": "text",
    "deadline": "datetime",
    "priority": "enum (high/medium/low)",
    "status": "enum (working/done/pending)",
    "remainder_sound": "string",
    "Reminder_duration": "integer"
  }
  ```
- **Output**:
  ```json
  {
    "success": true
  }
  ```

### 4. DELETE /api/tasks/delete/<task_id>/

- **Description**: Deletes a task.
- **Output**:
  ```json
  {
    "success": true
  }
  ```

## Edge Cases

- **Invalid User ID**: If the user ID provided does not exist, the API will return a 404 error.
- **Missing Fields**: If required fields are missing in the request, the API will return a 400 error with details of the missing fields.
- **Invalid Data Types**: If the data types of the fields are incorrect, the API will return a 400 error with details of the invalid fields.

## Examples

### Create Task

**Input**:
```json
{
  "userId": "123e4567-e89b-12d3-a456-426614174000",
  "title": "New Task",
  "description": "Task Description",
  "deadline": "2023-12-31T23:59:59Z",
  "priority": "medium",
  "estimated_time": 60,
  "remainder_sound": "/reminder-sound/Task/bell1",
  "Reminder_duration": 30
}
```

**Output**:
```json
{
  "success": true,
  "task_id": "123e4567-e89b-12d3-a456-426614174001"
}
```
```

This plan and code should cover the requirements specified.