from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from instructions import *
from timer import Timer

Window.clearcolor = (.1, .11, .12, 1)
lbl_color = (.9, .95, .50, 1)
btn_color = (.29, .53, .94, 1)

name = ""
age = 0
p1 = 0
p2 = 0
p3 = 0

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        insrt = Label(text=txt_instruction, color=lbl_color, bold=True)
        lbl_name = Label(text="Введіть ім'я:", halign='right', color=lbl_color, bold=True, font_size=40)
        self.input_name = TextInput(text="Микола", multiline=False)
        lbl_age = Label(text="Введіть вік:", halign='right', color=lbl_color, bold=True, font_size=40)
        self.input_age = TextInput(text="7", multiline=False)
        self.btn = Button(text='Почати', size_hint=(.3, .2), pos_hint={'center_x': .5}, bold=True, background_color=btn_color)
        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(.8, None), height="30sp")
        line2 = BoxLayout(size_hint=(.8, None), height="30sp")

        line1.add_widget(lbl_name)
        line1.add_widget(self.input_name)

        line2.add_widget(lbl_age)
        line2.add_widget(self.input_age)

        main_line = BoxLayout(orientation='vertical', padding=10, spacing=15)
        main_line.add_widget(insrt)
        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)

    def next(self):
        global name, age
        name = self.input_name.text
        age = check_int(self.input_age.text)
        if age <= 7 or age is False:
            age = 7
            self.input_age.text = str(age)
        else:
            self.manager.current = 'second'

class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        instr = Label(text=txt_test1, color=lbl_color, bold=True)

        self.lbl_sec = Timer(15, color=lbl_color, bold=True)
        lbl_result = Label(text="Введіть Результат:", halign='right', color=lbl_color, bold=True, font_size=35)
        self.input_result = TextInput(text="1", multiline=False)
        self.input_result.set_disabled(True)
        self.btn = Button(text='Почати', size_hint=(.3, .2), pos_hint={'center_x': .5}, bold=True, background_color=btn_color)
        self.btn.on_press = self.next

        main_line = BoxLayout(orientation='vertical', padding=10, spacing=15)
        main_line.add_widget(instr)
        main_line.add_widget(self.lbl_sec)
        line = BoxLayout(size_hint=(.8, None), height="30sp")
        line.add_widget(lbl_result)
        line.add_widget(self.input_result)
        main_line.add_widget(line)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)

    def next(self):
        global p1
        if not self.next_screen:
            self.input_result.set_disabled(False)
            self.lbl_sec.start()
        else:
            p1 = check_int(self.input_result.text)
            if p1 is False or p1 <= 1:
                p1 = 0
                self.input_result.text = str(p1)
            else:
                self.manager.current = 'third'

class SitsScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_sits, color=lbl_color, bold=True)

        self.sits = Label(text='Залишилось присідань: 30', color=lbl_color, bold=True)
        self.btn = Button(text='Почати', size_hint=(.3, .2), pos_hint={'center_x': .5}, bold=True, background_color=btn_color)
        self.btn.on_press = self.next

        main_line = BoxLayout(orientation='vertical', padding=10, spacing=15)
        main_line.add_widget(instr)
        main_line.add_widget(self.sits)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)

    def next(self):
        self.manager.current = 'fourth'

class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test3, color=lbl_color, bold=True)
        lbl_pulse = Label(text="Рахуйте пульс", color=lbl_color, bold=True)
        self.lbl_sec = Label(text="Пройшло секунд: 0", color=lbl_color, bold=True)

        lbl_result = Label(text="Результат", halign='right', color=lbl_color, bold=True, font_size=40)
        self.input_result = TextInput(text="0", multiline=False)
        lbl_after_res = Label(text="Результат після відпочинку:", halign='right', color=lbl_color, bold=True, font_size=23)
        self.input_after_res = TextInput(text="0", multiline=False)

        self.btn = Button(text='Почати', size_hint=(.3, .2), pos_hint={'center_x': .5}, bold=True, background_color=btn_color)
        self.btn.on_press = self.next

        main_line = BoxLayout(orientation='vertical', padding=10, spacing=15)
        main_line.add_widget(instr)
        main_line.add_widget(lbl_pulse)
        main_line.add_widget(self.lbl_sec)

        line1 = BoxLayout(size_hint=(.8, None), height="30sp")
        line2 = BoxLayout(size_hint=(.8, None), height="30sp")
        line1.add_widget(lbl_result)
        line1.add_widget(self.input_result)
        line2.add_widget(lbl_after_res)
        line2.add_widget(self.input_after_res)

        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)

    def next(self):
        self.manager.current = 'fifth'


class ResultScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.index_label = Label(text="Ваш індекс Руф'є: -14.8", color=lbl_color, bold=True, font_size=25)
        self.workability_label = Label(text="Працездатність серця: висока", color=lbl_color, bold=True, font_size=25)

        main_line = BoxLayout(orientation='vertical', padding=10, spacing=15)
        main_line.add_widget(self.index_label)
        main_line.add_widget(self.workability_label)

        self.add_widget(main_line)

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='first'))
        sm.add_widget(PulseScr(name='second'))
        sm.add_widget(SitsScr(name='third'))
        sm.add_widget(PulseScr2(name='fourth'))
        sm.add_widget(ResultScr(name='fifth'))
        return sm
    
app = HeartCheck()
app.run()
