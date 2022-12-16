from django.contrib import admin

from .models import UsersBot

class BotUsersAdmin(admin.ModelAdmin):
    class Meta:
        model = UsersBot
        fields = '__all__' 

admin.site.register(UsersBot, BotUsersAdmin)
