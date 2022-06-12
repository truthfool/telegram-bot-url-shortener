from django.urls import path
from . import views

urlpatterns = [
    path('shorten/',views.shorten_url,name='shortenurl'),
    path('<str:shorturl>',views.redirect_url,name='redirect_shorturl')
]
