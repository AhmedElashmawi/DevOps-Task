from django.contrib import admin
from .models import  Emolyees, Meetup, Participant, Programing_Language
from .models import Location
# Register your models here.




#manage Tabel view in Admin Dashboard by django 
class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title' , 'date' , 'location')
    list_filter = ('location','date') #useing filter in Admin board 
    prepopulated_fields={'slug' : ('title' ,)}


admin.site.register(Meetup,MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)




class EmolyeeAdmin(admin.ModelAdmin):
    list_display = ('name' , 'experiance' , 'city')
    list_filter = ('city','experiance') #useing filter in Admin board 
    prepopulated_fields={'city' : ('name',)}


class LangAdmin(admin.ModelAdmin):
    list_display = ('language_Name' , 'language_Name' , 'language_Name')
    list_filter = ('language_Name','language_Name','language_Name') #useing filter in Admin board 
    

admin.site.register(Programing_Language,LangAdmin)
admin.site.register(Emolyees,EmolyeeAdmin)
