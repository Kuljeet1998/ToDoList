from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from lists.serializers import *
# Create your views here.

@csrf_exempt

def lists_list(request):
	if (request.method=='GET'):
		lists=Todo.objects.all()
		serializer=ListsSerializer(lists,many=True)
		return JsonResponse(serializer.data,safe=False)

	elif(request.method=='POST'):
		data=JSONParser().parse(request)
		serializer=ListsSerializer(data=data)
		if(serializer.is_valid()):
			serializer.save()  #calls create fn in serializer
			return JsonResponse(serializer.data,status=201)
		return JsonResponse(serializer.errors,status=400)


@csrf_exempt
def lists_detail(request,pk):
	try:
		lists=Todo.objects.get(pk=pk)
	except Todo.DoesNotExist:
		return HttpResponse(status=404)

	if(request.method=='GET'):
		serializer=ListsSerializer(lists)
		return JsonResponse(serializer.data)

	elif(request.method=='PUT'):
		data=JSONParser().parse(request)
		serializer=ListsSerializer(lists,data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors,status=400)

	elif(request.method=='DELETE'):
		lists.delete()
		return HttpResponse(status=204)

	elif(request.method=='PATCH'):
