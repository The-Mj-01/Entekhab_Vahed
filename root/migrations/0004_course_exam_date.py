# Generated by Django 2.2.7 on 2019-11-08 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0003_auto_20191108_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='exam_date',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
