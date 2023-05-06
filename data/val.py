import requests  # Модуль для обработки URL
from bs4 import BeautifulSoup  # Модуль для работы с HTML
import time  # Модуль для остановки программы
import smtplib  # Модуль для работы с почтой


DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
Evro = "https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sxsrf=APwXEdde0l1Zlvua1JTMXxovQDoOrb3yyQ%3A1683356678622&ei=BvxVZKXQJYf1rgTuvI_wBg&oq=%D0%B5%D0%B2%D1%80%D0%BE&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMg0IABCKBRCxAxCDARBDMg0IABCKBRCxAxCDARBDMg0IABCKBRCxAxCDARBDMgcIABCKBRBDMgcIABCKBRBDMgcIABCKBRBDMgcIABCKBRBDMgcIABCKBRBDMgcIABCKBRBDMgcIABCKBRBDOgoIABBHENYEELADOgoIABCKBRCwAxBDOgUIABCABDoKCAAQgAQQFBCHAjoHCAAQgAQQCjoGCAAQFhAeOgkIABCABBAKECo6CAgAEBYQHhAKOgcIIxCKBRAnOgsIABCABBCxAxCDAToICAAQgAQQsQM6DAgjEIoFECcQRhCCAjoQCAAQgAQQFBCHAhCxAxCDAToOCAAQgAQQsQMQgwEQyQM6CAgAEIAEEJIDOgsIABCKBRCxAxCDAToRCC4QgAQQsQMQgwEQxwEQ0QM6CwguEIoFELEDEIMBOgcIIxDqAhAnOg8IABCKBRDqAhC0AhBDGAE6CwguEIMBELEDEIoFSgQIQRgAUN8FWOdPYLdaaANwAXgBgAH2A4gBlhiSAQwwLjExLjIuMS4wLjGYAQCgAQGwARTIAQrAAQHaAQYIARABGAE&sclient=gws-wiz-serp"
Yan = "https://www.google.com/search?q=%D1%8E%D0%B0%D0%BD%D1%8C+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sxsrf=APwXEdeXRCPWu48hol3cebaiTBtgJMqWKA%3A1683356745180&ei=SfxVZNXRCoKSwPAPtpiooAo&oq=%D1%8E+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB5KBAhBGABQAFjWHWDlMGgBcAF4AIABswOIAZgHkgEHMC4zLjQtMZgBAKABAcABAQ&sclient=gws-wiz-serp"
STR = "https://www.google.com/search?q=%D1%84%D1%83%D0%BD%D1%82+%D1%81%D1%82%D0%B5%D1%80%D0%BB%D0%B8%D0%BD%D0%B3%D0%BE%D0%B2+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sxsrf=APwXEdcKsJg6HSBV_oUN6QoPqRV0KvwQVw%3A1683358015833&ei=PwFWZPLDMo-yqwHropH4CQ&oq=%D1%84%D1%83%D0%BD%D1%82+%D1%81+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB46CggAEA0QgAQQsQM6BwgAEA0QgAQ6CggAEIoFELEDEEM6BwgAEIoFEEM6BQgAEIAEOg8IABCKBRCxAxBDEEYQggJKBAhBGABQAFiPGmDHKWgAcAF4AIABhAOIAdwIkgEHMC41LjAuMZgBAKABAcABAQ&sclient=gws-wiz-serp"
FR = "https://www.google.com/search?q=%D1%88%D0%B2%D0%B5%D0%B9%D1%86%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D0%B9+%D1%84%D1%80%D0%B0%D0%BD%D0%BA+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sxsrf=APwXEdfiPLT_-vQy5lam1PDvIFiTFtKGzQ%3A1683358517974&ei=NQNWZOaOO-bIrgS_-LvYDg&oq=%D1%89+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgBMgsIABAHEB4Q8QQQCjILCAAQBxAeEPEEEAoyCAgAEAgQBxAeMgoIABAFEAcQHhAKOgoIABBHENYEELADOgoIABCKBRCwAxBDSgQIQRgAULsOWLsOYPEfaAFwAXgAgAGXAYgBlwGSAQMwLjGYAQCgAQHIAQrAAQE&sclient=gws-wiz-serp"
# Основной класс
class Currency:
	# Ссылка на нужную страницу
	# Заголовки для передачи вместе с URL
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

	current_converted_price = 0
	difference = 5  # Разница после которой будет отправлено сообщение на почту

	def __init__(self, cur):
		# Установка курса валюты при создании объекта
		self.cur = cur
		self.current_converted_price = float(self.get_currency_price().replace(",", "."))

	# Метод для получения курса валюты
	def get_currency_price(self):
		# Парсим всю страницу
		full_page = requests.get(self.cur, headers=self.headers)

		# Разбираем через BeautifulSoup
		soup = BeautifulSoup(full_page.content, 'html.parser')

		# Получаем нужное для нас значение и возвращаем его
		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		return convert[0].text

	# Проверка изменения валюты
	def check_currency(self, cur):
		currency = float(self.get_currency_price().replace(",", "."))
		return currency
		# time.sleep(60)  # Засыпание программы на 3 секунды
		# self.check_currency()

