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
storage = firebase_config.storage()

#file name as your local file name
file = input("enter file name for upload: ")

#define direcotry give a file name ! this is not necessary to put the same name as local file
file_name_with_path = input("enter file name with directory: ")

storage.child(file_name_with_path).put(file)

# get file url
print(storage.child(file_name_with_path).get_url(None))






