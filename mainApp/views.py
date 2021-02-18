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
        

class ProductList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ProductSerializer(data=request.data)

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

class ProductsList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):
        productss=Products.objects.all()
        serializer=ProductsSerializer(productss,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ProductsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'新增成功','data':serializer.data}
            # return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductsDetails(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_object(self,id):
        try:
            products=Products.objects.get(id=id)
            return products
        except Products.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,id):
        products=self.get_object(id)
        serializer=ProductsSerializer(product)
        return Response(serializer.data)

    def put(self,request,id):
        products=self.get_object(id)
        serializer=ProductsSerializer(products,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'更新成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        products=self.get_object(id)
        products.delete()
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

class CompletedProjectList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):
        completedProject=CompletedProject.objects.all()
        serializer=CompleteProjectSerializer(completedProject,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=CompleteProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'新增成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CompletedProjectDetails(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_object(self,id):
        try:
            completedProject=CompletedProject.objects.get(id=id)
            return warehouse
        except CompletedProject.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,id):
        warehocompletedProjectuse=self.get_object(id)
        serializer=CompleteProjectSerializer(completedProject)
        return Response(serializer.data)

    def put(self,request,id):
        completedProject=self.get_object(id)
        serializer=CompleteProjectSerializer(completedProject,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'更新成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        completedProject=self.get_object(id)
        completedProject.delete()
        content={'s':1,'message':'刪除成功'}
        return Response(content)

class BlockedProjectList(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get(self,request):
        blockedProject=BlockedProject.objects.all()
        serializer=BlockedProjectSerializer(blockedProject,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=BlockedProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'新增成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CompletedProjectDetails(APIView):

    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]

    def get_object(self,id):
        try:
            blockedProject=BlockedProject.objects.get(id=id)
            return blockedProject
        except BlockedProject.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,id):
        blockedProject=self.get_object(id)
        serializer=BlockedProjectSerializer(blockedProject)
        return Response(serializer.data)

    def put(self,request,id):
        blockedProject=self.get_object(id)
        serializer=BlockedProjectSerializer(blockedProject,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={'s':1,'message':'更新成功','data':serializer.data}
            return Response(content)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        blockedProject=self.get_object(id)
        blockedProject.delete()
        content={'s':1,'message':'刪除成功'}
        return Response(content)
