import json
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .views import success,fail
import re


def remove_tags(text):
	TAG_RE = re.compile(r'<[^>]+>')
	return TAG_RE.sub('', text)
	


@csrf_exempt
def validateJson(request):
	strJson=request.POST.get('strjson',None)

	print(strJson)
	loadJson=None
	exceptionValue=None

	if(strJson != None):
		strJson=remove_tags(strJson)
		print(strJson)
		try:
			loadJson=json.loads(strJson)

		except Exception as e:
			print(e)
			exceptionValue=e
	if(exceptionValue != None):
		return fail(str(exceptionValue))

	return success("Valid json formate")



@csrf_exempt
def formateJson(request):
	strJson=request.POST.get('strjson',None)

	print(strJson)
	loadJson=None
	exceptionValue=None
	contentValue=None

	if(strJson != None):
		strJson=remove_tags(strJson)
		print(strJson)
		try:
			loadJson=json.loads(strJson)
			contentValue=json.dumps(loadJson)

		except Exception as e:
			print(e)
			exceptionValue=e
	if(exceptionValue != None):
		return fail(str(exceptionValue))

	content={}
	content['result']="success"
	content['description']="Valid json formate"
	content['content']=contentValue

	return HttpResponse(json.dumps(content))