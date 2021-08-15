# import requests
import cloudscraper
import time
import json
from random import randint
scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJDb3VudHJ5Q29kZSI6IlRIIiwiQ291bnRyeU5hbWUiOiJUaGFpbGFuZCIsIklQIjoiMTgwLjE4My4xNTMuMjMiLCJJRCI6MzAsImV4cCI6MTYyOTA0OTU0M30.ZHk25AqVJcibQQI2_FhNYgOENmFcRL-zcQ5Njd3zc-Y"
captcha_token = "05AGTLn29S1LEKo9BJtpgetKvVJzPuYg20lzoQ-qpCGlm3Jnvlh5CYiUe0bxRq2_vJ7x5hrTb93k5XytEgG-u14anguL3V6H1RJFsAmM57Vni62LkndwAZQftJ6QjItDRrvT6bbN0Xj_r7uTnSluN-EJCv6DOnOBrpm6Qpq6CfUY_HO90HLyqtuDDC69CWMmnhEEStaDyayPulDBQdV1mekPmUMJk"
clicked = 0
for i in range(9999999999):
	url = f"https://stats.popcat.click/pop?pop_count=800&captcha_token={captcha_token}&token={token}"
	res = scraper.get(url)
	if (res.text.startswith("{") and res.text.endswith("}")) or res.status_code == 201:
		res_json = json.loads(res.text)
		clicked += 800
		print(f"POP :O clicked : {clicked}")
		token = res_json["Token"]
	else:
		print(f"PIP :( {res.status_code}")
	time.sleep(30) #delay a bit