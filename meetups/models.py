from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
Experience_Level=(
    ('JONIOR','Jonior'),
    ('MID','Mid-level'),
    ('SENIOR','Senior'),
)

class Programing_Language(models.Model):
    language_Name = models.CharField(max_length=225)

    def __str__(self):
        return self.language_Name


class Participant(models.Model):
    email= models.EmailField(unique=True)


    def __str__(self):
        return self.email
    

class Location(models.Model):
    name = models.CharField(max_length=200)
    address= models.CharField(max_length=300)


    def __str__(self):
        return f'{self.name} ({self.address})'
    


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='image')
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True, null=True)
    programin_languages = models.ManyToManyField(Programing_Language,blank=True, null=True)
    
    
    # used to change text of admin dash-board 
    def __str__(self):
        return f'{self.title} - {self.slug}' 



class Emolyees(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    national_id = models.CharField(max_length=14,unique=True)
    name = models.CharField(max_length=225)
    city = models.CharField(max_length=120)
    email = models.EmailField()
    # slug = models.SlugField(unique=True)
    bio = models.TextField(max_length=2000)
    experiance = models.CharField(choices=Experience_Level,max_length=225)
    # friends = models.ManyToManyField(User, blank=True, related_name='friends')
    programing_languages= models.ManyToManyField(Programing_Language,null=True,blank=True)
    jobs = models.ManyToManyField(Meetup,blank=True,null=True)

    def __str__(self):
        return self.user.username




