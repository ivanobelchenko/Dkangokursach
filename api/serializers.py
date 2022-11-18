from rest_framework.serializers import ModelSerializer
from .models import User, Author, News


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'