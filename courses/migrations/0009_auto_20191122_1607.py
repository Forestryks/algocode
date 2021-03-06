# Generated by Django 2.2 on 2019-11-22 13:07

import courses.models
from django.db import migrations, models
import django.db.models.deletion


def change_olymp_to_type(apps, schema_editor):
    Standings = apps.get_model('courses', 'Standings')
    for standings in Standings.objects.all():
        if standings.olymp:
            standings.contest_type = courses.models.Standings.OLYMP
        else:
            standings.contest_type = courses.models.Standings.ACM
        standings.save()


def revert_type_to_olymp(apps, schema_editor):
    Standings = apps.get_model('courses', 'Standings')
    for standings in Standings.objects.all():
        if standings.contest_type == courses.models.Standings.OLYMP:
            standings.olymp = True
        else:
            standings.olymp = False
        standings.save()


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_contest_contest_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlitzProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_id', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('statements', models.FileField(upload_to=courses.models.get_blitz_statements_file_path)),
            ],
        ),
        migrations.RemoveField(
            model_name='contest',
            name='is_olymp',
        ),
        migrations.AddField(
            model_name='standings',
            name='contest_type',
            field=models.CharField(choices=[('AC', 'Acm'), ('OL', 'Olympiad'), ('BS', 'Battleship'), ('BT', 'Blitz')], default='AC', max_length=2),
        ),
        migrations.RunPython(change_olymp_to_type, revert_type_to_olymp),
        migrations.CreateModel(
            name='BlitzProblemStart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_id', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('bid', models.IntegerField(default=0)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='starts', to='courses.BlitzProblem')),
            ],
        ),
        migrations.AddField(
            model_name='blitzproblem',
            name='contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blitz_problems', to='courses.Contest'),
        ),
    ]
