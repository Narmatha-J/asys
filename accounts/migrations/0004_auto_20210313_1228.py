# Generated by Django 3.1.7 on 2021-03-13 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210313_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancedetails',
            name='studentname',
        ),
        migrations.AddField(
            model_name='attendancedetails',
            name='registernumber',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
