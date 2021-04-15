from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.loginUser,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('signup',views.signup,name='signup'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('sell',views.sell,name='sell'),
    path('search',views.search,name='search'),
    path('buy/<int:myid>',views.buy,name='buy')
]