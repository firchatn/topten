from django.shortcuts import render
import json
from collections import namedtuple
# Create your views here.
def index(request):
	with open('/home/firas/git/scripts-python/data.json') as data_file:
		data = json.load(data_file)
	info = [] 
	info = data
	return render(request,'top/index.html', {'info' : info})
