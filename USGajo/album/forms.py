from django import forms
from .models import User, Album

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname']

    def signup(self, request, user):
        user.nickname = self.cleaned_data['nickname']
        user.save()

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'image1',
            'image2',
            'image3',
        ]
        exclude = ()