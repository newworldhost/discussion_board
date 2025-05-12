from django import forms
from .models import Comment, Profile, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),  # Add a date picker
        }

class PostForm(forms.ModelForm):
    new_category = forms.CharField(max_length=100, required=False, label='New Category')
    new_subcategory = forms.CharField(max_length=100, required=False, label='New SubCategory')

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'subcategory']  # Removed 'status'

    def save(self, commit=True):
        # Save the new category and subcategory if they are provided
        new_category_name = self.cleaned_data.get('new_category')
        new_subcategory_name = self.cleaned_data.get('new_subcategory')
        category = self.cleaned_data.get('category')
        subcategory = self.cleaned_data.get('subcategory')

        if new_category_name:
            category, created = Category.objects.get_or_create(name=new_category_name)
            self.instance.category = category

        if new_subcategory_name and category:
            subcategory, created = SubCategory.objects.get_or_create(name=new_subcategory_name, category=category)
            self.instance.subcategory = subcategory

        # Call the parent save method to save the post instance
        return super().save(commit)

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