from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

__author__ = 'Matt Evans'
KM_CONVERSION = 1.60934


class ConvertNumberApp(App):
    """ ConvertNumberApp is a Kivy App for converting a number from miles to kilometers """
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (1000, 500)
        self.title = "Miles to Kilometers"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_increment(self, increment):
        value = self.get_valid_miles() + increment
        self.root.ids.input_number.text = str(value)
        self.handle_convert()

    def handle_convert(self):
        value = self.get_valid_miles()
        result = value * KM_CONVERSION
        self.root.ids.output_number.text = str(result)

    def get_valid_miles(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


ConvertNumberApp().run()
