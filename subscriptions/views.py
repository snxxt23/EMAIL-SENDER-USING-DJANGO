from subscriptions.forms import SubscribeForm
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render,redirect


def sendmail_(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = "This is the subject,sample example for django mail"
            message = "Body of mail,this is a test message"
            receipient = form.cleaned_data.get('email')
            send_mail(subject, message, settings.EMAIL_HOST_USER, [receipient], fail_silently=True)
            messages.success(request,'Message send successfully!')
            return redirect('sendmail_')
        else:
            return render(request,'detail.html',{'form':form})
    else:
        return render(request,'detail.html',{'form':form})
    