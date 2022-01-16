from dataclasses import field
from pyexpat import model
from statistics import mode
from rest_framework import serializers
from .models import Task, Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        #create user(これを使わないと、パスワードが暗号化されない。。)
        user = User.objects.create_user(**validated_data)
        return user

class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    # ↑日付データをそのまま扱うと長くなるので、上記のようにフォーマットを指定している。

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created_at')

class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-$m-%d %H:%M:%S", read_only=True)
    # ↑日付データをそのまま扱うと長くなるので、上記のようにフォーマットを指定している。

    class Meta:
        model = Task
        fields = ('id', 'title', 'created_at')
