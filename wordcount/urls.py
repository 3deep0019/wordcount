
from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='home'),
    path('Count/',views.count),
    path('About Me/',views.about_me,name='about_me')
]
