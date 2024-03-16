from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class AbstractModel(models.Model):
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
    class Meta:
        abstract =True

class GeneralSetting(AbstractModel):
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


    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name', )

class ImageSetting(AbstractModel):
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

        def __str__(self):
            return f'Image Setting: {self.name}'

        class Meta:
            verbose_name = 'Image Setting'
            verbose_name_plural = 'Image Settings'
            ordering = ('name',)


class Skill(AbstractModel):

    order =models.IntegerField(
        default=0,
        verbose_name='Order'
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text="This is veriable of settings"
    )
    percentage= models.IntegerField(
        default='50',
        verbose_name='Description',
        validators=[MinValueValidator(0),MaxValueValidator(100)]

    )

    def __str__(self):
        return f'Skill: {self.name}'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skill'
        ordering = ('name',)


class Experience(AbstractModel):

    company_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Company Name',
    )
    job_title = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Title',
    )
    job_location = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Location',
    )
    start_date = models.DateField(
        verbose_name='Start Date',
    )
    end_date = models.DateField(
        default=None,
        null=True,
        verbose_name='End Date',
        blank=True,
    )


    def __str__(self):
        return f'Experience: {self.company_name}'

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experience'
        ordering = ('start_date',)