import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
import requests
import bs4
cookies = {
    'SESSID': 'S1QyQlVGMjI3MDk5NQ==',
    'ROUTEID': '.BANAPP4',
    'accessibility': 'false',
    'IDMSESSID': 'A75188410',
    'sghe_magellan_username': 'QTc1MTg4NDEw',
    'sghe_magellan_locale': 'en_US',
    'WEBPATH': '.PROXY2',
}

headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://ssb.onecarolina.sc.edu',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,es-US;q=0.8,es;q=0.6,ru-BY;q=0.4,ru;q=0.2,en;q=0.2',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/60.0.3112.113 Chrome/60.0.3112.113 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cache-Control': 'no-cache',
    'Referer': 'https://ssb.onecarolina.sc.edu/BANP/bwskfcls.p_sel_crse_search',
    'Connection': 'keep-alive',
}



def searchCourses(subject="ACCT", crse='222'):


	data = [
	('term_in', '201808'),
	('sel_subj', 'dummy'),
	('sel_subj', str(subject)),
	('SEL_CRSE', str(crse)),
	('SEL_TITLE', ''),
	('BEGIN_HH', '0'),
	('BEGIN_MI', '0'),
	('BEGIN_AP', 'a'),
	('SEL_DAY', 'dummy'),
	('SEL_PTRM', 'dummy'),
	('END_HH', '0'),
	('END_MI', '0'),
	('END_AP', 'a'),
	('SEL_CAMP', 'dummy'),
	('SEL_CAMP', 'COL'),
	('SEL_SCHD', 'dummy'),
	('SEL_SESS', 'dummy'),
	('SEL_INSTR', 'dummy'),
	('SEL_INSTR', '%'),
	('SEL_ATTR', 'dummy'),
	('SEL_ATTR', '%'),
	('SEL_LEVL', 'dummy'),
	('SEL_LEVL', '%'),
	('SEL_INSM', 'dummy'),
	('sel_dunt_code', ''),
	('sel_dunt_unit', ''),
	('call_value_in', ''),
	('rsts', 'dummy'),
	('crn', 'dummy'),
	('path', '1'),
	('SUB_BTN', 'View Sections'),
	('SUB_BTN', 'View Sections'),
	]
	e = requests.post('https://ssb.onecarolina.sc.edu/BANP/bwskfcls.P_GetCrse', headers=headers, cookies=cookies, data=data).text
	if len(e) < 1000:
		print e
	a = bs4.BeautifulSoup(e, 'lxml')
	try:
		return str(a.select(".dddefault")[1]).partition("crn_in=")[2].partition('"')[0]
	except:
		return None

print searchCourses("PHIL", "103")
