# Generated by Django 3.1.7 on 2021-03-13 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210313_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancedetails',
            name='Status',
            field=models.CharField(max_length=10),
        ),
    ]