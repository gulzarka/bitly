  **ENG**
# Bitly shortener


The script shortens a link into a bitly link using www.bitly.com \
If you enter already shoretened bitly link, it counts total clicks on the link.


## Installation:
   - You need Python3 installed; 
   - Use  `virtualenv` for isolating the project: \
        `python3 -m venv env`
        `source venv/bin/activate
   - Install dependencies using pip (or pip3 if there is a conflict with Python2):  
     `pip install -r requirements.txt`   
    file requirements.txt will install following modules:   
     - python-dotenv  
      - requests  
      - urllib3  
 - Get your bitly token on  https://app.bitly.com/settings/api/
 - Save your token in .env file with variable BITLY_TOKEN = 
 
    

   
  
 
  

## Usage:
use command `-l`  or `--link` and put your link
Example:
```
- bitly$ python3 main.py -l https://www.auca.kg/
Битлинк: bit.ly/3EBrDZK
- bitly$ python3 main.py -l bit.ly/3EBrDZK
По вашей ссылке прошли 3 раз(а)
```














   **RUS**
    
   
# Обрезка ссылок Битли"

Программа сокращает ссылки в формате Битли ссылок. При введении уже сокращенной Битли ссылки, выдается общее количество переходов по указанной ссылке.

## Установка:
  - Python3 должен быть установлен. 
  - Испрользуйте pip(или pip3 в случае конфликта с Python2) для установки зависимостей.
    pip install -r requirements.txt
   Файл requirements.txt установит следуюшие модули:
    - python-dotenv
     - requests
     - urllib3
  - Рекомендуется использовать `virtualenv` для изоляции проекта:\
       `python3 -m venv env`
        `source venv/bin/activate`
 - Получите токен по адресу  https://app.bitly.com/settings/api/
 - Сохраните токен в файле .env в переменной BITLY_TOKEN =        
        
 
  

## Применение:

Введите команды `-l `, или `--link` и вашу ссылку.

Пример:
```
- bitly$ python3 main.py -l https://www.auca.kg/
Битлинк: bit.ly/3EBrDZK
- bitly$ python3 main.py -l bit.ly/3EBrDZK
По вашей ссылке прошли 3 раз(а)
```
