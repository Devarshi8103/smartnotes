from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer

# Create your views here.
# request - response , request handler , action

def say_hello(request):
    
    #Pull data , transform , send email
    return render(request,'hello.html', {'name':'jethya'})

def index(request):
    obj=User.objects.all()
    context={
        "obj":obj,
    }
    return render(request,'index.html',context)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer