# Generated by Django 3.1.3 on 2023-09-27 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='codigo',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='curso',
            name='creditos',
            field=models.CharField(max_length=50),
        ),
    ]
