# Generated by Django 5.0.4 on 2024-04-20 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
