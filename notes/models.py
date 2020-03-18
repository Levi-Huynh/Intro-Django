from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
#typing uuidgen in command creates random id numbers in mac 
#as identifer unique , big number in hexidexicmal 

class Note(models.Model): #inheritance  of model instance . Model is class we inherit. 
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)#dont need parens with uuid4, b/c callsit leader  #django lots of feild types options, can use to enforce data integrity django verifies for #url field for example 
    title = models.CharField(max_length=200) #oneline text input
    content = models.TextField(blank=True) #multi line text input    
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 

class PersonalNote(Note):   # Inherits from Note!
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #What this is doing is importing Django’s built in user class model with something called a foreign key to create a reference to data on another table. It works sort of like a pointer in C.
    #MAKES sure this isn't intact if what FK is pointing to is deleted
    
