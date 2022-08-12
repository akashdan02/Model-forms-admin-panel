from django.shortcuts import render, redirect
from .models import Application_settings
from .forms import ApplicationForm
# Create your views here.

def application(request):
    if request.method =="POST":
       form = ApplicationForm(request.POST)
       if form.is_valid():
           try:
               form.save()
               return redirect("/show")
           except:
               pass
    else:
        form = ApplicationForm()
    return render(request, "index.html", {'form': form})

def show(request):
    applications = Application_settings.objects.all()
    return render(request, 'show.html', {'applications':applications})

def edit(request, id):
    application = Application_settings.objects.get(id=id)
    return render(request, 'edit.html', {'application': application})

def update(request, id):
    application = Application_settings.objects.get(id=id)
    form = ApplicationForm(request.POST, instance = application)
    if form.is_valid():
        form.save()
        return redirect("/show")
    else:
        print("error")
        context = {'application': application}

    return render(request ,"edit.html", context)

def delete(request,id):
    application = Application_settings.objects.get(id=id)
    application.delete()
    return redirect('/show')

