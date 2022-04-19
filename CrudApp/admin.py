from django.contrib import admin

# Register your models here.
from CrudApp import models

admin.site.register(models.Login)
admin.site.register(models.Student)
