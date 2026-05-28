from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.label import Label

# Импорт для Android TTS
try:
    from jnius import autoclass
    from android import activity
    TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
    Locale = autoclass('java.util.Locale')
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("Не Android среда")

class TTSApp(App):
    def build(self):
        self.tts = None
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.text_input = TextInput(
            text="Привет! Как дела?",
            size_hint_y=0.4,
            multiline=True
        )
        layout.add_widget(self.text_input)
        
        # Кнопки
        btn_speak = Button(text="▶ Озвучить", size_hint_y=0.1)
        btn_speak.bind(on_press=self.speak)
        layout.add_widget(btn_speak)
        
        btn_stop = Button(text="⏹ Стоп", size_hint_y=0.1)
        btn_stop.bind(on_press=self.stop)
        layout.add_widget(btn_stop)
        
        # Скорость
        layout.add_widget(Label(text="Скорость речи"))
        self.speed_slider = Slider(min=0.5, max=2.0, value=1.0, size_hint_y=0.1)
        self.speed_slider.bind(value=self.update_speed)
        layout.add_widget(self.speed_slider)
        
        # Статус
        self.status_label = Label(text="Готов", size_hint_y=0.1)
        layout.add_widget(self.status_label)
        
        # Инициализация TTS после загрузки
        if TTS_AVAILABLE:
            self.tts = TextToSpeech(activity.get_activity(), None)
            self.tts.setLanguage(Locale("ru", "RU"))
            self.status_label.text = "TTS готов"
        else:
            self.status_label.text = "TTS не доступен"
        
        return layout
    
    def speak(self, instance):
        text = self.text_input.text
        if text and self.tts:
            self.status_label.text = "🎤 Говорит..."
            self.tts.speak(text, self.tts.QUEUE_FLUSH, None)
    
    def stop(self, instance):
        if self.tts:
            self.tts.stop()
            self.status_label.text = "Остановлено"
    
    def update_speed(self, instance, value):
        if self.tts:
            self.tts.setSpeechRate(value)

if __name__ == '__main__':
    TTSApp().run()    def speak(self, instance):
        text = self.text_input.text
        if text:
            self.status_label.text = "🎤 Говорит..."
            self.engine.say(text)
            self.engine.runAndWait()
            self.status_label.text = "Готов"
    
    def stop(self, instance):
        self.engine.stop()
        self.status_label.text = "Остановлено"
    
    def update_speed(self, instance, value):
        self.engine.setProperty('rate', int(150 * value))

if __name__ == '__main__':
    TTSTestApp().run()

#
