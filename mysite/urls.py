from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("welcome page")


urlpatterns = [
    path("", welcome),
    path("polls/", include("polls.urls")),
    path("auth/", include('accounts.urls')),
    path("admin/", admin.site.urls),
    
]

