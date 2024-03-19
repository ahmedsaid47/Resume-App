from django.shortcuts import render
from django.http import JsonResponse
from core.models import Document
from contact.models import Message
from contact.forms import ContactForm

# Create your views here.

def contact_form(request):


    if request.POST:
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            Message.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )

            contact_form.send_mail()


            success = True
            message = 'Contact from sent successfully!'
        else:
            success = False
            message = 'Please fill in the form properly!'
    else:
        success = False
        message = 'Something went wrong!'


    context={
        'success': success,
        'message': message,
    }
    return JsonResponse(context)

def contact(request):


    contact_form = ContactForm()
    documents = Document.objects.all()
    context = {
        'contact_form': contact_form,
        'documents': documents,
    }

    return render(request, 'contact.html', context=context)


