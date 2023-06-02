from django.db import models



class UploadLink(models.Model):
	Title=models.CharField(max_length=100)
	Descrpition=models.CharField(max_length=10000)
	link=models.CharField(max_length=1000)
	thumbnail=models.CharField(max_length=225,default="onimage.png")
	Updatetime=models.CharField(max_length=100,default="")
	softdelete=models.IntegerField(default=0)



class mentors(models.Model):
	mentors_name=models.CharField(max_length=100)
	mentors_Designation=models.CharField(max_length=1000)
	mentors_details=models.CharField(max_length=1000)
	image=models.CharField(max_length=225,default="onimage.png")
	registerdate=models.CharField(max_length=100,default="")
	softdelete=models.IntegerField(default=0)

class registerdata(models.Model):
	user_name=models.CharField(max_length=100)
	mobilenumber=models.CharField(max_length=13,default="",primary_key=True)
	email_id=models.CharField(max_length=100)
	created_on=models.CharField(max_length=100,default="")
	created_by=models.CharField(max_length=100,default="")
	registerdate=models.CharField(max_length=100,default="")
	softdelete=models.IntegerField(default=0)

class operatorregister(models.Model):
	Operatoruser_name=models.CharField(max_length=100)
	Operatormobile_number=models.CharField(max_length=13,default="",primary_key=True)
	Operatoremail_id=models.CharField(max_length=100)
	Operatorpassword=models.CharField(max_length=100)
	role=models.CharField(max_length=100)
	created_on=models.CharField(max_length=100,default="")
	created_by=models.CharField(max_length=100,default="")
	registerdate=models.CharField(max_length=100,default="")
	softdelete=models.IntegerField(default=0)
