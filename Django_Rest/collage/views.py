from django.shortcuts import render
from .models import Collage
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from .models import Collage
from .serializer import PostSerializer
# Create your views here.
def home1(request):
    list = Collage.objects.all()
    context ={
        'collages':list
    }
    return render(request,'home.html',context)

@api_view(['GET','POST'])
def product(request):
   if request.method == 'GET':
   	  list = Collage.objects.all()
   	  serializer = PostSerializer(list,many=True)
   	  return Response(serializer.data)


   elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
        	 serializer.save()
        	 return Response(serializer.data,status=status.TTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)	



@api_view(['GET','PUT','DELETE'])
def product_detail(request,pk):
    try:
        list = Collage.objects.get(id=pk)

    except Product.DoesNotExist:
        return Response(status= status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = PostSerializer(list)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(list,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


   
