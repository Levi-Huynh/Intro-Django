from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta: #MODEL AND feilds 
        model = PersonalNote
        fields = ('title', 'content')
    
    def create(self, validated_data): 
        self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        
        return note


class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer #instance
    queryset = PersonalNote.objects.all() #get_queryset overides the all to filter

    def get_queryset(self): #filters out & shows data of only logged in user
        logged_user = self.request.user #request in self. belongs to rest framework 
        if logged_user.is_anonymous:
            return PersonalNote.objects.none()

        else:
            return PersonalNote.objects.filter(user=logged_user) #filter ORM returns like #where in SQL


#python debugger 
# def get_queryset(self):
    #import pdb; pdb.set_trace() #; is a command seperator, allows several commands in same line
    #return PersonalNote.objects.all()

    #when writing frameworks, put in hooks/opportunties/timing that allow people to overide
    #it 