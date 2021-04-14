from django.db import models
from datetime import datetime


class ProjectCategory(models.Model):
	project_category = models.CharField(max_length=200)
	project_summary = models.CharField(max_length=200)


	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.project_category


class ProjectSeries(models.Model):
	Project_series = models.CharField(max_length=200)
	Project_category = models.ForeignKey(ProjectCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
	Project_summary = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Series"

	def __str__(self):
		return self.project_series


# Create your models here.
class Project(models.Model):
	project_title = models.CharField(max_length=200)
	project_content = models.TextField()
	project_published = models.DateTimeField("date published", default=datetime.now())

	project_series = models.ForeignKey(ProjectSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
	
	def __str__(self):
		return self.project_title
