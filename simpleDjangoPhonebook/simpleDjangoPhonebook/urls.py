from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
import rest_auth

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
