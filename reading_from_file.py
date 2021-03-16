import pyrebase
import urllib
from urllib import request



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


#books/shakes_file.txt


firebase_config = pyrebase.initialize_app(config)
storage = firebase_config.storage()

path_with_file = input("enter the path including file for reading : ")
print(storage.child(path_with_file).get_url(None))

url = storage.child(path_with_file).get_url(None)
f = request.urlopen(url).read()
print(f)