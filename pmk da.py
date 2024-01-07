from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.image import Image

class StartMenu(Screen):
    def _init_(self, **kwargs):
        super(StartMenu, self)._init_(**kwargs)
        layout = BoxLayout(orientation='vertical')
        start_button = Button(text='Start Game', on_press=self.start_game)
        exit_button = Button(text='Exit', on_press=self.exit_game)
        layout.add_widget(start_button)
        layout.add_widget(exit_button)
        self.add_widget(layout)

    def start_game(self, instance):
        self.manager.current = 'character_selection'

    def exit_game(self, instance):
        App.get_running_app().stop()

class CharacterSelection(Screen):
    character_data = [
        {'name': 'mani', 'skill': 'Super Strength'},
        {'name': 'aswhin', 'skill': 'Invisibility'},
        {'name': 'hariram', 'skill': 'Teleportation'},
        {'name': 'bose', 'skill': 'Fireball'},
        {'name': 'dhiwash', 'skill': 'Mind Control'},
        {'name': 'aathi', 'skill': 'Force Field'},
        {'name': 'Achu', 'skill': 'Healing Powers'},
        {'name': 'sriram', 'skill': 'Super Speed'},
        {'name': 'md_hariesh', 'skill': 'Electric Shock'},
        {'name': 'prassanna', 'skill': 'Time Manipulation'},
        {'name': 'Veera_mani', 'skill': 'Ice Blast'}
    ]

    def _init_(self, **kwargs):
        super(CharacterSelection, self)._init_(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Select Your Character')

        character_buttons = [Button(text=data['name'], on_press=self.select_character) for data in self.character_data]

        layout.add_widget(label)
        for button in character_buttons:
            layout.add_widget(button)
        self.add_widget(layout)

    def select_character(self, instance):
        selected_character = instance.text
        character_data = next(data for data in CharacterSelection.character_data if data['name'] == selected_character)
        print(f"Selected Character: {selected_character}, Skill: {character_data['skill']}")
        # Add logic for transitioning to the game screen with the selected character

class Enemy:
    def _init_(self, name, power):
        self.name = name
        self.power = power

class GameScreen(Screen):
    def _init_(self, **kwargs):
        super(GameScreen, self)._init_(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Game Screen - Work in Progress')
        layout.add_widget(label)

        # Creating enemy instances with names and powers
        enemies_data = [
            {'name': 'kunavathi', 'power': 'Mind Manipulation'},
            {'name': 'juteball', 'power': 'Telekinesis'},
            {'name': 'Ramesh', 'power': 'Inferno'},
            {'name': 'Raj Kumar', 'power': 'Lightning Strike'},
            {'name': 'jegadeesan', 'power': 'Poison Dart'}
        ]

        enemies = [Enemy(name=data['name'], power=data['power']) for data in enemies_data]

        # Displaying enemy information
        for enemy in enemies:
            enemy_label = Label(text=f"Enemy: {enemy.name}, Power: {enemy.power}")
            layout.add_widget(enemy_label)

        self.add_widget(layout)

class GameApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # Set background color
        sm = ScreenManager()
        sm.add_widget(StartMenu(name='start_menu'))
        sm.add_widget(CharacterSelection(name='character_selection'))
        sm.add_widget(GameScreen(name='game_screen'))
        return sm

if __name__ == '_main_':
    GameApp().run()
