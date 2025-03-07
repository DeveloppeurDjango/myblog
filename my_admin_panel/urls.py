from django.urls import path
from .views import *

urlpatterns = [
    path('', appadmin, name='appadmin'),
    path('my-articles', user_article, name='my-articles'),

]