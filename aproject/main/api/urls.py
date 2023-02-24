from django.urls import path, re_path
from . import views

app_name = 'main'

urlpatterns = [
  
    path('register/',views.register_list,name='user_list'),
    path('register/<pk>/',views.register_detail,name='user_detail'),

    path('works/',views.WorksListView.as_view(),name='work'),
    path('artist/',views.WorksListView.as_view(),name='artist'),

 
]
