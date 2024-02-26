"""djangoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

# this is used for when i connect to URL's
# so how do i connect mongoose to it?

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
#from ..database import app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),
    path('', TemplateView.as_view(template_name="Home.html")),
    path('about/', TemplateView.as_view(template_name="About.html")),
    path('contact/', TemplateView.as_view(template_name="Contact.html")),
    path('login/', TemplateView.as_view(template_name="index.html")),
    path('register/', TemplateView.as_view(template_name="index.html")),
#    path('fetchReviews/', include('database.app')),
#    path('fetchReviews/', include('djangoapp.urls')),
#    path('fetchReviews/', TemplateView.as_view(template_name="index.html")),
#    path('fetchDealers/', TemplateView.as_view(template_name="index.html")),
#    path(route='fetchDealers', view=views.logout_request, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


