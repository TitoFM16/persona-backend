# Generated by Django 4.1.5 on 2023-01-10 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_remove_persona_hobbies'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='hobbies',
            field=models.CharField(default='', max_length=100),
        ),
    ]