# Generated by Django 4.1.3 on 2022-12-03 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_proudcts_price_alter_proudcts_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='proudcts',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proudcts',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
