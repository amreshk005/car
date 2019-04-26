from django.shortcuts import render,reverse
from .forms import SuscribeForm
from django.http import HttpResponseRedirect

def register(request):
    if request.method == 'POST':
        form = SuscribeForm(request.POST)
        if form.is_valid():
            register = form.save()
            return HttpResponseRedirect('')
    else:
        form = SuscribeForm()    
    return render(request,'index.html',{'form':form})


def privacy(request):
    return render(request,'privacy_policy.html')