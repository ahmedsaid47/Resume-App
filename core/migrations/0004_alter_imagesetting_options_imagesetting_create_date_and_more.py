# Generated by Django 4.2.8 on 2024-03-14 08:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_imagesetting_alter_generalsetting_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagesetting',
            options={'ordering': ('name',), 'verbose_name': 'Image Setting', 'verbose_name_plural': 'Image Settings'},
        ),
        migrations.AddField(
            model_name='imagesetting',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Create Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagesetting',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Update Date'),
        ),
    ]
