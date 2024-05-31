# import pyo
# import numpy as np
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from pyo import *
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
from kivy.uix.screenmanager import ScreenManager, Screen

KV = '''
WindowManager:
    MainWindow:
    Screen_2:
    Screen_3:

<MainWindow>:
    name: "main"
    FloatLayout:
        orientation: 'vertical'
        MDRaisedButton:
            text: "Обработать аудиофайл"
            pos_hint: {'center_x':.5, 'center_y':.6}
            on_release:
                app.root.current = "second"
                root.manager.transition.direction = "left"
        MDRaisedButton:
            text: "Записать и обработать голос"
            pos_hint: {'center_x':.5, 'center_y':.5}
            on_release:
                app.root.current = "third"
                root.manager.transition.direction = "left"
                app.initial2()
        MDLabel:
            text: "Звуковые эффекты"
            pos_hint: {'center_x':.76, 'center_y':.8}
            color: 0.3, 0.7, 1, 1
            bold: True
            size_hint: 1, 0.1
            font_size: self.width/20

<Screen_2>:
    name: "second"
    BoxLayout:
        orientation: 'vertical'
        pos_hint:{'center_x':.5, 'center_y':1.4}
        BoxLayout:
            orientation: 'horizontal'
            padding: 10
            spacing: 10
            MDRaisedButton:
                text: "<<--"
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
            MDRoundFlatIconButton:
                id: b1
                text: "Выбрать аудиофайл"
                icon: "folder"
                on_release: app.file_manager_open2()
            MDRaisedButton:
                id: b2
                text: "Слушать"
                on_release: app.start_stop_playing_file(), root.change_title_b2()
            MDRoundFlatIconButton:
                id: b3
                text: "Выбрать папку для записи"
                icon: "folder"
                on_release: app.file_manager_open()
            MDRaisedButton:
                id: b4
                text: "Запись"
                on_release: app.start_stop_record(), root.change_title_b4()
            MDRaisedButton:
                id: b5
                text: "Запись c начала"
                on_release: app.start_stop_playing_and_record(), root.change_title_b5()
            MDRaisedButton:
                id: b6
                icon: "folder"
                text: "Сбросить эффекты"
                on_release: app.set_default(), root.set_default()
        BoxLayoutSliders:
            orientation: 'horizontal'
            padding: 30
            spacing: 10
            size_hint: 1.0, 0.9
            FloatLayout:
                Slider:
                    id: s_harmonizer
                    orientation: 'vertical'
                    pos_hint: {'center_x':.5, 'center_y':.45}
                    value_track: True
                    value_track_color: 0.3, 0.7, 1, 1
                    min: -24
                    max: 24
                    step: 1
                    value: 0
                    on_touch_move: app.slider1(s_harmonizer.value)
                Label:
                    text: "Гармонизатор"
                    color: 0.3, 0.7, 1, 1
                    pos_hint: {'center_x':.5, 'center_y':.99}
            FloatLayout:
                Slider:
                    id: s_delay
                    orientation: 'vertical'
                    pos_hint: {'center_x':.5, 'center_y':.45}
                    value_track: True
                    value_track_color: 0.3, 0.7, 1, 1
                    min: 0
                    max: 40
                    step: 1
                    value: 0
                    on_touch_move: app.slider2(s_delay.value)
                Label:
                    text: "Задержка"
                    color: 0.3, 0.7, 1, 1
                    pos_hint: {'center_x':.5, 'center_y':.99}
            FloatLayout:
                Slider:
                    id: s_echo
                    orientation: 'vertical'
                    pos_hint: {'center_x':.5, 'center_y':.45}
                    value_track: True
                    value_track_color: 0.3, 0.7, 1, 1
                    min: 0
                    max: 40
                    step: 1
                    value: 0
                    on_touch_move: app.slider3(s_echo.value)
                Label:
                    text: "Эхо"
                    color: 0.3, 0.7, 1, 1
                    pos_hint: {'center_x':.5, 'center_y':.99}
            FloatLayout:
                Slider:
                    id: s_voices
                    orientation: 'vertical'
                    pos_hint: {'center_x':.5, 'center_y':.45}
                    value_track: True
                    value_track_color: 0.3, 0.7, 1, 1
                    min: 0
                    max: 8
                    step: 1
                    value: 0
                    on_touch_move: app.slider4(s_voices.value)
                Label:
                    text: "Голоса"
                    color: 0.3, 0.7, 1, 1
                    pos_hint: {'center_x':.5, 'center_y':.99}
            FloatLayout:
                Slider:
                    id: s_freqshift
                    orientation: 'vertical'
                    pos_hint: {'center_x':.5, 'center_y':.45}
                    value_track: True
                    value_track_color: 0.3, 0.7, 1, 1
                    min: -20
                    max: 20
                    step: 1
                    value: 0
                    on_touch_move: app.slider5(s_freqshift.value)
                Label:
                    text: "Частота"
                    color: 0.3, 0.7, 1, 1
                    pos_hint: {'center_x':.5, 'center_y':.99}

<Screen_3>:
    name: "third"
    BoxLayout:
        orientation: 'vertical'
        spacing:10
        BoxLayout:
            orientation: 'horizontal'
            padding: 10
            spacing: 10
            size_hint: 1.0, 0.1
            MDRaisedButton:
                text: "<<--"
                on_release:
                    app.root.current = "main"
                    root.manager.transition.direction = "right"
            MDRaisedButton:
                id: b23
                icon: "folder"
                text: "Слышать себя"
                on_release: app.modus_x_2(), root.change_title_b23()
            MDRaisedButton:
                id: b33
                icon: "folder"
                text: "Запись"
                on_release: app.start_stop_record(), root.change_title_b33()
            MDRaisedButton:
                id: b34
                icon: "folder"
                text: "Сбросить эффекты"
                on_release: app.set_default(), root.set_default()
            MDRoundFlatIconButton:
                text: "Выбрать папку для записи"
                icon: "folder"
                on_release: app.file_manager_open()
        BoxLayoutSliders:
            orientation: 'horizontal'
            padding: 30
            spacing: 10
            size_hint: 1.0, 0.7
            FloatLayout:
                Slider:
                    id: s_harmonizer
                    orientation: 'vertical'
                    pos_hint: {'center_x':.5, 'center_y':.45}
                    value_track: True
                    value_track_color: 0.3, 0.7, 1, 1
                    min: -24
                    max: 24
                    step: 1
                    value: 0
                    on_touch_move: app.slider1(s_harmonizer.value)
                Label:
                    text: "Гармонизатор"
                    color: 0.3, 0.7, 1, 1
                    pos_hint: {'center_x':.5, 'center_y':.99}
            FloatLayout:
                Slider:
                    id: s_delay
                    orientation: 'vertical'
                    pos_hint: {'center_x':.5, 'center_y':.45}
                    value_track: True
                    value_track_color: 0.3, 0.7, 1, 1
                    min: 0
                    max: 40
                    step: 1
                    value: 0
                    on_touch_move: app.slider2(s_delay.value)
                Label:
                    text: "Задержка"
                    color: 0.3, 0.7, 1, 1
                    pos_hint: {'center_x':.5, 'center_y':.99}
            FloatLayout:
                Slider:
                    id: s_echo
                    orientation: 'vertical'
                    pos_hint: {'center_x':.5, 'center_y':.45}
                    value_track: True
                    value_track_color: 0.3, 0.7, 1, 1
                    min: 0
                    max: 40
                    step: 1
                    value: 0
                    on_touch_move: app.slider3(s_echo.value)
                Label:
                    text: "Эхо"
                    color: 0.3, 0.7, 1, 1
                    pos_hint: {'center_x':.5, 'center_y':.99}
            FloatLayout:
                Slider:
                    id: s_voices
                    orientation: 'vertical'
                    pos_hint: {'center_x':.5, 'center_y':.45}
                    value_track: True
                    value_track_color: 0.3, 0.7, 1, 1
                    min: 0
                    max: 8
                    step: 1
                    value: 0
                    on_touch_move: app.slider4(s_voices.value)
                Label:
                    text: "Голоса"
                    color: 0.3, 0.7, 1, 1
                    pos_hint: {'center_x':.5, 'center_y':.99}
            FloatLayout:
                Slider:
                    id: s_freqshift
                    orientation: 'vertical'
                    pos_hint: {'center_x':.5, 'center_y':.45}
                    value_track: True
                    value_track_color: 0.3, 0.7, 1, 1
                    min: -20
                    max: 20
                    step: 1
                    value: 0
                    on_touch_move: app.slider5(s_freqshift.value)
                Label:
                    text: "Частота"
                    color: 0.3, 0.7, 1, 1
                    pos_hint: {'center_x':.5, 'center_y':.99}

<BoxLayoutSliders@BoxLayout>:

<FileManager@BoxLayout>:
    orientation: 'vertical'
    BoxLayout:
        MDRaisedButton:
            text: "Назад"
            on_release: app.file_manager.back()
        MDRaisedButton:
            text: "Выход"
            on_release: app.exit_manager()
    MDFileManager:
        id: file_manager
        exit_manager: app.exit_manager
        select_path: app.select_path

'''


class WindowManager(ScreenManager):
    pass


class MainWindow(Screen):
    pass


class Screen_2(Screen):
    def change_title_b2(self):
        if self.ids.b2.text == 'Слушать':
            self.ids.b2.text = 'Стоп'
        else:
            self.ids.b2.text = 'Слушать'

    def change_title_b4(self):
        if self.ids.b4.text == 'Запись':
            self.ids.b4.text = 'Остановить запись'
        else:
            self.ids.b4.text = 'Запись'

    def change_title_b5(self):
        if self.ids.b5.text == 'Запись с начала':
            self.ids.b5.text = 'Остановить запись'
        else:
            self.ids.b5.text = 'Запись с начала'

    def set_default(self):
        self.ids.s_harmonizer.value = 0
        self.ids.s_delay.value = 0
        self.ids.s_echo.value = 0
        self.ids.s_voices.value = 0
        self.ids.s_freqshift.value = 0


class Screen_3(Screen):
    def change_title_b23(self):
        if self.ids.b23.text == 'Слышать себя':
            self.ids.b23.text = 'Стоп'
        else:
            self.ids.b23.text = 'Слышать себя'

    def change_title_b33(self):
        if self.ids.b33.text == 'Запись':
            self.ids.b33.text = 'Остановить запись'
        else:
            self.ids.b33.text = 'Запись'

    def set_default(self):
        self.ids.s_harmonizer.value = 0
        self.ids.s_delay.value = 0
        self.ids.s_echo.value = 0
        self.ids.s_voices.value = 0
        self.ids.s_freqshift.value = 0


class MyApp(MDApp):
    file_manager_obj = None
    dialog = None

    def build(self):
        self.title = "Звуковые эффекты"
        return Builder.load_string(KV)

    def on_start(self):
        Window.bind(on_keyboard=self.events)

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.file_manager_obj:
                self.file_manager_obj.back()
            return True

    def file_manager_open(self):
        self.file_manager_obj = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
        )
        self.file_manager_obj.show('/')

    def file_manager_open2(self):
        self.file_manager_obj = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path2,
        )
        self.file_manager_obj.show('/')

    def select_path(self, path):
        self.exit_manager()
        toast(path)

    def select_path2(self, path):
        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        self.file_manager_obj.close()

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="This is a test dialog",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        on_release=lambda x: self.dialog.dismiss()
                    ),
                ],
            )
        self.dialog.open()

    def modus_x_2(self):
        pass  # Add your logic here

    def initial2(self):
        pass  # Add your logic here

    def start_stop_playing_file(self):
        pass  # Add your logic here

    def start_stop_record(self):
        pass  # Add your logic here

    def start_stop_playing_and_record(self):
        pass  # Add your logic here

    def set_default(self):
        pass  # Add your logic here

    def slider1(self, value):
        pass  # Add your logic here

    def slider2(self, value):
        pass  # Add your logic here

    def slider3(self, value):
        pass  # Add your logic here

    def slider4(self, value):
        pass  # Add your logic here

    def slider5(self, value):
        pass  # Add your logic here


if __name__ == "__main__":
    MyApp().run()
