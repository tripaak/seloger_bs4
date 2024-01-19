import requests
import json
import csv
import time
import random
# proxy = random.choice(['http://8C6ySplWXnzqtzd:ERmOsIrVIhniiOt@176.46.131.28:49247', 'https://HmZGaGfwmUU3vvz:Xjc8Jv8UCiERSbb@176.116.132.226:47283','https://spaz33d1pDf5yTn:mBVtE9aLzFIwHeQ@89.38.44.147:48917',
_useragent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'
]
def get_useragent():
    return random.choice(_useragent_list)

# proxies = {
# "http": 'http://eokwpspa:j78QzVePkqxO0FAt@proxy.proxy-cheap.com:31112'
# }

proxies = {
"http": 'https://HmZGaGfwmUU3vvz:Xjc8Jv8UCiERSbb@176.116.132.226:47283'
}

# proxies = {
# "http": None
# }


payload = json.dumps({
  "from": None,
  "size": None,
  "projects": [
    1
  ],
  "agencyIds": None,
  "types": [
    2,
    1
  ],
  "propertySubTypes": None,
  "natures": None,
  "places": [],
  "searchAreas": None,
  "isochronePoints": None,
  "proximities": None,
  "geoloc": None,
  "geoPrecision": None,
  "pointOfInterests": None,
  "geoZone": None,
  "price": None,
  "sqrMeterPrice": None,
  "groundSurface": None,
  "surface": None,
  "bedrooms": None,
  "rooms": None,
  "bedroom": None,
  "room": None,
  "sort": [],
  "floor": None,
  "floors": [],
  "mandatoryCommodities": False,
  "lastFloor": None,
  "hearth": None,
  "guardian": None,
  "view": None,
  "balcony": None,
  "pool": None,
  "lift": None,
  "terrace": None,
  "cellar": None,
  "south": None,
  "parking": None,
  "box": None,
  "parquet": None,
  "locker": None,
  "furnished": None,
  "disabledAccess": None,
  "alarm": None,
  "toilet": None,
  "bathtub": None,
  "shower": None,
  "hall": None,
  "livingRoom": None,
  "diningRoom": None,
  "kitchen": None,
  "heating": None,
  "unobscured": None,
  "picture": None,
  "exclusiveness": None,
  "isEarlyAccess": None,
  "priceChange": None,
  "privateSeller": False,
  "video": None,
  "vv": None,
  "enterprise": False,
  "garden": None,
  "garage": None,
  "basement": None,
  "groundFloor": None,
  "intercom": None,
  "digicode": None,
  "prepare": None,
  "work": None,
  "seaSide": None,
  "singleStorey": None,
  "flatSharePossible": None,
  "student": None,
  "since": None,
  "houseboat": None,
  "farm": None,
  "epc": None,
  "textCriteria": None,
  "idPublication": None,
  "excluded": None
})

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
  'Accept': 'application/json',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Content-Type': 'application/json',
  # 'Referer': 'https://www.seloger.com/list.htm?projects=1&types=2^%^2C1&mandatorycommodities=0&privateseller=0&enterprise=0&qsVersion=1.0&LISTING-LISTpg=13',
  'Origin': 'https://www.seloger.com',
  'Connection': 'keep-alive',
  # 'Cookie': 'didomi_token=eyJ1c2VyX2lkIjoiMThkMjE5ZDItZTYwZC02ZjY3LWE0NmQtZjI4OGE0ZDc4MzY1IiwiY3JlYXRlZCI6IjIwMjQtMDEtMTlUMTI6MDY6MDUuNzkwWiIsInVwZGF0ZWQiOiIyMDI0LTAxLTE5VDEyOjA2OjA3LjEwNFoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpkdjM2MC1tUkhmcXFoRyIsImM6cGVyc29uYWxpei1NRWt5VzYybSIsImM6ZmFjZWJvb2stTGY2UWtVM0giLCJjOmdvb2dsZWFuYS1QZ2VYakVtayIsImM6eW91dHViZS04VDY4Q1Y3ViIsImM6aW50ZXJjb20teUJaN2tucTMiLCJjOm1hcGJveC1aQlJlWlpITSIsImM6YWxnb2xpYS1mVVlMMmhtVyIsImM6cG9seWZpbGwtYk1FOE1uVjYiLCJjOmhpZ2hjaGFydHMtZzdUcUdKUngiLCJjOmdvb2dsZXRhZy1xZm03YWZ6RSIsImM6bXlmZWVsYmEteUFZM0hYVW4iLCJjOm5ld3JlbGljLVVMOTNVOWJVIiwiYzpyZWFseXRpY3MtWmluckZuZ1QiLCJjOmdvb2dsZXJlLW02MkpmRmRLIiwiYzpzaGllbGRzcXUtVU1XbUtRYVQiLCJjOm1pY3Jvc29mdC1CbVg0elAzRSIsImM6dGFib29sYS1XY042a0JlTCIsImM6Y3JpdGVvLXo0OGdraDkzIiwiYzpmb250YXdlc28tdHloM2VheGMiLCJjOmdvb2dsZWZvbi1lbURpbjRxYyIsImM6bGlua2VkaW4tRE0zQkZGMjgiLCJjOmluc3RhcGFnZS1yVEJMRVdBRiIsImM6bWVpbGxldXJzLTl4OGdkTUdkIiwiYzpzZW50cnktcmdlODdmZGQiLCJjOnRva2VuLVhxUmN6NkhmIiwiYzpoYXJ2ZXN0LVBWVFR0VVA4IiwiYzphYnRhc3R5LWNiQkROWFRIIiwiYzpkYXRhZG9tZS1rbUJwZ2lnRyIsImM6bGF1bmNoZGFyLThxYThRanQ3IiwiYzpncm91cGVzZS1ZeHFSSDZlUCIsImM6aG90amFyLUxZZ2h3blVKIiwiYzphZGR0b2FueS1GcWFybkFmMyIsImM6aWFkdml6ZS0zcjdQbmRZciIsImM6ZGlnaXRhbGNsLU5UQmZpcDZrIiwiYzpmYWxndWllcmUtYzdUYlVCUVkiLCJjOmRhdGFkb2ctaDQ5MmVyZnkiLCJjOmxpZnVsbGNvbi14Z1liRTJjdyIsImM6YWRqdXN0LVdoRHlYN3FYIiwiYzpmbG9vZGxpZ2h0LVhMTTRuamtGIl19LCJwdXJwb3NlcyI6eyJlbmFibGVkIjpbInBlcnNvbmFsaXotR1A5NjlrcTQiLCJhZHZhbmNlZGMtNFBUd25EY3IiLCJhdWRpZW5jZSIsImZ1bmN0aW9ubmEtbUo5Y2V5YTciLCJwdXJwb3NlX2FuYWx5dGljcyIsImFuYWx5c2VkZS1WRFRVVWhuNiIsImdlb2xvY2F0aW9uX2RhdGEiLCJkZXZpY2VfY2hhcmFjdGVyaXN0aWNzIl19LCJ2ZW5kb3JzX2xpIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpsYXVuY2hkYXItOHFhOFFqdDciXX0sInB1cnBvc2VzX2xpIjp7ImVuYWJsZWQiOlsiYW5hbHlzZWRlLVZEVFVVaG42Il19LCJ2ZXJzaW9uIjoyLCJhYyI6IkREYUFDRERZLkREYUFDRERZIn0=; _gcl_au=1.1.1033232258.1705665966; datadome=07l7sDyri5U~0AOK1HlUL_W7MtQkeCqduDvk5bkOcQDmaoq3H6Rc4KXbcZiQ0HM4WtEVRPhrXs1ACjGmNNxo_4e8I7qs7EnUwJAIhcmzqiaiCbeKxval4rsy~qk8mL3r; euconsent-v2=CP4oVMAP4oVMAAHABBENAjEsAP_gAEPgAAAAJCQLIAFAAcABUADgAIAAVAAtABkADQAHsARABHACYAFAAKgAWwAvABhADMAIAAQgAjABHACXgFIAUoArQBcADSAH6AQOAg4CEQEcAR0ArIBgQDCAGdAP0Ao8BeYDFgGMgMkAa0A70CAIEhASEgOwAKAAsABwAFQAOAAgABkADQAH4ARAAjgBMACgAFsAMwAfgBCACOAFKAP2Ag4CEAEWgI4AjoBNAFHgLzAYsAyQCAIEhAAA.f_wACHwAAAAA; visitId=1705665967222-217222129; _ga_MC53H9VE57=GS1.1.1705669880.2.1.1705671069.0.0.0; _ga=GA1.2.1294999864.1705665967; ry_ry-s3oa268o_realytics=eyJpZCI6InJ5XzE4RTg1M0JCLUVGMjAtNDE5Ni1CMEJCLTMxQkE5NjZGREREMiIsImNpZCI6bnVsbCwiZXhwIjoxNzM3MjAxOTY3NjY2LCJjcyI6MX0^%^3D; _gid=GA1.2.1712254989.1705665968; cto_bundle=4YFj9V9hSUhDMWhMaWk3NHgyMkpYUGtvemhxUnNZUjhNbiUyQnIwTTRlckpsU3lOa1cwQ0RBJTJCMlh4V01wSmJrVGFpJTJCWGt3VlFoViUyQk5qZkVMZjFEZ1BNdzBOZ3Y4M09OdTZUT3I4aThPWTM1OW9GdzdLcU5wJTJGWllJeDdiU0l6YVNHOEt5TFd5NGJ4UDNtZlNPeDlwZEROT2Y3VExRJTNEJTNE; ep-authorization=isDisconnected; __gads=ID=856143b53884ebbb:T=1705665970:RT=1705671050:S=ALNI_MbkSCWYwPR6jywtOPTsC_FfRklWJw; __gpi=UID=00000cf9d9758b00:T=1705665970:RT=1705671050:S=ALNI_MZouNkEjJOO46c-WPFOaqEtJWXEqw; _fbp=fb.1.1705665972007.1541848104; _hjSessionUser_736989=eyJpZCI6IjhmNzkyNDI4LTkwMDUtNTM2MS05OGU1LTg2NWJmZjFmNzAzNSIsImNyZWF0ZWQiOjE3MDU2NjU5NzIxMTQsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample_736989=0; _hjHasCachedUserAttributes=true; __gsas=ID=5d9130e43fcf06f9:T=1705665972:RT=1705665972:S=ALNI_MYQsMLZqrOZv5cwcySZU3OZV2Pueg; realytics=1; ry_ry-s3oa268o_so_realytics=eyJpZCI6InJ5XzE4RTg1M0JCLUVGMjAtNDE5Ni1CMEJCLTMxQkE5NjZGREREMiIsImNpZCI6bnVsbCwib3JpZ2luIjp0cnVlLCJyZWYiOm51bGwsImNvbnQiOm51bGwsIm5zIjpmYWxzZX0^%^3D; _hjSession_736989=eyJpZCI6ImY1YjAzZTgwLWY1YjQtNGVjYS1iMGIyLTlmNmZlMGU5MzU4NiIsImMiOjE3MDU2Njk4ODYyNzEsInMiOjAsInIiOjAsInNiIjoxLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _gat_tracker_pageview=1; _gat_tracker_ecommerce=1; datadome=slKrBboo0ccQYsT3jhEOZX9HTiDe33tdXgTJt3MHxgXJw3t_NraMyBqNT2QF7s5P3hqjITCMnjL_YUHOXnodmo23m7d7R0DyZNSRqBJpiob1OlhnCT0SLCZ4ue2Mahpq',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin'
}

session = requests.session()

for page in range(10000, 60000, 25):
  count = 2
  url = f"https://www.seloger.com/search-bff/api/externaldata?from={page}&size=25"
  response = session.post(url,  data=payload, proxies=proxies)
  print(f"for {page}: status {response.status_code}")
  if response.status_code == 403:
    exit()
  if response.status_code == 200:
    json_data = response.json()['listingData']['cards']
    for row in json_data:
      if row['type'] == 0:
        item = {}
        item['page'] = page
        try:  
          item['listing_url'] = row['listing']['classifiedURL'] 
        except:
          item['listing_url'] = None  
        try:
          item['agency_id'] = row['listing']['contact']['agencyId']
        except:
          item['agency_id'] = None
        try:
          item['agency_seloger_profile'] = row['listing']['contact']['agencyPage']
        except:
          item['agency_seloger_profile'] = None  
        try:
          item['agency_name'] = row['listing']['contact']['contactName']
        except:
          item['agency_name'] = None  
        try:
          item['agency_phone_number'] = row['listing']['contact']['phoneNumber']
        except:
          item['agency_phone_number'] = None  
        try:
          item['agency_website'] = row['listing']['contact']['agencyLink']
        except:
          item['agency_website'] = None 
        
        with open('seloger_api.csv','a',encoding='utf-8',newline='') as op_file:
          fields = ['page','listing_url','agency_name','agency_id','agency_website','agency_seloger_profile','agency_phone_number']
          writer = csv.DictWriter(op_file,fieldnames=fields, extrasaction='ignore')
          writer.writerow(item) 
  time.sleep(3)
  count+=1
        




