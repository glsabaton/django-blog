from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from theblog.models import Profile


class CreateProfileViewForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'facebook_url',
                  'instagram_url', 'twitter_url']
        widgets = {
            # 'profile_pic': forms.ImageField(attrs={'class': 'image-control', }),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': "form-control"}),
            'instagram_url': forms.TextInput(attrs={'class': "form-control"}),
        }


class PasswordsChangeForm(PasswordChangeForm):
    # new_password1 = forms.CharField(
    #   max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))  # init olmadan  da yapılabilir

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(PasswordsChangeForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class UserEditForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password")
        """
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "This is title placeholder"}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.Textarea(attrs={'class': "form-control"}),
            'last_name': forms.Textarea(attrs={'class': "form-control"}),
        }
        """
