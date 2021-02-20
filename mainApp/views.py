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

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from django.core.files.uploadedfile import InMemoryUploadedFile
import os 
from django.conf import settings


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
#--------------------------------------api----------------------------------------------------

class Login(APIView):
    def post(self,request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
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
        worksheets=WorkSheet.objects.all()
        serializer=ProductSerializer(worksheets,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=WorkSheetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'新增成功','data':serializer.data}
            return Response(content)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class WorkSheetDetails(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_object(self,id):
        try:
            worksheets=WorkSheet.objects.get(id=id)
            return worksheets
        except WorkSheet.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,id):
        worksheets=self.get_object(id)
        serializer=WorkSheetSerializer(worksheets)
        return Response(serializer.data)

    def put(self,request,id):
        worksheets=self.get_object(id)
        serializer=WorkSheetSerializer(worksheets,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'更新成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        worksheets=self.get_object(id)
        worksheets.delete()
        content={'s':1,'message':'刪除成功'}
        return Response(content)


class WorkSheetProductsList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_product_id(self,code):
        try:
            product=Product.objects.get(code=code)
            return product.id
        except Product.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request):
        worksheet_productss=WorkSheetProducts.objects.all()
        serializer=WorkSheetProductsSerializer(worksheet_productss,many=True)
        return Response(serializer.data)

    def post(self,request):
        # data={'product':self.get_product_id(request.data['code']),
        # 'amount':request.data['amount'],
        # 'worksheet':request.data['worksheet']}
        # print(data)
        serializer=WorkSheetProductsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'新增成功','data':serializer.data}
            return Response(content)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class WorkSheetProductsDetails(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_object(self,id):
        try:
            worksheet_productss=WorkSheet.objects.get(id=id)
            return worksheets
        except WorkSheet.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,id):
        worksheet_productss=self.get_object(id)
        serializer=WorkSheetProductsSerializer(worksheet_productss)
        return Response(serializer.data)

    def put(self,request,id):
        worksheet_productss=self.get_object(id)
        serializer=WorkSheetProductsSerializer(worksheet_productss,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'更新成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        worksheet_productss=self.get_object(id)
        worksheet_productss.delete()
        content={'s':1,'message':'刪除成功'}
        return Response(content)

class GetProductSheetList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):
        get_product_sheets=GetProductSheet.objects.all()
        serializer=GetProductSheetSerializer(get_product_sheets,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=GetProductSheetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'新增成功','data':serializer.data}
            return Response(content)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

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
        serializer=GetProductSheetSerializer(get_product_sheet)
        return Response(serializer.data)

    def put(self,request,id):
        get_product_sheet=self.get_object(id)
        serializer=GetProductSheetSerializer(get_product_sheet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'更新成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        get_product_sheet=self.get_object(id)
        get_product_sheet.delete()
        content={'s':1,'message':'刪除成功'}
        return Response(content)


class GetProductSheetProductsList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):
        get_product_sheet_productss=GetProductSheetProducts.objects.all()
        serializer=GetProductSheetProductsSerializer(get_product_sheet_productss,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=GetProductSheetProductsSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'新增成功','data':serializer.data}
            return Response(content)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class GetProductSheetProductsDetails(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_object(self,id):
        try:
            get_product_sheet_products=GetProductSheetProducts.objects.get(id=id)
            return get_product_sheet_products
        except GetProductSheetProducts.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,id):
        get_product_sheet_products=self.get_object(id)
        serializer=GetProductSheetProductsSerializer(get_product_sheet_products)
        return Response(serializer.data)

    def put(self,request,id):
        get_product_sheet_products=self.get_object(id)
        serializer=GetProductSheetProductsSerializer(get_product_sheet_products,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'更新成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        get_product_sheet_products=self.get_object(id)
        get_product_sheet_products.delete()
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
        serializer=UseProductSheetSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'新增成功','data':serializer.data}
            return Response(content)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

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
        serializer=UseProductSheetSerializer(get_product_sheet)
        return Response(serializer.data)

    def put(self,request,id):
        use_product_sheet=self.get_object(id)
        serializer=UseProductSheetSerializer(use_product_sheet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'更新成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        use_product_sheet=self.get_object(id)
        use_product_sheet.delete()
        content={'s':1,'message':'刪除成功'}
        return Response(content)


class UseProductSheetProductsList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):
        use_product_sheet_productss=UseProductSheetProducts.objects.all()
        serializer=UseProductSheetProductsSerializer(use_product_sheet_productss,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=UseProductSheetProductsSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'新增成功','data':serializer.data}
            return Response(content)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UseProductSheetProductsDetails(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_object(self,id):
        try:
            use_product_sheet_products=UseProductSheetProducts.objects.get(id=id)
            return use_product_sheet_products
        except UseProductSheetProducts.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,id):
        use_product_sheet_products=self.get_object(id)
        serializer=UseProductSheetProductsSerializer(use_product_sheet_products)
        return Response(serializer.data)

    def put(self,request,id):
        use_product_sheet_products=self.get_object(id)
        serializer=UseProductSheetProductsSerializer(use_product_sheet_products,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'更新成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        use_product_sheet_products=self.get_object(id)
        use_product_sheet_products.delete()
        content={'s':1,'message':'刪除成功'}
        return Response(content)

#--------------------------




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

class GetSquadWorkSheet(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request,id):
        squad=Squad.objects.get(id=id)
        work_sheets=squad.work_sheets.all()
        serializer=WorkSheetSerializer(work_sheets,many=True)
        return Response(serializer.data)
