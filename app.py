

from mongoengine import *

from flask import Flask, request, render_template

app = Flask(__name__)

connect(db='festzone',host = '127.0.0.1',port = 27017)
class Customers(Document):
    Name = StringField()
    Username = StringField()
    Password = StringField()
    Email = StringField()

@app.route('/signup', methods = ['POST'])
def signup():


    name= request.form["Name"]
    user=request.form["Username"]
    passwd=request.form["Username"]
    em=request.form["Email"]
        
        
    record=Customers(Name = name,Username = user,Password = passwd,Email = em)
    record.save()
if __name__=='__main__':
   app.run()








'''app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'your_database',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

class User(db.Document):
    name = db.StringField()
    Username = db.StringField()
    Password = db.StringField()
    Email = db.StringField()

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.festzone
customer = db.customer

@app.route('/index.html', methods=('GET', 'POST'))
def index():

    if request.method=='POST':
        Name = request.form.get['Name']
        Username = request.form['Username']
        Password = request.form['Password']
        Email = request.form['Email']


        customer.insert_one({ 
          "name": Name,
          "username": Username,
          "password": Password,
          "Email": Email
          })
        return redirect(url_for('index'))

    all_todos = customer.find()
    return render_template('index.html', todos=all_todos)
    app.run(localhost,2020)
index()

db=client['festzone']

collection = db['customer']
record = { 
          "name": Name,
          "username": User,
          "password": Passwd,
          "Email": Email,
          "category":Cat}

rec_id1 = collection.insert_one(record)'''