from django import forms

from .models import (
    task,
    team,
    account,
    person, 
    feedback
)

class TaskForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea(attrs={
        'type':'text'
    }))


class TeamForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    image = forms.CharField(label="Image Collection Name")


class AccountForm(forms.Form):
    youtube = forms.URLField()
    twitter = forms.URLField()
    tiktok = forms.URLField()
    facebook = forms.URLField()
    instagram = forms.URLField()
    linkedin = forms.URLField()

class PersonForm(forms.ModelForm):
    class Meta:
        model = person
        fields = ['first_name', 'last_name', 'age', 'email', 'contact', 'location', 'title']
# class PersonForm(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     user_name = forms.CharField()
#     user_image = forms.CharField()
#     age = forms.IntegerField()
#     email = forms.EmailField()
#     contact = forms.IntegerField()
#     location = forms.CharField()
#     title = forms.CharField()
#     user_task = forms.ModelMultipleChoiceField(queryset=task.objects.all(),blank=True, required=False)
#     user_team = forms.ModelChoiceField(queryset=team.objects.all(), empty_label="select", blank=True, required=False)
#     user_account = forms.ModelChoiceField(queryset=account.objects.all(), empty_label="select", blank=True, required=False)


class FeedbackForm(forms.Form):
    customer_name = forms.CharField(max_length=30)
    customer_email = forms.EmailField()
    subject = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea(attrs={
        'type':'text'
    }))


class Person_Image_Form(forms.Form):
    collection = forms.ModelChoiceField(
        queryset=person.objects.all())
    image = forms.ImageField()


class Team_Image_Form(forms.Form):
    collection = forms.ModelChoiceField(
        queryset=team.objects.all(), label="Team")
    image = forms.ImageField()

