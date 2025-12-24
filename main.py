import requests

# 1. Ma'lumot yuboriladigan URL
url = "https://login.emaktab.uz/login/?ReturnUrl=https%3a%2f%2femaktab.uz%2fuserfeed"

# 2. Siz taqdim etgan response'dan olingan cookie-lar
# Bu ma'lumotlar brauzerga "men tizimga kirdim" deyish uchun kerak
cookies = {
	'sst': '2200b7cc-c1b9-4d74-a31c-e4542ca0f065|24/12/2025 20:24:57',
	    'UZDnevnikAuth_l': '1snyX7Tt2Ff6tG%2Fne6O9DZnId3yyUam74szC%2B5zZzq34CPYa54ERtAFZqb7K4%2B4is%2FBDICMPksqFb9MMp%2BcIsT1eknJFFeYeVs45PBOf907JFxZQ8wLaN8Bd6EdRkD%2Bc1TRfiJQk00WhSif3utopO17ibp%2BrJk%2FT%2BJ12x8rjhTrUDHyEcwbvtkhsxRbwAOgo0uZCpHTLgsINgQzDEaEqdmM3iGxdijS6g%2FDaTVi4Iav3rnyVapJPEtRTPefsH106OBxzKm%2FCP7nJS1YDIyknydyxmSXJYTs%2BVAxvkBntXMfiGixH5IH9CNLIjb%2FfOE97qSKdpw%3D%3D',
	    'UZDnevnikAuth_a': 'PoRYN%2BH8HJAc%2FWEtwi7XSsgVDibv90LsiMfi%2FeVINHu8%2Be7aF%2BNJx6dru3SPt4ap29fGUAcH1hj3%2FkYMJeAsSAO14hEgsO3e0yx3xgIlTy4vGNDyH4Cy0QZjaripr0vqwc1pXQ%3D%3D ',
	    'Dnevnik_localization': 'uz-Latn-UZ',
	    'a_r_p_i': '23.3'
}

# 3. Headerlar (Sizni bot deb o'ylamasligi uchun)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://login.emaktab.uz/',
}

# 4. POST so'rovini yuborish
# Eslatama: Odatda bu cookie-lar bilan GET so'rovi yuboriladi, 
# lekin siz POST so'raganingiz uchun post ko'rinishida yozdim:
response = requests.post(url, cookies=cookies, headers=headers)

# Natijani tekshirish
print(f"Status Code: {response.status_code}")
print("Sahifa mazmuni (qisqa):", response.text)