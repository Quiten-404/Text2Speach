[app]

# Имя приложения (как будет отображаться на телефоне)
title = НейроГолос

# Уникальный идентификатор пакета (как в Google Play)
package.name = neurovoice

# Домен (можно свой или оставить так)
package.domain = org.ttsapp

# Исходная папка
source.dir = .

# Какие файлы включить в APK
source.include_exts = py,png,jpg,kv,atlas,txt

# Версия приложения
version = 1.0.0

# Требования (библиотеки, которые нужно установить)
requirements = python3,kivy,kivymd,pyjnius,android,pyttsx3

# Ориентация экрана
orientation = portrait

# Разрешения Android
android.permissions = INTERNET, RECORD_AUDIO

# Минимальная версия Android
android.minapi = 21

# Целевая версия Android
android.api = 31

# Версия NDK
android.ndk = 23b

# SDK версия
android.sdk = 30

# Иконка приложения (положите icon.png в папку проекта)
android.icon = icon.png

# Заставка приложения (положите presplash.jpg в папку проекта)
android.presplash = presplash.jpg

# Архитектуры (arm64-v8a для современных телефонов)
android.archs = arm64-v8a, armeabi-v7a

# Логгирование
log_level = 2

# Разрешить запись на SD карту
android.permissions = WRITE_EXTERNAL_STORAGE

# Для работы с TTS
android.add_src = 

# Резервные строки (для русского языка)
android.strings_en = True
android.strings_ru = True

# Поддержка русского языка в интерфейсе
android.locale = ru

# Fullscreen режим
fullscreen = 0

# Имя файла APK
android.whitelist = 

# Исключения для требований
p4a.whitelist = 

# Методы для исключения
p4a.blacklist = 

# Включить Cython
cython.enable = 1

# Включить упаковку
p4a.allow_gradle_download = 1