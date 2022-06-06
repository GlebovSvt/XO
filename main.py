from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.button import Button

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 450)


class MyLayout(Widget):
    turnFlag = 1
    def click(self, instance):

        if self.turnFlag == 1:
            instance.text = 'X'
        else:
            instance.text = 'O'
        self.turnFlag *= -1
        self.checkWin(self.ids._1, self.ids._2, self.ids._3)
        self.checkWin(self.ids._1, self.ids._4, self.ids._7)
        self.checkWin(self.ids._1, self.ids._5, self.ids._9)
        self.checkWin(self.ids._2, self.ids._5, self.ids._8)
        self.checkWin(self.ids._3, self.ids._5, self.ids._7)
        self.checkWin(self.ids._4, self.ids._5, self.ids._6)
        self.checkWin(self.ids._7, self.ids._8, self.ids._9)


    def restart(self, *args):
        self.ids._1.text = ''
        self.ids._2.text = ''
        self.ids._3.text = ''
        self.ids._4.text = ''
        self.ids._5.text = ''
        self.ids._6.text = ''
        self.ids._7.text = ''
        self.ids._8.text = ''
        self.ids._9.text = ''
        self.ids._1.background_color = (255, 255, 255, 1)
        self.ids._2.background_color = (255, 255, 255, 1)
        self.ids._3.background_color = (255, 255, 255, 1)
        self.ids._4.background_color = (255, 255, 255, 1)
        self.ids._5.background_color = (255, 255, 255, 1)
        self.ids._6.background_color = (255, 255, 255, 1)
        self.ids._7.background_color = (255, 255, 255, 1)
        self.ids._8.background_color = (255, 255, 255, 1)
        self.ids._9.background_color = (255, 255, 255, 1)
        self.ids._1.color = (0, 0, 0, 1)
        self.ids._2.color = (0, 0, 0, 1)
        self.ids._3.color = (0, 0, 0, 1)
        self.ids._4.color = (0, 0, 0, 1)
        self.ids._5.color = (0, 0, 0, 1)
        self.ids._6.color = (0, 0, 0, 1)
        self.ids._7.color = (0, 0, 0, 1)
        self.ids._8.color = (0, 0, 0, 1)
        self.ids._9.color = (0, 0, 0, 1)
        self.turnFlag = 1

    def checkWin(self, x, x1, x2):
        if x.text == x1.text == x2.text and x.text != '':
            popup = Popup(title='Congratulations!',
                          content=Button(text=f'{x.text} WIN!', font_size=50, on_release=lambda *args: popup.dismiss()))
            popup.open()
            win = x.text
            print(f'{x.text} WIN!')
            self.restart()
            x.text = win
            x1.text = win
            x2.text = win
            self.ids._1.background_color = (0, 0, 0, 1)
            self.ids._2.background_color = (0, 0, 0, 1)
            self.ids._3.background_color = (0, 0, 0, 1)
            self.ids._4.background_color = (0, 0, 0, 1)
            self.ids._5.background_color = (0, 0, 0, 1)
            self.ids._6.background_color = (0, 0, 0, 1)
            self.ids._7.background_color = (0, 0, 0, 1)
            self.ids._8.background_color = (0, 0, 0, 1)
            self.ids._9.background_color = (0, 0, 0, 1)
            x.color = (0, 1, 0, 1)
            x1.color = (0, 1, 0, 1)
            x2.color = (0, 1, 0, 1)




class XoApp(App):
    def build(self):
        return MyLayout()



if __name__ == '__main__':
    XoApp().run()