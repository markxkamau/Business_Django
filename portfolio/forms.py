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
    price = forms.DecimalField(decimal_places=2, max_digits=10)
    person = forms.ModelChoiceField(queryset=person.objects.all())


class TeamForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(queryset=person.objects.all())

    class Meta:
        model = team
        fields = ['team_name', 'team_images', 'members']


class AccountForm(forms.Form):
    account_type = forms.CharField(max_length=100)
    account_value = forms.URLField()
    person = forms.ModelChoiceField(queryset=person.objects.all())


class PersonForm(forms.ModelForm):
    image = forms.ImageField(required=False)  # Add the image field
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
        queryset=team.objects.all())
    image = forms.ImageField()
