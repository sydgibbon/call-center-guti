from assets.computers.serializers import *
from rest_framework import serializers  # import de serializers
from rest_framework import generics, viewsets, views, permissions, status  # import de ViewSets
from assets import serializers  # import de todos los serializers,
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

