from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status, pagination
from rest_framework import response

from .models import Project,ProjectCategory,ProjectSeries
from .serializers import ProjectSerializer,ProjectCategorySerializer,ProjectSeriesSerializer

class ProjectCategoryView(generics.GenericAPIView):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    def get(self,request,*args,**kwargs):
        projectCategory = ProjectCategory.objects.all()
        serilized = self.get_serializer(projectCategory,many = True)
        return response.Response(serilized.data,status = status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        serilized = self.get_serializer(data = request.data)
        if serilized.is_valid():
            serilized.save()
            return response.Response(status=status.HTTP_201_CREATED)
        return response.Response(serilized.errors)

class ProjectCategoryViewDetails(generics.GenericAPIView):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    def get(self,request,*args,**kwargs):
        if kwargs.get('pk'):
            projectCategory =ProjectCategory.objects.get(pk = kwargs.get('pk'))
            serilized = self.get_serializer(projectCategory)
            return response.Response(serilized.data,status = status.HTTP_200_OK)
    def put (self,request,*args,**kwargs):
        if kwargs.get('pk'):
            projectCategory = ProjectCategory.objects.get(pk = kwargs.get('pk'))
            serialized = self.get_serializer(projectCategory,data = request.data)
            if serialized.is_valid():
                serialized.save()
                return response.Response(serialized.data,status=status.HTTP_204_NO_CONTENT)
            return response.Response(serialized.errors)
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            projectCategory = ProjectCategory.objects.get(pk=kwargs.get('pk'))
            projectCategory.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class ProjectSeriesView(generics.GenericAPIView):
    queryset = ProjectSeries.objects.all()
    serializer_class = ProjectSeriesSerializer
    def get(self,request,*args,**kwargs):
        projectSeries = ProjectSeries.objects.all()
        serilized = self.get_serializer(projectSeries,many = True)
        return response.Response(serilized.data,status = status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        serilized = self.get_serializer(data = request.data)
        if serilized.is_valid():
            serilized.save()
            return response.Response(status=status.HTTP_201_CREATED)
        return response.Response(serilized.errors)

class ProjectSeriesViewDetails(generics.GenericAPIView):
    queryset = ProjectSeries.objects.all()
    serializer_class = ProjectSeriesSerializer
    def get(self,request,*args,**kwargs):
        if kwargs.get('pk'):
            projectSeries =ProjectSeries.objects.get(pk = kwargs.get('pk'))
            serilized = self.get_serializer(projectSeries)
            return response.Response(serilized.data,status = status.HTTP_200_OK)
    def put (self,request,*args,**kwargs):
        if kwargs.get('pk'):
            projectSeries = ProjectSeries.objects.get(pk = kwargs.get('pk'))
            serialized = self.get_serializer(projectSeries,data = request.data)
            if serialized.is_valid():
                serialized.save()
                return response.Response(serialized.data,status=status.HTTP_204_NO_CONTENT)
            return response.Response(serialized.errors)
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def delete(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            projectSeries = ProjectSeries.objects.get(pk=kwargs.get('pk'))
            projectSeries.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class ProjectView(generics.GenericAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    def get(self,request,*args,**kwargs):
        project = Project.objects.all()
        serilized = self.get_serializer(project,many = True)
        return response.Response(serilized.data,status = status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        serilized = self.get_serializer(data = request.data)
        if serilized.is_valid():
            serilized.save()
            return response.Response(status=status.HTTP_201_CREATED)
        return response.Response(serilized.errors)

class ProjectViewDetails(generics.GenericAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    def get(self,request,*args,**kwargs):
        if kwargs.get('pk'):
            project =Project.objects.get(pk = kwargs.get('pk'))
            serilized = self.get_serializer(project)
            return response.Response(serilized.data,status = status.HTTP_200_OK)
    def put (self,request,*args,**kwargs):
        if kwargs.get('pk'):
            project = Project.objects.get(pk = kwargs.get('pk'))
            serialized = self.get_serializer(project,data = request.data)
            if serialized.is_valid():
                serialized.save()
                return response.Response(serialized.data,status=status.HTTP_204_NO_CONTENT)
            return response.Response(serialized.errors)
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def delete(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            project = Project.objects.get(pk=kwargs.get('pk'))
            project.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


