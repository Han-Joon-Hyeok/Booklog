from django.contrib import admin

# Register your models here.
from signup.models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(MyUser, MyUserAdmin)
