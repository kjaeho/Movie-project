from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
   path('userdetail/', views.userdetail, name='userDetail'),
   path('rating-check/',views.user_rating_check),
   path('update-user/<str:useremail>/', views.updateUser),
]