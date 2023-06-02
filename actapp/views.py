from django.shortcuts import render
from actapp.models import registerdata,operatorregister,mentors,UploadLink
from django.core.files.storage import FileSystemStorage
import datetime

def displayliks(request):
	data=""
	data=UploadLink.objects.all()
	return render(request,"displayliks.html",{"data":data})


def uploadlink(request):
	msg=""
	if request.method=="POST":
		g=UploadLink()
		g.Title=request.POST["texttitle"]
		g.Descrpition=request.POST["txtDescription"]
		g.link=request.POST["link"]	

		file=request.FILES["myimage"]
		fs=FileSystemStorage()
		thumbnail=fs.save(file.name,file)
		g.thumbnail=fs.url(file)
		g.Updatetime=datetime.datetime.now()
		g.save()
		msg="uploadlink successfully"
	else:
		msg=""
	return render(request,"uploadlink.html",{"msg":msg})

def mentorsSearch(request):
	msg=""
	data=""
	if request.method=="POST":
		action=request.POST["btnsubmit"]
		if action=="Update":
			did=request.POST["did"]

			file=request.FILES["newimage"]
			fs=FileSystemStorage()
			image=fs.save(file.name,file)
			image=fs.url(file)
			
			data=mentors.objects.filter(id=did)
			data.update(mentors_name=request.POST["mentors_name"],mentors_Designation=request.POST["mentors_Designation"],mentors_details=request.POST["mentors_details"],image=fs.url(file))
			msg="mentor Details Updated"
			return render(request,"mentorssearch.html",{"msg":msg,"data":data})

		elif action=="Edit":
			did=request.POST["did"]
			data=mentors.objects.filter(id=did)
			return render(request,"mentoredit.html",{"msg":msg,"data":data})

		elif action=="Delete":
			did=request.POST["did"]
			data=mentors.objects.filter(id=did).delete()
			data=softdelete=0
			msg="Mentor data deleted successfully"
		else:
			filename=request.POST["ddfname"]
			searchvalue=request.POST["txtsearch"]
			if searchvalue.isnumeric() and filename=="id":
				if mentors.objects.filter(id=searchvalue):
					data=mentors.objects.filter(id=searchvalue)
				else:
					msg="Record Not found"
			else:
				if(filename=="mentors_name"):
					if mentors.objects.filter(mentors_name__icontains=searchvalue).exists():
						data=mentors.objects.filter(mentors_name__icontains=searchvalue)
					else:
						msg="Record Not found"
	return render(request,"mentorssearch.html",{"msg":msg,"data":data})



def uplodmentors(request):
	msg=""
	if request.method=="POST":
		a=mentors()
		a.mentors_name=request.POST["textname"]
		a.mentors_Designation=request.POST["txtDesignatio"]
		a.mentors_details=request.POST["txtdetails"]
		file=request.FILES["myfile"]
		fs=FileSystemStorage()
		image=fs.save(file.name,file)
		a.image=fs.url(file)
		a.registerdate=datetime.datetime.now()
		a.save()
		msg="Registered successfully"
	else:
		msg=""
	return render(request,"uplodmentors.html",{"msg":msg}) 


def operatorRegister(request):
	msg=""
	if request.method=="POST":
		d=operatorregister()
		d.Operatoruser_name=request.POST["textname"]
		d.Operatormobile_number=request.POST["textmobilenumber"]
		d.Operatoremail_id=request.POST["textemailid"]
		d.Operatorpassword=request.POST["textPassword"]
		d.Operatorrole=request.POST["ddlads"]
		d.registerdate=datetime.datetime.now()
		d.save()
		msg="Registered Successfully"
	else:
		msg=""
	return render(request,"operatorRegister.html",{"msg":msg})

def userregister(request):
	msg=""
	if request.method=="POST":
		s=registerdata()
		s.user_name=request.POST["textname"]
		s.mobilenumber=request.POST["textmobilenumber"]
		s.email_id=request.POST["textemail"]
		s.registerdate=datetime.datetime.now()
		s.save()
		msg="Registered Successfully"
	else:
		msg=""
	return render(request,"userregister.html",{"msg":msg})


