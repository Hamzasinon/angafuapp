"""
URL configuration for angapro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from angaapp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('home2', home2, name='home2'),
    path('reserve/<int:societe_id>', reserve, name='reserve'),
    path('addreserve/<int:societe_id>', addreserve, name='addreserve'),
    path('api/societes/', SocieteListView.as_view(), name='societe-list'),
    path('api/reserve/', ReservationsListView.as_view(), name='reserve-list'),
    path('api/heur/', HeurListView.as_view(), name='heur-list'),
    path('api/destination/', DetinationListView.as_view(), name='destination-list'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
