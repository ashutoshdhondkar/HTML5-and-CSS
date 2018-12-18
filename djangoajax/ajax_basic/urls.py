from django.urls import path
from . import views
urlpatterns = [
	path('',views.basic,name='index'),
	path('submit',views.index,name='basic'),
]