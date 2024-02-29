from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


from .models import *
from django.contrib.auth.models import User

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        
        clienteToken = Cliente.objects.get(usuario=user)
        

        token['username'] = user.username
        token['clienteid'] = clienteToken.pk
        return token
    
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    cedula = serializers.CharField(required=True)
    nro_pasaporte = serializers.CharField()
    celular = serializers.CharField(required=True)

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)







    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name','cedula','nro_pasaporte','celular')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}

        }


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "los passwords no coinciden"})
        
        return attrs
    

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )



        user.set_password(validated_data['password'])
        user.save()
        #registramos el cliente
        cliente = Cliente.objects.create(
            usuario = user,
            cedula = validated_data['cedula'],
            nro_pasaporte = validated_data['nro_pasaporte'],
            celular = validated_data['celular']
        )
        
        dictClienteReturn = {
            'cliente_id':cliente.id
        }

        return dictClienteReturn