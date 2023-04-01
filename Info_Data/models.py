from django.db import models
from django.core.exceptions import ValidationError

Project_Visibility = ['None', 'All', 'Owners_Of_Applied_Projects']
Profile_Visibility = ['None', 'All', 'Owners_Of_Applied_Projects']
Color_Theme = ['Light_Mode', 'Dark_Mode']
Tags_Category = ['Language', 'Framework', 'Group']


def validate_Color_Theme(value):
    if value not in Color_Theme:
        raise ValidationError("Invalid value!")


def validate_Project_Visibility(value):
    if value not in Project_Visibility:
        raise ValidationError("Invalid value!")


def validate_Profile_Visibility(value):
    if value not in Profile_Visibility:
        raise ValidationError("Invalid value!")


class Tags(models.Model):
    Name = models.CharField(max_length=50)
    Category = models.CharField(max_length=100,)

    def __str__(self):
        return self.Name


class User(models.Model):
    Name = models.CharField(max_length=50, null=False)
    E_mail = models.CharField(max_length=50, null=False)
    GitHub_ID = models.CharField(max_length=50, null=True, blank=True)
    Programme = models.CharField(max_length=50, null=False)
    Department = models.CharField(max_length=50, null=False)
    Year = models.CharField(max_length=4, null=False)
    Miscellaneous = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Name
    # Projects=models.ManyToManyField(Project,null=True)
    # Groups=models.ManyToManyRel(Group,null=True)


class User_Tag(models.Model):
    Tag_id = models.ForeignKey(Tags, on_delete=models.CASCADE)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Settings(models.Model):
    Color_Theme=models.CharField(max_length=50,validators=[validate_Color_Theme])
    Project_Visibility=models.CharField(max_length=50,validators=[validate_Project_Visibility])
    Profile_Visibility=models.CharField(max_length=50,validators=[validate_Profile_Visibility])
    User_id=models.ForeignKey(User,on_delete=models.CASCADE)


class Project(models.Model):
    Title = models.CharField(max_length=50)
    Owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Abstract = models.TextField()
    Getting_Started = models.TextField()
    Completed_Status = models.BooleanField()
    Deadline = models.DateTimeField()

    def __str__(self):
        return self.Title


class Project_Tag(models.Model):
    Tag_id = models.ForeignKey(Tags, on_delete=models.CASCADE)
    Project_id = models.ForeignKey(Project, on_delete=models.CASCADE)


class Project_Applicant(models.Model):
    Project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    Applicant_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Appeal=models.CharField(max_length=500)


class Project_Member(models.Model): # Indexed by project ( to list all members when we go on project page)
    Project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    Member_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Member_Project(models.Model): # Indexed by user ( to list all projects when we go on profile page)
    Member_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Project_id = models.ForeignKey(Project, on_delete=models.CASCADE)


class Chat_Rooms(models.Model):
    User_id1 = models.BigIntegerField()
    User_id2 = models.BigIntegerField()


class Individual_Chat(models.Model):
    User_id = models.BigIntegerField()
    Time = models.DateTimeField()
    content = models.TextField()
    Chat_id = models.ForeignKey(Chat_Rooms, on_delete=models.CASCADE)
    Parent_id = models.BigIntegerField(null=True, blank=True)


class Project_Chat(models.Model):
    Project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Time = models.DateTimeField()
    Content = models.TextField()

# Create your models here.
class Group(models.Model):
    Name=models.CharField(max_length=50)
    Description=models.TextField()
    Certified=models.BooleanField()


class Group_members(models.Model):
    Group_id=models.ForeignKey(Group, on_delete=models.CASCADE)
    Mmeber_id=models.ForeignKey(User, on_delete=models.CASCADE)
    Role=models.CharField(max_length=50)


