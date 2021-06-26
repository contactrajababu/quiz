from django.urls import path
from . import views
urlpatterns = [
path('employees',views.employeelist.as_view())
]