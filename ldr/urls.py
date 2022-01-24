from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ldr import views

urlpatterns = [
    path('messages/', views.MessageList.as_view()),
    path('messages/<int:pk>/', views.MessageDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('setread/<int:pk>/', views.SetRead.as_view()),
    path('unread/', views.Unread.as_view())
]
# to set read, use http -a peterlok:Sunhero123 PATCH http://127.0.0.1:8080/setread/<id>/ read=True (remember whitespace)
urlpatterns = format_suffix_patterns(urlpatterns)