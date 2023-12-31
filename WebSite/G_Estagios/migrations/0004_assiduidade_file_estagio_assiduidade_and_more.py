# Generated by Django 4.2.5 on 2023-10-11 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('G_Estagios', '0003_alter_estagio_id_empresa_alter_estagio_id_aluno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assiduidade',
            name='File',
            field=models.FileField(blank=True, upload_to='Documentos/Assiduidade/'),
        ),
        migrations.AddField(
            model_name='estagio',
            name='Assiduidade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='G_Estagios.assiduidade'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assiduidade',
            name='data',
            field=models.DateField(auto_created=True, blank=True),
        ),
        migrations.AlterField(
            model_name='assiduidade',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nome_curso',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='curso',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='escola',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='morada',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='privilegio',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nome',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='estagio',
            name='Ano_Letivo',
            field=models.CharField(blank=True, max_length=9),
        ),
        migrations.AlterField(
            model_name='estagio',
            name='horas_totais',
            field=models.IntegerField(blank=True),
        ),
        migrations.CreateModel(
            name='Protocolos',
            fields=[
                ('data', models.DateField(auto_created=True, blank=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('File', models.FileField(blank=True, upload_to='Documentos/Protocolos/')),
                ('id_Aluno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='estagio',
            name='id_Protocolos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='G_Estagios.protocolos'),
            preserve_default=False,
        ),
    ]
