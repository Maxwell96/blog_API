from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth import get_user_model

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

class UserDetail(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()