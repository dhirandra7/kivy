from kivy.app import App
from kivy.uix.button import Button


class HelloworldApp(App):
    def build(self):
        
        button=Button(text="jainex modi")
        return button
        
        
    
if __name__== '__main__':
    HelloworldApp().run()

