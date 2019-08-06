from rest_framework import serializers
from . import models

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'user', 'title', 'content', 'publishing_date', 'image', 'slug', )
        model = models.Post