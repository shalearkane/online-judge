from django.shortcuts import render
import pyrebase
import json
from django.conf import settings
import users.models
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
with open(settings.BASE_DIR + '/realtimedbcreds.json') as f:
    config = json.load(f)

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

# json structure
# {
#     "submission_id" : {
#         "user_id" : user_id,
#         "question_id" : question_id,
#         "code" : code,
#         "language" : language,
#     }
# }


@csrf_exempt
def compile_run(request):
    # accessing our firebase data and storing it in a variable
    received_json_data = json.loads(request.body)
    sub_id = received_json_data['submission_id']
    submission_details = dict(database.child(sub_id).get().val())
    question_id = submission_details['question_id']
    question = users.models.Question(pk=question_id)
    testcases = question.testcases.all()
    language = submission_details['language']

    return render(request, 'index.html', {"data": submission_details})
