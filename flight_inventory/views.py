from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from flight_inventory.models import Flight
from .serializers import FlightPublicSerializer, FlightAuthSerializer, UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class SignUpAPIView(APIView):
    def post(self, request):
        payload = request.data
        serialized = UserSerializer(data=payload)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response({
            'success':'True',
            'message':'User Registered Successfully !'
        }, status=status.HTTP_201_CREATED)

class FlightPublicSearchAPIView(APIView):
    def get(self, request):
        query_set = Flight.objects.defer('base_fare', 'tax')
        serialized_data = FlightPublicSerializer(query_set, many=True)
        print(query_set)
        return Response({
            'success':True,
            'data': serialized_data.data
        })

class FlightAuthSearch(APIView):
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        query_set = Flight.objects.all()
        print(query_set)
        serialized_data = FlightAuthSerializer(query_set, many=True)
        print(query_set)
        return Response({
            'success':True,
            'data': serialized_data.data
        }, status=status.HTTP_200_OK)

