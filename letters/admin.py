from django.contrib import admin

from .models import Letter, Setting

admin.site.register(Letter)

class SettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']

admin.site.register(Setting, SettingAdmin)