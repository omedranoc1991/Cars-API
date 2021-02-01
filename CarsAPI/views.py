from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cars
from .serializers import CarSerializer

@api_view(['GET'])
def cars_list(request):   
    if request.method == 'GET':
        cars = Cars.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def car_detail(request,pk):
    try:
        detail = Cars.objects.get(pk=pk)
    except Cars.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CarSerializer(detail)
        return Response(serializer.data)

@api_view(['POST'])
def car_create(request):    
    if request.method == 'POST':        
        serializer = CarSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def car_update(request,pk):    
    if request.method == 'PUT':
        detail = Cars.objects.get(pk=pk)
        serializer = CarSerializer(detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['DELETE'])
def car_delete(request,pk):
    if request.method == 'DELETE':
        detail = Cars.objects.get(pk=pk)
        detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   
   
