import requests

cookies = {
		'SESSID': 'SFZTOVkxMjI3MDk5NQ==',
		'ROUTEID': '.BANAPP4',
		'accessibility': 'false',
		'IDMSESSID': 'A75188410',
		'sghe_magellan_username': 'QTc1MTg4NDEw',
		'sghe_magellan_locale': 'en_US',
		'WEBPATH': '.PROXY1',
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
		'Referer': 'https://ssb.onecarolina.sc.edu/BANP/bwskfcls.P_GetCrse',
		'Connection': 'keep-alive',
}


def searchCourses(subject="ACCT"):
		data = [
		('rsts', 'dummy'),
		('crn', 'dummy'),
		('term_in', '201808'),
		('sel_subj', 'dummy'),
		('sel_subj', subject),
		('sel_day', 'dummy'),
		('sel_schd', 'dummy'),
		('sel_insm', 'dummy'),
		('sel_camp', 'dummy'),
		('sel_camp', 'COL'),
		('sel_levl', 'dummy'),
		('sel_sess', 'dummy'),
		('sel_instr', 'dummy'),
		('sel_ptrm', 'dummy'),
		('sel_ptrm', '%'),
		('sel_attr', 'dummy'),
		('sel_crse', ''),
		('sel_title', ''),
		('sel_from_cred', ''),
		('sel_to_cred', ''),
		('begin_hh', '0'),
		('begin_mi', '0'),
		('end_hh', '0'),
		('end_mi', '0'),
		('begin_ap', 'x'),
		('end_ap', 'y'),
		('path', '1'),
		('SUB_BTN', 'Course Search'),
		('SUB_BTN', 'Course Search'),
		]
		return requests.post('https://ssb.onecarolina.sc.edu/BANP/bwskfcls.P_GetCrse', headers=headers, cookies=cookies, data=data).text

