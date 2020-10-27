from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'myapp/index', views.index, name='index'),
    path(r'myapp/about', views.about, name='about'),
    path(r'myapp/<int:topic_id>', views.detail, name='detail')
    ]
