# Generated by Django 4.0.3 on 2022-05-08 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0023_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainproduct',
            name='price',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
