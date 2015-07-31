from django.shortcuts import render

# Create your views here.

def home(request):
    if request.user.is_authenticated():
        #sample = "Praneeth Kumar Pidugu"
        context = {"sample":request.user}
    else:
        context = {"sample": request.user}
    template = 'base.html'
    return render(request, template, context)