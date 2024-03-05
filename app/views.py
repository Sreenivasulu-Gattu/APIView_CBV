from django.shortcuts import render

# Create your views here.

from app.models import *
from rest_framework.decorators import APIView
from app.serializers import *
from rest_framework.response import Response


class ProCrud(APIView):
    def get(self,request,id):
        orm = Product.objects.all()
        Jobj = ProductModelSerializer(orm,many=True)
        Jdata = Jobj.data
        return Response(Jdata)
    def post(self,request,id):
        ormobj = ProductModelSerializer(data = request.data)
        if ormobj.is_valid():
            ormobj.save()
            return Response({'Inserted':'Successful Message'})
        else:
            return Response({'Error':'Invalid Dataa'})
    def put(self,request,id):
        PO = Product.objects.get(id=id)
        ormdata = ProductModelSerializer(PO,request.data)
        if ormdata.is_valid():
            ormdata.save()
            return Response({'update':'Successful Message'})
        else:
            return Response({'Error':'Invalid Data'})
    def patch(self,request,id):
        po = Product.objects.get(id = id)
        ormdata = ProductModelSerializer(po,request.data,partial = True)
        if ormdata.is_valid():
            ormdata.save()
            return Response({'Update':'Successful'})
        else:
            return Response({'error':'Invalid data'})
    def delete(self,request,id):
        Product.objects.get(id=id).delete()
        return Response({'Deleted':'Successful'})
            
        