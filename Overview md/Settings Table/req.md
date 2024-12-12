# Settings Table

## Settings:

### Fields:

- **user**: ForeignKey (User)
- **goal**: string (default: "Data Engineering")
- **alarm_tune**: string
- **progress_status**: enum

### API Endpoints:

#### Settings

1. **Get Settings**

   - **Endpoint**: `GET /api/settings/?userId=<userId>`
   - **Input**: Provide `userId` as a query parameter.
   - **Output**:
     ```json
     {
       "goal": "string",
       "alarm_tune": "string"
     }
     ```

2. **Update Settings**

   - **Endpoint**: `PUT /api/settings/update/`
   - **Input**:
     ```json
     {
       "userId": "UUID",
       "goal": "string",
       "alarm_tune": "string"
     }
     ```
   - **Output**:
     ```json
     {
       "success": true
     }
     ```

3. **Get Progress Status**
   - **Endpoint**: `GET /api/settings/progress_status/?userId=<userId>`
   - **Input**: Provide `userId` as a query parameter.
   - **Output**:
     ```json
     {
       "progress_status": "enum"
     }
     ```
