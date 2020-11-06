from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton
from kivymd.uix.button import MDFloatingActionButton,MDRoundFlatIconButton,MDRaisedButton
from kivymd.uix.button import MDFillRoundFlatButton,MDFillRoundFlatIconButton
from kivymd.uix.button import MDRectangleFlatIconButton,MDFloatingRootButton


class buttonapp(MDApp):
    def build(self):
        scr = MDScreen()
        but1 = MDFlatButton(text='next->', pos_hint={'center_x': 0.1, 'center_y': 0.1})
        but2 = MDRectangleFlatButton(text='next->',pos_hint={'center_x':0.2,'center_y':0.2})
        but3 = MDIconButton(icon="language-python",pos_hint={'center_x': 0.3, 'center_y': 0.3})
        but4 = MDRoundFlatIconButton(text='hii', pos_hint={'center_x': 0.4, 'center_y': 0.4})
        but5 = MDFloatingActionButton(icon="language-python",pos_hint={'center_x': 0.5, 'center_y': 0.5})
        but6 = MDRaisedButton(text='kkkk',pos_hint={'center_x': 0.6, 'center_y': 0.6})
        but7 = MDFillRoundFlatButton(text='AAA',pos_hint={'center_x': 0.7, 'center_y': 0.7})
        but8 = MDFillRoundFlatIconButton(icon="language-python",pos_hint={'center_x': 0.8, 'center_y': 0.8})
        but9 = MDRectangleFlatIconButton(icon="language-python", pos_hint={'center_x': 0.9, 'center_y': 0.9})
        but10 = MDFloatingRootButton(icon="language-python",pos_hint={'center_x':0.1, 'center_y': 0.7})
        scr.add_widget(but1)
        scr.add_widget(but2)
        scr.add_widget(but3)
        scr.add_widget(but4)
        scr.add_widget(but5)
        scr.add_widget(but6)
        scr.add_widget(but7)
        scr.add_widget(but8)
        scr.add_widget(but9)
        scr.add_widget(but10)
        return scr

if __name__ == '__main__':
    buttonapp().run()
