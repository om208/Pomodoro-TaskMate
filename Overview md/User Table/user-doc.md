### `User` Table Class Diagram

**Class Diagram:**

```plaintext
+-------------------+
|      User         |
+-------------------+
| id: UUID          |
| email: string     |
| password: string  |
| oauth_provider:   |
| enum              |
| date_joined:      |
| datetime          |
+-------------------+
```

**Class Diagram with Default Values:**

```plaintext
+-------------------+
|      User         |
+-------------------+
| id: UUID          | (Auto-generated)
| email: string     | (No default, required)
| password: string  | (No default, required)
| oauth_provider:   |
| enum              | (Default: None)
| date_joined:      |
| datetime          | (Default: current datetime)
+-------------------+
```

**Class Diagram with Cardinality:**

```plaintext
+-------------------+
|      User         |
+-------------------+
| id: UUID          | 1
| email: string     | 1
| password: string  | 1
| oauth_provider:   |
| enum              | 0..1
| date_joined:      |
| datetime          | 1
+-------------------+
```

---

### API Documentation for `User`

#### **Authentication**

1. **POST /api/auth/signup/**

   - **Input**:
     ```json
     {
       "email": "string",
       "password": "string",
       "confirm_password": "string"
     }
     ```
   - **Validations**:

     - `email`: Must be a valid email format, unique in the database.
     - `password`: Must meet password strength criteria.
     - `confirm_password`: Must match the `password`.

   - **Output**:
     ```json
     {
       "success": true,
       "message": "Account created."
     }
     ```

2. **POST /api/auth/login/**

   - **Input**:
     ```json
     {
       "email": "string",
       "password": "string"
     }
     ```
   - **Validations**:

     - `email`: Must exist in the database.
     - `password`: Must match the stored hashed password.

   - **Output**:
     ```json
     {
       "token": "JWT",
       "user": {
         "id": "UUID",
         "email": "string"
       }
     }
     ```

3. **POST /api/auth/oauth/**

   - **Input**:
     ```json
     {
       "provider": "Google | GitHub",
       "token": "string"
     }
     ```
   - **Validations**:

     - `provider`: Must be `Google` or `GitHub`.
     - `token`: Must be a valid OAuth token.

   - **Output**:
     ```json
     {
       "token": "JWT",
       "user": {
         "id": "UUID",
         "email": "string"
       }
     }
     ```
