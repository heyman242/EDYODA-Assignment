from django.urls import path
from . import views

app_name = 'MelodyShare'

urlpatterns = [
    #path('', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),

]