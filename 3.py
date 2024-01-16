from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout

class HelloworldApp(App):
    def build(self):
        layout = BoxLayout()
        checkbox=CheckBox(group="a")
        checkbox1=CheckBox(group="a")
        label = Label(text='Hello world!')
        
        layout.add_widget(label)
        layout.add_widget(checkbox)
        layout.add_widget(checkbox1)

        return layout
    
if __name__== '__main__':
    HelloworldApp().run()