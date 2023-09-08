# -*- coding: utf-8 -*-

from getuseragent import UserAgent
import random, json, os

class DefaultTools:
    def clearConsole(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def randomUserAgent(self):
        return UserAgent().Random()

    def reparseCookie(self, stringCook):
        return json.loads('{"' + stringCook.replace("; ", '", "').replace("=;", '","').replace("=", '":"') + '"}')

    def randomFirstName(self):
        randomFirstNameList = ["Станіслав", "Анатолій", "Артем", "Антон", "Сергій", "Іван", "Ярослав", "Микита", "Ігор", "Дмитро", "Максим", "Констянтин", "Григорій", "Петро"]
        return random.choice(randomFirstNameList)

    def randomLastName(self):
        randomLastNameList = ["Андрійченко", "Патик", "Покляцький", "Абрамов", "Стефанчук", "Ардашов", "Подолян", "Мельник", "Іваніщенко", "Богомолов", "Кислиця", "Мазур", "Большанек", "Мефодій"]
        return random.choice(randomLastNameList)

    def randomEmail(self):
        randomEmailList = ["superstar@gmail.com", "ivanishenko@gmail.com", "abrams11@gmail.com", "podolyan2@gmail.com"] #Нужно дополнить не хватает фантазии
        return random.choice(randomEmailList)

    def readAttackSettings(self):
        with open('tools/settings.json', 'r') as settings:
            data = json.load(settings)
            loops = data.get("loops")
            loopsDelay = data.get("loopsDelay")
            return [loops, loopsDelay]

    def updateAttackSettings(self, loops = None, loopsDelay = None):
        if loops != None or loopsDelay != None:
            with open('tools/settings.json', 'r+') as settings:
                data = json.load(settings)
                if loops != None:
                    data["loops"] = int(loops)
                if loopsDelay != None:
                    data["loopsDelay"] = int(loopsDelay)
                settings.seek(0)
                settings.truncate()
                json.dump(data, settings)