import requests
import re

cookies = {
    '_ga': 'GA1.2.1115113190.1568662281',
    '_gid': 'GA1.2.1641915368.1568662281',
    '__gads': 'ID=b5fd50264c907972:T=1568662347:S=ALNI_MbYL_CMpUVk7YnrPQYb03f895ggyA',
    '_gat_gtag_UA_122711_39': '1',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'https://www.brutto-netto-rechner.info',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Sec-Fetch-Site': 'same-origin',
    'Referer': 'https://www.brutto-netto-rechner.info/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
}

for i in xrange(30000, 100000, 100):
  data = [
    ('f_start', '1'),
    ('ok', '1'),
    ('ok', '1'),
    ('f_bruttolohn', str(i)),
    ('f_abrechnungszeitraum', 'jahr'),
    ('f_geld_werter_vorteil', ''),
    ('f_abrechnungsjahr', '2019'),
    ('f_steuerfreibetrag', ''),
    ('f_steuerklasse', '1'),
    ('f_kirche', 'nein'),
    ('f_bundesland', 'berlin'),
    ('f_alter', '24'),
    ('f_kinder', 'nein'),
    ('f_kinderfreibetrag', '0'),
    ('f_krankenversicherung', 'pflichtversichert'),
    ('f_private_kv', ''),
    ('f_arbeitgeberzuschuss_pkv', 'ja'),
    ('f_KVZ', '0.9'),
    ('f_rentenversicherung', 'pflichtversichert'),
    ('f_arbeitslosenversicherung', 'pflichtversichert'),
  ]

  response = requests.post('https://www.brutto-netto-rechner.info/', headers=headers, cookies=cookies, data=data)

  s = re.findall(r"&nbsp;<b>.+?&nbsp;&euro;", response.content)[0]

  print str([i, float(s[s.find('&nbsp;<b>')+9:s.find('&nbsp;&euro;')].replace('.', '').replace(',','.'))]) + ','
