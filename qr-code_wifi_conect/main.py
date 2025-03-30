from dotenv import load_dotenv
import os
import qrcode

# Загружаем секреты
load_dotenv()  # Загрузка из .env
wifi_name = os.getenv("Name")  # Имя сети
wifi_password = os.getenv("Password")  # Пароль сети

wifi_string = f"WIFI:T:WPA;S:{wifi_name};P:{wifi_password};;"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(wifi_string)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white") # Цвета qr-code
img.save("qr_code_wifi.png")  # Путь к файлу
