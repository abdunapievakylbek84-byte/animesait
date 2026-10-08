from django.urls import path
from .views import home  # <-- ДОБАВЬТЕ ЭТУ СТРОКУ

urlpatterns = [
    path('', home, name='home'),
]