from django.contrib import admin
from myapp.models import register,booking,feedback

# Register your models here.
admin.site.register(register)
admin.site.register(booking)
admin.site.register(feedback)