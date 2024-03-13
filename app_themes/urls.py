from django.urls import path

from .views import home,themes,pupil,show_pupil,show_themes,exam,price

urlpatterns = [
    path('themes/',themes,name='themes'),
    path('pupil/',pupil,name='pupil'),
    path('exam/',exam,name='exam'),
    path('pupils/<int:pk>', show_pupil, name='pupils'),
    path('topic/<int:pk>', show_themes, name='topic'),
    path('price/<int:pk>', price, name='price'),
    path('',home,name='home'),
]