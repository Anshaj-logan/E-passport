from django.contrib import admin
from predict.models import user_model
from predict.models import user_siup

admin.site.register(user_model)

# Register your models here.
admin.site.register(user_siup)