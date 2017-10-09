from django.shortcuts import render
import json
from collections import namedtuple
# Create your views here.
def index(request):
	with open('/home/firas/git/youtubetop/data/data.json') as data_file:
		data = json.load(data_file)
	info = [] 
	info = data[:50] #top 50 video 
	return render(request,'top/index.html', {'info' : info})
