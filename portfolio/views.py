from django.shortcuts import render, redirect
from .forms import (
    PersonForm,
    TaskForm,
    TeamForm,
    AccountForm,
    FeedbackForm,
    Person_Image_Form,
    Team_Image_Form
)
from .models import (
    person,
    task,
    team,
    account,
    feedback,
    person_image,
    team_image
)


def create_user(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person.objects.create(**form.cleaned_data)
            return redirect('/portfolio/create_account/')
    obj = {
        "form": form
    }
    return render(request, "User/create_user.html", obj)

# Homepage


def user_detail(request, id):
    object = person.objects.get(id=id)
    tasks = task.objects.filter(person=object)
    accounts = account.objects.filter(person=object)
    obj = {
        "object": object,
        "task": tasks,
        "account": accounts
    }
    return render(request, "User/user_detail.html", obj)

# Community link


def user_team_detail(request, id):
    user = person.objects.get(id=id)
    teams = team.objects.filter(members=user)

    obj = {
        "object": user,
        "team": teams,
        "account": account.objects.filter(person=user)

    }
    return render(request, "Team/team_detail.html", obj)

# Services Link


def user_task_detail(request, id):
    user = person.objects.get(id=id)
    tasks = task.objects.filter(person=user)
    obj = {
        "object": user,
        "task": tasks,
        "account": account.objects.filter(person=user)
    }

    return render(request, "Task/task_detail.html", obj)


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


def task_detail(request, id):
    object = task.objects.get(id=id)
    obj = {
        "object": object
    }
    return render(request, "Task/task_detail.html", obj)


def create_team(request):
    object = TeamForm()
    if request.method == 'POST':
        object = TeamForm(request.POST)
        if object.is_valid():
            team_obj = object.save()  # Save the form and retrieve the Team object
            # save_instance(object, team_obj)  # Save the many-to-many relationships            # return redirect('team_detail', pk=team_obj.pk)  # Redirect to the team detail page
            # team.objects.create(**object.cleaned_data)
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
            return redirect('/portfolio/create_task')
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
