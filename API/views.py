from .serializers import PersonSerializer
from .models import Person
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def personDetail(requst, format=None):
    if requst.method == 'GET':
        perosn = Person.objects.all()
        serializer = PersonSerializer(perosn, many=True)
        return Response(serializer.data)
    if requst.method == 'POST':
        serialize = PersonSerializer(data=requst.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        
@api_view(['PUT', 'DELETE', 'GET'])
def personid(request, id, format=None):
    
    try:
        person = Person.objects.get(pk=id)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)