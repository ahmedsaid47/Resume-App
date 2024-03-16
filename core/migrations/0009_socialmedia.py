# Generated by Django 4.2.8 on 2024-03-16 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_education_alter_experience_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('link', models.URLField(blank=True, default='', max_length=254, verbose_name='Link')),
                ('icon', models.CharField(blank=True, default='', max_length=254, verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'SocialMedia',
                'verbose_name_plural': 'SocialMedia',
                'ordering': ('order',),
            },
        ),
    ]