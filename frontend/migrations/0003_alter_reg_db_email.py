# Generated by Django 4.2.7 on 2023-12-12 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_reg_db'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_db',
            name='Email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
