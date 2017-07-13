# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader

def dashboard(request):
    return render_to_response("webapp/dashboard.html")

def charitiesList(request):
	charities = ['charity water', 'breast cancer awareness', 'wah'];
	return render_to_response('webapp/charitieslist.html', {'charities':charities})

def index(request):
	return HttpResponse("Hello, world. You're at charities.")

def new_charity_form(request):
	if request.method == 'POST': 
		form = NewCharityForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/home/charities')
	return render_to_response('webapp/new_charities_form.html')
