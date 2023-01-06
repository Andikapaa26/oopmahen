from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('form/', views.form, name='tambah' ),
    path('<int:id>/', views.form, name='ubah' ),
    path('hapus/<int:id>/', views.hapus, name='hapus'), 
    path('list/', views.list, name='list'), 
    path('', views.index, name='index'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('tambahpeta/', views.formpeta, name='tambahpeta' ),
    path('peta/', views.peta, name='peta'),
    path('<int:id>//', views.formpeta, name='ubahpeta'),
    path('hapuspeta/<int:id>/', views.hapuspeta, name='hapuspeta'),

]
