from django.shortcuts import render,redirect
from .models import message
from .forms import MessageForm

# Create your views here.
def home(request):

    if request.method=="POST":
        form=MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
        else:
            print(form.error)
    else:
       form=MessageForm()

    if request.method=="GET":
        searched_name=request.GET.get("query_name")   
        if searched_name:
            filtered_msgs=message.objects.filter(recipient_name__iexact=searched_name)
        else:
            filtered_msgs=message.objects.all()

    context={'msgs':filtered_msgs,'form':form,'searched_name':searched_name}
    return render(request,'messageapp/home.html',context)