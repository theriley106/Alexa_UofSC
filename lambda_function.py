import alexaHelper
import Courses

SKILLNAME = ""
INITIALSPEECH = ""
REPEATSPEECH = ""

def genCourseText(crn):
	courseInfo = Courses.grabCourse(crn)



def lambda_handler(event, context):
	appID = event['session']['application']['applicationId']
	try:
		appPerson = appInfo[appID]
	except:
		appPerson = appInfo[appID]
	if event["request"]["type"] == "LaunchRequest":
		return alexaHelper.returnSpeech("Ayy this works.  This is where the you should have class info")
	elif event["request"]["type"] == "IntentRequest":
		return on_intent(event["request"], event["session"], appPerson)

def on_intent(intent_request, session, author):
	intent = intent_request["intent"]
	intent_name = intent_request["intent"]["name"]
	if intent_name == 'searchClass':
		return alexaHelper.returnSpeech("Ayy this works.  This is where the you should have class info")
	elif intent_name == 'aboutDev':
		return alexaHelper.devInfo()
	elif intent_name == "AMAZON.HelpIntent":
		return alexaHelper.get_help_response(REPEATSPEECH)
	elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
		return alexaHelper.handle_session_end_request()
