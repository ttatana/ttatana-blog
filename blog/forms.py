from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment, UserProfile, PostImage


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class PostForm(forms.ModelForm):
    images = MultipleFileField(
        required=True,
        help_text='Select multiple images (hold Ctrl/Cmd to select multiple files)',
        widget=MultipleFileInput(attrs={
            'class': 'form-file',
            'accept': 'image/*'
        })
    )
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'location']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Give your story a title...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-input', 
                'rows': 4, 
                'placeholder': 'Tell the story behind these photos...'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Where were these taken?'
            }),
        }


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image', 'caption']
        widgets = {
            'caption': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Add a caption for this image...'
            }),
            'image': forms.FileInput(attrs={'class': 'form-file'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-textarea', 
                'rows': 2, 
                'placeholder': 'Add a comment...'
            }),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio', 'location', 'website']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-textarea', 
                'rows': 3, 
                'placeholder': 'Tell us about yourself...'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Your location'
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Your website'
            }),
            'avatar': forms.FileInput(attrs={'class': 'form-file'}),
        }