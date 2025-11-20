from django.contrib import admin
from finance.models import *

class FinanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email', 'valor', 'tipo', 'data', 'categoria', 'descricao')
    list_display_links = ('id', 'nome', 'cpf', 'email')
    list_per_page = 20
    search_fields = ('id', 'nome', 'cpf')

admin.site.register(finance, FinanceAdmin)
