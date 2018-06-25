# Generated by Django 2.0.4 on 2018-06-24 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=45)),
                ('senha', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=200)),
                ('banco_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('rua_mora', models.CharField(max_length=45)),
                ('cidade_mora', models.CharField(max_length=45)),
                ('estado_mora', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('login', models.CharField(max_length=15)),
                ('senha', models.CharField(max_length=15)),
                ('data_cadastro', models.DateField()),
                ('adm_cadastrou', models.ForeignKey(on_delete=models.SET(None), to='bankserverapp.Administrador')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='funcionario_cadastrou',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankserverapp.Funcionario'),
        ),
        migrations.AddField(
            model_name='administrador',
            name='agencia',
            field=models.ForeignKey(on_delete=models.SET(None), to='bankserverapp.Agencia'),
        ),
    ]
