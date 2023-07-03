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
        'type': 'text'
    }))
    person = forms.ModelChoiceField(queryset=person.objects.all())


class TeamForm(forms.Form):
    team_name = forms.CharField(widget=forms.TextInput)
    team_images = forms.CharField(widget=forms.TextInput)
    members = forms.ModelMultipleChoiceField(queryset=person.objects.all())


class AccountForm(forms.Form):
    account_type = forms.CharField(max_length=100)
    account_value = forms.URLField()
    person = forms.ModelChoiceField(queryset=person.objects.all())


class PersonForm(forms.ModelForm):
    class Meta:
        model = person
        fields = '__all__'


class FeedbackForm(forms.Form):
    customer_name = forms.CharField(max_length=30)
    customer_email = forms.EmailField()
    subject = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea(attrs={
        'type': 'text'
    }))


class Person_Image_Form(forms.Form):
    collection = forms.ModelChoiceField(
        queryset=person.objects.all())
    image = forms.ImageField()


class Team_Image_Form(forms.Form):
    collection = forms.ModelChoiceField(
        queryset=team.objects.all(), label="Team")
    image = forms.ImageField()
