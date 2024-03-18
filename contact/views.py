from django.shortcuts import render
from django.http import JsonResponse
from core.models import Document
from contact.models import Message

# Create your views here.

def contact_form(request):

    if request.method == 'POST':
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

        success = True
        message = 'Contact from sent successfully!'
    else:
        success = False
        message = 'Something went wrong!'


    context={
        'success': success,
        'message': message,
    }
    return JsonResponse(context)

def contact(request):
    documents = Document.objects.all()

    context = {
        'documents': documents,
    }
    return render(request, 'contact.html', context=context)


