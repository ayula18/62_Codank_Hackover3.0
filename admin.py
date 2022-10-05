
from mongoengine import *
connect(db='festzone',host = '127.0.0.1',port = 27017)
class Admin(Document):
    Name = StringField()
    Username = StringField()
    Password = StringField()
    Email = StringField()
record1=Admin(Name = "Ayush",Username = "AyushLahoti",Password = "Ayush@123",Email = "ayush123@gmail.com")
record1.save()
record2=Admin(Name = "Kaushal",Username = "KaushalAgg",Password = "Kash@123",Email = "kash@gmail.com")
record2.save()
record3=Admin(Name = "Gaurav",Username = "Gaurav124",Password = "Gaurav@1508",Email = "gaurav@gmail.com")
record3.save()
record4=Admin(Name = "Anushka",Username = "AnushkaBehere",Password = "Anushka@1808",Email = "anushka@gmail.com")
record4.save()

print("Sucessful")
