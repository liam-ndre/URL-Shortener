from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import KirrURL
# Create your views here.

def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
    return HttpResponse("Hello {sc}".format(sc=shortcode))

class KirrCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse("Hello Again {sc}".format(sc=shortcode))