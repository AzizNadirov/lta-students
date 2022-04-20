from django import forms
from student.models import Profile



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_name', 'email', 'image', 'about']