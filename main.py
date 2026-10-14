from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock

# Sabitler ve Simülasyon
BANNED_IPS = ["192.168.1.999"]
CURRENT_USER_IP = "192.168.1.5"

class BanScreen(Screen):
    """ Neon Mavi İnfaz ve IP Ban Ekranı """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        self.msg_label = Label(
            text="kurucu DEV:Cxrfex tarafından ip banı yediniz",
            color=(0, 0.94, 1, 1), # Neon Mavi (#00F0FF)
            font_size=22,
            halign='center',
            bold=True
        )
        
        self.timer_label = Label(
            text="Sistem imha ediliyor: 10",
            color=(1, 1, 1, 1),
            font_size=18
        )
        
        layout.add_widget(self.msg_label)
        layout.add_widget(self.timer_label)
        self.add_widget(layout)
        
        self.seconds_left = 10

    def on_enter(self):
        Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        if self.seconds_left > 0:
            self.timer_label.text = f"Sistem imha ediliyor: {self.seconds_left}"
            self.seconds_left -= 1
        else:
            Clock.unschedule(self.update_timer)
            App.get_running_app().stop()

class DashboardScreen(Screen):
    """ Ana Panel: Coin ve Kod Onay Ekranı """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        
        self.balance_label = Label(text="Bakiye: 600 Coin", font_size=18)
        self.code_input = TextInput(hint_text="Google Play / E-Pin Kodu Girin", multiline=False)
        self.redeem_btn = Button(text="Kodu Onayla & Coin Yükle", background_color=(0, 0.7, 1, 1))
        
        layout.add_widget(self.balance_label)
        layout.add_widget(self.code_input)
        layout.add_widget(self.redeem_btn)
        
        self.add_widget(layout)

class CxrfexApp(App):
    def build(self):
        if CURRENT_USER_IP in BANNED_IPS:
            sm = ScreenManager()
            sm.add_widget(BanScreen(name='ban'))
            return sm
        
        sm = ScreenManager()
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(BanScreen(name='ban'))
        return sm

if __name__ == '__main__':
    CxrfexApp().run()
