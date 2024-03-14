from django.db import models

# Create your models here.

class GeneralSetting(models.Model):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',

    )

    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter',

    )
    update_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Update Date',

    )
    create_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Create Date',
    )

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name', )

class ImageSetting(models.Model):
        name = models.CharField(
            default='',
            max_length=254,
            blank=True,
            verbose_name='Name',
            help_text="This is veriable of swttings"
        )
        description = models.CharField(
            default='',
            max_length=254,
            blank=True,
            verbose_name='Description',
            help_text=""
        )

        file = models.ImageField(
            default='',
            max_length=254,
            blank=True,
            upload_to="images/",
        )
        update_date = models.DateTimeField(
            blank=True,
            auto_now=True,
            verbose_name='Update Date',

        )
        create_date = models.DateTimeField(
            blank=True,
            auto_now_add=True,
            verbose_name='Create Date',
        )

        def __str__(self):
            return f'Image Setting: {self.name}'

        class Meta:
            verbose_name = 'Image Setting'
            verbose_name_plural = 'Image Settings'
            ordering = ('name',)
