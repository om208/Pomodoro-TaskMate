# Task Management API Documentation

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
        "id": "0fd82fd3-7d73-40cf-9bb3-6d2b672e378c",
        "title": "Complete project documentation",
        "description": "Finish writing the documentation for the project by the end of the week.",
        "initial_deadline": "2023-10-20T17:00:00Z",
        "deadline": "2023-10-20T17:00:00Z",
        "priority": "medium",
        "estimated_time": 5,
        "remainder_sound": "/reminder-sound/Task/bell1",
        "status": "pending",
        "Reminder_duration": 30,
        "created_on": "2024-12-11T09:39:03.870948Z",
        "completed_on": null,
        "user": "3f766ccc-af76-4c90-aa15-3a663309693d"
      }
    ]
  }
  ```

### 2. POST /api/tasks/add/

- **Description**: Adds a new task to the database.
- **Input**:
  ```json
  {
    "user": "3f766ccc-af76-4c90-aa15-3a663309693d",
    "title": "Complete project documentation",
    "description": "Finish writing the documentation for the project by the end of the week.",
    "initial_deadline": null,
    "deadline": "2023-10-20T17:00:00Z",
    "priority": "medium",
    "estimated_time": 5,
    "remainder_sound": "/reminder-sound/Task/bell1",
    "status": "pending",
    "Reminder_duration": 30,
    "completed_on": null
  }
  ```
- **Output**:

  ```json
  {
    "success": true,
    "task_id": "0fd82fd3-7d73-40cf-9bb3-6d2b672e378c",
    "task": {
      "id": "0fd82fd3-7d73-40cf-9bb3-6d2b672e378c",
      "title": "Complete project documentation",
      "description": "Finish writing the documentation for the project by the end of the week.",
      "initial_deadline": "2023-10-20T17:00:00Z",
      "deadline": "2023-10-20T17:00:00Z",
      "priority": "medium",
      "estimated_time": 5,
      "remainder_sound": "/reminder-sound/Task/bell1",
      "status": "pending",
      "Reminder_duration": 30,
      "created_on": "2024-12-11T09:39:03.870948Z",
      "completed_on": null,
      "user": "3f766ccc-af76-4c90-aa15-3a663309693d"
    }
  }
  ```

### 3. PUT /api/tasks/edit/?userId=<task_id>/

- **Description**: Updates an existing task.
- **Input**:

```json
{
  "id": "0fd82fd3-7d73-40cf-9bb3-6d2b672e378c",
  "title": "Complete project+++",
  "description": "Finish writing the documentation for the project by the end of the week.+++",
  "initial_deadline": "2023-12-20T17:00:00Z",
  "deadline": "2023-12-20T17:00:00Z",
  "priority": "high",
  "estimated_time": 120,
  "remainder_sound": "/reminder-sound/Task/bell2",
  "status": "done",
  "Reminder_duration": 120,
  "created_on": "2024-12-11T09:39:03.870948Z",
  "completed_on": "2024-12-11T09:39:03.870948Z",
  "user": "3f766ccc-af76-4c90-aa15-3a663309693d"
}
```

- **Output**:
  ```json
  {
    "success": true
  }
  ```

### 4. DELETE /api/tasks/delete/?userId=<task_id>/

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
