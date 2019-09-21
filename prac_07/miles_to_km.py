from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

__author__ = 'Matt Evans'


class ConvertNumberApp(App):
    """ ConvertNumberApp is a Kivy App for converting a number from miles to kilometers """
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (1000, 500)
        self.title = "Miles to Kilometers"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_increment(self,increment):
        self.root.ids.input_number.text = str(int(self.root.ids.input_number.text) + increment)

    def handle_convert(self):
        self.message = str(int(self.root.ids.input_number.text) * 1.60934)


ConvertNumberApp().run()
