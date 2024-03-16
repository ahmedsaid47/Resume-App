from django.contrib import admin
from core.models import *

# Register your models here.

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter','update_date', 'create_date']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']

    class Meta:
        model = GeneralSetting


@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'file', 'update_date', 'create_date']
    search_fields = ['name', 'description', 'file']
    list_editable = ['description', 'file']

    class Meta:
        model = ImageSetting



@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'percentage','update_date', 'create_date']
    search_fields = ['name']
    list_editable = ['order', 'name', 'percentage']

    class Meta:
        model = Skill


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'job_title', 'job_location','start_date', 'end_date', 'update_date', 'create_date']
    search_fields = ['company_name', 'job_title', 'job_location']
    list_editable = ['company_name', 'job_title', 'job_location','start_date', 'end_date']

    class Meta:
        model = Experience
