# Task-Management-Pomodoro API Documentation

## User Management

### 1. Create a User
- **URL**: `/api/users/`
- **Method**: `POST`
- **Headers**: `Content-Type: application/json`
- **Body**:
    ```json
    {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword"
    }
    ```

### 2. Get User Details
- **URL**: `/api/users/{id}`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer {token}`

### 3. Update User
- **URL**: `/api/users/{id}`
- **Method**: `PUT`
- **Headers**: `Content-Type: application/json`, `Authorization: Bearer {token}`
- **Body**:
    ```json
    {
        "username": "updateduser",
        "email": "updateduser@example.com"
    }
    ```

### 4. Delete User
- **URL**: `/api/users/{id}`
- **Method**: `DELETE`
- **Headers**: `Authorization: Bearer {token}`

## Task Management

### 1. Create a Task
- **URL**: `/api/tasks/`
- **Method**: `POST`
- **Headers**: `Content-Type: application/json`, `Authorization: Bearer {token}`
- **Body**:
    ```json
    {
        "title": "New Task",
        "description": "Task description",
        "due_date": "2023-12-31T23:59:59Z"
    }
    ```

### 2. Get Task Details
- **URL**: `/api/tasks/{id}`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer {token}`

### 3. Update Task
- **URL**: `/api/tasks/{id}`
- **Method**: `PUT`
- **Headers**: `Content-Type: application/json`, `Authorization: Bearer {token}`
- **Body**:
    ```json
    {
        "title": "Updated Task",
        "description": "Updated description",
        "due_date": "2023-12-31T23:59:59Z"
    }
    ```

### 4. Delete Task
- **URL**: `/api/tasks/{id}`
- **Method**: `DELETE`
- **Headers**: `Authorization: Bearer {token}`

## Pomodoro Management

### 1. Start Pomodoro
- **URL**: `/api/pomodoro/start`
- **Method**: `POST`
- **Headers**: `Content-Type: application/json`, `Authorization: Bearer {token}`
- **Body**:
    ```json
    {
        "task_id": "{task_id}"
    }
    ```

### 2. Stop Pomodoro
- **URL**: `/api/pomodoro/stop`
- **Method**: `POST`
- **Headers**: `Content-Type: application/json`, `Authorization: Bearer {token}`
- **Body**:
    ```json
    {
        "task_id": "{task_id}"
    }
    ```

### 3. Get Pomodoro Status
- **URL**: `/api/pomodoro/status`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer {token}`