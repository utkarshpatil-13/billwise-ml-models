from django.urls import path
from myapp.views import flowerPredict, monthlyExpenditure

urlpatterns = [
    path('flower/', flowerPredict),
    path('monthly-exp/', monthlyExpenditure),
]