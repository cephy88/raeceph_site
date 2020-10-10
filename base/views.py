from django.shortcuts import render

# Create your views here.


def resume(request):
	return render(request, 'base/resume.html')

def base(request):
	return render(request, 'base/base.html')