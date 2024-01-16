from kivy.app import App
from kivy.uix.image import Image

class HelloworldApp(App):
    def build(self):
        return Image(source="dp1.jpg")
    
if __name__== '__main__':
    HelloworldApp().run()