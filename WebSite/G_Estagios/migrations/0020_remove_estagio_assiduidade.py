# Generated by Django 3.2.6 on 2023-12-20 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('G_Estagios', '0019_alter_estagio_ano_letivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estagio',
            name='Assiduidade',
        ),
    ]
