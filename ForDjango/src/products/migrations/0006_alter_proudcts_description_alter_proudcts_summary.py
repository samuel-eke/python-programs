# Generated by Django 4.1.3 on 2022-12-12 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_proudcts_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proudcts',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='proudcts',
            name='summary',
            field=models.TextField(blank=True, default='This is an example of a default text'),
        ),
    ]