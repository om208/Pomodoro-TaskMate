# Settings API

## Endpoints

### 1. Get Settings

**Endpoint**: `GET /api/settings/?userId=<userId>`

**Description**: This endpoint retrieves the settings for a specific user.

**Input**:

- `userId` (UUID): The ID of the user whose settings are being retrieved.

**Output**:

- `goal` (string): The goal of the user.
- `alarm_tune` (string): The alarm tune for the user.

**Example Request**:

```
GET /api/settings/?userId=1
```

**Example Response**:

```json
{
  "goal": "Data Engineering",
  "alarm_tune": "Morning Tune"
}
```

**Error Responses**:

- If the settings are not found:
  ```json
  {
    "error": "Settings not found"
  }
  ```

### 2. Update Settings

**Endpoint**: `PUT /api/settings/update/`

**Description**: This endpoint updates the settings for a specific user.

**Input**:

- `user` (UUID): The ID of the user whose settings are being updated.
- `goal` (string): The new goal of the user.
- `alarm_tune` (string): The new alarm tune for the user.
- `progress_status` (enum): The new progress status of the user. Possible values are `not_started`, `in_progress`, `completed`.

**Output**:

- `success` (boolean): Indicates whether the settings were successfully updated.

**Example Request**:

```json
{
  "userId": "1",
  "goal": "Software Development",
  "alarm_tune": "Evening Tune",
  "progress_status": "in_progress"
}
```

**Example Response**:

```json
{
  "success": true
}
```

**Error Responses**:

- If the settings are not found:
  ```json
  {
    "error": "Settings not found"
  }
  ```

### 3. Get Progress Status

**Endpoint**: `GET /api/settings/progress_status/?userId=<userId>`

**Description**: This endpoint retrieves the progress status for a specific user.

**Input**:

- `userId` (UUID): The ID of the user whose progress status is being retrieved.

**Output**:

- `progress_status` (enum): The progress status of the user. Possible values are `not_started`, `in_progress`, `completed`.

**Example Request**:

```
GET /api/settings/progress_status/?userId=1
```

**Example Response**:

```json
{
  "progress_status": "in_progress"
}
```

**Error Responses**:

- If the settings are not found:
  ```json
  {
    "error": "Settings not found"
  }
  ```

### 4. Create User Settings

**Endpoint**: `POST /api/settings/add/`

**Description**: This endpoint allows you to create a new user settings entry.

**Input**:

- `user` (UUID): The ID of the user for whom the settings are being created.
- `goal` (string): The goal of the user. Default is "Data Engineering".
- `alarm_tune` (string): The alarm tune for the user.
- `progress_status` (enum): The progress status of the user. Possible values are `not_started`, `in_progress`, `completed`.

**Output**:

- `success` (boolean): Indicates whether the settings were successfully created.
- `settings` (object): The created settings object, containing:
  - `user` (UUID): The ID of the user.
  - `goal` (string): The goal of the user.
  - `alarm_tune` (string): The alarm tune for the user.
  - `progress_status` (enum): The progress status of the user.

**Example Request**:

```json
{
  "user": "1",
  "goal": "Software Development",
  "alarm_tune": "Evening Tune",
  "progress_status": "in_progress"
}
```

**Example Response**:

```json
{
  "success": true,
  "settings": {
    "user": "1",
    "goal": "Software Development",
    "alarm_tune": "Evening Tune",
    "progress_status": "in_progress"
  }
}
```

**Error Responses**:

- If the user ID does not exist:
  ```json
  {
    "error": "User not found"
  }
  ```

**Edge Cases**:

1. **Invalid User ID**: If the `userId` does not exist, the API will return a 404 error with the message "User not found".
2. **Missing Parameters**: If required parameters are missing, the API will return a 400 error.
3. **Invalid Data**: If the data provided does not match the expected format, the API will return a 400 error.

This documentation should help you understand how to use the provided endpoints for managing user settings.
