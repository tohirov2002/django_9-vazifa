from django.urls import path

from .views import home,themes,pupil,show_pupil

urlpatterns = [
    path('themes/',themes,name='themes'),
    path('pupil/',pupil,name='pupil'),
    path('pupils/<int:pk>', show_pupil, name='pupils'),
    path('',home,name='home'),
]