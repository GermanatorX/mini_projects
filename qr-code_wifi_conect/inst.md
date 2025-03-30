**.env и .gitgnore может и не быть, но я их сделал для сохранения конфиденциальности**
## **main.py**
**Библиотеки** - from dotenv import load_dotenv, import os, import qrcode
**Установка библиотек** - pip install dotenv, qrcode

***Загрузка файлов из .env***
```python
# Загружаем секреты
load_dotenv()  # Загрузка из .env
wifi_name = os.getenv("Name")  # Имя сети
wifi_password = os.getenv("Password")  # Пароль сети
```

**load_dotenv(**) - С помощью модуля os загружаем файлы из .env
**wifi_name = os.getenv("Name")**  - C помощью os и функции os.getenv указываем с скобках имя из .env
**wifi_password = os.getenv("Password")**  - Тоже самое как с wifi_name


***Создание Qr-code***
```python
img = qr.make_image(fill_color="black", back_color="white")
img.save(qr_code_wifi.png")
```
**img = qr.make_image(fill_color="black", back_color="white"**) - Указания цветов qr кода
**img.save("qr_code_wifi.png")** - сохранение qr кода 

## **.env**
В этом файле состоит вся конфиденциальная информация.
```env
wifi_name=123_wi-fi
wifi_password=123_wi-fi-password
```
**Сюда вы вписываете имя и пароль своей сети**

## **.gitignore**
Сюда для связи файлов вписываете
```gitignore
.env
```
**То есть это для связи файлов, чтобы из .env файлы смогли загрузиться в main.py**
