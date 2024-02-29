from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import *
from .serializers import *

from django.contrib.auth.models import User

### para jwt
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView


class indexView(APIView):
    
    def get(self,request):
        context = {
            'ok':True,
            'content':'API REST ACTIVO'
        }
        return Response(context)

################ ENDPOINTS PARA AUTENTICACIÓN #########################
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
    
class RegistroView(APIView):

    def post(self,request):
        ClienteSer = RegisterSerializer(data=request.data)
        ClienteSer.is_valid(raise_exception=True)
        ClienteSer.save()
        
        context = {
            'ok':True,
            'content':'cliente registrado'
        }
        return Response(context)
    
################ ENDPOINTS HABTACION ###################################
class HabitacionView(APIView):
    
    #permission_classes = [IsAuthenticated]
    
    def get(self,request):
        HabitacionData = Habitacion.objects.all()
        HabitacionSer = HabitacionSerializer(HabitacionData,many=True)
        context = {
            'ok':True,
            'content':HabitacionSer.data
        }
        return Response(context)
    
    def post(self,request):
        HabitacionSer = HabitacionSerializer(data=request.data)
        HabitacionSer.is_valid(raise_exception=True)
        HabitacionSer.save()
        
        context = {
            'ok':True,
            'content':HabitacionSer.data
        }
        return Response(context)
    
class HabitacionDetailView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self,request,habitacion_id):
        HabitacionData = Habitacion.objects.get(pk=habitacion_id)
        HabitacionSer = HabitacionSerializer(HabitacionData)
        context = {
            'ok':True,
            'content':HabitacionSer.data
        }
        return Response(context)
    
    def put(self,request,habitacion_id):
        HabitacionData = Habitacion.objects.get(pk=habitacion_id)
        HabitacionSer = HabitacionSerializer(HabitacionData,data=request.data)
        HabitacionSer.is_valid(raise_exception=True)
        HabitacionSer.save()
        context = {
            'ok':True,
            'content':HabitacionSer.data
        }
        return Response(context)
    
    def delete(self,request,habitacion_id):
        HabitacionData = Habitacion.objects.get(pk=habitacion_id)
        HabitacionSer = HabitacionSerializer(HabitacionData)
        HabitacionData.delete()
        context = {
            'ok':True,
            'content':HabitacionSer.data
        }
        return Response(context)

################ ENDPOINTS CLIENTE ###################################
class ClienteView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        ClienteData = Cliente.objects.all()
        ClienteSer = ClienteSerializer(ClienteData,many=True)
        context = {
            'ok':True,
            'content':ClienteSer.data
        }
        return Response(context)
    
    def post(self,request):
        ClienteSer = RegisterSerializer(data=request.data)
        ClienteSer.is_valid(raise_exception=True)
        ClienteSer.save()
        
        context = {
            'ok':True,
            'content':'cliente registrado'
        }
        return Response(context)
    
class ClienteDetailView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self,request,cliente_id):
        ClienteData = Cliente.objects.get(pk=cliente_id)
        ClienteSer = ClienteSerializer(ClienteData)
        context = {
            'ok':True,
            'content':ClienteSer.data
        }
        return Response(context)
    
    def put(self,request,cliente_id):
        ClienteData = Cliente.objects.get(pk=cliente_id)
        ClienteSer = ClienteSerializer(ClienteData,data=request.data)
        ClienteSer.is_valid(raise_exception=True)
        ClienteSer.save()
        context = {
            'ok':True,
            'content':ClienteSer.data
        }
        return Response(context)
    
    def delete(self,request,cliente_id):
        ClienteData = Cliente.objects.get(pk=cliente_id)
        ClienteSer = ClienteSerializer(ClienteData)
        ClienteData.delete()
        context = {
            'ok':True,
            'content':ClienteSer.data
        }
        return Response(context)

################ ENDPOINTS RESERVAS ###################################
class ReservaView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        ReservaData = Reserva.objects.all()
        ReservaSer = ReservaSerializer(ReservaData,many=True)
        context = {
            'ok':True,
            'content':ReservaSer.data
        }
        return Response(context)
    
    def post(self,request):
        ReservaSer = ReservaSerializer(data=request.data)
        ReservaSer.is_valid(raise_exception=True)
        ReservaSer.save()
        
        context = {
            'ok':True,
            'content':ReservaSer.data
        }
        return Response(context)
    
class ReservaDetailView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self,request,reserva_id):
        ReservaData = Reserva.objects.get(pk=reserva_id)
        ReservaSer = ReservaSerializer(ReservaData)
        context = {
            'ok':True,
            'content':ReservaSer.data
        }
        return Response(context)
    
    def put(self,request,reserva_id):
        ReservaData = Reserva.objects.get(pk=reserva_id)
        ReservaSer = ReservaSerializer(ReservaData,data=request.data)
        ReservaSer.is_valid(raise_exception=True)
        ReservaSer.save()
        context = {
            'ok':True,
            'content':ReservaSer.data
        }
        return Response(context)
    
    def delete(self,request,reserva_id):
        ReservaData = Reserva.objects.get(pk=reserva_id)
        ReservaSer = ReservaSerializer(ReservaData)
        ReservaData.delete()
        context = {
            'ok':True,
            'content':ReservaSer.data
        }
        return Response(context)