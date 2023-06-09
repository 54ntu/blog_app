from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index_post'),
    path('show/<int:id>',views.show,name='show_post'),
    path('about/',views.about,name='about_post'),
    path('contact/',views.contact_post,name="contact_post"),

]
