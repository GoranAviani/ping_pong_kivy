import kivy
kivy.require('1.11.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class PongGame(Widget):
    pass

class PongApp(App):

    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()