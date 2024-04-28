from organization.models import Organization
from django.shortcuts import render, redirect
from .models import ContactForm
from .forms import EnquiryForm
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            data = ContactForm()
            data.full_name = form.cleaned_data['full_name']
            data.email = form.cleaned_data['email']
            data.job_title = form.cleaned_data['job_title']
            data.phone = form.cleaned_data['phone']
            data.channel = form.cleaned_data['channel']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.save()
            messages.success(request, 'Thank you! Your enquiry has been successfully submitted.')
        return redirect('contact')

    else:
        form = EnquiryForm()

    context = {

        'form': form,

    }
    return render(request, 'contact.html', context)
