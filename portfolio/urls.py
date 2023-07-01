from django.urls import include, path
from .views import (
    create_feedback, create_account, create_task, create_team, create_user,
    user_detail, task_detail
)

urlpatterns = [
    path("user/<int:id>/", user_detail, name="user_detail"),
    path('create_user/', create_user, name="create_user"),
    path('task/<int:id>/', task_detail, name="task_detail"),
    path('create_task/', create_task, name="create_task"),
    path('create_team/', create_team, name="create_team"),
    path('create_account/', create_account, name="create_account"),
    path('create_feedback/', create_feedback, name="create_feedback")

]
