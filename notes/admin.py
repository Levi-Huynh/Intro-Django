from django.contrib import admin
from .models import Note
from .models import PersonalNote
# Register your models here.
#this tells admin interface which tables were
#interested in seeing

#registering more models example:
#admin.site.register(PersonalNote)

class NoteAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified') #this allows it to be displayed in admin browser

admin.site.register(Note, NoteAdmin) 
admin.site.register(PersonalNote) #admin.site.register(PersonalNote, Noteadmin) 
#allows readonly_fields/ NoteAdmin attribute to show up in PersonalNote dash of admin browser
# #both personal note and noteadmin should share the feild ..for readlonly?
# if do a sql bash with personal note, only shows the feilds unique to personal note, 
# since the rest is inheriting from note 
