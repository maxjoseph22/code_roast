from django.contrib import admin
from django.contrib.auth.models import Group, User

# Unregister groups
admin.site.unregister(Group)

# Edit User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    #Add favourite programming lanauge to user
    fields = ["Username"]
