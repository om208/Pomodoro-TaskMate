from django.shortcuts import render

def api_documentation(request):
    api_endpoints = [
        {
            "category": "User Authentication",
            "endpoints": [
                {"method": "POST", "url": "/api/auth/signup/", "description": "Register a new user account."},
                {"method": "POST", "url": "/api/auth/login/", "description": "Authenticate an existing user and obtain a JWT token."},
                {"method": "POST", "url": "/api/auth/oauth/", "description": "Authenticate a user via OAuth provider."},
            ]
        },
        {
            "category": "Task Management",
            "endpoints": [
                {"method": "GET", "url": "/api/tasks/?userId=3f766cccaf764c90aa153a663309693d", "description": "Retrieves a list of all tasks for a specific user."},
                {"method": "POST", "url": "/api/tasks/add/", "description": "Adds a new task to the database."},
                {"method": "PUT", "url": "/api/tasks/edit/?userId=3f766cccaf764c90aa153a663309693d", "description": "Updates an existing task."},
                {"method": "DELETE", "url": "/api/tasks/delete/?userId=<task_id>", "description": "Deletes a task."},
            ]
        },
        {
            "category": "Settings",
            "endpoints": [
                {"method": "GET", "url": "/api/settings/?userId=3f766cccaf764c90aa153a663309693d", "description": "Retrieves the settings for a specific user."},
                {"method": "PUT", "url": "/api/settings/update/", "description": "Updates the settings for a specific user."},
                {"method": "GET", "url": "/api/settings/progress_status/?userId=3f766cccaf764c90aa153a663309693d", "description": "Retrieves the progress status for a specific user."},
                {"method": "POST", "url": "/api/settings/add/", "description": "Creates a new user settings entry."},
            ]
        },
        {
            "category": "Pomodoro Session",
            "endpoints": [
                {"method": "POST", "url": "/api/pomodoro/start/", "description": "Starts a new Pomodoro session."},
                {"method": "POST", "url": "/api/pomodoro/stop/<session_id>", "description": "Stops an ongoing Pomodoro session."},
            ]
        },
    ]
    return render(request, 'api_documentation.html', {'api_endpoints': api_endpoints})