# Generated by Django 2.0.4 on 2018-06-13 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankserverapp', '0003_auto_20180613_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='endereco',
            field=models.CharField(max_length=100),
        ),
    ]