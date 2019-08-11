from django.shortcuts import render

def contact_detail(request):
	return render(request,'contact/contactus.html',{})


