# Generated by Django 3.0 on 2020-07-29 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHG_Panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Middle_Name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]