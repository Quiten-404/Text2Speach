[app]
title = НейроГолос
package.name = neurovoice
package.domain = org.ttsapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy,kivymd,pyjnius,android,pyttsx3
orientation = portrait
android.permissions = INTERNET, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30
log_level = 2
android.log_level = 2
fullscreen = 0
android.gradle_repo = https://repo1.maven.org/maven2/

[buildozer]
log_level = 2
warn_on_root = 1
