from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    #review
    path('<int:movie_pk>/review-list/',views.review_list),
    path('<int:review_pk>/review-detail/',views.review_detail),
    path('create-review/',views.create_review),
    path('<int:review_pk>/update-review/',views.update_review),
    path('<int:review_pk>/delete-review/',views.delete_review),
    #comment
    path('<int:review_pk>/comment-list/',views.comment_List),
    path('<int:review_pk>/create-comment/',views.create_comment),
    path('<int:comment_pk>/update-comment/',views.update_comment),
    path('<int:comment_pk>/delete-comment/',views.delete_comment),
]