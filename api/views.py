from datetime import datetime
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import URLShortenModel
import random
from .serializers import URLShortenSerializer
import os
from dotenv import load_dotenv
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
load_dotenv('../.env')

# BASE_URL="http://127.0.0.1:8000/"
characters_available="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!*^$-_"

@api_view(['POST','GET'])
def shorten_url(request,name=None):
    if request.method=='POST':
        data=request.data
        suffix_url=("".join(random.sample(characters_available,6)))
        shorturl=os.environ.get("BASE_URL")+suffix_url
        URLShortenModel.objects.create(
            name=data['name'] or "No Name",
            long_url=data['longurl'],
            short_url=shorturl
        )
        return Response({'name':data['name'],'longurl':data['longurl'],'shorturl':shorturl })

    elif request.method=='GET':
        try:
            name=request.query_params.get('name',None)
            snippet=URLShortenModel.objects.get(name=name)
            serializer=URLShortenSerializer(snippet)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

def redirect_url(request,urlname):
    try:
        urlname=os.environ.get("BASE_URL")+urlname
        url_obj=URLShortenModel.objects.get(short_url=urlname)
        if url_obj is not None:
            longurl=url_obj.long_url
            return redirect(longurl)
    except ObjectDoesNotExist as e:
        print(e)

