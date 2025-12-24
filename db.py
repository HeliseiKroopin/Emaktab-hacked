import requests
tokens = [
	"5wgzSFYCm5NLQ2MFTYL2a5FBjmAnY%2BX0xE11kC310gFAUiDXRAZ6qZ8i0PbT03Acg%2FCT3LzYdwTmglY47tHE3BVaAU%2FIwfW8YAgOAzQua7FVfSmMQvgPP0I3mN2DldDw60OKTtmdyHQi8fCT3Fn%2BTEZMmXNUCO%2BlOTvjz3u4svuVCQa4g4zkQtFstAzKPDDttOIMdV%2BS7qu2ELz4%2BHhExUO4iAsduK4SdId08tU2D1iVfQpgIJUHdxslyGLXLXVxSVXF6Q%3D%3D",
	"6paN0PHk9EL9BcJsNEOvoyWvS0KmIXo%2BjznBooiLQji3IofrV%2BcWqMJUfvJHRsUMhrUXs%2Bldqd5OM2RaPNcxnqQt0AxGi63Z3EKwN62iDjYSlUt90uNAKGOFj%2BjyeHMms1bwn0%2BbjcHWIu7nxGmMKUcKHcEk%2BNxOwB9IWAofv9lumKNFqkSrn%2F0uwRNHBBy3tmDIP%2FanF2vVeaSPn7lp%2FEr3zTGfiHIM9jhANpiB5dHudktHUnQTf8iCV0SSBVC12unl2g%3D%3D",
	"g4av4ms9BVhiHxD7rTjgSIH2HLnxa474d0CeSCjZ3x0FxQ341HJQ6bpHjSjZqlobGwBmhHrH%2BgSIemlrtKG0SAQGr6nrJ%2FnkZSvsI79kI7rd7w%2B6wo%2Bi%2Bsbkk2hFROR9fzhG%2F0AKgf6I%2BvR8Qsl7%2BgBJ60C5uP4Tdgm3SGnAN1Zuhw2rdXffNvCysAtvMm8QGtKgIax8%2BTGcHxif1sf61obvCpgWF%2BSa19nzyTzEk%2FF9oOfk%2BrX9B%2B23tHshv2gNS17LEg%3D%3D",
	"AP4iXyZ0k0iYDdPJfS6cnqRkkbsCzgyIYst9d10FM%2B50fcX%2BddYPip5eIih757BMali%2BJ4LFGgYqxbwhhNBXaKBJzNCujX5VeXnE8T%2FSFD7HFtFHE64EFtUYCnsjkYps26vbBcHoZoK%2FJ11VJ9bxq7zbrZzVamdrxOWuCrFP8pzzW%2FR7BQVWVjrqOJEvR1BXRVoCSY9M4BYKZAT%2FOzBh6LRJvrVTqur1zeppKG1ZfvboEIGMQlcBjUzREWIZvJ%2BMIhM36g%3D%3D",
	"tfsv34Vg5K1ZLAxMtm16%2FWWX4gMcRi3dXIZC2kQiy%2FKeGG7T5d8GJnIaSe70yuFPR4z5JH%2B6TBTdnxg0Kd7awgKBxI2EOuH1ZHIWZAiTVRlKJ2aZbbueSO2gcbAxGGDCQJZF2g%3D%3D",
	"KlzCcBF1eSPciyTjMB%2BR1MoqCzkEhtSCQVURb%2F7M6N%2F5%2FZS7hDXcvhqRgFPH%2BCW5GTUpQCj3KSP%2Bj2zaZO8YMj%2FBne2M46AxCF0nVUKlQ5r0w8F65kPiKLvwdQyZ9qOHM%2BR%2FkQ%3D%3D",
	"REuZLAAbC1K0%2Bs7%2BFVbN7qxK6lnNQzddYoZsqY53drSzjdBPFj%2F3vrpBpBYRB0AGSx5pwHKhoBQdCO0ig4RL%2FniCtbWW6w0AhrNJZjUQn306aIzS01z3AMw0%2BLjqxMNTD4aPJQ%3D%3D",
	"JH1%2BjgoFxIvPsMth2aLoojjJ7ALHgCQ9ZQP7skuh%2FuqfnciCzBH3%2BjtTspRIYlsseg9dhfpvWK7wl0Gryjbje%2BfQdZJ%2BF%2F9scICdK%2BMZKlyVDRUDXVd4im8UQZTS%2F8STjML94A%3D%3D",
	"uI2QpF1T81HIAO4JoSIEtS2N%2FjOrxxiMDxfbfX5njsj1xU14tYf%2B3qALlDDACILRbO6XM9emineaPgBPFKk3KHUCaPZyTVQgETRNiXOWgM%2FCW2GYW1ECMalGTc3JdXE088pXrw%3D%3D",
	"%2F9KpFGe9j0PVX6wFb4NR%2Bb4%2FT3Ki7DRgbnejmRZNxC12Rt6%2Bv1ZaIbRLlJdZ1xns7wSpSCpn6kVp7edJeTAb%2FZht%2BG60x%2BpM0J6Nzeqj2YtwtCDLtcVv0L%2F8JKmM0u%2BFR3lQIw%3D%3D",
	"JXRdEZHxRyeyjYR5sFkKLljeeITpAQcnNS9YlVMi%2FaoogdbO0arGF6kHWMgBOduZ8FbDGQAIibjDd0mviLgbXgFg5DzrBroSIQu%2BxsWhtgPoe0SRfBVeXNkgl1z85fZjfbB19w%3D%3D",
	"9Hf6NNF%2BD%2FbdXb172o%2FWhWwQkvQR4dh%2BUMke1Vw5K9cmDx5csNib%2FPtxN5fJxIABWo%2BSEyT0d3aD5K6CEg%2FviTYYraNdA%2Bj2WeKhA5DbV7mTQSjjmMqMMGlnI1XQL05wTzPmFA%3D%3D",
	"PoRYN%2BH8HJAc%2FWEtwi7XSsgVDibv90LsiMfi%2FeVINHu8%2Be7aF%2BNJx6dru3SPt4ap29fGUAcH1hj3%2FkYMJeAsSAO14hEgsO3e0yx3xgIlTy4vGNDyH4Cy0QZjaripr0vqwc1pXQ%3D%3D",
	"Sw6lwhoc5IAPAWSsrAWGde7ylWkdleAdeLdHKco3j3YPNbj8GReEneWNOIywLwePe3rjVWjJxZryEAweB08EKnabmkrDyuhXuKAx520Ht%2Flcz8n2cpNcCd8M2luUCi3NYD06tw%3D%3D"
	"SQtC2mm2aQV81CAGo4O9QpvbDOXkkYKTsPhBiT5X4TEBR61uTCVKmw4tkwm2dsNOAH8bRbJCN7Zny6jgI73%2F3na1WOV%2F0P1h2%2BSLMgupq%2BYY4xAudnFkjSke2BQH3rC%2BS3c15A%3D%3D",
	"KI1FsFw78SYQWaDHUvjZ5YAC%2Bbf5FDU91RJODpgD366ZSH%2Fmx9PLbGEFRQFddunnnBrIUsDOD6YmYl83XBIlA05ymDWeeiIVlQ%2FmSjr2LEUn%2BlXg7HzH4m4ccpxLGYY4%2BojllQ%3D%3D",
	"IFH7pr9UlJ58CK3eV1oDSJYL9X8xjgaBIG1EYdU17xTrU4acmhmcIXp0xgMv2tLYYWIcDP4pbbvoxGQzPH%2BATNYnlYJ%2BQeuw%2B0cJkNdQ5n%2FOsHAyojXE3OMSgDU8hsmtO71xgQ%3D%3D",
	"oygzCKTbbXsUDHJtpk6P66EQCPjqOaZLx4%2FsPIsdmkLpauj0CWQlLouw617IloecDEG3RfN%2BQzDs2sV%2BMOVen0%2FIOZbaSMh%2FeSCL9Dm94ClSyRpocBWhbTaTwu875dTQuHOuYA%3D%3D",
	"cTGwY69ToAwM3Nofv4jLsP7Qed%2BUVwn7K4psHhL9tLDP8lvINuQdp588N5WNS12SGtKcnoNxLBFn6hKSr1q4rDH93UuGH8Fo3UC62gVGlGsTzcHHbBmaOaPhHTjoiqp9zHw9Mw%3D%3D",
	"pfTsAnzmZEWKfjptUt5sFxG5jgzdlalbSea0rWGeNaSR62hzbzUF1shsyhxUJq2GUvgGysErz5wopI3MSwzTChXggI%2FJV6V5TSky26x5tFLgyuTuYV0k5ED8dK8OcsChzaxZGA%3D%3D",
	"goE%2Fva%2FQ9VBRf%2BsgkPx%2Fl6DCOS1AvDBssTMbgXR27Pf7ZKDI%2BgpziPPrpdzqnJFQwNZK4ilvTWj%2FsnwcTdD3lHCk8Gmo4yd2bu%2BDkRSpnj5EmRoOEgg185Bdyf5lozziHZUB3Q%3D%3D",
	"dnzbOmIA5GHJQnNxfPbdSW%2By333G%2Fpv2CdqJV3RHdYCCq%2B6IjiK4aQE1pTqsltxLhRvRBoSwAS1467Uncq5Ev0Nqh06PqNnSYdsmS64Ousro6HLZj12Q%2BVAcbLfM41B0IBoM1A%3D%3D",
	"3XV5wa4BoRY6%2BFacw6LOCjQaEJ1JR2JYJlpujdlE64Cc56YP6UJYg%2FCU%2FVGXrvBAG%2FEUtqZTspBdXu3KZ%2B1ktyHD1ZKUs3%2B2oAQSBbD24SIrRs10QwuBkaOa3R3UgByHTwSV8A%3D%3D",
	"lTbkQVJq264PVXqpE9xhd4n1pfNnxpodSoWAgM143ZkGrglsfuO6rkCHZDyQhhwz7scwdaGCC3Fm7ZhoPI4hWtN%2FovaEq2jn8kF%2BcUiyxHERY8WCsrdy89Hl4nGxWZz%2Ban1etQ%3D%3D",
	"7%2FmQ93J7n6DQMxexjZYDko%2BEc1Cj6z%2F6l6TiwxY5fCTj6mOOwqSHYpQA4woQQEdGXkirAhBlC2zv7PdhdyQw9b9ewQUYmKI3cYdgOywvl4oDOePKipcTxO4oVhEe7cFuUJbheg%3D%3D",
	"73pZDm%2FGZcSMRBl1MRSejoU%2BlIHiftFXH0MCwBqNg1RgibVt9b7uk5qG%2FglrKr7qtpoJbBygxVnPSFhrIisv4vSN2%2BJfSEQeCHNDj1llUYbdmisRmOjXqOFaflPSt68cfDQADA%3D%3D",
	"h9%2BHB2kXORRD%2FNlLFmAyOEYEmxUhysslwMYwrLGK%2BKKLQg2o2ywLutXXHxCfa1H0l98zPFSqrPI8Dr2eTezDaoxMTGoxYtwCiqXb7oGBY8z4kriHai7dSDdE3ZdX1EYuFP7DLw%3D%3D",
]

"""
template:

'sst': '2200b7cc-c1b9-4d74-a31c-e4542ca0f065|24/12/2025 20:24:57',
	    'UZDnevnikAuth_l': '${token}',
	    'UZDnevnikAuth_a': '6paN0PHk9EL9BcJsNEOvoyWvS0KmIXo%2BjznBooiLQji3IofrV%2BcWqMJUfvJHRsUMhrUXs%2Bldqd5OM2RaPNcxnqQt0AxGi63Z3EKwN62iDjYSlUt90uNAKGOFj%2BjyeHMms1bwn0%2BbjcHWIu7nxGmMKUcKHcEk%2BNxOwB9IWAofv9lumKNFqkSrn%2F0uwRNHBBy3tmDIP%2FanF2vVeaSPn7lp%2FEr3zTGfiHIM9jhANpiB5dHudktHUnQTf8iCV0SSBVC12unl2g%3D%3D',
	    'Dnevnik_localization': 'uz-Latn-UZ',
	    'a_r_p_i': '23.3'
"""



# 1. Ma'lumot yuboriladigan URL
url = "https://login.emaktab.uz/login/?ReturnUrl=https%3a%2f%2femaktab.uz%2fuserfeed"

# 2. Siz taqdim etgan response'dan olingan cookie-lar
# Bu ma'lumotlar brauzerga "men tizimga kirdim" deyish uchun kerak

# 3. Headerlar (Sizni bot deb o'ylamasligi uchun)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://login.emaktab.uz/',
}

for token in tokens:
	cookies = {
	'sst': '2200b7cc-c1b9-4d74-a31c-e4542ca0f065|24/12/2025 20:24:57',
	    'UZDnevnikAuth_l': '1snyX7Tt2Ff6tG%2Fne6O9DZnId3yyUam74szC%2B5zZzq34CPYa54ERtAFZqb7K4%2B4is%2FBDICMPksqFb9MMp%2BcIsT1eknJFFeYeVs45PBOf907JFxZQ8wLaN8Bd6EdRkD%2Bc1TRfiJQk00WhSif3utopO17ibp%2BrJk%2FT%2BJ12x8rjhTrUDHyEcwbvtkhsxRbwAOgo0uZCpHTLgsINgQzDEaEqdmM3iGxdijS6g%2FDaTVi4Iav3rnyVapJPEtRTPefsH106OBxzKm%2FCP7nJS1YDIyknydyxmSXJYTs%2BVAxvkBntXMfiGixH5IH9CNLIjb%2FfOE97qSKdpw%3D%3D',
	    'UZDnevnikAuth_a': f'{token}',
	    'Dnevnik_localization': 'uz-Latn-UZ',
	    'a_r_p_i': '23.3'
	}
	response = requests.post(url, cookies=cookies, headers=headers)
	print("otdi");

# 4. POST so'rovini yuborish
# Eslatama: Odatda bu cookie-lar bilan GET so'rovi yuboriladi, 
# lekin siz POST so'raganingiz uchun post ko'rinishida yozdim:

# Natijani tekshirish
print(f"Status Code: {response.status_code}")
print("Sahifa mazmuni (qisqa):", response.text)