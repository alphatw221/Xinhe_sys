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

    path('squad_list/',SquadList.as_view()),
    path('squad_detail/<int:id>',SquadDetails.as_view()),

    path('worker_list/',WorkerList.as_view()),
    path('worker_detail/<int:id>',WorkerDetails.as_view()),

    path('warehouse_list/',WarehouseList.as_view()),
    path('warehouse_detail/<int:id>',WarehouseDetails.as_view()),

    
]
