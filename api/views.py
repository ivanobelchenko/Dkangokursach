from rest_framework.viewsets import ModelViewSet
from .serializers import NewsSerializer, UserSerializer, AuthorSerializer
from .models import User, News, Author
from rest_framework.generics import ListAPIView 
from rest_framework.decorators import action
from rest_framework.response import Response
import django_filters.rest_framework
from django.db.models import Q

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GetUserView(ListAPIView):
    queryset = User.objects.filter(Q(likes__gt=15))
    serializer_class = UserSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GetNewsView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['title', 'likes']

class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    @action(methods=['Delete'], detail=True, url_path='delete') 
    def delNews(self,request, pk=None):
        news=self.queryset.get(id=pk)
        news.delete()
        return Response('Новость была удалена')