# DjangoExample
1. to create admin module
django-admin startproject projectname

2. to create api module
python manage.py startapp api

## manage.py will generate with 1st command

Coding steps:
1. Install "djangorestframework" library to use restapi
2. add this rest_framework into settings.py
3. In api module, create models, serializers for model, create views, and setup urls
4. add api module in admin settings.py
5. add api base url in urls "api/v1/"
6. Run python manage.py makemigrations - to migrate model with database
7. Update all changes in database - python manage.py migrate
8. Run Server - python manage.py runserver

9. Add this to handle api access on production in settings.py

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    # remove api from browser
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

10. register api in admin - update code of api->admin.py

11. generate superadmin - python manage.py createsuperuser