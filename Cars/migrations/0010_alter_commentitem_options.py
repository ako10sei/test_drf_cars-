# Generated by Django 4.1.1 on 2022-09-09 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0009_alter_commentitem_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentitem',
            options={'verbose_name': 'Комменатрий ', 'verbose_name_plural': 'Комментарии'},
        ),
    ]
