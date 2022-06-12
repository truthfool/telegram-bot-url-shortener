from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import URLShortenModel
import random
from .serializers import URLShortenSerializer
# Create your views here.

BASE_URL="http://127.0.0.1:8000/"
characters_available="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!*^$-_"

@api_view(['POST','GET'])
def shorten_url(request,name=None):
    if request.method=='POST':
        data=request.data
        suffix_url=("".join(random.sample(characters_available,6)))
        shorturl=BASE_URL+suffix_url
        URLShortenModel.objects.create(
            name=data['name'] or "",
            long_url=data['longurl'],
            short_url=shorturl
        )
        return Response({'name':data['name'],'longurl':data['longurl'],'shorturl':shorturl })

    if request.method=='GET':
        try:
            snippet=URLShortenModel.objects.filter(name=name)
            serializer=URLShortenSerializer(snippet)
            return Response(serializer.data)
        except URLShortenModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

def redirect_url(request,shorturl):
    try:
        url_obj=URLShortenModel.objects.filter(short_url=shorturl)
        if url_obj is not None:
            longurl=url_obj.long_url
            return redirect(longurl)
    except BaseException as e:
        return e

