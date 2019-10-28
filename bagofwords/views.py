from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bagofwords.models import Sentiment, Dictionary
from bagofwords.serializers import UserSerializer, GroupSerializer, SentimentSerializer, DictionarySerializer
from bagofwords.modifiers import Modifiers

@api_view(['POST'])
def analyze(request):
    text = request.POST['text_to_analyze']
    # 1- turn the text into words

    #text = Modifiers.lowercase_and_cleanup(text)
    #text = Modifiers.remove_stop_words(text)
    #text = Modifiers.stemmize(text)
    text = Modifiers.lemmatize(text)
    word_list = Modifiers.turn_text_into_words(text[0])

    # 2- get all the words from dictionary - Parametricize this with a dictionary id 
    dictionary_list = get_all_dictionary_words()
    
    # 3- get the intersection
    detected_sentiments = set(word_list).intersection(dictionary_list)

    # Phase 2:
    # 4- get the values of intersection
    result_list = []
    for word in detected_sentiments:
        sentiment = Sentiment.objects.filter(unit=word).first()
        result_list.append(sentiment)
    # values = 
    # 5- print out the amount of negative words
    # 6- print out the amount of positive words
    # 7- print out objectivity sum
    # 8- print out polarity sum
    # 9- print out 
   
    serializer = SentimentSerializer(result_list, many=True)
    return Response(serializer.data)
    #return Response({"detected": result})

def get_all_dictionary_words():
    sentiments = Sentiment.objects.values_list('unit', flat=True)
    return list(sentiments)

# Default object serializers start below
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SentimentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sentiment units to be viewed or edited.
    """
    queryset = Sentiment.objects.all().order_by('id')
    serializer_class = SentimentSerializer
    lookup_field = 'unit'

class DictionaryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows dictionaries to be viewed or edited.
    """
    queryset = Dictionary.objects.all().order_by('id')
    serializer_class = DictionarySerializer
