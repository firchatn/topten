from django.shortcuts import render
import json
# Create your views here.
def index(request):
	with open('/home/firas/git/scripts-python/data.json') as data_file:
		info = json.load(data_file)
	return render(request,'top/index.html', {'info' : info})