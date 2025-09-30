from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Email

from . forms import EmailForm

# Create your views here.
def index(request):

    form = EmailForm()

    context = {
        'form': form,
    }

    if (request.method == 'POST'):

        # Validating Email and input data
        form = EmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            mail_data = Email.objects.create(name=name, email=email, message=message)
            mail_data.save()

            return redirect('index'),  # Redirect to the same page to show the success message
    
    return render(request, 'portfolio/index.html', context=context)