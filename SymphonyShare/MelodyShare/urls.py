from django.urls import path
from . import views

app_name = 'MelodyShare'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('main/id/<int:user_id>/', views.main, name='main'),
    path('main/upload/id/<int:user_id>/', views.upload, name='upload'),

]