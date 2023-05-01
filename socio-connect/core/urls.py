from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('changepass', views.changepass, name='changepass'),
    #path('passw', views.passw, name='passw'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('feedback', views.feedback, name='feedback'),
    path('like-post', views.like_post, name='like-post'),
    path('deletepost/<str:id>', views.deletepost, name='deletepost'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('aboutus', views.aboutus, name='aboutus'),
    
]

