from django.shortcuts import render, HttpResponse

# Create your views here.
def loggedin(request):
	return HttpResponse('You have been logged in!')

def index(request):
	return render(request, 'accounts/index.html')