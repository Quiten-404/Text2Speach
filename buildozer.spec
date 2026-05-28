name: Build APK

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: |
          sudo apt update
          sudo apt install -y git zip unzip openjdk-17-jdk autoconf libtool
          pip install buildozer cython
      
      - name: Setup Android SDK
        run: |
          # Устанавливаем Android SDK командной строки
          wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip
          mkdir -p ~/.buildozer/android/platform/android-sdk/cmdline-tools
          unzip commandlinetools-linux-11076708_latest.zip -d ~/.buildozer/android/platform/android-sdk/cmdline-tools
          mv ~/.buildozer/android/platform/android-sdk/cmdline-tools/cmdline-tools ~/.buildozer/android/platform/android-sdk/cmdline-tools/latest
          export PATH=$PATH:~/.buildozer/android/platform/android-sdk/cmdline-tools/latest/bin
          # Принимаем лицензии
          yes | ~/.buildozer/android/platform/android-sdk/cmdline-tools/latest/bin/sdkmanager --licenses
      
      - name: Build APK
        run: buildozer android debug
      
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: Text2Speach-App
          path: bin/*.apk
