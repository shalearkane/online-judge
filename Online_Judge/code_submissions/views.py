from django.shortcuts import render
import pyrebase
import json
from django.conf import settings

# Create your views here.
with open(settings.BASE_DIR + '/realtimedbcreds.json') as f:
    config = json.load(f)

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()


def index(request):
    # accessing our firebase data and storing it in a variable
    name = database.child('Data').child('Name').get().val()
    stack = database.child('Data').child('Stack').get().val()
    framework = database.child('Data').child('Framework').get().val()

    context = {
        'name': name,
        'stack': stack,
        'framework': framework
    }
    print(context)
    return render(request, 'index.html', context)
