import alexaHelper

SKILLNAME = ""
INITIALSPEECH = ""
REPEATSPEECH = ""

def lambda_handler(event, context):
	appID = event['session']['application']['applicationId']
	try:
		appPerson = appInfo[appID]
	except:
		appInfo = updateAfterIntent.updateAppInfo()
		appPerson = appInfo[appID]
	if event["request"]["type"] == "LaunchRequest":
		return alexaHelper.get_welcome_response(SKILLNAME.replace("$NAME", appPerson), INITIALSPEECH.replace("$NAME", appPerson), REPEATSPEECH)
	elif event["request"]["type"] == "IntentRequest":
		return on_intent(event["request"], event["session"], appPerson)

def on_intent(intent_request, session, author):
	intent = intent_request["intent"]
	intent_name = intent_request["intent"]["name"]
	elif intent_name == 'aboutDev':
		return alexaHelper.devInfo()
	elif intent_name == "AMAZON.HelpIntent":
		return alexaHelper.get_help_response(REPEATSPEECH)
	elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
		return alexaHelper.handle_session_end_request()
