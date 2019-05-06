"""trydjango18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from newsletter import views as myviews
from . import views
from django.views.generic.base import TemplateView
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',myviews.home,name="home"),
    path('contact',myviews.contact,name="contact"),
    path('about',views.about,name="about"),
    path('accounts/', include('registration.backends.default.urls')),
    #path('newsletter/', include('newsletter.urls')),
    #path('about',newsletter.)


    #tutorials link
    #path('c++',TemplateView.as_view(template_name="c++.html"),name="c++"),
    path('c++',views.Cpp.as_view(),name="c++"),
    path('java',views.Java.as_view(),name="java"),
    path('python',views.Python.as_view(),name="python"),
    # path('java',TemplateView.as_view(template_name="java.html"),name="java"),
    # path('python',TemplateView.as_view(template_name="python.html"),name="python"),


    #####################################################################################################
    #python links:


    #basics:

    path('python/intro/',TemplateView.as_view(template_name="pyintro.html"),name="pyintro"),
    path('python/install/',TemplateView.as_view(template_name="pyinstall.html"),name="pyinstall"),
    path('python/ide/',TemplateView.as_view(template_name="pyide.html"),name="pyide"),
    path('python/comments/',TemplateView.as_view(template_name="pycomm.html"),name="pycomm"),

    #control:
    path('python/if/',TemplateView.as_view(template_name="pyif.html"),name="pyif"),
    path('python/ifelse/',TemplateView.as_view(template_name="pyifelse.html"),name="pyifelse"),
    path('python/ifelif/',TemplateView.as_view(template_name="pyifelif.html"),name="pyifelif"),
    path('python/nestedif/',TemplateView.as_view(template_name="pynestedif.html"),name="pynestedif"),
    path('python/for/',TemplateView.as_view(template_name="pyfor.html"),name="pyfor"),
    path('python/while/',TemplateView.as_view(template_name="pywhile.html"),name="pywhile"),
    path('python/break/',TemplateView.as_view(template_name="pybreak.html"),name="pybreak"),
    path('python/cont/',TemplateView.as_view(template_name="pycont.html"),name="pycont"),

    #datatypes
    path('python/num/',TemplateView.as_view(template_name="pynum.html"),name="pynum"),
    path('python/list/',TemplateView.as_view(template_name="pylist.html"),name="pylist"),
    path('python/string/',TemplateView.as_view(template_name="pystring.html"),name="pystring"),
    path('python/tuple/',TemplateView.as_view(template_name="pytuple.html"),name="pytuple"),


    #functions
    path('python/func/',TemplateView.as_view(template_name="pyfunc.html"),name="pyfunc"),
    path('python/rec/',TemplateView.as_view(template_name="pyrec.html"),name="pyrec"),
    

    #oops
    path('python/oops/',TemplateView.as_view(template_name="pyoops.html"),name="pyoops"),
    path('python/class/',TemplateView.as_view(template_name="pyclass.html"),name="pyclass"),
    path('python/constructor/',TemplateView.as_view(template_name="pyconstructor.html"),name="pyconstructor"),
    




    #################################################################################################

    #c++ links:

    #basics:
    path('c++/hello',TemplateView.as_view(template_name="cpphello.html"),name="cpphello"),
    path('c++/var',TemplateView.as_view(template_name="cppvar.html"),name="cppvar"),
    path('c++/datatypes',TemplateView.as_view(template_name="cppdatatypes.html"),name="cppdatatypes"),
    path('c++/operators',TemplateView.as_view(template_name="cppoperators.html"),name="cppoperators"),


    #control statements:
    path('c++/if',TemplateView.as_view(template_name="cppif.html"),name="cppif"),
    path('c++/switch',TemplateView.as_view(template_name="cppswitch.html"),name="cppswitch"),
    path('c++/for',TemplateView.as_view(template_name="cppfor.html"),name="cppfor"),
    path('c++/while',TemplateView.as_view(template_name="cppwhile.html"),name="cppwhile"),
    path('c++/dowhile',TemplateView.as_view(template_name="cppdowhile.html"),name="cppdowhile"),
    path('c++/cont',TemplateView.as_view(template_name="cppcont.html"),name="cppcont"),
    path('c++/break',TemplateView.as_view(template_name="cppbreak.html"),name="cppbreak"),
    path('c++/goto',TemplateView.as_view(template_name="cppgoto.html"),name="cppgoto"),



    #functions:
    path('c++/func',TemplateView.as_view(template_name="cppfunc.html"),name="cppfunc"),
    path('c++/def',TemplateView.as_view(template_name="cppdef.html"),name="cppdef"),
    path('c++/rec',TemplateView.as_view(template_name="cpprec.html"),name="cpprec"),


    #arrays:
    path('c++/array',TemplateView.as_view(template_name="cpparray.html"),name="cpparray"),
    path('c++/multi',TemplateView.as_view(template_name="cppmulti.html"),name="cppmulti"),
    path('c++/pass',TemplateView.as_view(template_name="cpppass.html"),name="cpppass"),
    path('c++/string',TemplateView.as_view(template_name="cppstring.html"),name="cppstring"),

    #pointers
    path('c++/pointer',TemplateView.as_view(template_name="cpppointer.html"),name="cpppointer"),
    path('c++/this',TemplateView.as_view(template_name="cppthis.html"),name="cppthis"),


    #oops:
    path('c++/oops',TemplateView.as_view(template_name="cppoops.html"),name="cppoops"),
    path('c++/const',TemplateView.as_view(template_name="cppconst.html"),name="cppconst"),
    path('c++/dest',TemplateView.as_view(template_name="cppdest.html"),name="cppdest"),
    path('c++/struct',TemplateView.as_view(template_name="cppstruct.html"),name="cppstruct"),
    path('c++/funcpass',TemplateView.as_view(template_name="cppfuncpass.html"),name="cppfuncpass"),
    path('c++/enum',TemplateView.as_view(template_name="cppenum.html"),name="cppenum"),
    path('c++/inherit',TemplateView.as_view(template_name="cppinherit.html"),name="cppinherit"),
    path('c++/poly',TemplateView.as_view(template_name="cpppoly.html"),name="cpppoly"),
    path('c++/over',TemplateView.as_view(template_name="cppover.html"),name="cppover"),
    path('c++/override',TemplateView.as_view(template_name="cppoverride.html"),name="cppoverride"),
    path('c++/virtual',TemplateView.as_view(template_name="cppvirtual.html"),name="cppvirtual"),
    path('c++/encap',TemplateView.as_view(template_name="cppencap.html"),name="cppencap"),
    path('c++/abstract',TemplateView.as_view(template_name="cppabstract.html"),name="cppabstract"),
    path('c++/inter',TemplateView.as_view(template_name="cppinter.html"),name="cppinter"),
    path('c++/passobj',TemplateView.as_view(template_name="cpppassobj.html"),name="cpppassobj"),
    path('c++/friend',TemplateView.as_view(template_name="cppfriend.html"),name="cppfriend"),
    
##############################################################################################################


    #java links:
    
    #basics:
    path('java/intro',TemplateView.as_view(template_name="javaintro.html"),name="javaintro"),
    path('java/first',TemplateView.as_view(template_name="javafirst.html"),name="javafirst"),
    path('java/var',TemplateView.as_view(template_name="javavar.html"),name="javavar"),
    path('java/datatype',TemplateView.as_view(template_name="javadatatype.html"),name="javadatatype"),
    path('java/op',TemplateView.as_view(template_name="javaop.html"),name="javaop"),
    path('java/if',TemplateView.as_view(template_name="javaif.html"),name="javafirst"),
    path('java/switch',TemplateView.as_view(template_name="javaswitch.html"),name="javaswitch"),
    path('java/for',TemplateView.as_view(template_name="javafor.html"),name="javafor"),
    path('java/while',TemplateView.as_view(template_name="javawhile.html"),name="javawhile"),
    path('java/dowhile',TemplateView.as_view(template_name="javadowhile.html"),name="javadowhile"),
    path('java/cont',TemplateView.as_view(template_name="javacont.html"),name="javacont"),
    path('java/break',TemplateView.as_view(template_name="javabreak.html"),name="javabreak"),


    #oops:
    path('java/const',TemplateView.as_view(template_name="javaconst.html"),name="javaconst"),
    path('java/static',TemplateView.as_view(template_name="javastatic.html"),name="javastatic"),
    path('java/inherit',TemplateView.as_view(template_name="javainherit.html"),name="javainherit"),
    path('java/super',TemplateView.as_view(template_name="javasuper.html"),name="javasuper"),
    path('java/poly',TemplateView.as_view(template_name="javapoly.html"),name="javapoly"),
    path('java/inter',TemplateView.as_view(template_name="javainter.html"),name="javainter"),
    path('java/encap',TemplateView.as_view(template_name="javaencap.html"),name="javaencap"),
    path('java/access',TemplateView.as_view(template_name="javaaccess.html"),name="javaaccess"),
    

    #exception:
    path('java/handle',TemplateView.as_view(template_name="javahandle.html"),name="javahandle"),
    path('java/try',TemplateView.as_view(template_name="javatry.html"),name="javatry"),
    path('java/finally',TemplateView.as_view(template_name="javafinally.html"),name="javafinally"),
    path('java/throw',TemplateView.as_view(template_name="javathrow.html"),name="javathrow"),

    #collections:
    path('java/array',TemplateView.as_view(template_name="javaarray.html"),name="javaarray"),
    path('java/link',TemplateView.as_view(template_name="javalink.html"),name="javalink"),
    path('java/vect',TemplateView.as_view(template_name="javavect.html"),name="javavect"),
    path('java/hash',TemplateView.as_view(template_name="javahash.html"),name="javahash"),
    path('java/tree',TemplateView.as_view(template_name="javatree.html"),name="javatree"),
    path('java/hashset',TemplateView.as_view(template_name="javahashset.html"),name="javahashset"),
    path('java/treeset',TemplateView.as_view(template_name="javatreeset.html"),name="javatreeset"),
    path('java/linkhash',TemplateView.as_view(template_name="javalinkhash.html"),name="javalinkhash"),


    #misc:
    path('java/string',TemplateView.as_view(template_name="javastring.html"),name="javastring"),
    path('java/multi',TemplateView.as_view(template_name="javamulti.html"),name="javamulti"),
    path('java/serial',TemplateView.as_view(template_name="javaserial.html"),name="javaserial"),
    path('java/awt',TemplateView.as_view(template_name="javaawt.html"),name="javaawt"),
    path('java/swing',TemplateView.as_view(template_name="javaswing.html"),name="javaswing"),

]
