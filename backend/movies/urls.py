from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('recent-list/<int:page_num>/<int:flag>/',views.recentList),
    path('listby-category/<str:genre>/<str:nation>/<str:year>/<int:page_num>/<int:sort>/',views.listByCategory),
    path('listby-genre/<str:genre>/<int:page_num>/',views.listByGenre),
    path('listby-yearly/<str:year>/<int:page_num>/',views.listByYear),
    path('listby-actor/<str:actor>/<int:page_num>/',views.listByActor),
    path('listby-keyword/<str:keyword>/<int:page_num>/',views.listByKeyword),
    path('listby-dirctor/<str:year>/<int:page_num>/',views.listByDirctor),
    path('listby-nation/<str:nation>/<int:page_num>/',views.listBynation),
    path('movie-serach/<str:word>/',views.movieSearch),
    path('today/movie/',views.todaymovies),
    path('tenmillion/',views.tenmillion),
    path('<str:movie_pk>/', views.movieDetail),
    path('tenmillion/',views.tenmillion),

    path('rate-movie/<str:movie_pk>/', views.rate_movie),
    path('cancel-rating/<str:movie_pk>/', views.cancel_rating),
    path('get-rating/<str:movie_pk>/', views.get_rating),


    # 유저 성향 추천 영화
    path('recommend/ratinguser/', views.recommend_rating_movie),
    path('recommend/rating/', views.recommend_rating_user),

    path('most-viewed/director/',views.most_viewed_director),
    path('most-viewed/genre/',views.most_viewed_genre),
    path('most-viewed/keyword/',views.most_viewed_keyword),
    path('most-viewed/actor/',views.most_viewed_actor),
]   