from django.shortcuts import render, redirect, get_object_or_404
from core.models import GeneralSetting, ImageSetting, Skill, Experience, Education, SocialMedia, Document


# Create your views here.

def layout(request):
    #General Settings
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameter
    home_banner_title = GeneralSetting.objects.get(name='home_banner_title').parameter
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').parameter
    about_myself_welcome = GeneralSetting.objects.get(name='about_myself_welcome').parameter
    about_myself_footer = GeneralSetting.objects.get(name='about_myself_welcome').parameter

    # image
    header_logo = ImageSetting.objects.get(name='header_logo').file
    site_favicon = ImageSetting.objects.get(name='site_favicon').file
    home_banner_image = ImageSetting.objects.get(name='home_banner_image').file

    # Documents
    documents = Document.objects.all()

    # SocialMedia
    social_medias = SocialMedia.objects.all()


    context = {
        'documents': documents,

        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself_welcome': about_myself_welcome,
        'about_myself_footer': about_myself_footer,
        'social_medias': social_medias,
        'header_logo': header_logo,
        'site_favicon': site_favicon,
        'home_banner_image': home_banner_image,

    }
    return context




def index(request):

    #Skills
    skills = Skill.objects.all()

    #Ekperience
    experiences = Experience.objects.all()

    #Education
    educations = Education.objects.all()




    context = {


        'skills': skills,
        'experiences': experiences,
        'educations': educations,

    }

    return render(request, 'index.html', context=context)


def redirect_urls(request, slug):
    doc = get_object_or_404( Document, slug=slug)

    return redirect(doc.file.url)
