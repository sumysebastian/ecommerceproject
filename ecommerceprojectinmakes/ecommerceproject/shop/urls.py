
from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
    path('',views.allprodCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allprodCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail'),

]