# Generated by Django 4.0.2 on 2022-02-19 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('host', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Psychiatrist',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='persons.person')),
                ('verified', models.BooleanField(default=False)),
                ('available_times', models.TextField(blank=True, max_length=100, null=True)),
            ],
            bases=('persons.person',),
        ),
        migrations.CreateModel(
            name='ReviewBoardMember',
            fields=[
                ('psychiatrist_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='psychiatrists.psychiatrist')),
            ],
            bases=('psychiatrists.psychiatrist',),
        ),
        migrations.CreateModel(
            name='PsychiatristExpertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decription', models.TextField()),
                ('expertise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychiatrists.expertise')),
                ('psychiatrist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychiatrists.psychiatrist')),
            ],
        ),
        migrations.CreateModel(
            name='PsychiatristDegree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('institutuion', models.CharField(max_length=100)),
                ('graduation_date', models.DateField()),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychiatrists.degree')),
                ('psychiatrist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychiatrists.psychiatrist')),
            ],
        ),
        migrations.CreateModel(
            name='PsychiatristAward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychiatrists.award')),
                ('psychiatrist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychiatrists.psychiatrist')),
            ],
        ),
        migrations.AddField(
            model_name='psychiatrist',
            name='awards',
            field=models.ManyToManyField(through='psychiatrists.PsychiatristAward', to='psychiatrists.Award'),
        ),
        migrations.AddField(
            model_name='psychiatrist',
            name='degrees',
            field=models.ManyToManyField(through='psychiatrists.PsychiatristDegree', to='psychiatrists.Degree'),
        ),
        migrations.AddField(
            model_name='psychiatrist',
            name='expertises',
            field=models.ManyToManyField(through='psychiatrists.PsychiatristExpertise', to='psychiatrists.Expertise'),
        ),
    ]
