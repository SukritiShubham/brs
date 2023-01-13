from rest_framework import serializers
from .models import *


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ["id","company","quarter" , "profit" , "expected" , "submitted"]