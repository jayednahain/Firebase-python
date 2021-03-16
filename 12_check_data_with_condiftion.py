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

search_data = input("enter data for search: ")
new_data = input("enter new name: ")

data_slot = database.child('testing3').child('testing3testing3').get()

for data in data_slot.each():
   if data.val == search_data:
      database.child("testing3").child("testing3").update({data.val():new_data})
   else:
      print(data ," not found !")

