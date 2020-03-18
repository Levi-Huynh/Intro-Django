from django.contrib import admin
from .models import Note
# Register your models here.
#this tells admin interface which tables were
#interested in seeing

#registering more models example:
#admin.site.register(PersonalNote)

class NoteAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

admin.site.register(Note, NoteAdmin) 