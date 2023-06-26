from django.db import models


class task(models.Model):
    title = models.CharField(max_length=256, default="default")
    content = models.TextField()


class team(models.Model):
    name = models.TextField()
    image = models.CharField(max_length=256, default="")


class account(models.Model):
    youtube = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    tiktok = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)


class person(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    user_name = models.CharField(max_length=10)
    user_image = models.CharField(max_length=256, default="")
    age = models.IntegerField()
    email = models.EmailField()
    contact = models.IntegerField()
    location = models.CharField(max_length=20)
    title = models.CharField(max_length=20, default="")
    user_task = models.ManyToManyField(task, related_name='users', name='Tasks',null=True, blank=True)
    user_team = models.ForeignKey(team, on_delete=models.CASCADE, name= 'Team', blank=True, null=True)
    user_account = models.ForeignKey(account, on_delete=models.CASCADE, name='Account', blank=True, null=True)


class feedback(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField()


class person_image(models.Model):
    collection = models.ForeignKey(
        person, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()


class team_image(models.Model):
    collection = models.ForeignKey(
        team, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()
