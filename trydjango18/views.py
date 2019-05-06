from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
# Create your views here.
def about(request):
    context={}
    return render(request,"about.html",context)


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls,**kwargs):
        view=super(LoginRequiredMixin,cls).as_view(**kwargs)
        return login_required(view)

class Cpp(LoginRequiredMixin,TemplateView):
    template_name="c++.html"


class Java(LoginRequiredMixin,TemplateView):
    template_name="java.html"


class Python(LoginRequiredMixin,TemplateView):
    template_name="python.html"