from django import forms
from .models import Comment, Profile

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'location', 'birth_date']
        
        
class RegisterForm(forms.Form):
        username = forms.CharField(max_length=150)
        email = forms.EmailField()
        password = forms.CharField(widget=forms.PasswordInput)
        confirm_password = forms.CharField(widget=forms.PasswordInput)

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get("password")
                confirm_password = cleaned_data.get("confirm_password")

                if password != confirm_password:
                    raise forms.ValidationError("Passwords do not match")

                return cleaned_data
