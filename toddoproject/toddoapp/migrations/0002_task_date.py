# Generated by Django 4.2.8 on 2024-01-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toddoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1991-07-07'),
            preserve_default=False,
        ),
    ]
