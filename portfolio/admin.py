from django.contrib import admin
from .models import (
    person,
    feedback,
    account,
    task,
    team
)
admin.site.register([task, team, account, person, feedback])
