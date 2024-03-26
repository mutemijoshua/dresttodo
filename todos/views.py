from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from rest_framework import permissions,filters
from todos.serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from todos.models import Todo
from django_filters.rest_framework import DjangoFilterBackend
from todos.pagination import CustomPageNumberPagination
# Create your views here.

class TodosAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['id','title','desc','is_complete']
    search_fields = ['id','title','desc','is_complete']
    ordering_fields = ['id','title','desc','is_complete']
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)