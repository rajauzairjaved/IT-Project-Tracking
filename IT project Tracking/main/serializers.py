from rest_framework import serializers
from .models import ProjectCategory,Project,ProjectSeries



class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = '__all__'


class ProjectSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSeries
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
