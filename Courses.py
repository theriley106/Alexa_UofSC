import requests
import bs4
import re

a = json.load(open('subjectInfo.json'))

URL_FORMAT = "https://ssb.onecarolina.sc.edu/BANP/bwckschd.p_disp_detail_sched?term_in={0}&crn_in={1}"

def grabCourse(crn, term='201808'):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	info = {}
	url = URL_FORMAT.format(term, crn)
	res = requests.get(url)
	page = bs4.BeautifulSoup(res.text, 'lxml')
	listOfElems = page.select(".dddefault .dddefault")
	labelInfo = page.select(".dddefault")[0]
	info["Capacity"] = listOfElems[0].getText()
	# People registered
	info["Actual"] = listOfElems[1].getText()
	# Total spots available
	info["Remaining"] = listOfElems[2].getText()
	# Spots remaining
	info["Campus"] = extractCampusName(labelInfo)
	# This is the course location
	info["Hours"] = extractCourseHours(labelInfo)
	# This is the course hours
	info["SpaceAvailable"] = (info["Remaining"] > 0)
	# Boolean
	return info

def extractCampusName(labelInfo):
	return "USC " + str(re.findall('\w+\sCampus', str(labelInfo))[0])

def extractCourseHours(labelInfo):
	return int(re.findall("(\d+)\S\d+\s+Credit", str(labelInfo))[0])

def getCRN()

class SearchCourse(object):
	def __init__():
		pass

	print searchCourses()

if __name__ == '__main__':
	while True:
		print grabCourse(raw_input("CRN: "))
