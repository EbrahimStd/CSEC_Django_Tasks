from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from accounts.forms import SignupForm

# Create your views here.


def signup(request):
   # check if form is submitted 
   if request.method == 'POST':
      # get request data
      form = SignupForm(request.POST)
      # check if form data is valid before save in DB
      if form.is_valid():
         form.save()
         # login after save
         username = form.cleaned_data['username']
         password = form.cleaned_data['password1']
         print('will authenticate')
         user = authenticate(username=username, password=password)
         print('will login')
         login(request, user)
         print('redirect to profile')
         return redirect('/accounts/profile')         

   else: # else return form as empty
      print('Not valid form')
      form = SignupForm()
   return render(request,'registration/signup.html',{'form':form})



# show profile data to user
@login_required
def profile(request):
   profile = request.user
   context = {'profile':profile}
   return render(request, 'profile/profile.html',context)
