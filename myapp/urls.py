from django.urls import path
from myapp import views

urlpatterns =[
    path('weicome/',views.karibu),
    path('',views.welcome,name='my_index'),
    path('about/',views.aboutus,name='my_aboutus'),
    path('services/',views.services,name='my_service'),
    path('contact/',views.contactus,name='my_contact'),
    path('gallery/',views.gallery,name='my_gallery')

]