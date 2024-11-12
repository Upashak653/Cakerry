from django.shortcuts import render
from cake.models import Book_cake,ItemList,Items,AboutUs,Feedback
from django.shortcuts import redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
#from .forms import UserRegistrationForm


# Create your views here.

def Home(request):
   items = Items.objects.all()
   list = ItemList.objects.all()
   review = Feedback.objects.all()
   return render(request,'home.html',{'items':items,'list':list , 'review':review})

def About(request):
   data = AboutUs.objects.all()
   return render(request,'about.html',{'data':data})

def Menu(request):
   items=Items.objects.all()
   list = ItemList.objects.all()
   return render(request,'menu.html',{'items':items,'list':list}) 

@login_required
def Booking(request):
   if request.method=='POST':
      name = request.POST.get('user_name')
      email = request.POST.get('user_email')
      cake=request.POST.get('user_cake')
      persons = request.POST.get('user_persons')
      occassion = request.POST.get('user_occassion')
      cakesize = request.POST.get('user_cakesize')
      date = request.POST.get('date')

      if name !='' and email !='' and persons !='' and occassion !='' and cakesize !='' and date !='':
         data = Book_cake(Name=name,
                          Email_number=email,
                          Cake=cake,
                          Total_person=persons,
                          Occassion=occassion,
                          Cake_size=cakesize,
                          Booking_date=date)
         data.save()
         messages.success(request,"Hurray we have got your order.Please take your seat for a while")
         return redirect('Home')

   return render(request,'book.html')

@login_required
def FeedBack(request):
   if request.method == 'POST':
       clientname= request.POST.get('user_name')
       clientexperience= request.POST.get('description')
       clientrating=request.POST.get('user_rating')

       if clientname !='' and clientexperience !='' and clientrating != '' :
         data2= Feedback( User_name=clientname,
                       Description=clientexperience,
                       Rating=clientrating,)
         data2.save()
         messages.success(request,"Thank you for your rating")
         return redirect('Home')
   return render(request,'feedback.html')
   

def Logout(request):
   if request.method=='POST':
    logout(request)
    messages.success(request,"Logout Succesfull.")
   return redirect('Home')

      

def Register(request):
      if request.method == 'POST':
          form = UserCreationForm(request.POST,request.FILES or None)
          if form.is_valid():
           form.save()
           messages.success(request,"Registration Succesfull.")
           return redirect("Home")
      else:
         form = UserCreationForm()
         
      return render(request, 'register.html',{'form':form} )

