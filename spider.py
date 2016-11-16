import requests

url_search = 'https://booking.hkexpress.com/zh-cn/Search'
url_select = 'https://booking.hkexpress.com/zh-cn/select'
url_test = 'http://httpbin.org/cookies'
headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Host':'booking.hkexpress.com',
'Referer':'https://booking.hkexpress.com/zh-cn',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}

headers2 = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, sdch',
	'Accept-Language': 'zh-CN,zh;q=0.8',
	'Connection': 'keep-alive',
'Host':	'booking.hkexpress.com',
'Referer':	'https://booking.hkexpress.com/zh-CN/Search',

'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0',

#'Cookie': '54B5; D_HID=+Vos841ykPL8GfyHMkkQCzu48FckZ6bdypY/GvDW7U4; D_ZID=477A7892-8CF6-3BB6-B664-43E37FD8AD3F; D_ZUID=3CFD98B9-16B2-32E3-B2DB-2C1FE9826147; ASP.NET_SessionId=xiokbg0bun55bylbjqw3izeo; _ga=GA1.2.561309588.1479302773; Hm_lvt_8012a04a2785e383e35b961c488c737f=1479302773; Hm_lpvt_8012a04a2785e383e35b961c488c737f=1479305126; wcs_bt=s_1f3d7117180:1479304306; _gr_ep=/; __utma=133237661.561309588.1479302773.1479302836.1479302836.1; __utmc=133237661; __utmz=133237661.1479302836.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); uoid=2b40ad18-3bff-4f58-1d3b-4e15069283a9; avl=5VDxM3FfLTOUEbYB; __RequestVerificationToken=QpL5M6H9IXlNtcfqr2HeEPLAbjx4lmTsXKp9IrN_5ULZhTkBRYVGFA77dVHIonSXyA22pJkaj5vQ4Ijv-RYvv1d35Ew1; s_fid=328B652276ACD1E7-01BD47FE9BB89810; s_cc=true; iUUID=290d160c4cb801c0a70abc1eb555321a; granify.uuid=b8582890-2090-4860-8860-3018f078b8d8; granify.flags.1381=136; granify.lasts.1381=1479302962862; granify.session.1381=1479302962862; granify.session_init.1381=1; s_sq=hkexpress-web-prd%3D%2526c.%2526a.%2526activitymap.%2526page%253Dbooking.hkexpress.com%25252Fzh-cn%25252Fsearch%2526link%253D%2525E6%252590%25259C%2525E5%2525AF%2525BB%2526region%253Dsearch_flight%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dbooking.hkexpress.com%25252Fzh-cn%25252Fsearch%2526pidt%253D1%2526oid%253D%2525E6%252590%25259C%2525E5%2525AF%2525BB%2526oidt%253D3%2526ot%253DSUBMIT; __sonar=632934863857892428; __utma=211774860.561309588.1479302773.1479303297.1479303297.1; __utmb=211774860.4.10.1479303297; __utmc=211774860; __utmz=211774860.1479303297.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); innity.dingo.cks.adnxs=1; multilink_pl=zh-hans; appier_uid_1=159f2442-e472-4b9d-eef5-dd0a6fd1ed3e; appier_pv_counter_99u5VlwJ4N4c6iB=0; _gr_ep_sent=1; _gr_ga1381=1'

}
# BIGipServerPOOL-distil-support-pool=2791706796.20480.0000; BIGipServerPOOL-119.9.81.221-80=2103840940.20480.0000; D_SID=220.179.147.62:MQXSXBCrLJuamnwC3lcV/hh/WBWyaZhGHeJiZZs57pU; D_PID=93308F68-50BF-3C57-8385-0DE082BCCE5A; D_IID=AAC43D13-67E4-39A7-B065-903D9D331718; D_UID=0CEABFC3-861B-3C9D-A020-27B4635E54B5; D_HID=+Vos841ykPL8GfyHMkkQCzu48FckZ6bdypY/GvDW7U4; D_ZID=477A7892-8CF6-3BB6-B664-43E37FD8AD3F; D_ZUID=3CFD98B9-16B2-32E3-B2DB-2C1FE9826147; ASP.NET_SessionId=xiokbg0bun55bylbjqw3izeo; _ga=GA1.2.561309588.1479302773; Hm_lvt_8012a04a2785e383e35b961c488c737f=1479302773; Hm_lpvt_8012a04a2785e383e35b961c488c737f=1479305126; wcs_bt=s_1f3d7117180:1479304306; _gr_ep=/; __utma=133237661.561309588.1479302773.1479302836.1479302836.1; __utmc=133237661; __utmz=133237661.1479302836.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); uoid=2b40ad18-3bff-4f58-1d3b-4e15069283a9; avl=5VDxM3FfLTOUEbYB; __RequestVerificationToken=QpL5M6H9IXlNtcfqr2HeEPLAbjx4lmTsXKp9IrN_5ULZhTkBRYVGFA77dVHIonSXyA22pJkaj5vQ4Ijv-RYvv1d35Ew1; s_fid=328B652276ACD1E7-01BD47FE9BB89810; s_cc=true; iUUID=290d160c4cb801c0a70abc1eb555321a; granify.uuid=b8582890-2090-4860-8860-3018f078b8d8; granify.flags.1381=136; granify.lasts.1381=1479302962862; granify.session.1381=1479302962862; granify.session_init.1381=1; s_sq=hkexpress-web-prd%3D%2526c.%2526a.%2526activitymap.%2526page%253Dbooking.hkexpress.com%25252Fzh-cn%25252Fsearch%2526link%253D%2525E6%252590%25259C%2525E5%2525AF%2525BB%2526region%253Dsearch_flight%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dbooking.hkexpress.com%25252Fzh-cn%25252Fsearch%2526pidt%253D1%2526oid%253D%2525E6%252590%25259C%2525E5%2525AF%2525BB%2526oidt%253D3%2526ot%253DSUBMIT; __sonar=632934863857892428; __utma=211774860.561309588.1479302773.1479303297.1479303297.1; __utmb=211774860.4.10.1479303297; __utmc=211774860; __utmz=211774860.1479303297.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); innity.dingo.cks.adnxs=1; multilink_pl=zh-hans; appier_uid_1=159f2442-e472-4b9d-eef5-dd0a6fd1ed3e; appier_pv_counter_99u5VlwJ4N4c6iB=0; _gr_ep_sent=1; _gr_ga1381=1

search_headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Host':'booking.hkexpress.com',
'Referer':'https://booking.hkexpress.com/zh-cn/Search',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}

post_data = {
	'Adults':1,
	'Children':0,
	'DepartureDate':'16 / 11 / 2016',
	'DestinationStation':'FUK',
	'Infants':0,
	'LowFareFinderSelected':False,
	'MultiDestinationStation2':'HKG',
	'MultiOriginStation1':'HKG',
	'OriginStation':'HKG',
	'PromotionCode':None,
	'SearchType':'Oneway',
}

cookies = {
	'avi': 'X/lkE3FfLTOUEcf9',
'uoid':'5450775d-ee34-4f07-b8ab-3aab3b7fe912',
	'__RequestVerificationToken' : 'NxVX3dEUxV_RLIR6fd67bdQPEcYfAH3u_5FfnfhWe-3OLp0yNXJzwvzZBbHCTc8KfCUPkBgjkMdBF8a3iVxNPmcKPU81',
}

# res = requests.get(url=url, headers=headers2, cookies=cookies)
search_res = requests.post(url=url_search, headers=search_headers, data=post_data)

# res = requests.get(url=url, headers=headers)

print search_res.status_code
print search_res.text
