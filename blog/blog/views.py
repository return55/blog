from django.contrib.auth.views import logout_then_login
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

#finita
def logout_view(request):
    return logout_then_login(request)

def index(request):
    return HttpResponseRedirect(reverse('articolo:index'))

