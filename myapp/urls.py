from django.urls import path
from .import views
urlpatterns =[
    path('',views.index, name='index'),
    path('register/',views.register),
    path('index/',views.index),
    path('about/',views.about),
    path('service/',views.service),
    path('price/',views.price),
    path('booking/',views.bookings),
    path('contact/',views.contact),
    path('login/', views.login, name= 'login'),
    path('logout/', views.logoutUser, name='logout'),
    path('up/',views.userpage),
    path('book/',views.booking1),
    path('book1/',views.booking2),
    path('book2/',views.booking3),
    path('vb/',views.viewbook),
    path('cb/',views.cancelbook),
    path('canb/<int:id>/',views.removebooking),
    path('nfeed/', views.addfeedback),
    path('passs/',views.changepassword),
]