# Generated by Django 2.0.6 on 2018-06-03 23:23

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
                ('login', models.CharField(max_length=15)),
                ('pwd', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone1', models.CharField(max_length=13)),
                ('telefone2', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='ClienteFisico',
            fields=[
                ('cliente_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bankserverapp.Cliente')),
                ('cpf', models.CharField(max_length=11)),
            ],
            bases=('bankserverapp.cliente',),
        ),
        migrations.CreateModel(
            name='ClienteJuridico',
            fields=[
                ('cliente_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bankserverapp.Cliente')),
                ('cnpj', models.CharField(max_length=11)),
            ],
            bases=('bankserverapp.cliente',),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankserverapp.Telefone'),
        ),
    ]