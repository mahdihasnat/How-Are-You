# Generated by Django 4.0.2 on 2022-02-19 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('take_questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='response',
            field=models.IntegerField(),
        ),
    ]
