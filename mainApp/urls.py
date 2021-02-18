from django.urls import path
from .views import *



urlpatterns = [
    
    path('login_page/',login_page),
    path('control_panel/',control_panel),

    #api
    path('login/',Login.as_view()),
    path('logout/',Logout.as_view()),

    path('product_list/',ProductList.as_view()),
    path('product_detail/<int:id>',ProductDetails.as_view()),


    
]
