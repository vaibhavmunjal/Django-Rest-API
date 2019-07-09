from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from drfApi import views

urlpatterns = [
    path('drf/', views.SnippetList.as_view()),
    path('drf/<int:pk>/', views.SnippetDetail.as_view()),
    path('vanilla/', views.get_create_data),
    path('vanilla/<int:pk>/', views.retrieve_put_patch_delete),
]

urlpatterns = format_suffix_patterns(urlpatterns)