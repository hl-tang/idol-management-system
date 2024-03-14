from django.contrib import admin

# Register your models here.
from .models import Group, Idol, CD

admin.site.register(Group)
admin.site.register(Idol)
admin.site.register(CD)