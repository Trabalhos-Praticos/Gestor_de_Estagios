# Generated by Django 3.2.6 on 2023-12-20 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('G_Estagios', '0014_documento_mes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_professor',
        ),
    ]