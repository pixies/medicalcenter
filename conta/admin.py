from django.contrib import admin
from conta.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

