from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


# Create your views here.

class HelloApiView(APIView):
	"""Test ApiView"""

	serializer_class = serializers.HelloSerializer
	

	def get(self, request, format=None):
		""" Return a list of APIView features """

		an_apiview = [
			'Uses HTTP methods as functions (get, post, patch, put, delete)',
			'It is similar to a traditional Django view',
			'Gives you most control over your logic',
			'Is mapped manually to URLs'
		]

		return Response({'message': 'Hello!', 'an_apiview': an_apiview})

	def post(self, request):
		"""Create a hello message with our name"""

		serializer = serializers.HelloSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name)

			return Response({'message': message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk=None):
		"""Handles updating an object."""

		return Response({'method': 'put'})

	def patch(seld, request, pk=None):
		"""Patch request, only updates fields provided in the request """

		return Response({'method': 'patch'})

	def delete(self, request, pk=None):
		"""Delete an object """

		return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
	"""Test API viewset"""
	
	def list(self, request):
		"""Return a hello message"""

		a_viewset = [
			'Users actions (list, create, retrieve, update, partial_update)',
			'Automatically maps to URLS using Rousters',
			'Provides more functionality with less code.'
		]

		return Response({'message': 'Hello', 'a_viewset':a_viewset})