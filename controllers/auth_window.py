from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
class LoginRoot(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def login(self):
        print("Click en login")
    def register(self):
        print("Click en registrar")

class SessionApp(App):
    def build(self):
        return LoginRoot()