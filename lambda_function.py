import alexaHelper
import Courses
import json
SKILLNAME = ""
INITIALSPEECH = '''Thanks for checking out the unofficial University of South Carolina
Alexa Skill.  You can ask to track busses, view registration info, or even ask about nearby amenities'''
REPEATSPEECH = ""
dictVal = json.load(open('subjectInfo.json'))
class newIntent(object):
	def __init__(self):
		self.type = None
		self.num = None
		self.crn = None

sessionVal = newIntent()

def convertToAbbr(fullName):
	for val in dictVal:
		if val['Name'] == str(fullName):
			return val["Course"]

def genCourseText(crn):
	courseInfo = Courses.grabCourse(crn)

def lambda_handler(event, context):
	appID = event['session']['application']['applicationId']
	if event["request"]["type"] == "LaunchRequest":
		#return alexaHelper.returnSpeech("Ayy this works.  This is where the you should have class info")
		return colaHacksTemplate(INITIALSPEECH)
	elif event["request"]["type"] == "IntentRequest":
		return on_intent(event["request"], event["session"])

def on_intent(intent_request, session):
	print("This works")
	intent = intent_request["intent"]
	intent_name = intent_request["intent"]["name"]
	if intent_name == 'searchClass':
		return searchClasses()
	elif intent_name == 'selectClass':
		a = intent_request["intent"]['slots']['class']['resolutions']['resolutionsPerAuthority'][0]["values"][0]['value']['name']
		sessionVal.type = str(a)
		return colaHacksTemplate("Searching for a {} class.  What course number?".format(str(a)))
	elif intent_name == 'selectNum':
		a = intent_request["intent"]['slots']['courseNum']['value']
		sessionVal.num = str(a)
		try:
			cval = convertToAbbr(str(sessionVal.type))
		except:
			return colaHacksTemplate("abbreviation not valid {}".format(str(sessionVal.type)))
		sessionVal.crn = Courses.searchCourses(cval, sessionVal.num)
		courseInfo = Courses.grabCourse(str(sessionVal.crn))
		return colaHacksTemplate("Yaaaboy",str(courseInfo))
	elif intent_name == 'aboutDev':
		return alexaHelper.devInfo()
	elif intent_name == "AMAZON.HelpIntent":
		return alexaHelper.get_help_response(REPEATSPEECH)
	elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
		return alexaHelper.handle_session_end_request()

def searchClasses():
	return colaHacksTemplate("What class type do you want to search for?")

def colaHacksTemplate(text, displayText="Project for Cola Hacks"):
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
								"text": displayText,
								"type": "PlainText"
							}
						}
					}
				}],
				"outputSpeech": {
					"type": "PlainText",
					"text": text
				},
				"shouldEndSession": False
			}}

