from django.shortcuts import render
import pyrebase
import json
from django.conf import settings

# Create your views here.
with open(settings.BASE_DIR + '/realtimedbcreds.json') as f:
    config = json.load(f)

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def index(request):
    # accessing our firebase data and storing it in a variable
    name = database.child('Data').child('another').get().val()
    stack = database.child('Data').child('something').get().val()

    context = {
        'name': name,
        'stack': stack,
    }
    print(context)
    return render(request, 'index.html', context)
