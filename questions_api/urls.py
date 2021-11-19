from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/useraccount', views.UserAccountList.as_view(), name='useraccount_list'),
    path('api/useraccount/<int:pk>', views.UserAccountDetail.as_view(), name='useraccount_detail'),
    path('api/useraccount/login', csrf_exempt(views.check_login), name="check_login"),
    path('api/questions', views.QuestionList.as_view(), name='question_list'),
    path('api/questions/<int:pk>', views.QuestionDetail.as_view(), name='question_detail'),
    path('api/comments',views.CommentList.as_view(),name='comment_list'),
    path('api/comments/<int:pk>',views.CommentDetail.as_view(), name='comment_detail'),

]
