# Generated by Django 2.1.7 on 2019-03-15 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20190314_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='about',
            field=models.TextField(blank=True, verbose_name='About the course'),
        ),
    ]
