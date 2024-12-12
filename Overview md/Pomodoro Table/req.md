# Pomodoro Session Table

## PomodoroSession:

### Fields:

- **id**: UUID
- **task**: ForeignKey (Task)
- **start_time**: datetime
- **end_time**: datetime
- **duration**: integer (minutes)

### API Endpoints:

#### Pomodoro Sessions

1. **Start Pomodoro Session**

   - **Endpoint**: `POST /api/pomodoro/start/`
   - **Input**: `{ task_id as param}`
   - **Background Action**:
     - Create `session_id`
     - Set `start_time` to current date & time
     - Add entry to database
   - **Output**:
     ```json
     {
       "session_id": "UUID",
       "start_time": "datetime"
     }
     ```

2. **Stop Pomodoro Session**
   - **Endpoint**: `POST /api/pomodoro/stop/<session_id>/`
     - **backgrund Action** : Take session_id as inpt param
   - **Output**:
     ```json
     {
       "success": true,
       "duration": "integer (minutes)"
     }
     ```
