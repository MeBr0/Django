# Generated by Django 2.2 on 2020-02-23 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField()),
                ('due_on', models.DateTimeField()),
                ('is_done', models.BooleanField(default=False)),
                ('notes', models.CharField(blank=True, default='', max_length=255)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='main.ToDoList')),
            ],
        ),
    ]
