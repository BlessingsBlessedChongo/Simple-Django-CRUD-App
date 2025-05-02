from django.contrib import admin
"""
This module is used to register the Task model with the Django admin site.
Classes:
    None
Functions:
    None
Usage:
    - The `admin.site.register(Task)` line registers the Task model so that it can be managed through the Django admin interface.
    - Importing `Task` from the local `models` module ensures that the model is available for registration.
Dependencies:
    - django.contrib.admin: Provides the admin interface for managing models.
    - .models: Contains the definition of the Task model.
"""
from .models import Task

admin.site.register(Task)
