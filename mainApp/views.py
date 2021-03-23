from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import *
from .serializers import *
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from django.core.files.uploadedfile import InMemoryUploadedFile
import os 
from django.conf import settings
import json
from django.db.models import Avg, Max, Min, Sum
class TwentyPagenation(PageNumberPagination):
        page_size = 20
        page_size_query_param = 'size'  
        page_query_param = 'page'  
        max_page_size = None  

class FiftyPagenation(PageNumberPagination):
        page_size = 50
        page_size_query_param = 'size'  
        page_query_param = 'page'  
        max_page_size = None  

class HundredPagenation(PageNumberPagination):
        page_size = 100
        page_size_query_param = 'size'  
        page_query_param = 'page'  
        max_page_size = None  

def login_page(request):
    
    context={}
    return render(request,'login_page.html',context)

def control_panel(request):
    key=request.COOKIES.get('token')
    try:
        token=Token.objects.get(key=key)
    except Token.DoesNotExist:
        return render(request,'login_page.html')

    context={'products':Product.objects.all(),'squads':Squad.objects.all(),'Workers':Worker.objects.all(),'warehouses':Warehouse.objects.all()}
    return render(request,'control_panel.html',context)


def worksheet_page(request):
    key=request.COOKIES.get('token')
    try:
        token=Token.objects.get(key=key)
    except Token.DoesNotExist:
        return render(request,'login_page.html')

    context={'products':Product.objects.all(),
    'squads':Squad.objects.all(),
    'Workers':Worker.objects.all(),
    'warehouses':Warehouse.objects.all(),
    'worksheets':WorkSheet.objects.all(),
    'type1s':Type1.objects.all(),
    'type2s':Type2.objects.all(),
    'statuss':Status.objects.all(),
    'regions':Region.objects.all(),
    'projects':Project.objects.all()}
    return render(request,'pages/worksheet.html',context)

def get_product_page(request):
    key=request.COOKIES.get('token')
    try:
        token=Token.objects.get(key=key)
    except Token.DoesNotExist:
        return render(request,'login_page.html')

    context={'products':Product.objects.all(),
    'squads':Squad.objects.all(),}
    return render(request,'pages/get_product_page.html',context)

def get_product_dashboard(request):
    key=request.COOKIES.get('token')
    try:
        token=Token.objects.get(key=key)
    except Token.DoesNotExist:
        return render(request,'login_page.html')

    context={'products':Product.objects.all(),
    'squads':Squad.objects.all(),
    'Workers':Worker.objects.all(),
    'warehouses':Warehouse.objects.all(),
    'worksheets':WorkSheet.objects.all(),
    'type1s':Type1.objects.all(),
    'type2s':Type2.objects.all(),
    'statuss':Status.objects.all(),
    'regions':Region.objects.all(),
    'projects':Project.objects.all()}
    return render(request,'pages/get_product_dashboard.html',context)

def use_product_page(request):
    key=request.COOKIES.get('token')
    try:
        token=Token.objects.get(key=key)
    except Token.DoesNotExist:
        return render(request,'login_page.html')

    context={'products':Product.objects.all(),
    'squads':Squad.objects.all(),
    'statuss':Status.objects.all(),}
    return render(request,'pages/use_product_page.html',context)

def dashboard_page(request):
    key=request.COOKIES.get('token')
    try:
        token=Token.objects.get(key=key)
    except Token.DoesNotExist:
        return render(request,'login_page.html')

    context={'products':Product.objects.all(),
    'squads':Squad.objects.all(),
    'Workers':Worker.objects.all(),
    'warehouses':Warehouse.objects.all(),
    'worksheets':WorkSheet.objects.all(),
    'type1s':Type1.objects.all(),
    'type2s':Type2.objects.all(),
    'statuss':Status.objects.all(),
    'regions':Region.objects.all(),
    'projects':Project.objects.all()}
    return render(request,'pages/dashboard_page.html',context)

def update_worksheet_page(request,id):
    key=request.COOKIES.get('token')
    try:
        token=Token.objects.get(key=key)
    except Token.DoesNotExist:
        return render(request,'login_page.html')

    
    worksheet=WorkSheet.objects.get(id=id)

    context={'products':Product.objects.all(),
    'squads':Squad.objects.all(),
    'worksheet':worksheet,
    'type1s':Type1.objects.all(),
    'type2s':Type2.objects.all(),
    'statuss':Status.objects.all(),
    'regions':Region.objects.all(),
    'projects':Project.objects.all()}
    return render(request,'pages/update_worksheet_page.html',context)

def update_use_product_sheet_page(request,id):
    key=request.COOKIES.get('token')
    try:
        token=Token.objects.get(key=key)
    except Token.DoesNotExist:
        return render(request,'login_page.html')
    use_product_sheet=UseProductSheet.objects.get(id=id)
    warehouses=use_product_sheet.squad.warehouses.all()
    context={
    'statuss':Status.objects.all(),
    'warehouses':warehouses}
    return render(request,'pages/update_use_product_sheet_page.html',context)

def update_get_product_sheet_page(request,id):
    key=request.COOKIES.get('token')
    try:
        token=Token.objects.get(key=key)
    except Token.DoesNotExist:
        return render(request,'login_page.html')
    
    context={
    'squads':Squad.objects.all()}
    return render(request,'pages/update_get_product_sheet_page.html',context)

def warehouse_page(request):
    key=request.COOKIES.get('token')
    try:
        token=Token.objects.get(key=key)
    except Token.DoesNotExist:
        return render(request,'login_page.html')

    context={
    'squads':Squad.objects.all(),
    'Workers':Worker.objects.all()}
    return render(request,'pages/warehouse_page.html',context)

def warehouse_total_page(request):
    key=request.COOKIES.get('token')
    try:
        token=Token.objects.get(key=key)
    except Token.DoesNotExist:
        return render(request,'login_page.html')

    context={
    'warehouses':Warehouse.objects.all(),
    'products':Product.objects.all(),}
    return render(request,'pages/warehouse_total_page.html',context)


#--------------------------------------api----------------------------------------------------

class Login(APIView):
    def post(self,request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        print(user)
        if user is not None:
            try:
                token=Token.objects.get(user=user)
                token.delete()
            except Token.DoesNotExist:
                pass
            
            token=Token.objects.create(user=user)
        
            content={'token':token.key}
            return Response(content)
        return Response('登入失敗')
        

class Logout(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def post(self,request):
        key=request.headers['Authorization'][6:]
        token=Token.objects.get(key=key)
        token.delete()
        content={'s':1,'message':'登出成功'}
        return Response(content)

class WorkSheetList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    

    def get(self,request):
        worksheets=WorkSheet.objects.all().order_by('date')
        twentyPagenation=TwentyPagenation()
        page_worksheets=twentyPagenation.paginate_queryset(queryset=worksheets,request=request,view=self)
        serializer=WorkSheetSerializer(page_worksheets,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer1=WorkSheetSerializer(data=request.data['worksheet'])
        productss=request.data['worksheet_productss']
        
        if serializer1.is_valid() :
            serializer1.save()
            print(serializer1.data)
            for products in productss:
                products['worksheet']=serializer1.data['id']
            serializer2=WorkSheetProductsSerializer(data=productss,many=True)
            if serializer2.is_valid():
                serializer2.save()
                content={'s':1,'message':'新增成功','data':{'worksheet':serializer1.data,'worksheet_productss':serializer2.data}}
                return Response(content)
        
        print(serializer1.errors)
        WorkSheet.objects.get(id=serializer1.data['id']).delete()
        return Response(serializer1.errors,status=status.HTTP_400_BAD_REQUEST)

class WorkSheetDetails(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_object(self,id):
        try:
            worksheet=WorkSheet.objects.get(id=id)
            return worksheet
        except WorkSheet.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,id):
        worksheet=self.get_object(id)
        serializer=WorkSheetSerializer(worksheet)
        return Response(serializer.data)

    def put(self,request,id):
        worksheet=self.get_object(id)
        serializer=WorkSheetSerializer(worksheet,data=request.data['worksheet'])
        serializer2=WorkSheetProductsSerializer(data=request.data['worksheet_productss'],many=True)
        if serializer.is_valid() and serializer2.is_valid():
            worksheet_productss=worksheet.work_sheet_productss.all()
            for worksheet_products in worksheet_productss:
                worksheet_products.delete()
            serializer.save()
            serializer2.save()
            content={'s':1,'message':'更新成功','data':{'worksheet':serializer.data,'worksheet_productss':serializer2.data}}
            return Response(content)
        print(serializer.errors)
        print(serializer2.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        worksheets=self.get_object(id)
        worksheets.delete()
        content={'s':1,'message':'刪除成功'}
        return Response(content)


# class WorkSheetProductsList(APIView):

#     authentication_classes=[TokenAuthentication]
#     premission_classes=[IsAuthenticated]

#     def get_product_id(self,code):
#         try:
#             product=Product.objects.get(code=code)
#             return product.id
#         except Product.DoesNotExist:
#             return Response(status=HTTP_404_NOT_FOUND)

#     def get(self,request):
#         worksheet_productss=WorkSheetProducts.objects.all()
#         serializer=WorkSheetProductsSerializer(worksheet_productss,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         # data={'product':self.get_product_id(request.data['code']),
#         # 'amount':request.data['amount'],
#         # 'worksheet':request.data['worksheet']}
#         # print(data)
#         serializer=WorkSheetProductsSerializer(data=request.data,many=True)

#         if serializer.is_valid():
#             serializer.save()
#             content={'s':1,'message':'新增成功','data':serializer.data}
#             return Response(content)
#         print(serializer.errors)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class WorkSheetProductsDetails(APIView):

#     authentication_classes=[TokenAuthentication]
#     premission_classes=[IsAuthenticated]

#     def get_object(self,id):
#         try:
#             worksheet_productss=WorkSheet.objects.get(id=id)
#             return worksheets
#         except WorkSheet.DoesNotExist:
#             return Response(status=HTTP_404_NOT_FOUND)

#     def get(self,request,id):
#         worksheet_productss=self.get_object(id)
#         serializer=WorkSheetProductsSerializer(worksheet_productss)
#         return Response(serializer.data)

#     def put(self,request,id):
#         worksheet_productss=self.get_object(id)
#         serializer=WorkSheetProductsSerializer(worksheet_productss,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             content={'s':1,'message':'更新成功','data':serializer.data}
#             return Response(content)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,id):
#         worksheet_productss=self.get_object(id)
#         worksheet_productss.delete()
#         content={'s':1,'message':'刪除成功'}
#         return Response(content)

class GetProductSheetList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):
        get_product_sheets=GetProductSheet.objects.all()
        serializer=GetProductSheetSerializer(get_product_sheets,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer1=GetProductSheetSerializer(data=request.data['get_product_sheet'])
        productss=request.data['get_product_sheet_productss']
        if serializer1.is_valid() :
            get_product_sheet=GetProductSheet.objects.create(serial_number=request.data['get_product_sheet']['serial_number'],
            squad=Squad.objects.get(id=request.data['get_product_sheet']['squad']),
            date=request.data['get_product_sheet']['date'],
            warehouse=Warehouse.objects.get(id=request.data['get_product_sheet']['warehouse']),
            out_warehouse=Warehouse.objects.get(id=request.data['out_warehouse']))
            if request.data['auto_gen']:
                get_product_sheet.serial_number='GEN'+str(get_product_sheet.id)
                get_product_sheet.save()
            for products in productss:
                products['get_product_sheet']=get_product_sheet.id
                products['date']=get_product_sheet.date
                products['out_warehouse']=request.data['out_warehouse']
            serializer2=GetProductSheetProductsSerializer(data=productss,many=True)
            if serializer2.is_valid():
                serializer2.save()
                sheet_excel={'serial_number':get_product_sheet.serial_number,
                'squad':get_product_sheet.squad.name,
                'warehouse':Warehouse.objects.get(id=request.data['get_product_sheet']['warehouse']).name,
                'date':get_product_sheet.date,
                'out_squad':Squad.objects.get(id=request.data['out_squad']).name,
                'out_warehouse':Warehouse.objects.get(id=request.data['out_warehouse']).name}
                productss_excel=[]
                for products in productss:
                    product=Product.objects.get(id=products['product'])
                    productss_excel.append({'code':product.code,
                    'name':product.name,
                    'amount':products['amount'],
                    'unit':product.unit,})
                content={'s':1,'message':'新增成功','data':{'get_product_sheet':sheet_excel,'get_product_sheet_productss':productss_excel}}
                return Response(content)
            print(serializer2.errors)
            get_product_sheet.delete()
            return Response(serializer2.errors,status=status.HTTP_400_BAD_REQUEST)
        print(serializer1.errors)
        return Response(serializer1.errors,status=status.HTTP_400_BAD_REQUEST)

class GetProductSheetDetails(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_object(self,id):
        try:
            get_product_sheet=GetProductSheet.objects.get(id=id)
            return get_product_sheet
        except GetProductSheet.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,id):
        get_product_sheet=self.get_object(id)
        products=[]
        
        for x in get_product_sheet.get_product_sheet_productss.all():
            products.append({
                'product':x.product.id,
                'name':x.product.name,
                'code':x.product.code,
                'amount':x.amount,
                'unit':x.product.unit
            })
        data={
                'get_product_sheet':{
                    'id':get_product_sheet.id,
                    'serial_number':get_product_sheet.serial_number,
                    'squad':get_product_sheet.squad.id,
                    'date':get_product_sheet.date,
                    'warehouse':get_product_sheet.warehouse.id,
                    'warehouses':WarehouseSerializer(get_product_sheet.squad.warehouses,many=True).data,
                    'out_squad':get_product_sheet.out_warehouse.squad.id,
                    'out_warehouse':get_product_sheet.out_warehouse.id,
                    'out_warehouses':WarehouseSerializer(get_product_sheet.out_warehouse.squad.warehouses,many=True).data,
                },
                'products':products 
            }
        return Response(data)

    def put(self,request,id):
        get_product_sheet=self.get_object(id)
        serializer=GetProductSheetSerializer(get_product_sheet,data=request.data['get_product_sheet'])
        serializer2=GetProductSheetProductsSerializer(data=request.data['get_product_sheet_productss'],many=True)
        if serializer.is_valid() and serializer2.is_valid():
            get_product_sheet.get_product_sheet_productss.all().delete()
            serializer.save()
            serializer2.save()
            get_product_sheet=self.get_object(id)
            sheet_excel={'serial_number':get_product_sheet.serial_number,
                'squad':get_product_sheet.squad.name,
                'warehouse':Warehouse.objects.get(id=request.data['get_product_sheet']['warehouse']).name,
                'date':get_product_sheet.date,
                'out_squad':Squad.objects.get(id=request.data['get_product_sheet']['out_squad']).name,
                'out_warehouse':Warehouse.objects.get(id=request.data['get_product_sheet']['out_warehouse']).name}
            productss_excel=[]
            productss=request.data['get_product_sheet_productss']
            for products in productss:
                product=Product.objects.get(id=products['product'])
                productss_excel.append({'code':product.code,
                                    'name':product.name,
                                    'amount':products['amount'],
                                    'unit':product.unit,})
            content={'s':1,'message':'新增成功','data':{'get_product_sheet':sheet_excel,'get_product_sheet_productss':productss_excel}}
            return Response(content)
        print(serializer.errors)
        print(serializer2.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        get_product_sheet=self.get_object(id)
        get_product_sheet.delete()
        content={'s':1,'message':'刪除成功'}
        return Response(content)





#---------------------------------------------------------------------------------------------------
class UseProductSheetList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):
        use_product_sheets=UseProductSheet.objects.all()
        serializer=UseProductSheetSerializer(use_product_sheets,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer1=UseProductSheetSerializer(data=request.data['use_product_sheet'])
        productss=request.data['use_product_sheet_productss']
        
        if serializer1.is_valid() :
            serializer1.save()
            for products in productss:
                products['use_product_sheet']=serializer1.data['id']
                products['date']=serializer1.data['date']
            serializer2=UseProductSheetProductsSerializer(data=productss,many=True)
            if serializer2.is_valid():
                serializer2.save()
                #改工作聯單狀態
                worksheet=WorkSheet.objects.get(id=request.data['use_product_sheet']['worksheet'])
                worksheet.status=Status.objects.get(id=request.data['use_product_sheet']['status'])
                worksheet.save()
                content={'s':1,'message':'新增成功','data':{'use_product_sheet':serializer1.data,'use_product_sheet_productss':serializer2.data}}
                return Response(content)
            print(serializer2.errors)
            UseProductSheet.objects.get(id=serializer1.data['id']).delete()
            return Response(serializer2.errors,status=status.HTTP_400_BAD_REQUEST)
        print(serializer1.errors)
        return Response(serializer1.errors,status=status.HTTP_400_BAD_REQUEST)

class UseProductSheetDetails(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_object(self,id):
        try:
            use_product_sheet=UseProductSheet.objects.get(id=id)
            return use_product_sheet
        except UseProductSheet.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,id):
        use_product_sheet=self.get_object(id)
        products=[]
        
        for x in use_product_sheet.use_product_sheet_productss.all():
            products.append({
                'product':x.product.id,
                'name':x.product.name,
                'code':x.product.code,
                'amount':x.amount,
                'unit':x.product.unit
            })
        data={
                'use_product_sheet':{
                    'worksheet':use_product_sheet.worksheet.id,
                    'id':use_product_sheet.id,
                    'status':use_product_sheet.status.id,
                    'status_name':use_product_sheet.status.name,
                    'serial_number':use_product_sheet.worksheet.serial_number,
                    'squad_name':use_product_sheet.squad.name,
                    'squad':use_product_sheet.squad.id,
                    'date':use_product_sheet.date,
                    'point':use_product_sheet.point,
                    'discription':use_product_sheet.discription,
                    'warehouse':use_product_sheet.warehouse.id,
                    'project':use_product_sheet.project.id,
                    'project_name':use_product_sheet.project.name,
                },
                'products':products 
            }
        return Response(data)

    def put(self,request,id):
        use_product_sheet=self.get_object(id)
        serializer=UseProductSheetSerializer(use_product_sheet,data=request.data['use_product_sheet'])
        serializer2=UseProductSheetProductsSerializer(data=request.data['use_product_sheet_productss'],many=True)
        if serializer.is_valid() and serializer2.is_valid():
            use_product_sheet.use_product_sheet_productss.all().delete()
            serializer.save()
            serializer2.save()
            content={'s':1,'message':'更新成功','data':{'use_product_sheet':serializer.data,'use_product_sheet_productss':serializer2.data}}
            return Response(content)
        print(serializer.errors)
        print(serializer2.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        use_product_sheet=self.get_object(id)
        use_product_sheet.delete()
        content={'s':1,'message':'刪除成功'}
        return Response(content)





class ProductList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ProductSerializer(data=request.data)

        print(request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'新增成功','data':serializer.data}
            # return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductDetails(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_object(self,id):
        try:
            product=Product.objects.get(id=id)
            return product
        except Product.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,id):
        product=self.get_object(id)
        serializer=ProductSerializer(product)
        return Response(serializer.data)

    def put(self,request,id):
        product=self.get_object(id)
        serializer=ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'更新成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        product=self.get_object(id)
        product.delete()
        content={'s':1,'message':'刪除成功'}
        return Response(content)

    
class SquadList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):
        squad=Squad.objects.all()
        serializer=SquadSerializer(squad,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=SquadSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'新增成功','data':serializer.data}
            # return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class SquadDetails(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_object(self,id):
        try:
            squad=Squad.objects.get(id=id)
            return squad
        except Squad.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,id):
        squad=self.get_object(id)
        serializer=SquadSerializer(squad)
        return Response(serializer.data)

    def put(self,request,id):
        squad=self.get_object(id)
        serializer=SquadSerializer(squad,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'更新成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        product=self.get_object(id)
        product.delete()
        content={'s':1,'message':'刪除成功'}
        return Response(content)

class WorkerList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):
        worker=Worker.objects.all()
        serializer=SquadSerializer(worker,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=WorkerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'新增成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class WorkerDetails(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_object(self,id):
        try:
            worker=Worker.objects.get(id=id)
            return worker
        except Worker.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,id):
        worker=self.get_object(id)
        serializer=WorkerSerializer(worker)
        return Response(serializer.data)

    def put(self,request,id):
        worker=self.get_object(id)
        serializer=WorkerSerializer(worker,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'更新成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        worker=self.get_object(id)
        worker.delete()
        content={'s':1,'message':'刪除成功'}
        return Response(content)

class WarehouseList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):
        warehouse=Warehouse.objects.all()
        serializer=WarehouseSerializer(warehouse,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=WarehouseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'新增成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class WarehouseDetails(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_object(self,id):
        try:
            warehouse=Warehouse.objects.get(id=id)
            return warehouse
        except Warehouse.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,id):
        warehouse=self.get_object(id)
        serializer=WarehouseSerializer(warehouse)
        return Response(serializer.data)

    def put(self,request,id):
        warehouse=self.get_object(id)
        serializer=WarehouseSerializer(warehouse,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'更新成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        warehouse=self.get_object(id)
        warehouse.delete()
        content={'s':1,'message':'刪除成功'}
        return Response(content)


class GetSquadWarehouses(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request,id):
        squad=Squad.objects.get(id=id)
        warehouses=squad.warehouses.all()
        serializer=WarehouseSerializer(warehouses,many=True)
        return Response(serializer.data)

class GetWorksheetWithSerialNumber(APIView):
    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]
    def get(self,request):
        try:
            data={}
            serial_number=request.query_params.get('serial_number')
            print(serial_number)
            worksheet=WorkSheet.objects.get(serial_number=serial_number)
            print(worksheet)
            data['worksheet_id']=worksheet.id
            data['squad_id']=worksheet.squad.id
            data['squad_name']=worksheet.squad.name
            data['warehouses']=WarehouseSerializer(worksheet.squad.warehouses,many=True).data
            data['point']=int(worksheet.point)
            data['project_id']=worksheet.project.id
            data['project_name']=worksheet.project.name
            return Response(data)
        except:
            return Response()
class GetAllDict(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):


        squads=Squad.objects.all()
        squad_dict={}
        i=0
        for i in range(len(squads)):
            squad_dict[squads[i].id]=squads[i].name

        statuss=Status.objects.all()
        status_dict={}
        i=0
        for i in range(len(statuss)):
            status_dict[statuss[i].id]=statuss[i].name

        type1s=Type1.objects.all()
        type1_dict={}
        i=0
        for i in range(len(type1s)):
            type1_dict[type1s[i].id]=type1s[i].name

        type2s=Type2.objects.all()
        type2_dict={}
        i=0
        for i in range(len(type2s)):
            type2_dict[type2s[i].id]=type2s[i].name

        regions=Region.objects.all()
        region_dict={}
        i=0
        for i in range(len(regions)):
            region_dict[regions[i].id]=regions[i].name

        
        projects=Project.objects.all()
        project_dict={}
        i=0
        for i in range(len(projects)):
            project_dict[projects[i].id]=projects[i].name

        data={
            'squad_dict':squad_dict,'status_dict':status_dict,
            'type1_dict':type1_dict,'type2_dict':type2_dict,
            'region_dict':region_dict,'project_dict':project_dict
        }
        return Response(data)

class GetWorksheetProductss(APIView):
    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request,id):
        worksheet=WorkSheet.objects.get(id=id)
        work_sheet_productss=worksheet.work_sheet_productss.all()
        data=[]
        for i in range(len(work_sheet_productss)):
            data.append({'product':work_sheet_productss[i].product.id,
            'name':work_sheet_productss[i].product.name,
            'code':work_sheet_productss[i].product.code,
            'amount':work_sheet_productss[i].amount,
            'unit':work_sheet_productss[i].product.unit})
        return Response(data)

class GetGetProductSheetProductss(APIView):
    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request,id):
        get_product_sheet=GetProductSheet.objects.get(id=id)
        get_product_sheet_productss=get_product_sheet.get_product_sheet_productss.all()
        data=[]
        for i in range(len(get_product_sheet_productss)):
            data.append({'product':get_product_sheet_productss[i].product.id,
            'name':get_product_sheet_productss[i].product.name,
            'code':get_product_sheet_productss[i].product.code,
            'amount':get_product_sheet_productss[i].amount,
            'unit':get_product_sheet_productss[i].product.unit})
        return Response(data)

class GetWorksheetUseProductSheet(APIView):
    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request,id):
        worksheet=WorkSheet.objects.get(id=id)
        use_product_sheets=worksheet.use_product_sheets.all()
        data=[]
        for x in use_product_sheets:
            data.append({
                'id':x.id,
                'date':x.date,
                'status':x.status.name,
                'discription':x.discription,
                'point':x.point,
            })
        return Response(data)

class GetProductWithCode(APIView):
    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):
        try:
            product=Product.objects.get(code=request.query_params.get('code'))
            serializer=ProductSerializer(product)
            return Response(serializer.data)

        except Product.DoesNotExist:
            return Response()

class SearchWorksheet(APIView):
    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]
    def get(self,request):
        worksheets=WorkSheet.objects.all().order_by('date')
        serial_number=request.query_params.get('serial_number')
        squad=request.query_params.get('squad')
        status=request.query_params.get('status')
        type1=request.query_params.get('type1')
        type2=request.query_params.get('type2')
        region=request.query_params.get('region')
        project=request.query_params.get('project')
        if serial_number:
            worksheets=worksheets.filter(serial_number=serial_number)
        if  squad != '0':
            worksheets=worksheets.filter(squad=squad)
        if status != '0':
            worksheets=worksheets.filter(status=status)
        if type1 != '0':
            worksheets=worksheets.filter(type1=type1)
        if type2 != '0':
            worksheets=worksheets.filter(type2=type2)
        if region != '0':
            worksheets=worksheets.filter(region=region)
        if project != '0':
            worksheets=worksheets.filter(project=project)
        twentyPagenation=TwentyPagenation()
        page_worksheets=twentyPagenation.paginate_queryset(queryset=worksheets,request=request,view=self)
        serializer=WorkSheetSerializer(page_worksheets,many=True)
        return Response(serializer.data)

class SearchGetProductSheet(APIView):
    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]
    def get(self,request):
        get_product_sheet=GetProductSheet.objects.all().order_by('date')
        print(get_product_sheet)
        serial_number=request.query_params.get('serial_number')
        squad=request.query_params.get('squad')
        date=request.query_params.get('date')
        warehouse=request.query_params.get('warehouse')
        if serial_number:
            get_product_sheet=get_product_sheet.filter(serial_number=serial_number)
        if  squad != '0':
            get_product_sheet=get_product_sheet.filter(squad=squad)
        if date :
            get_product_sheet=get_product_sheet.filter(date=date)
        if warehouse !='0':
            get_product_sheet=get_product_sheet.filter(warehouse=warehouse)
        twentyPagenation=TwentyPagenation()
        page_get_product_sheet=twentyPagenation.paginate_queryset(queryset=get_product_sheet,request=request,view=self)
        serializer=GetProductSheetSerializer(page_get_product_sheet,many=True)
        dict_data={}
        dict_data['warehouse_dict']=dict((x.pk, WarehouseSerializer(x).data) for x in Warehouse.objects.all())
        dict_data['squad_dict']=dict((x.pk, SquadSerializer(x).data) for x in Squad.objects.all())
        return Response({'data':serializer.data,'dict_data':dict_data})

class GetWarehouseInOut(APIView):
    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]
    def post(self,request,id):
        squad=Squad.objects.get(id=request.data['squad'])
        data={}
        inout={}
        total={}
        data['product_dict']=dict((x.pk, ProductSerializer(x).data) for x in Product.objects.all())
        data['get_product_sheet_dict']=dict((x.pk,GetProductSheetSerializer(x).data) for x in GetProductSheet.objects.all())
        data['use_product_sheet_dict']=dict((x.pk,UseProductSheetSerializer(x).data) for x in squad.use_product_sheets.all())
        data['warehouse_dict']=dict((x.pk, x.squad.name) for x in Warehouse.objects.all())
        # try:
        #     products_id=request.data['ids']
        #     warehouse=Warehouse.objects.get(id=id)
        #     for product_id in products_id:
        #         get_productss=warehouse.get_product_sheet_productss.filter(product=product_id)
        #         get_productss_total=get_productss.aggregate(Sum('amount'))
        #         use_productss=warehouse.use_product_sheet_productss.filter(product=product_id)
        #         use_productss_total=use_productss.aggregate(Sum('amount'))
        #         out_productss=warehouse.out_productss.filter(product=product_id)
        #         out_productss_total=out_productss.aggregate(Sum('amount'))
        #         inout[product_id]=self.merge(get_productss,use_productss,out_productss)
        #         total[product_id]=int(0 if get_productss_total['amount__sum'] is None else get_productss_total['amount__sum'])-int(0 if use_productss_total['amount__sum'] is None else use_productss_total['amount__sum'])-int(0 if out_productss_total['amount__sum'] is None else out_productss_total['amount__sum'])
        #     data['inout']=inout
        #     data['total']=total
        #     return Response(data)
        # except:
        #     return Response('輸入資料錯誤',status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        products_id=request.data['ids']
        warehouse=Warehouse.objects.get(id=id)
        for product_id in products_id:
            get_productss=warehouse.get_product_sheet_productss.filter(product=Product.objects.get(id=product_id)).order_by('date')
            get_productss_total=get_productss.aggregate(Sum('amount'))
            use_productss=warehouse.use_product_sheet_productss.filter(product=Product.objects.get(id=product_id)).order_by('date')
            use_productss_total=use_productss.aggregate(Sum('amount'))
            out_productss=warehouse.out_productss.filter(product=Product.objects.get(id=product_id)).order_by('date')
            out_productss_total=out_productss.aggregate(Sum('amount'))
            inout[product_id]=self.merge(get_productss,use_productss,out_productss)
            total[product_id]=int(0 if get_productss_total['amount__sum'] is None else get_productss_total['amount__sum'])-int(0 if use_productss_total['amount__sum'] is None else use_productss_total['amount__sum'])-int(0 if out_productss_total['amount__sum'] is None else out_productss_total['amount__sum'])
        data['inout']=inout
        data['total']=total
        return Response(data)
    def merge(self,a,b,c):
        i=0
        j=0
        k=0
        data=[]
        while(i<len(a) and j<len(b) and k<len(c)):
            if a[i].date <= b[j].date and a[i].date <= c[k].date:
                data.append(GetProductSheetProductsSerializer(a[i]).data)
                i=i+1
            elif b[j].date <= a[i].date and b[j].date <= c[k].date:
                data.append(UseProductSheetProductsSerializer(b[j]).data)
                j=j+1
            else:
                data.append(GetProductSheetProductsSerializer(c[k]).data)
                k=k+1
        if i == len(a):
            while(j<len(b) and k<len(c)):
                if b[j].date <= c[k].date:
                    data.append(UseProductSheetProductsSerializer(b[j]).data)
                    j=j+1
                else:
                    data.append(GetProductSheetProductsSerializer(c[k]).data)
                    k=k+1
            if j==len(b):
                for x in c[k:len(c)]:
                    data.append(GetProductSheetProductsSerializer(x).data)
            else:
                for x in b[j:len(b)]:
                    data.append(UseProductSheetProductsSerializer(x).data)

        elif j== len(b):
            while(i<len(a) and k<len(c)):
                if a[i].date <= c[k].date:
                    data.append(GetProductSheetProductsSerializer(a[i]).data)
                    i=i+1
                else:
                    data.append(GetProductSheetProductsSerializer(c[k]).data)
                    k=k+1
            if i==len(a):
                for x in c[k:len(c)]:
                    data.append(GetProductSheetProductsSerializer(x).data)
            else:
                for x in a[i:len(a)]:
                    data.append(GetProductSheetProductsSerializer(x).data)
        elif k==len(c):
            while(i<len(a) and j<len(b)):
                if a[i].date <= b[j].date:
                    data.append(GetProductSheetProductsSerializer(a[i]).data)
                    i=i+1
                else:
                    data.append(UseProductSheetProductsSerializer(b[j]).data)
                    j=j+1
            if i==len(a):
                for x in b[j:len(b)]:
                    data.append(UseProductSheetProductsSerializer(x).data)
            else:
                for x in a[i:len(a)]:
                    data.append(GetProductSheetProductsSerializer(x).data)
        return data

class GetAllWarehouseTotal(APIView):
    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]
    def get(self,request):
        products=Product.objects.all()
        warehouses=Warehouse.objects.all()
        data={}
        product2warehouse={}
        data['product_dict']=dict((x.code, ProductSerializer(x).data) for x in Product.objects.all())
        data['warehouse_dict']=dict((x.pk, WarehouseSerializer(x).data) for x in Warehouse.objects.all())

        for product in products:
            product2warehouse[product.code]={}
            for warehouse in warehouses:
                get_productss_total=warehouse.get_product_sheet_productss.filter(product=product).aggregate(Sum('amount'))
                use_productss_total=warehouse.use_product_sheet_productss.filter(product=product).aggregate(Sum('amount'))
                out_productss_total=warehouse.out_productss.filter(product=product).aggregate(Sum('amount'))
                total=int(0 if get_productss_total['amount__sum'] is None else get_productss_total['amount__sum'])-int(0 if use_productss_total['amount__sum'] is None else use_productss_total['amount__sum'])-int(0 if out_productss_total['amount__sum'] is None else out_productss_total['amount__sum'])
                product2warehouse[product.code][warehouse.id]=total
        data['product2warehouse']=product2warehouse
        return Response(data)
