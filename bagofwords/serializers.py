from django.contrib.auth.models import User, Group
from bagofwords.models import Sentiment, Dictionary 
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model = Group
        fields = ('url', 'name')

class SentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentiment
        fields = ('id', 'unit', 'positivity', 'negativity', 'objectivity', 'polarity', 'dictionary')

class DictionarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dictionary
        fields = ('id', 'name')
