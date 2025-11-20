from django.http import JsonResponse

def transacoes(request):
    if request.method == "GET":
        transacao = {
            'id': '1',
            'nome': '',
            'valor': '',
            'horario': ''
        }
        return JsonResponse(transacao)