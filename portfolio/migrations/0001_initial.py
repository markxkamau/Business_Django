# Generated by Django 4.2.2 on 2023-06-26 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube', models.URLField()),
                ('twitter', models.URLField()),
                ('tiktok', models.URLField()),
                ('facebook', models.URLField()),
                ('instagram', models.URLField()),
                ('linkedin', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.TextField()),
                ('customer_email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='default', max_length=256)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('user_name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField(max_length=10)),
                ('location', models.TimeField()),
                ('user_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.account')),
                ('user_task', models.ManyToManyField(related_name='users', to='portfolio.task')),
                ('user_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.team')),
            ],
        ),
    ]