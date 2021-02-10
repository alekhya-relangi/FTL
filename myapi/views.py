from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MemberSerializer
from .models import members

# Create your views here.

class MemberViewSet(viewsets.ModelViewSet):
    queryset = members.objects.all().order_by('m_id')
    serializer_class = MemberSerializer