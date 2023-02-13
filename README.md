# learn-selenium

podstawowe informacje o bibliotece do testowania app webowych - Selenium

Na postawie kursu [Twój pierwszy automatyczny test w Python](https://videopoint.pl/kurs/selenium-kurs-video-twoj-pierwszy-automatyczny-test-w-python-tomasz-kaniecki,vteaue.htm)

Dokumnetacja: https://selenium-python.readthedocs.io/installation.html

## Wprowadzenie

### Python

Selenium opiera się o język Python.

Język wysokopoziomowy, ogólnego przeznaczenia. Popularność zyskał dzięki dużej liczbie różnych bibliotek.
Pierwsza wersja to rok 1994.
Kod charakteryzuje się wysoką czytelnością. Zmienne nie są typowane statycznie.
Obecna wersja to 3.10

Wspiera protokoły SSL oraz różne bazy danych oraz pliki CSV.

### Selenium

Biblioteka napisana dla różncyh języków (Java,Phyton,CSharp, Ruby, JavaScript, Kotlin), służąca do testowania aplikacji webowych. Do seswów wykorzytuje tzw. "webdrive'y", dedykowane dla różnych przegładarek. Komunikacja odbywa się za pomocą api przeglądarki (aplikacja wydaje komendy do sterowania przeglądarką).

**Webdriver** - obiekt przeglądarki internetowaj, który steruje przeglądarką za pomocą jej api.

Narzędzia Selenium:

-   Selenium Webdriver - wykorzystuje api przeglądarki
-   Selenium Grid - uruchamianie testów z wykorzstaniem Webdrive na różnych przeglądarkach sprzętowych.
-   Selenium IDE - wtyczka do przeglądarki, pozwala na nagrywanie i edycję krótków, które ma realizować dana przeglądarka.

## Instalacja

1. Zainstalować Pythona ze strony [python.org](https://www.python.org)
2. Zainstalować [PyCharm](https://www.jetbrains.com/pycharm) - dla Linux komendą z konsoli:
   `sudo snap install pycharm-community --classic`
3. Zainstalować driver dla przeglądarki, która będzie używana do testów - dla Chrome'a: będzie to [ChromeDriver](https://chromedriver.chromium.org). (Przed pobraniem sprawdzić wersję przeglądarki). Rozpakowany plik przeglać do katalogu projektu.
4. Instalujemy Selenium: `pip install selenium`
5. Test poprawności instalacji - utworzyć plik 'test.py' z poniższym kodem:

```
import time
from selenium import  webdriver

browser = webdriver.Chrome()
browser.get(url='https://google.com')
time.sleep(3)
```

W przypadu poprawnej instalacji, po wystartowaniu aplikacji okno przeglądarki Chrome powinno zostać wyświetlone (na 3 sekundy), dodatkowo przeglądarka wyświetla komunikat o sterowaniu.

## Elementy Selenium

### Lokalizacja elementów

```
find_element lub find_elements

find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")
```

### Waits

driver.implicitly_wait
