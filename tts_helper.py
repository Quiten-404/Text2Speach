from kivy.logger import Logger
import threading

class TTSHelper:
    """Класс для работы с Android Text-to-Speech через PyJNIus"""
    
    def __init__(self):
        self.tts = None
        self.is_ready = False
        self.current_language = "ru"
        self.speech_rate = 1.0
        self.pitch = 1.0
        
    def init_tts(self):
        """Инициализация TTS движка (вызывать в основном потоке)"""
        try:
            from jnius import autoclass
            from android.permissions import request_permissions, Permission
            
            # Запрашиваем разрешения (если нужны)
            request_permissions([Permission.INTERNET])
            
            # Получаем Java классы
            Locale = autoclass('java.util.Locale')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
            
            # Создаем TTS с listener
            class TTSListener:
                def onInit(self, status):
                    if status == TextToSpeech.SUCCESS:
                        self.is_ready = True
                        Logger.info("TTS: Инициализация успешна")
                        # Устанавливаем язык
                        self._set_language()
                    else:
                        Logger.error("TTS: Ошибка инициализации")
            
            # Создаем экземпляр
            self.tts = TextToSpeech(PythonActivity.mActivity, None)
            self.is_ready = True
            self._set_language()
            
        except Exception as e:
            Logger.error(f"TTS: Ошибка инициализации - {e}")
            self.is_ready = False
    
    def _set_language(self):
        """Установка языка TTS"""
        if not self.tts:
            return
            
        try:
            from jnius import autoclass
            Locale = autoclass('java.util.Locale')
            
            if self.current_language == "ru":
                locale = Locale("ru", "RU")
            else:
                locale = Locale.US
            
            result = self.tts.setLanguage(locale)
            if result == self.tts.LANG_MISSING_DATA or result == self.tts.LANG_NOT_SUPPORTED:
                Logger.warning(f"TTS: Язык {self.current_language} не поддерживается")
                # Пробуем установить английский как fallback
                self.tts.setLanguage(Locale.US)
            else:
                Logger.info(f"TTS: Язык установлен - {self.current_language}")
                
        except Exception as e:
            Logger.error(f"TTS: Ошибка установки языка - {e}")
    
    def set_language(self, lang_code):
        """Смена языка (ru/en)"""
        self.current_language = lang_code
        if self.is_ready:
            self._set_language()
    
    def set_speech_rate(self, rate):
        """Установка скорости речи (0.5 - 2.0)"""
        self.speech_rate = rate
        if self.tts:
            self.tts.setSpeechRate(rate)
    
    def set_pitch(self, pitch):
        """Установка тона голоса (0.5 - 2.0)"""
        self.pitch = pitch
        if self.tts:
            self.tts.setPitch(pitch)
    
    def speak(self, text):
        """Озвучивание текста"""
        if not self.is_ready or not self.tts or not text:
            return
        
        try:
            # QUEUE_FLUSH - очистить очередь и начать новый
            self.tts.speak(text, self.tts.QUEUE_FLUSH, None, None)
        except Exception as e:
            Logger.error(f"TTS: Ошибка воспроизведения - {e}")
    
    def stop(self):
        """Остановка озвучки"""
        if self.tts:
            self.tts.stop()
    
    def shutdown(self):
        """Закрытие TTS"""
        if self.tts:
            self.tts.stop()
            self.tts.shutdown()