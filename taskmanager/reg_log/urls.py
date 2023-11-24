from django.conf import settings
from django.conf.urls.static import static
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_view, name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)