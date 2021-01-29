from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "author",
                  "category", "body", "snippet", "header_image")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', "value": '', 'id': 'elder', "type": "hidden"}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': "form-control"}),
            'snippet': forms.Textarea(attrs={'class': "form-control", 'placeholder': "Leave a short description for your post"}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),

        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "body", "snippet")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "This is title placeholder"}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': "form-control"}),
            'snippet': forms.Textarea(attrs={'class': "form-control"}),

        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Please enter here your name"}),
            'body': forms.Textarea(attrs={'class': "form-control"}),

        }
