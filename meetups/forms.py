from django import forms
from django.contrib.auth.forms import UserCreationForm, UserModel
from django.contrib.auth.models import User, UserManager
from django.db.models import fields
from .models import Meetup,Emolyees, Participant, Programing_Language

Experience_Level=(
    ('JONIOR','Jonior'),
    ('MID','Mid-level'),
    ('SENIOR','Senior'),
)


class RegistrationForm(forms.ModelForm):

    email = forms.EmailField(label='Your email')

    class Meta:
        model= Participant
        fields=['email']



    



class JobsForm(forms.ModelForm):


    class Meta:
        model = Meetup
        fields =['title','organizer_email','date','image'
        ,'slug','description','description','location'
        ,'programin_languages']







class EmployeesForm(UserCreationForm):

    email = forms.EmailField()
    
    class Metas:
        model= User
        fields={'username','email','password1','password2','national_id',
        'name'}

    def save(self, commit: bool = True):
        
        user= super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user

    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class empReg(forms.ModelForm):
    class Meta:
        model=Emolyees
        fields={'city','bio','experiance','programing_languages','national_id','name'}


