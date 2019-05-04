"""pizzashop_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from pizzashop_app import views

from django.contrib.auth.views import LoginView, LogoutView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('pizzashop_app/sign_in/', LoginView.as_view(template_name='pizzashop_app/sign_in.html'), name='pizzashop_app-sign_in'),
    path('pizzashop_app/sign_out/', LogoutView.as_view(next_page='/'), name='pizzashop_app-sign_out'),
    path('pizzashop_app/', views.pizzashop_app_home, name='pizzashop_app-home'),
    path('pizzashop_app/sign_up', views.pizzashop_app_sign_up, name='pizzashop_app_sign_up'),
    path('pizzashop_app/account', views.pizzashop_app_account, name='pizzashop_app_account'),
    path('pizzashop_app/pizza', views.pizzashop_app_pizza, name='pizzashop_app_pizza'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
