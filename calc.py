from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class CalculatorApp (App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        self.solution = TextInput(multiline=False, font_size=55, halign="right", readonly=False)
        main_layout.add_widget(self.solution)

        buttons = [
            ["(", ")", "^", "del"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={"center_x=": 0.5, "center_y": 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(text="=", pos_hint={"center_x": 0.5, "center_y": 0.5})
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        if instance.text == "C":
            self.solution.text = ""
        elif instance.text == "del":
            self.solution.text = self.solution.text[:-1]
        else:
            self.solution.text += instance.text

    def on_solution(self, instance):
        if self.solution.text:
            try:
                example = self.solution.text
                for i in range(len(example) - 1):
                    if example[i] == "^": example = example[:i] + "**" + example[i + 1:]
                self.solution.text = str(eval(example))
            except:
                self.solution.text = "ERROR"


if __name__ == "__main__":
    CalculatorApp().run()
