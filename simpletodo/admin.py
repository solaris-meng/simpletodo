from django.contrib import admin

from .models import Todo,TodoFile
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_start','time_end', 'user', 'status', 'content')

admin.site.register(Todo, TodoAdmin)
admin.site.register(TodoFile)
