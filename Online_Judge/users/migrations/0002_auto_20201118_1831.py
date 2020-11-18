# Generated by Django 3.0.9 on 2020-11-18 13:01

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='notifications',
            field=jsonfield.fields.JSONField(default={'isnull': True}),
        ),
        migrations.AddField(
            model_name='userdata',
            name='runtime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userdata',
            name='timelimit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='tags',
            field=jsonfield.fields.JSONField(default={'isnull': True}),
        ),
    ]