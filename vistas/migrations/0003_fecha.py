# Generated by Django 3.0.8 on 2020-07-28 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vistas', '0002_delete_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fecha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
            ],
        ),
    ]
