from django.contrib import admin
from .models import (
    person,
    feedback,
    account,
    task,
    team, 
    person_image,
    team_image
)
admin.site.register([task, team, account, person, feedback, person_image, team_image])
