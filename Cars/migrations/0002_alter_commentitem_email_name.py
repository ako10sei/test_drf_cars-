# Generated by Django 4.1.1 on 2022-09-08 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentitem',
            name='email_name',
            field=models.EmailField(max_length=50, unique=True, verbose_name='Электронная почта автора:'),
        ),
    ]