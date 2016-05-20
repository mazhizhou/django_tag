from django.shortcuts import render, render_to_response

# Create your views here.

def d3_index(request):
	return render_to_response('d3_index.html')

def d3_pop(request):
    return render_to_response('pop.html')
