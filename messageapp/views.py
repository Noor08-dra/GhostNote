from django.shortcuts import render,redirect
from .models import message
from .forms import MessageForm
from django.views.generic.edit import UpdateView,DeleteView,CreateView,FormMixin
from django.views.generic import ListView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request,'messageapp/home.html')


class MessageCreateView(LoginRequiredMixin,CreateView):
     model=message
     template_name="messageapp/create_page.html"
     form_class=MessageForm
     success_url=reverse_lazy("home-page")

     login_url=reverse_lazy("account_login")
     redirect_field_name="next"


     
class MessageListView(ListView):
     model=message
     template_name="messageapp/messages_list.html"
     context_object_name="msgs"
     ordering=["-date_posted"]   

     def get_queryset(self,*args,**kwargs):
          qs=super().get_queryset(*args,**kwargs)
          searched_name=self.request.GET.get("query_name") #context variable
          if searched_name:
               qs=qs.filter(recipient_name__icontains=searched_name)
          return qs  

     def get_context_data(self,*args,**kwargs):
          context=super().get_context_data(*args,**kwargs)
          context["searched_name"]=self.request.GET.get("query_name")
          return context  
     
class MessageDeleteView(LoginRequiredMixin,DeleteView):
     model=message
     context_object_name='msg'
     success_url=reverse_lazy("message_list")

class MessageEditView(LoginRequiredMixin,UpdateView):
     model=message
     context_object_name='msg'
     template_name="messageapp/create_page.html"
     form_class=MessageForm     
     success_url=reverse_lazy("message_list")
     
