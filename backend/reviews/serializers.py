from .models import Review, Comment
from rest_framework import serializers
from accounts.serializers import UserSerializer

class ReviewListSerializer(serializers.ModelSerializer):
    writer = UserSerializer(required=False)
    class Meta:
        model = Review
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    writer = UserSerializer(required=False)
    class Meta:
        model = Review
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    writer = UserSerializer(required=False)
    review = ReviewSerializer(required=False)  
    class Meta:
        model = Comment
        fields = '__all__'