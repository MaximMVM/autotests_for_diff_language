# autotests for different language of web pages by pytest and selenium

Тест написан для firefox, обязательно укажите путь к вебдрайверу gecko, если он не в /usr/local/bin или если он указан в переменной PATH.
Если захотите использовать Chrome, то расскоментируйте функцию browser (соответственно закомментировавав или переименовав ф-цию browser для firefox) и добавьте импорт:

`from selenium.webdriver.chrome.options import Options`

