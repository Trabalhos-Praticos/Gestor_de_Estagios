# Generated by Django 3.2.6 on 2023-11-27 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('G_Estagios', '0009_customuser_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='ano',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
