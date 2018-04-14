import alexaHelper
import Courses

SKILLNAME = ""
INITIALSPEECH = ""
REPEATSPEECH = ""

def genCourseText(crn):
	courseInfo = Courses.grabCourse(crn)



def lambda_handler(event, context):
	appID = event['session']['application']['applicationId']
	if event["request"]["type"] == "LaunchRequest":
		#return alexaHelper.returnSpeech("Ayy this works.  This is where the you should have class info")
		return test()
	elif event["request"]["type"] == "IntentRequest":
		return on_intent(event["request"], event["session"], '')

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



def test():
	return {
			"version": "1.0",
			"sessionAttributes": {},
			"response": {

				"directives": [{
					"type": "Display.RenderTemplate",
					"template": {
						"type": "BodyTemplate1",
						"token": "T123",
						"backButton": "HIDDEN",
						"backgroundImage": {
							"contentDescription": "StormPhoto",
							"sources": [{
								"url": "https://raw.githubusercontent.com/theriley106/Alexa_UofSC/master/logo.png"
							}]
						},
						"title": "USC Helper",
						"textContent": {
							"primaryText": {
								"text": "Project for Cola Hacks",
								"type": "PlainText"
							}
						}
					}
				}],
				"outputSpeech": {
					"type": "PlainText",
					"text": "Ayy this works this is our project for colahacks"
				},
				"shouldEndSession": False
			}}

