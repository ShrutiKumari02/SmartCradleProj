from django.shortcuts import render
import pyrebase

config={
    "apiKey": "AIzaSyC8_PaL11nRYh4iC8irN21PhamEGgw8ufw",
    "authDomain": "fir-iot-5be90.firebaseapp.com",
    "databaseURL": "https://fir-iot-5be90-default-rtdb.firebaseio.com",
    "projectId": "fir-iot-5be90",
    "storageBucket": "fir-iot-5be90.appspot.com",
    "messagingSenderId": "387618892766",
    "appId": "1:387618892766:web:992fcbca402ec4e4b80b4f",
}
firebase=pyrebase.initialize_app(config)
authe=firebase.auth()
database=firebase.database()

def index(request):
    distance = database.child('FirebaseIOT').child('cm').get().val()
    humidity = database.child('FirebaseIOT').child('humidity').get().val()
    temperature = database.child('FirebaseIOT').child('temperature').get().val()
    bpm = database.child('FirebaseIOT').child('beatsPerMinute').get().val()
    bavg = database.child('FirebaseIOT').child('beatAvg').get().val()
    babydata = database.child('FirebaseIOT').child('babydata').get().val()
    babydata=int(babydata)
    return render(request,'index.html',{
        "distance":distance,
        "humidity":humidity,
        "temperature":temperature,
        "bpm":bpm,
        "bavg":bavg,
        "babydata":babydata
    })

def about(request):
    return render(request,'about.html')