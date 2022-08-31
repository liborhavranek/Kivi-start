# ------------------- instal in terminal ----------------------
# py -m pip install cython
# py -m pip install pygame
# py -m pip install Pillow
# Poté nainstalujeme samotný Kivy framework:
#
# py -m pip install kivy


# Importujeme Kivy
import kivy
# Minimální potřebná verze pro spuštění
kivy.require("1.10.1")
# Importujeme Tlačítko
from kivy.uix.button import Button
# Importujeme Label
from kivy.uix.label import Label
# Importujeme Aplikaci
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGridLayout(GridLayout):
	def __init__(self, **kwargs):
		# call grid layout constructor
		super(MyGridLayout, self).__init__(**kwargs)
		# set columns
		self.cols = 1
		self.row_force_default = True
		self.row_default_height = 140
		self.col_force_default = True
		self.col_default_width = 300

		# create second grid layout
		self.top_grid = GridLayout(
		row_force_default=True,
		row_default_height=40,
		col_force_default = True,
		col_default_width = 200
		)
		self.top_grid.cols = 2


		# add widgets
		self.top_grid.add_widget(Label(text="Name: ",
		                               size_hint_y=None,
		                               height=50,
		                               size_hint_x=None,
		                               width=300
		                               ))
		# add input box
		self.name = TextInput(multiline=False)
		self.top_grid.add_widget(self.name)

		# add widgets
		self.top_grid.add_widget(Label(text="Favorite pizza: "))
		# add input box
		self.pizza = TextInput(multiline=False)
		self.top_grid.add_widget(self.pizza)

		# add widgets
		self.top_grid.add_widget(Label(text="Favorite color: "))
		# add input box
		self.color = TextInput(multiline=False)
		self.top_grid.add_widget(self.color)

		# add new grid to my app
		self.add_widget(self.top_grid)

		# create submit button
		self.submit = Button(text='submit', font_size=32,
		                     size_hint_y=None,
		                     height=50,
		                     size_hint_x=None,
		                     width=300)
		self.submit.bind(on_press=self.press_button)
		self.add_widget(self.submit)

	def press_button(self, instance):
		name = self.name.text
		pizza = self.pizza.text
		color = self.color.text
		self.add_widget(Label(text=f'Hello {name} you like {pizza}, and {color}'))

		print(f'Hello {name} you like {pizza}, and {color}')




#Vytvoříme třídu aplikace
class MainApp(App):
    #Metoda, která vrátí tlačítko, které se má zobrazit
    def build(self):
        return MyGridLayout()

#Spuštění
app = MainApp()
app.run()