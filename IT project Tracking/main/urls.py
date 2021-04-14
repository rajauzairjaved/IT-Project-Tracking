from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="PROJECT API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.track-it.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

from django.urls import path
from main.views import ProjectView,ProjectViewDetails,ProjectCategoryView,ProjectCategoryViewDetails,ProjectSeriesView,ProjectSeriesViewDetails


app_name = 'main' 

urlpatterns = [


    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('project_series/', ProjectSeriesView.as_view()),
    path('project_series/<int:pk>', ProjectSeriesViewDetails.as_view()),

    path('project_category/', ProjectCategoryView.as_view()),
    path('project_category/<int:pk>', ProjectCategoryViewDetails.as_view()),

    path('project/',ProjectView.as_view()),
    path('project/<int:pk>',ProjectViewDetails.as_view()),






]