import requests
import bs4



URL_FORMAT = "https://ssb.onecarolina.sc.edu/BANP/bwckschd.p_disp_detail_sched?term_in={0}&crn_in={1}"

def grabCourse(crn, term='201808'):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	info = {}
	url = URL_FORMAT.format(term, crn)
	res = requests.get(url)
	page = bs4.BeautifulSoup(res.text, 'lxml')
	listOfElems = page.select(".dddefault .dddefault")
	info["Capacity"] = listOfElems[0].getText()
	info["Actual"] = listOfElems[1].getText()
	info["Remaining"] = listOfElems[2].getText()
	return info


if __name__ == '__main__':
	while True:
		print grabCourse(raw_input("CRN: "))
