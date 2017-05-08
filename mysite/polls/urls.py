from django.conf.urls import url

from . import views

app_name='polls'
urlpatterns=[
    url(r'^$',views.index,name="index"),
    url('marble/',views.marble,name="marble"),
    url('wishlist/',views.wishlist,name="wishlist"),
    url('vote/',views.vote,name="vote"),
]
