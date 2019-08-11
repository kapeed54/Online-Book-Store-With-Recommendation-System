from django.shortcuts import render

def about_detail(request):
	return render(request,'about/aboutus.html',{})


