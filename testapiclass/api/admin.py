from django.contrib import admin
from .models import Note
# Register your models here.
@admin.register(Note)
class ad(admin.ModelAdmin):
    list_display = ['title','content']