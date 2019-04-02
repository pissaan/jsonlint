from django.shortcuts import render,HttpResponse

import json
# Create your views here.

def index(request):
	return render(request,"index.html",{})



def success(message):
	content={}
	content['result']="success"
	content['description']=message
	return HttpResponse(json.dumps(content))

def fail(message):
	content={}
	content['result']="fail"
	content['description']=message
	return HttpResponse(json.dumps(content))