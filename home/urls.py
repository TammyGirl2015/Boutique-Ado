#from django.contrib import admin
#from django.urls import path
#from . import views

#urlpatterns = [
#    path('', 'http://8000-tammygirl20-boutiqueado-he3fbmrbdyi.ws.codeinstitute-ide.net/', views.home, name='home'),
#] 

from django.contrib import admin
from django.urls import path, include
from . import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.index, name='home'),
]
