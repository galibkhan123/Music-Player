


from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang.builder import Builder
from kivy.core .window import Window
from kivy.uix.effectwidget import *
from kivy.animation import Animation
from kivy.properties import NumericProperty
from pygame import mixer
from kivymd.utils import asynckivy
from tkinter import Tk, filedialog

from kivymd.utils import asynckivy
import time
mixer.init()
style =('''
ScreenManager:
   
    Second:
    First:


<Second>
    name:'2'
    FitImage:
        source:'splash.jpg'
    

<First>
    name:"1"
        # EffectWidget:
        #     effects:[VerticalBlurEffect(size=10)]
        
    FitImage:
        id:changer
        size_hint_y: 1 
        source: "song.jpg"


    FitImage:
        
        source:"crop1.png"
        pos_hint:{'center_y':0.7,'center_x':0.5}
        size_hint:0.7,0.5
        radius: [250, 250, ]
        canvas.before:
            PushMatrix
            Rotate:
                id:change
                angle: app.angle
                origin: self.center
        canvas.after:
            PopMatrix

            
    MDBoxLayout:
        padding:55
        spacing:20
        pos_hint:{"center_y":0.2,"center_x":0.5}
        # padding_y:100

        MDIconButton:
            
            icon:'skip-backward'
            pos_hint:{"center_y":0.5,"center_x":0.5}
            color_mode:"custom"
            text_color: (1,1,1,1)
            user_font_size:30
            
        MDIconButton:
            id:play
            icon:'pause'
            pos_hint:{"center_y":0.5,"center_x":0.5}
            color_mode:"custom"
            text_color: (1,1,1,1)
            user_font_size:50
            on_release:app.change()
            
        MDIconButton:
            
            icon:'skip-forward'
            pos_hint:{"center_y":0.5,"center_x":0.5}
            color_mode:"custom"
            text_color: (1,1,1,1)
            user_font_size:30
            

        MDIconButton:
            
            icon:'menu'
            pos_hint:{"center_y":0.5,"center_x":0.5}
            color_mode:"custom"
            text_color: (1,1,1,1)
            user_font_size:30
            on_release:app.upload()
    

            min:0


            
''')
class First(Screen):
    pass
class Second(Screen):
    pass
sm = ScreenManager()
sm.add_widget(First(name="1"))
sm.add_widget(Second(name="2"))
class demoApp(MDApp):
    angle = NumericProperty()
    anim = Animation(angle=360,d=3,t='linear')
    anim +=Animation(angle=0,d=0,t='linear')
    anim.repeat = True
  
    prog = Animation(value=100,d=100,t='linear')

    
            
    def build(self):
        self.code = Builder.load_string(style)
        screen=Screen()
        screen.add_widget(self.code)

        self.set_heading()
        
        return screen


    def convert(seconds):
        hours = seconds // 3600
        seconds %= 3600

        mins = seconds // 60
        seconds %= 60

        return hours, mins, seconds

    # Create an MP3 object
    # Specify the directory address to the mp3 file as a parameter
 

    # Contains all the metadata about the mp3 file
 

    

   



 
    
    def upload(self):
        root = Tk()
        root.withdraw()

        self.file_path = filedialog.askopenfilename()
        print(self.file_path)

    def click(self):
        self.code.get_screen('2').manager.current = '2'
        
  
    # def set_heading(self):
    #     async def set_heading():
    #         for i in range(self.b):
    #             await asynckivy.sleep(1)
    #             self.code.get_screen('1').ids.pro.value=(i)
            

    #     asynckivy.start(set_heading())

    def back(self):
        self.code.get_screen('1').manager.current = '1'

    def change(self):
        if self.code.get_screen('1').ids.play.icon=='play':
            self.code.get_screen('1').ids.play.icon='pause'
            self.stop()
            # asynckivy.sleep(self.set_heading())
            
            mixer.music.pause()	
        # elif self.code.get_screen('1').ids.play.icon=='pause':
        #         self.code.get_screen('1').ids.play.icon='play'
        #         mixer.music.unpause()
        # elif mixer.music.load=="":
        #     self.upload  
        elif self.code.get_screen('1').ids.play.icon=='pause':
            try:
                self.code.get_screen('1').ids.play.icon='play'
                # self.code.get_screen('1').ids.pro.max=self.b
                self.rote()
                # self.set_heading()
                self.a=mixer.music.load(f"{self.file_path}")
                mixer.music.set_volume(0.7)
                mixer.music.play()
            except:
                self.upload()
                self.code.get_screen('1').ids.play.icon='pause'
                
                self.stop()
                
        
        

            
            
    def rote(self):
        self.anim.start(self)
        
    def stop(self):
        self.anim.stop(self)

    def set_heading(self):
            async def set_heading():
                
                    await asynckivy.sleep(5)
                    self.code.get_screen('1').manager.current = '1'
                

            asynckivy.start(set_heading())
    
Window.size=350,500


demoApp().run()
