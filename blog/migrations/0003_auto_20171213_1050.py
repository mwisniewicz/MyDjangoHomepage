# Generated by Django 2.0 on 2017-12-13 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171212_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.CharField(max_length=1000),
        ),
    ]
