# Generated by Django 5.2.1 on 2025-06-02 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='test@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(default='defaultpassword123', max_length=255),
        ),
    ]
