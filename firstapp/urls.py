from django.urls import path
from . import views 

urlpatterns = [
    path('function', views.hello_world),
    path('class', views.HelloBangladesh.as_view()), # As_view() is used to convert class-based view to function-based view  
    path('reservation', views.home), # This is the URL for the home page where the form is displayed
]