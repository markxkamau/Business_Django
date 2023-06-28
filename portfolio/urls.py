from django.urls import include, path
from .views import (
    create_feedback, create_account, create_task, create_team, create_user,
    user_detail
)

urlpatterns = [
    path("user/<int:id>/", user_detail),
    path('create_user/', create_user),
    path('create_task/', create_task),
    path('create_team/', create_team),
    path('create_account/', create_account),
    path('create_feedback/', create_feedback)

]
