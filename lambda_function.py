import alexaHelper
import Courses
import json
import random
from random import *
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
		try:
			a = intent_request["intent"]['slots']['class']['resolutions']['resolutionsPerAuthority'][0]["values"][0]['value']['name']
			sessionVal.type = str(a)
		except:
			return colaHacksTemplate("Are you sure that's the class you're looking for?  It doesn't seem to exist at the University of South Carolina")
		return colaHacksTemplate("Searching for a {} class.  What course number?".format(str(a)))
	elif intent_name == 'selectNum':
		a = intent_request["intent"]['slots']['courseNum']['value']
		sessionVal.num = str(a)
		try:
			try:
				cval = convertToAbbr(str(sessionVal.type))
			except:
				return colaHacksTemplate("abbreviation not valid {}".format(str(sessionVal.type)))
			sessionVal.crn = Courses.searchCourses(cval, sessionVal.num)
			courseInfo = Courses.grabCourse(str(sessionVal.crn))
			if courseInfo == None:
				return colaHacksTemplate("This class is currently in a closed enrollment phase")
			else:
				return colaHacksTemplate("Yaaaboy",str(courseInfo))
		except:
			e = getInfo("{}{}".format(sessionVal.type, sessionVal.num))
			if e != None:
				return colaHacksTemplate("{} {} session number 1 currently has {} seats available for enrollment".format(str(sessionVal.type), str(sessionVal.num), e['Remaining']), endSession=True)
			else:
				return colaHacksTemplate("This class is currently in a closed enrollment phase")
	elif intent_name == 'aboutDev':
		return alexaHelper.devInfo()
	elif intent_name == 'RestaurantRecommendations':
		restaurants = ['Topio\'s', 'Moe\'s', 'Taco Bell', 'Chick-fil-A', 'Maddio\'s', 'Community Table', 'Top of Carolina']
		return colaHacksTemplate("You should check out {} in Downtown Columbia!  It's one of my favorite places to eat around campus!".format(choice(restaurants)), endSession=True)
	elif intent_name == 'Events':
		events = ["River Rocks Festival","2018 Indie Grits Festival","2018 World Famous Hip Hop Family Day","Columbia International Festival"]
		return colaHacksTemplate("You can check out the {} in {} this weekend!".format(choice(events), choice(["Downtown Columbia", "Greenville", "Spartanburg"])), endSession=True)
	elif intent_name == "AMAZON.HelpIntent":
		return alexaHelper.get_help_response(REPEATSPEECH)
	elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
		return alexaHelper.handle_session_end_request()

def searchClasses():
	return colaHacksTemplate("What class type do you want to search for?")

def getInfo(className):
	try:
		classInfo = json.loads(open("/tmp/info.json").read())
	except:
		with open('/tmp/info.json', 'w') as outfile:
			json.dump([], outfile)
		classInfo = json.loads(open("/tmp/info.json").read())
	for val in classInfo:
		if val["Class"] == str(className):
			return val
	return None

def colaHacksTemplate(text, displayText="Project for Cola Hacks", endSession=False):
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
				"shouldEndSession": endSession
			}}


