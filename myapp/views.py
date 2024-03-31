from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import pickle
import numpy as np

@api_view(["POST"])
def flowerPredict(request):
	try:
		model_loaded = pickle.load(open('static/model_saved', 'rb'))
		mydata=request.data
		# print(mydata)
		unit=np.array(list(mydata.values()))
		unit=unit.reshape(1,-1)
		y_pred=model_loaded.predict(unit)
		return JsonResponse('Your Flower is {}'.format(y_pred), safe=False)
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
	
@api_view(["POST"])
def monthlyExpenditure(request):
	try:
		model_loaded = pickle.load(open('static/monthly_exp', 'rb'))
		mydata=request.data
		print(mydata)
		unit=np.array(list(mydata.values()))
		unit=unit.reshape(1,-1)
		y_pred=model_loaded.predict(unit)
		return JsonResponse('Next Predicted Expenditure {}'.format(y_pred), safe=False)
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
	
