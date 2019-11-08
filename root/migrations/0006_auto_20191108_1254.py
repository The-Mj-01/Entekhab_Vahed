# Generated by Django 2.2.7 on 2019-11-08 12:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('root', '0005_auto_20191108_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='exam_date',
            field=models.CharField(max_length=120),
        ),
        migrations.CreateModel(
            name='GiveUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]