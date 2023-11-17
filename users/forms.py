from django.forms import widgets
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill


class CustomUserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password1',
            'password2'
        ]

    def __init__(self, *args, **kwargs):
        super(CustomUserCreation, self).__init__(*args, **kwargs)

        for mame, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


"""
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.TextInput(attrs={'class': 'input'}),
            'username': forms.TextInput(attrs={'class': 'input'}),
            'password1': forms.PasswordInput(attrs={'class': 'input'}),
            'password2': forms.PasswordInput(attrs={'class': 'input '}),
        }
"""


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'email',
            'username',
            'location',
            'bio',
            'short_intro',
            'profile_img',
            'social_github',
            'linkedin',
            'social_twitter',
            'social_youtube'
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for mame, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for mame, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
