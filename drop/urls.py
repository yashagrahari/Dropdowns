from django.conf.urls import url
from .views import func

urlpatterns=[
	
	url(r'^$' , func),
]