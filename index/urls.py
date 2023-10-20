from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('course/', course, name='course'),
    path('batch/', batch, name='batch'),
    path('sign_up/', signup, name='signup'),
    path('sign_in/', signin, name='signin'),
    path('sign_out/', signout, name='signout'),
    path('feedback/', feedback, name='feedback'),
    path('dashboard/', dashboard, name='dashboard'),

    path('course_details/<str:coursetag>', course_details, name='course_details'),
]