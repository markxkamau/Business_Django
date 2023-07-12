from django.db import models


class person(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    user_name = models.CharField(max_length=10)
    user_image = models.CharField(max_length=256)
    age = models.IntegerField()
    email = models.EmailField()
    contact = models.IntegerField()
    location = models.CharField(max_length=20)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name

# Mainly for online accounts e.g. Facebook etc,


class account(models.Model):
    account_type = models.CharField(max_length=100, default="")
    account_value = models.URLField(default="")
    person = models.ForeignKey(person, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.account_type


class team(models.Model):
    team_name = models.CharField(max_length=100, default="")
    team_images = models.CharField(max_length=256, default="")
    members = models.ManyToManyField(person, through='team_person')

    def __str__(self):
        return self.team_name


class team_person(models.Model):
    team = models.ForeignKey(team, on_delete=models.CASCADE)
    person = models.ForeignKey(person, on_delete=models.CASCADE)


class task(models.Model):
    title = models.CharField(max_length=256, default="default")
    content = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    person = models.ForeignKey(person, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class feedback(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.customer_name


class person_image(models.Model):
    collection = models.ForeignKey(
        person, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()

    def __str__(self):
        return self.collection


class team_image(models.Model):
    collection = models.ForeignKey(
        team, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()

    def __str__(self):
        return self.collection
