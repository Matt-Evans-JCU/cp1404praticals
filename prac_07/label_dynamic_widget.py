from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class LabelDynamicWidgetApp(App):

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Label Dynamic Widget"
        self.root = Builder.load_file('label_dynamic_widget.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name,id=name)
            self.root.ids.entries_labels.add_widget(temp_label)


LabelDynamicWidgetApp().run()