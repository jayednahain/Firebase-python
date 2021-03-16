
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

authentication= firebase_config.auth()


try:
   def sine_up():
      email = input("enter email: ")
      passsword =input("enter password: ")
      try:
         new_user = authentication.create_user_with_email_and_password(email,passsword)
         print("account created successfully !")
         login_notice = input("do you want to log in now ? [y/n] ")
         if login_notice == "y":
            log_in()
         else:
            print("as your wish! ")

      except:
         print("this emai already create")
except:
   print("email error")

def log_in():
   try:
      email = input("enter email:")
      password = input("enter passsword: ")
      login = authentication.sign_in_with_email_and_password(email, password)
      #for values in dir(login):
         #print(values)
      print("log in successfully! ")
      # getting account info !
      print(authentication.get_account_info())
      #print(login.values())
   except:
      print("invalled user id and passsword !")





ans = input("are you a new user [y/n]: ")

if ans == "y":
   sine_up()
elif ans == "n":
   log_in()


