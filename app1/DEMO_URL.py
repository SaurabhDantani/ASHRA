from django.contrib import admin
from django.urls import path

from.import views

urlpatterns = [

    #path('admin/', admin.site.urls),
    path('header',views.header,name="header"),
    #path('contact',views.contact,name="contact"),
    path('',views.index,name="index"),
    path('footer',views.footer,name="footer"),
    path('contact',views.contact,name="contact"),
    path('why-us',views.why,name="why"),
    path('client',views.client,name="client"),
    path('skills',views.skills,name="skills")
]