import pyrebase




config ={
    'apiKey': "AIzaSyDvYny5xfQor_flForVWYYU0y9d6F54BtQ",
    "authDomain": "attendance-system-9fbec.firebaseapp.com",
    "databaseURL":"https://attendance-system-9fbec-default-rtdb.firebaseio.com/",
    "projectId": "attendance-system-9fbec",
    "storageBucket": "attendance-system-9fbec.appspot.com",
    "messagingSenderId": "314768776178",
    "appId": "1:314768776178:web:f30ae218e4cc433679e96b",
    "measurementId": "G-D99TF7MPCS"
  }




firebase_config = pyrebase.initialize_app(config)


database = firebase_config.database()


name = input("enter name: ")
#id = input("enter id : ")
#city = input("enter city name")

data_send = {
   "name":"jayed",
   "id":"123",
   "city":"comilla"
}

database.child(name).set(data_send)