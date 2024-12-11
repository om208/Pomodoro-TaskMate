# Web Application Design Document

## Overview
The application is a Pomodoro timer-based task management system with a React >=18 frontend, Django backend, and SQLite3 database. It includes user authentication (via email/password, Google, and GitHub), task management, analytics, and Pomodoro cycles.

## Structure and Components

### Frontend (React >=18)
**Directory Structure:**
```markdown
src/
├── components/
│   ├── Auth/
│   │   ├── SignIn.jsx
│   │   ├── SignUp.jsx
│   │   └── OAuth.jsx
│   ├── TaskManagement/
│   │   ├── TaskList.jsx
│   │   ├── TaskDetails.jsx
│   │   └── AddTaskForm.jsx
│   ├── Pomodoro/
│   │   ├── Timer.jsx
│   │   ├── ReminderPopup.jsx
│   │   └── ActiveTimer.jsx
│   ├── Settings/
│   │   └── Settings.jsx
│   ├── Analytics/
│   │   └── ProductivityChart.jsx
│   └── Layout/
│       ├── Header.jsx
│       ├── Sidebar.jsx
│       └── Footer.jsx
├── contexts/
│   └── AppContext.jsx
├── redux/
│   ├── actions/
│   ├── reducers/
│   └── store.js
├── utils/
│   ├── api.js
│   ├── validators.js
│   └── helpers.js
└── App.js
```

### Backend (Django)
**Directory Structure:**
```markdown
backend/
├── app/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── tasks.py
│   ├── settings.py
│   ├── tests.py
│   └── utils.py
├── auth/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── tests.py
│   └── utils.py
└── manage.py
```

**Frontend Components**
1. **Auth Components**:
    - **SignIn**: Handles email/password, Google, and GitHub login.
    - **SignUp**: Allows user registration.
    - **OAuth**: Manages third-party authentication.

2. **Task Management Components**:
    - **TaskList**: Displays tasks categorized as Today, Tomorrow, etc.
    - **TaskDetails**: Editable fields like title, deadline, priority, etc.
    - **AddTaskForm**: Form for adding new tasks with validations.

3. **Pomodoro Components**:
    - **Timer**: Visual circular timer with start/pause functionality.
    - **ReminderPopup**: Pop-up for Pomodoro reminders and feedback.
    - **ActiveTimer**: Displays the ongoing task with elapsed/remaining time.

4. **Settings**:
    - Manage reminder tunes and user goals.

5. **Analytics**:
    - Productivity insights and task completion stats.

### Backend Models

#### `User`:
- **Fields**:
  - `id`: UUID
  - `email`: string, unique
  - `password`: hashed string
  - `oauth_provider`: enum (Google/GitHub/None)
  - `date_joined`: datetime

#### `Task`:
- **Fields**:
  - `id`: UUID
  - `user`: ForeignKey (User)
  - `title`: string
  - `description`: text
  - `initial_deadline`: datetime
  - `deadline`: datetime
  - `priority`: enum (high/medium/low)
  - `remainder_sound`: string
  - `status`: enum (working/done/pending)
  - `created_on`: datetime
  - `completed_on`: datetime (nullable)

#### `PomodoroSession`:
- **Fields**:
  - `id`: UUID
  - `task`: ForeignKey (Task)
  - `start_time`: datetime
  - `end_time`: datetime
  - `duration`: integer (minutes)

#### `Settings`:
- **Fields**:
  - `user`: ForeignKey (User)
  - `goal`: string
  - `alarm_tune`: string
  - `progress_status`: enum

### API Endpoints
#### **Authentication**
1. **POST /api/auth/signup/**
    - **Input**: `{ email, password, confirm_password }`
    - **Output**: `{ success: true, message: "Account created." }`

2. **POST /api/auth/login/**
    - **Input**: `{ email, password }`
    - **Output**: `{ token: "JWT", user: { id, email } }`

3. **POST /api/auth/oauth/**
    - **Input**: `{ provider, token }`
    - **Output**: `{ token: "JWT", user: { id, email } }`

#### **Task Management**
1. **GET /api/tasks/**
    - **Output**: `{ tasks: [ { id, title, description, deadline, priority, status } ] }`

2. **POST /api/tasks/add/**
    - **Input**: `{ title, description, deadline, priority }`
    - **Output**: `{ success: true, task_id: "UUID" }`

3. **PUT /api/tasks/edit/<task_id>/**
    - **Input**: `{ title, description, deadline, priority, status }`
    - **Output**: `{ success: true }`

4. **DELETE /api/tasks/delete/<task_id>/**
    - **Output**: `{ success: true }`

#### **Pomodoro Sessions**
1. **POST /api/pomodoro/start/**
    - **Input**: `{ task_id }`
    - **Output**: `{ session_id: "UUID", start_time }`

2. **POST /api/pomodoro/stop/<session_id>/**
    - **Output**: `{ success: true, duration }`

#### **Settings**
1. **GET /api/settings/**
    - **Output**: `{ goal, alarm_tune }`

2. **PUT /api/settings/update/**
    - **Input**: `{ goal, alarm_tune }`
    - **Output**: `{ success: true }`

### Class Diagram
```markdown
+------------------+
|     User         |
+------------------+
| id: UUID         |
| email: string    |
| password: string |
| oauth_provider   |
| date_joined      |
+------------------+
           |
           |
           |
+-------------------+
|      Task         |
+-------------------+
| id: UUID          |
| user: FK (User)   |
| title: string     |
| description: text |
| deadline: datetime|
| priority: enum    |
| status: enum      |
+-------------------+
           |
           |
+-------------------+
| PomodoroSession   |
+-------------------+
| id: UUID          |
| task: FK (Task)   |
| start_time        |
| end_time          |
| duration: integer |
+-------------------+
           |
           |
+-------------------+
|     Settings      |
+-------------------+
| user: FK (User)   |
| goal: string      |
| alarm_tune: string|
| progress_status:  |
| enum              |
+-------------------+
```

---
This document defines the frontend, backend, and API with a clear understanding of inputs, outputs, and validations. It ensures modularity and scalability.

