from django.urls import path
from .views import *



urlpatterns = [
    
    path('login_page/',login_page),
    path('control_panel/',control_panel),
    path('worksheet_page/',worksheet_page),
    path('get_product_sheet_page/',get_product_page),
    path('use_product_sheet_page/',use_product_page),
    path('dashboard_page/',dashboard_page),
    path('update_worksheet_page/<int:id>',update_worksheet_page),
    path('warehouse_page/',warehouse_page),
    #api
    path('login/',Login.as_view()),
    path('logout/',Logout.as_view()),

    #工作單 工作批料
    path('worksheet_list/',WorkSheetList.as_view()),  #同時新增工作單以及多個批料
    path('worksheet_detail/<int:id>',WorkSheetDetails.as_view()), #同時修改工作單以及多個批料
    path('worksheet_products_list/',WorkSheetProductsList.as_view()),  #一次新增多個
    path('worksheet_products_detail/<int:id>',WorkSheetProductsDetails.as_view()),

    #領貨單 領貨批料
    path('get_product_sheet_list/',GetProductSheetList.as_view()), #同時新增領貨單以及多個批料
    path('get_product_sheet_detail/<int:id>',GetProductSheetDetails.as_view()),
    path('get_product_sheet_products_list/',GetProductSheetProductsList.as_view()),
    path('get_product_sheet_products_detail/<int:id>',GetProductSheetProductsDetails.as_view()),

    #完工單 完工批料
    path('use_product_sheet_list/',UseProductSheetList.as_view()),
    path('use_product_sheet_detail/<int:id>',UseProductSheetDetails.as_view()),
    path('use_product_sheet_products_list/',UseProductSheetProductsList.as_view()),
    path('use_product_sheet_products_detail/<int:id>',UseProductSheetProductsDetails.as_view()),

    path('product_list/',ProductList.as_view()),
    path('product_detail/<int:id>',ProductDetails.as_view()),

    path('squad_list/',SquadList.as_view()),
    path('squad_detail/<int:id>',SquadDetails.as_view()),

    path('worker_list/',WorkerList.as_view()),
    path('worker_detail/<int:id>',WorkerDetails.as_view()),

    path('warehouse_list/',WarehouseList.as_view()),
    path('warehouse_detail/<int:id>',WarehouseDetails.as_view()),

    #查找工班的倉庫
    path('get_squad_warehouses/<int:id>',GetSquadWarehouses.as_view()),

    #查找工班的工作單
    path('get_squad_worksheet/<int:id>',GetSquadWorkSheet.as_view()),

    #取得table的id字典
    path('get_all_dict/',GetAllDict.as_view()),

    #取得工作單的預估廖
    path('get_worksheet_productss/<int:id>',GetWorksheetProductss.as_view()),

    #用料號取料名
    path('get_product_with_code/',GetProductWithCode.as_view()),

    #工作單篩選
    path('search_worksheet/',SearchWorksheet.as_view()),

    #取得倉庫所有進貨出貨資料
    path('get_warehouse_inout/<int:id>',GetWarehouseInOut.as_view()),
]
