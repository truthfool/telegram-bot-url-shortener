from django.urls import path
from . import views

urlpatterns = [
    path('shorten/',views.shorten_url),
    path('shorten/<str:name>/',views.shorten_url),
    path('<str:urlname>',views.redirect_url)
]
