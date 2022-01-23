from django.contrib import admin
from api.models import PersonalComputer, Profile


@admin.register(PersonalComputer)
class PersonalComputerAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
