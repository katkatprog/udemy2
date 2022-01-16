import imp
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets
from .serializers import TaskSerializer, UserSerializer, PostSerializer
from .models import Task, Post
# Create your views here.

class CreateUserView(generics.CreateAPIView):
    # ↑CreateAPIViewは、Createに特化したビュー
    serializer_class = UserSerializer
    permission_classes = (AllowAny, ) 
    # ↑デフォルトでは、全てのビューに対してJWT認証が適用される(settings.py参照)
    # ところが、ユーザー作成(signup)に関しては、認証が通ってない状態で行うので、AllowAnyに上書き

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny, )
    # ↑デフォルトでは、全てのビューに対してJWT認証が適用される(settings.py参照)
    # しかし、JWT認証を適用したいのはTaskのCRUDに対してなので、それ以外のビューはAllowAnyに設定

class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny, )

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny, )

class TaskRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny, )

class TaskViewSet(viewsets.ModelViewSet):
    #これがTaskのCRUDを行うビュー。ModelViewSetを継承するとCRUDが全てできる。
    #このビューに対してはJWT認証を適用させたいので、AllowAnyは設定しない。
    queryset = Task.objects.all()
    serializer_class = TaskSerializer