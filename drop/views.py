from django.http import HttpResponse
from drop.models import course,branch,sem,section
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from django.contrib.sessions.models import Session

# Create your views here.

def func(request):


	
	# if request.method == 'POST':
	# 	data = json.loads(request.body)

	# 	obj=course.objects.all()
	# 	for x in obj:
	# 	 	if (x.co==data['course']):
	# 	 		q=course.objects.filter(co=data['course']).values('id')
	# 	 		q2=branch.objects.filter(link1=q[0]['id']).values('br')
		 		
	# 	 		return JsonResponse(list(q2),safe=False)

	if request.method == "GET":

			c=request.GET.get('course', '1')
			d = request.GET.get('br','1')
			e = request.GET.get('id','1')


			if(c=="1" and d=="1"):
				q=course.objects.filter().values('co')
				print(q)
				return JsonResponse(list(q), safe=False)

			elif(c!="1" and d=="1"):
				q1=course.objects.filter(co=c).values('id')
				q2=branch.objects.filter(link1=q1[0]['id']).values('br','link1__id')
				print(q2)
				return JsonResponse(list(q2),safe=False)
			

			elif(c=="1" and d!="1"):
				q1=branch.objects.filter(br=d, link1=e).values('id')
				q2=sem.objects.filter(link2=q1[0]['id']).values('sems')
				print(q2)
				return JsonResponse(list(q2),safe=False)
		 			 		


			# for x in obj:
		 # 		if ():
		 # 			q=course.objects.filter(co=data['course']).values('id')
		 # 			q2=branch.objects.filter(link1=q[0]['id']).values('br')
		 		
		 # 			return JsonResponse(list(q2),safe=False)


		# except:
			
		# 	d = request.GET.get('br','1')

		# 	obj1=branch.objects.all()

		# 	for x in obj1:
		# 		q1=branch.objects.filter(br=d).values('id')
		# 		q12=sem.objects.filter(link2=q1[0]['id']).values('sems')
		# 		return JsonResponse (list(q12), safe=False)




