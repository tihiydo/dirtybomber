import json
from colorama import Fore, Back, Style
import tools, time, os, re
from runner import Runner

class Menu:

    def mainMenu(self):
        tools.DefaultTools().clearConsole()
        print(f"{Fore.YELLOW + Style.BRIGHT}◥█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ■ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀█◤")
        print(f" █{Fore.BLUE + Style.BRIGHT} 1. Почати атаку на номер       {Fore.YELLOW + Style.BRIGHT}█")
        print(f" █{Fore.BLUE + Style.BRIGHT} 2. Налаштування                {Fore.YELLOW + Style.BRIGHT}█")
        print(f" █{Fore.BLUE + Style.BRIGHT} 3. Про програму                {Fore.YELLOW + Style.BRIGHT}█")
        print(f"◢█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ □ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄█◣{Style.RESET_ALL}\n\n\n")
        try:
            a = int(input(f"{Fore.BLUE + Style.BRIGHT}■{Fore.YELLOW + Style.BRIGHT} Введіть вашу дію: {Style.RESET_ALL}"))
        except ValueError:
            print(f"{Fore.BLUE + Style.BRIGHT}□{Fore.YELLOW + Style.BRIGHT} Введено некоректне значення. Спробуйте ще раз.{Style.RESET_ALL}")
            time.sleep(2)
            self.mainMenu()
        if a == 1:
            self.menuAttack()
        if a == 2:
            self.menuSetting()
        if a == 3:
            self.menuAbout()

    def menuAttack(self):
        tools.DefaultTools().clearConsole()
        print(f"{Fore.YELLOW + Style.BRIGHT}◥█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ■ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀█◤")
        print(f" █{Fore.BLUE + Style.BRIGHT} Введіть номер разом з +        {Fore.YELLOW + Style.BRIGHT}█")
        print(f" █{Fore.BLUE + Style.BRIGHT} Наприклад - +380123456789      {Fore.YELLOW + Style.BRIGHT}█")
        print(f" █                                █")
        print(f" █{Fore.BLUE + Style.BRIGHT} 0. Назад                       {Fore.YELLOW + Style.BRIGHT}█")
        print(f"◢█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ □ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄█◣{Style.RESET_ALL}\n\n\n")
        try:
            a = str(input(f"{Fore.BLUE + Style.BRIGHT}■{Fore.YELLOW + Style.BRIGHT} Введіть вашу дію: {Style.RESET_ALL}"))
            if a == "0":
                self.mainMenu()
            elif re.match(r'^\+380\d{9}$', a):
                Runner(a)
            else:
                print(f"{Fore.BLUE + Style.BRIGHT}□{Fore.YELLOW + Style.BRIGHT}  Номер введено некоректно. Спробуйте ще раз.{Style.RESET_ALL}")
                time.sleep(2)
                self.menuAttack()
        except ValueError:
            print(f"{Fore.BLUE + Style.BRIGHT}□{Fore.YELLOW + Style.BRIGHT} Введено некоректне значення. Спробуйте ще раз.{Style.RESET_ALL}")
            time.sleep(2)
            self.menuAttack()

    def menuSetting(self):
        tools.DefaultTools().clearConsole()
        settings = tools.DefaultTools().readAttackSettings()
        temporyArray = []
        temporyArray.append(str(settings[0]).ljust(18))
        temporyArray.append(str(settings[1]).ljust(18))

        print(f"{Fore.YELLOW + Style.BRIGHT}◥█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ■ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀█◤")
        print(f" █{Fore.BLUE + Style.BRIGHT} 1. Ввести кількість кіл за     {Fore.YELLOW + Style.BRIGHT}█")
        print(f" █{Fore.BLUE + Style.BRIGHT} замовчуванням                  {Fore.YELLOW + Style.BRIGHT}█")
        print(f" █{Fore.BLUE + Style.BRIGHT} Рекомендація - 4, поточне      {Fore.YELLOW + Style.BRIGHT}█")
        print(f" █{Fore.BLUE + Style.BRIGHT} значення - {temporyArray[0]}  {Fore.YELLOW + Style.BRIGHT}█")
        print(f" █{Fore.BLUE + Style.BRIGHT} 2. Ввести затримку між колами  {Fore.YELLOW + Style.BRIGHT}█")
        print(f" █{Fore.BLUE + Style.BRIGHT} за замовчуванням (в секундах)  {Fore.YELLOW + Style.BRIGHT}█")
        print(f" █{Fore.BLUE + Style.BRIGHT} Рекомендація - 40, поточне     {Fore.YELLOW + Style.BRIGHT}█")
        print(f" █{Fore.BLUE + Style.BRIGHT} значення - {temporyArray[1]}  {Fore.YELLOW + Style.BRIGHT}█")
        print(" █                                █")
        print(f" █{Fore.BLUE + Style.BRIGHT} 0. Назад                       {Fore.YELLOW + Style.BRIGHT}█")
        print(f"◢█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ □ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄█◣{Style.RESET_ALL}\n\n\n")

        try:
            a = int(input(f"{Fore.BLUE + Style.BRIGHT}■{Fore.YELLOW + Style.BRIGHT} Введіть вашу дію: {Style.RESET_ALL}"))
            if a == 0:
                self.mainMenu()
            elif a == 1:
                tools.DefaultTools().clearConsole()
                try:
                    b = int(input("■ Введіть кількість кіл (1 - 50): "))
                    if b <= 0 or b > 50:
                        print(f"{Fore.BLUE + Style.BRIGHT}□{Fore.YELLOW + Style.BRIGHT} Введено некоректне значення.{Style.RESET_ALL}")
                        time.sleep(2)
                        self.menuSetting()
                    else:
                        tools.DefaultTools().updateAttackSettings(b)
                        time.sleep(2)
                        self.menuSetting()
                except ValueError:
                    print(f"{Fore.BLUE + Style.BRIGHT}□{Fore.YELLOW + Style.BRIGHT} Введено некоректне значення. Спробуйте ще раз.{Style.RESET_ALL}")
                    time.sleep(2)
                    self.menuSetting()
            elif a == 2:
                tools.DefaultTools().clearConsole()
                try:
                    c = int(input("■ Введіть затримку між колами (1 - 999): "))
                    if c <= 0 or c > 999:
                        print(f"{Fore.BLUE + Style.BRIGHT}□{Fore.YELLOW + Style.BRIGHT} Введено некоректне значення.{Style.RESET_ALL}")
                        time.sleep(2)
                        self.menuSetting()
                    else:
                        tools.DefaultTools().updateAttackSettings(None, c)
                        time.sleep(2)
                        self.menuSetting()
                except ValueError:
                    print(f"{Fore.BLUE + Style.BRIGHT}□{Fore.YELLOW + Style.BRIGHT} Введено некоректне значення. Спробуйте ще раз.{Style.RESET_ALL}")
                    time.sleep(2)
                    self.menuSetting()
            else:
                print(f"{Fore.BLUE + Style.BRIGHT}□{Fore.YELLOW + Style.BRIGHT} Вибрано некоректну дію.{Style.RESET_ALL}")
                time.sleep(2)
                self.menuAbout()
        except ValueError:
            print(f"{Fore.BLUE + Style.BRIGHT}□{Fore.YELLOW + Style.BRIGHT} Введено некоректне значення. Спробуйте ще раз.{Style.RESET_ALL}")
            time.sleep(2)
            self.menuSetting()

    def menuAbout(self):
        tools.DefaultTools().clearConsole()
        print(f"{Fore.YELLOW + Style.BRIGHT}◥█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ■ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀█◤")
        print(f" █{Fore.BLUE + Style.BRIGHT} Сашко розробник, я люблю їсти  {Fore.YELLOW + Style.BRIGHT}█")
        print(" █                                █")
        print(f" █{Fore.BLUE + Style.BRIGHT} 0. Назад                       {Fore.YELLOW + Style.BRIGHT}█")
        print(f"◢█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ □ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄█◣{Style.RESET_ALL}\n\n\n")
        try:
            a = int(input(f"{Fore.BLUE + Style.BRIGHT}■{Fore.YELLOW + Style.BRIGHT} Введіть вашу дію: {Style.RESET_ALL}"))
            if a == 0:
                self.mainMenu()
            else:
                print(f"{Fore.BLUE + Style.BRIGHT}□{Fore.YELLOW + Style.BRIGHT} Вибрано некоректну дію.{Style.RESET_ALL}")
                time.sleep(2)
                self.menuAbout()
        except ValueError:
            print(f"{Fore.BLUE + Style.BRIGHT}□{Fore.YELLOW + Style.BRIGHT} Введено некоректне значення. Спробуйте ще раз.{Style.RESET_ALL}")
            time.sleep(2)
            self.menuAbout()