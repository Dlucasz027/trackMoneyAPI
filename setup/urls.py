
from django.contrib import admin
from django.urls import path
from finance.views import transacoes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('transacoes/', transacoes, name='transacoes'),
]
