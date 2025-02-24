from django.urls import path
from . import views
#localhost:8000/start
#localhost:8000/start/order
urlpatterns = [
     
    path('',views.all_chai,name="all_chai"),
    path('index/',views.all_chai,name="all_chai"),
    
     
]
