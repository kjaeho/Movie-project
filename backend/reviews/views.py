from django.shortcuts import render,get_object_or_404
from .serializers import ReviewListSerializer, ReviewSerializer, CommentSerializer
from .models import Review, Comment
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET'])
def review_list(request,movie_pk):
    review_list = Review.objects.filter(movie_id=movie_pk)
    serializer = ReviewSerializer(review_list,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request):
    serializer=ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(writer=request.user)
        return Response(serializer.data)

@api_view(['POST'])
def update_review(request,review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    print(request.data)
    serializer = ReviewSerializer(data=request.data,instance=review)

    if serializer.is_valid(raise_exception=True):
        serializer.save(writer=request.user)
        return Response()

@api_view(['DELETE'])
def delete_review(request,review_pk):
    review=get_object_or_404(Review,pk=review_pk)
    review.delete()
    return Response()


@api_view(['GET'])
def comment_List(reqeuest,review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    comments = review.comment_set.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_comment(request,review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(writer=request.user, review=review)
        return Response(serializer.data)

@api_view(['POST'])
def update_comment(request,comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    serializer = CommentSerializer(data=request.data,instance=comment)
    if serializer.is_valid():
        serializer.save(writer=request.user)
        return Response()

@api_view(['DELETE'])
def delete_comment(request,comment_pk):
    comment=get_object_or_404(Comment,pk=comment_pk)
    comment.delete()
    return Response()    