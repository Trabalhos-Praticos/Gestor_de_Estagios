# Generated by Django 3.2.6 on 2024-01-08 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('G_Estagios', '0027_auto_20240105_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertas',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='G_Estagios.curso'),
        ),
    ]