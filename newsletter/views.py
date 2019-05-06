from django.shortcuts import render
from django.conf import settings
from .forms import SignUpForm,ContactForm
from django.core.mail import send_mail
from .models import SignUp
from django.utils import translation
# Create your views here.
def home(request):
    if 'lang' in request.GET:
        translation.activate(request.GET.get('lang'))
    print(SignUp.objects.all())


    for o in SignUp.objects.all():
        print(o.full_name)
    form=SignUpForm(request.POST or None)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.save()
    title="Welcome"
    if request.user.is_authenticated:
        title="Hello MR.{g}".format(g=request.user)
    return render(request,"home.html",{"t":title,"form":form})
def contact(request):
    title="Contact Me"
    form=ContactForm(request.POST or None)
    if form.is_valid():
        email=form.cleaned_data.get('email')
        message=form.cleaned_data.get('message')
        full_name=form.cleaned_data.get('full_name')
        from_email=settings.EMAIL_HOST_USER
        send_mail('Contact App mail','Test with code mail',from_email,[from_email,'priyadamani94@gmail.com',],fail_silently=False,)
    context={"form":form,"title":title}
    return render(request,"forms.html",context)