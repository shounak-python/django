# Generated by Django 4.0.7 on 2022-10-18 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_specialization_cred_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialization',
            name='issue_date',
            field=models.CharField(default='', max_length=20),
        ),
    ]