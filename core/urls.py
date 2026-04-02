from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/3rdparty/login/cancelled/', RedirectView.as_view(url='/', permanent=False)),
    path('accounts/', include('allauth.urls')),
    path('', include('main.urls')),
    path('settings/', include('theme.urls')),
]