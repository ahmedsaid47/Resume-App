# Generated by Django 4.2.8 on 2024-03-19 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(blank=True, default='', max_length=254, null=True, verbose_name='Subject'),
        ),
    ]