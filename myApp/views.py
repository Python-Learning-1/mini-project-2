from django.shortcuts import render
from .models import Product

from django.core.mail import send_mail
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import ContactForm

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')


def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            email_message = EmailMessage(
                subject=f"Contact Us Message from {name}",
                body=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.DEFAULT_FROM_EMAIL],
            )
            email_message.send()
            return render(request, 'contact_us.html', {'form': form, 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})

