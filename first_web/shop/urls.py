from django.urls import path
from . import views
urlpatterns = [
########进货的url#######
    path('jinhuo/', views.jinhuo_list),
    path('jinhuo/add_jinhuo/', views.add_jinhuo),
    path('jinhuo/del_jinhuo/', views.del_jinhuo),
    path('jinhuo/edit_jinhuo/', views.eidt_jinhuo),
    path('', views.shouye),
    path('jinhuo/search_jinhuo/', views.search_jinhuo),
##########销售的url#############
    path('xiaoshou/', views.xiaoshou_list),
    path('xiaoshou/add_xiaoshou/', views.add_xiaoshou),
    path('xiaoshou/search_xiaoshou/', views.search_xiaoshou),
##########库存的url##############
    path('kucun/', views.kucun_list),
    path('kucun/search_kucun/', views.search_kucun),
##############返货的url##########
    path('fanhuo/', views.fanhuo_list),
    path('fanhuo/add_fanhuo/', views.add_fanhuo),
    path('fanhuo/search_fanhuo/', views.search_fanhuo),
##############会员积分################
    path('vip/', views.vip_list),
    path('vip/add_vip/', views.add_vip),
    path('vip/add_yucun/', views.add_yucun),
    path('vip/duihuan/', views.jifen_duihuan),
    path('vip/vip_detial/', views.vip_detial),
    path('vip/search_vip/', views.search_vip)
]