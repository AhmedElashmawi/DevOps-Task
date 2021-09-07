from meetups.models import Emolyees, Programing_Language
from django import forms    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



Experience_Level=(
    ('JONIOR','Jonior'),
    ('MID','Mid-level'),
    ('SENIOR','Senior'),
)



class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=225,required=True,widget=forms.EmailInput())
    national_id = forms.CharField(max_length=14,min_length=14,required=True)
    name = forms.CharField(max_length=14,required=False)
    city = forms.CharField(max_length=225,required=False)
    bio = forms.CharField(max_length=2500,required=True,widget=forms.Textarea)
    experience_level = forms.ChoiceField(choices= Experience_Level, required=True)
    programing_language = forms.ModelMultipleChoiceField(queryset=Programing_Language.objects.all())
    

    
    class Metas:
        model= User
        fields={'username','email','password1','password2','national_id',
        'name','city','bio','experience_level','Programing_Language'}


    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None