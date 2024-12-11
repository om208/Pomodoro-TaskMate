### **Task Table**

#### **Fields**:

- **id**: `UUID`
- **user**: `ForeignKey (User)`
- **title**: `string`
- **description**: `text`
- **initial_deadline**: `datetime`
- **deadline**: `datetime`
- **priority**: `enum (high/medium/low)` (default: **medium**)
- **estimated_time**: `integer`
- **remainder_sound**: `string` (default: **"/reminder-sound/Task/bell1"**)
- **status**: `enum (working/done/pending)` (default: **pending**)
- **Reminder_duration**: `integer` (default: **30**)
  - _(Note: This is in minutes)_
- **created_on**: `datetime`
- **completed_on**: `datetime` _(nullable)_

---

### **API Endpoints**

#### **1. GET /api/tasks/?userId=<USER_ID>**

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

---

#### **2. POST /api/tasks/add/**

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
- **Action**:
  - Assign `initial_deadline = deadline`.
  - Assign `created_on = current date and time`.
  - Add all parameters to the **Task** table.
- **Output**:
  ```json
  {
    "success": true,
    "task_id": "UUID"
  }
  ```

---

#### **3. PUT /api/tasks/edit/<task_id>/**

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

---

#### **4. DELETE /api/tasks/delete/<task_id>/**

- **Description**: Deletes a task.
- **Output**:
  ```json
  {
    "success": true
  }
  ```
