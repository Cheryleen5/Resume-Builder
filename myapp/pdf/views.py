from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io

# Create your views here.
def accept(request):
    if request.method =="POST":
        Name=request.POST.get("name","")
        Phone=request.POST.get("phone","")
        Email=request.POST.get("email","")
        About_you=request.POST.get("about_you","")
        School=request.POST.get("school","")
        Degree=request.POST.get("degree","")
        University=request.POST.get("university","")
        Previous_work=request.POST.get("previous_work","")
        Skill=request.POST.get("skill","")
        Certificate=request.POST.get("certificate","")
        Language=request.POST.get("language","")
        Hobby=request.POST.get("hobby","")
        Project = request.POST.get('project', '')
        profile=Profile(name=Name, phone=Phone, email=Email, about_you=About_you, school=School, degree=Degree, university=University, skill=Skill, certificate=Certificate, language=Language, hobby=Hobby, previous_work=Previous_work, project=Project)
        profile.save()  
        
    return render(request, 'accept.html')

def resume(request, id):
    user_profile=Profile.objects.get(pk=id)
    template = loader.get_template('resume.html')
    html = template.render({'user_profile':user_profile})
    option = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }   
    pdf = pdfkit.from_string(html, False, option)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachments'
    return response
   
def list(request):
    profile=Profile.objects.all()
    return render(request, 'list.html', {'profile':profile})
        