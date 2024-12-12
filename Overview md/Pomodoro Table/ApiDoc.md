# Pomodoro Session API

## Endpoints

### Start Pomodoro Session

- **Endpoint**: `POST /api/pomodoro/start/`
- **Input**: `{ "task_id": "UUID" }`
- **Output**:
  ```json
  {
    "session_id": "UUID",
    "start_time": "datetime"
  }
  ```

### Stop Pomodoro Session

- **Endpoint**: `POST /api/pomodoro/stop/<session_id>/`
- **Input**: `{ "session_id": "session_id" }`
- **Output**:
  ```json
  {
    "success": true,
    "duration": "integer (minutes)"
  }
  ```

## Edge Cases

1. **Invalid Task ID**: If the `task_id` provided does not exist, the API will return a 404 error.
2. **Invalid Session ID**: If the `session_id` provided does not exist, the API will return a 404 error.
3. **Session Already Stopped**: If the session is already stopped, the API will return the existing duration.

## Example

### Start Pomodoro Session

**Request**:

```json
{
  "task_id": "0fd82fd3-7d73-40cf-9bb3-6d2b672e378c"
}
```

**Response**:

```json
{
  "session_id": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p",
  "start_time": "2023-10-15T10:00:00Z"
}
```

### Stop Pomodoro Session

**Request**:

```json
{
  "session_id": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p"
}
```

**Response**:

```json
{
  "success": true,
  "duration": 25
}
```
