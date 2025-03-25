from django.shortcuts import render, redirect
from app.forms import studentForm
from django.contrib import messages

# Create your views here.
def add(request):
    if request.method == 'POST':
        fm = studentForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Student added successfully!")  # Flash message
            return redirect('add')
    else:
        fm = studentForm()
    
    return render(request, 'html/add.html', {'form': fm})



def update(request):
    return render(request,'html/update.html')