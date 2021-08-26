# import requests
import cloudscraper
import time
import json
from random import randint
scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJDb3VudHJ5Q29kZSI6IlRIIiwiQ291bnRyeU5hbWUiOiJUaGFpbGFuZCIsIklQIjoiMTgwLjE4My4xNTMuMjMiLCJJRCI6MzAsImV4cCI6MTYyOTA0OTU0M30.ZHk25AqVJcibQQI2_FhNYgOENmFcRL-zcQ5Njd3zc-Y"
captcha_token = "05AGTLn28Xykn95ZX13K81HfcVdWtHRldVt1ze47T7IANl03wPqFTIHcbd3HxcvwAc8hU7gfZjylC-3YVi4fzdzAc-ZpQ0DR9rsvgfU9s7esi-EbVgqtIVtDdsgb66W93cySxP8cJDnNPgzVcq72GpHv79DlPKtxqjfiEWxdwfyz_8W04vr9s0W4zeM0MWheiLcE81l8HcyYBeQ5lorMx9C9DAsVZ7u39WKKdDxhRk3Iii2DTxkNek0kpK0eab78u13fdHLh4Se2Zur6FpzSgIHM4V1dhzI4Izyx-zyoyj19dYMm5GsHQuQDGn8EeUfQbPN0kObKQkOOrwhtj_Plnxilm7rDdAuZmP"
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