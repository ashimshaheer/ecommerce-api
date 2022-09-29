
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import UserSerializer,ProductSerializer
from rest_framework import generics,serializers,permissions
from .models import Product
# Create your views here.

@api_view(['POST'])
def login_api(request):
    serializer=AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user =serializer.validated_data['user']
    _,token=AuthToken.objects.create(user)

    return Response({
        'user_info': {
            'id':user.id,
            'username':user.username,
            'email':user.email
        },
        'token':token
    })

@api_view(['GET'])
def get_user_data(request):
    user=request.user
    
    if user.is_authenticated:
        return Response({
            'user_info':{
                'id':user.id,
                'username':user.username,
                'email':user.email
            }
        })

    return Response({'error':'not authenticated'},status=400)

@api_view(['POST'])
def register_api(request):
    serializer=UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user=serializer.sava()
    _,token=AuthToken.objects.create(user)

    return Response({
        'user_info': {
            'id':user.id,
            'username':user.username,
            'email':user.email
        },
        'token':token
    })

class Listproduct(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class Detailproduct(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


def  add_product(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        desc=request.POST.get('desc')
        image=request.FILES['upload']
        sellername=request.user
        product= Product(name=name,price=price,desc=desc,image=image,seller_name=sellername)
        product.save()

        return Response({
        'product_info': {
            'name':Product.name,
            'price':Product.price,
            'desc':Product.desc
        },
        
    })
    return Response({
        'product_info': {
            'name'
            'price'
            'desc'
        },
        
    })
  
