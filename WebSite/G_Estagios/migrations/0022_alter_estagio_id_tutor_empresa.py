# Generated by Django 3.2.6 on 2023-12-21 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('G_Estagios', '0021_auto_20231220_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estagio',
            name='id_Tutor_empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tutor_Empresa', to='G_Estagios.empresa'),
        ),
    ]
