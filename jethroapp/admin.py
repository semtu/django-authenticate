from django.contrib import admin
from .models import form_model,user_model
# Register your models here.
admin.site.register(form_model)
admin.site.register(user_model)