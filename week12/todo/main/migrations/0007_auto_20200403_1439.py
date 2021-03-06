# Generated by Django 2.2 on 2020-04-03 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200301_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='attachments'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
