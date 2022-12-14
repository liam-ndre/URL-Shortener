"""kirr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, re_path
from django.contrib import admin

from shortener.views import kirr_redirect_view, KirrCBView

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^a/(?P<shortcode>[\w-]+)/$', kirr_redirect_view),
    re_path(r'^b/(?P<shortcode>[\w-]+)/$', KirrCBView.as_view()),
]
