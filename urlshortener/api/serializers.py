from csv import field_size_limit
from rest_framework import serializers
from .models import URLShortenModel

class URLShortenSerializer(serializers.ModelSerializer):
    class Meta:
        model=URLShortenModel
        fields='__all__'
