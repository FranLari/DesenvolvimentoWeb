from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(["GET"])
def welcome(request):
	content = {"message": "Minha primeira view em Django!"}
	return JsonResponse(content)

@api_view(["GET"])
def disciplina(request):
	disciplina = [
		{"Nome da Disciplina": "Matemática Aplicada", "UNID1":"8","UNID2":"9", "Media Final":"8.5", "Situação":"Aprovado"},
	{"Nome da Disciplina": "Banco de Dados", "UNID1":"8","UNID2":"9", "Media Final":"8.5", "Situação":"Aprovado"}
	]
	return JsonResponse(disciplina, safe-false)
	