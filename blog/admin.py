from django.contrib import admin
from .models import Post

admin.site.register(Post)

# Для создания админа python manage.py createsuperuser