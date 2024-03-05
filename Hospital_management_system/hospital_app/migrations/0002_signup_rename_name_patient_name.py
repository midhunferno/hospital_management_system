# Generated by Django 5.0.1 on 2024-02-29 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=25)),
                ('Confirm_Password', models.CharField(max_length=25)),
            ],
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Name',
            new_name='name',
        ),
    ]