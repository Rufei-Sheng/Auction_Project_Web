from django.conf.urls import url
from . import  views


urlpatterns = [
    url(r'^register/', views.register),
    url(r'^login/', views.login),
    url(r'^publish/', views.publish),
    url(r'^get_product_list/', views.get_product_list),
    url(r'^get_prise/', views.get_prise),
    url(r'^add_prise/', views.add_prise),
    url(r'^add_buy/', views.add_buy),
    url(r'^get_auction_list/', views.get_auction_list),
    url(r'^get_post_list/', views.get_post_list),
    url(r'^up_user_info/', views.up_user_info),
    url(r'^del_user_info/', views.del_user_info),
    url(r'^get_liked/', views.get_liked),
    url(r'^update_end_success/', views.update_end_success),
]