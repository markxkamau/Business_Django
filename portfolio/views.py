from django.shortcuts import render
from .forms import (
    PersonForm,
    TaskForm,
    TeamForm,
    AccountForm,
    FeedbackForm
)
from .models import (
    person,
    task,
    team,
    account,
    feedback
)


def create_user(request):
    object = PersonForm()
    if request.method == 'POST':
        object = PersonForm(request.POST)
        if object.is_valid():
            person.objects.create(**object.cleaned_data)
        else:
            object = PersonForm()
    obj = {
        "object": object
    }
    return render(request, "User/create_user.html", obj)


def user_detail(request):
    object = person.objects.all()
    obj = {
        "object": object
    }
    return render(request, "base.html", obj)


def create_task(request):
    object = TaskForm()
    if request.method == 'POST':
        object = TaskForm(request.POST)
        if object.is_valid():
            task.objects.create(**object.cleaned_data)
    obj = {
        "object": object
    }
    return render(request, "Task/create_task.html", obj)


def create_team(request):
    object = TeamForm()
    if request.method == 'POST':
        object = TeamForm(request.POST)
        if object.is_valid():
            team.objects.create(**object.cleaned_data)
    obj = {
        "object": object
    }
    return render(request, "Team/create_team.html", obj)


def create_account(request):
    object = AccountForm()
    if request.method == 'POST':
        object = AccountForm(request.POST)
        if object.is_valid():
            account.objects.create(**object.cleaned_data)
    obj = {
        "object": object
    }
    return render(request, "Account/create_account.html", obj)


def create_feedback(request):
    object = FeedbackForm()
    if request.method == 'POST':
        object = FeedbackForm(request.POST)
        if object.is_valid():
            feedback.objects.create(**object.cleaned_data)
    obj = {
        "object": object
    }
    return render(request, "Feedback/create_feedback.html", obj)
# image_collection = ImageCollection.objects.create(name="My Image Collection")

# image1 = Image.objects.create(collection=image_collection, image='path/to/image1.jpg')
# image2 = Image.objects.create(collection=image_collection, image='path/to/image2.jpg')
# image_collection = ImageCollection.objects.get(id=1)
# images = image_collection.images.all()

# for image in images:
#     print(image.image.url)
