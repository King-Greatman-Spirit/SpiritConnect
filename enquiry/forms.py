from django import forms
from .models import ContactForm

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = [
            'full_name',
            'email',
            'job_title',
            'phone',
            'channel',
            'subject',
            'message',
         ]
    def __init__(self, *args, **kwargs):
        super(EnquiryForm, self).__init__(*args, **kwargs)
        # self.fields['channel'].empty_label = 'Select How you heard about us'
        self.fields['channel'].widget.attrs['placeholder'] = 'Select How you heard about us'
        self.fields['channel'].widget.attrs['class'] = 'form-control'

        self.fields['full_name'].widget.attrs['placeholder'] = 'Enter Full Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['job_title'].widget.attrs['placeholder'] = 'Enter Job Title'
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['subject'].widget.attrs['placeholder'] = 'Enter Subject'
        self.fields['message'].widget.attrs['placeholder'] = 'Enter Message'

        for field in ('full_name', 'email', 'job_title', 'phone', 'subject'):
            self.fields[field].widget.attrs['class'] = 'form-control'

        self.fields['message'].widget.attrs['class'] = 'form-control'
