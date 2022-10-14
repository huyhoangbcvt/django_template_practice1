# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from .models.account_model import Author
from .modules.views_auth import CustomUserAdmin

# Register your models here
admin.site.register(Author)
# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
