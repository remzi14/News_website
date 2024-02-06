from django.contrib import admin
from django.urls import path
from .views import home,aloqa,single,sport_new,texno,mahaliy_new,xorij,SearchNew,addnew,addcat,Editnew,Delet


urlpatterns=[
    path('',home,name='saxifa'),
    path('aloqa/',aloqa,name='alo'),
    path('sport/',sport_new,name='sports'),
    path('texno/',texno,name='tex'),
    path('xorij/',xorij,name='xo'),
    path('mahal/',mahaliy_new,name='mahaliy'),
    path('single/<slug:slug>/',single,name='page'),
    path('search/',SearchNew,name='qidir'),
    path('add/',addnew,name='ad'),
    path('add_cat/',addcat,name='ad_cat'),
    path('edit/<slug:slug>/',Editnew,name='edit'),
    path('delet/<slug:slug>/',Delet,name='del'),
]


