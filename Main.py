from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.fitimage.fitimage import FitImage
from kivy.properties import StringProperty
from kivy.lang import Builder
import threading
import receive
import request
import time
from kivy.animation import Animation
from kivy.core.window import Window


class Frog(MDBoxLayout):
    message = StringProperty('')
    name = StringProperty('')
    source = "frog.png"
    visible = True
    
    def __init__(self, name, message, **kwargs):
        super(Frog, self).__init__(**kwargs)
        self.name=name
        self.message=message
        
        
    def setMessage(self, newMessage): ##Change the message on the frog card
        self.message = ""
        print("setMessage")
        for i in newMessage: ##typing text system
            self.message+=i
            time.sleep(.06)
            
    def setSource(self, newSource):
        self.source = newSource

    def flip_logic(self, person, location="none"):
        print("flip")

        FitImages = []        
        for widget in self.walk():
            if isinstance(widget, FitImage) and widget.source != None:    ## *Find the FitImages that house the frog logos. I might end up doing this a different way
                FitImages.append(widget)
                
        
               
        if location == "gone":         ##*If the person is saying that they are leaving then get rid of the photo
            anim = Animation(opacity=0)
            anim.start(FitImages[0])
            self.visible = False
            
            
        elif location == "home":    ##*If they are saying that they are coming home then put the photo back
            anim = Animation(opacity=1)
            anim.start(FitImages[0])
            self.visible = True
            
            
        else: ##*If the subject is neither gone nor home
            if self.visible: ##*if the card is set to the person being gone then flip it to them being home
                anim = Animation(opacity=0)
                anim.start(FitImages[0])
                self.visible = False
                
                
                
            else:  ##*If the card is set to the person being home then flip it to them being gone
                anim = Animation(opacity=1)
                anim.start(FitImages[0])
                self.visible = True

          
                
        
        
class MyApp(MDApp):
    thread2 = ""
    run_thread = True
    
    def boot(self):
        #calling this thread 2 since main thread has to be running GUI
        self.thread2 = threading.Thread(target=self.constant_fetch)
        self.thread2.start()
        
        time.sleep(.2)
        self.run()
        
    def constant_fetch(self): ##Have a cozy spot for the thread to chase its tail
        while self.run_thread:
            try:
                receive.login(army)
                request.request_API(army)
                time.sleep(5)
                ##after the first time this runs the frogs are initialized and added to the army so I can do stuff from here
            except:
                pass
    
        
    ##Build app in general
    def build(self):
        global army
        Window.bind(on_request_close=self.on_request_close)
        self.title = "Shinobi Frogs"
        self.icon = "frog.png"
        army = []
        Builder.load_file("gui.kv")
        layout = MDBoxLayout(orientation="horizontal", size_hint=(1, 1))
        Window.size = (800, 580)
        ##Create shinobi info
        data = [
            {"name": "Sam", "message": "Heading out! Be back in an hour!"},
            {"name": "Jane", "message": ""},
            {"name": "John", "message": ""}
        ]
        for item in data:
            frog = Frog(**item) ##Create frogs
            layout.add_widget(frog) ##Add frogs to app
            army.append(frog)
        return layout
        
    ##Safeish close system
    def on_request_close(self, *args):
        print("Will close when threads are killed...")
        self.run_thread = False
        self.thread2.join()
        quit(0)

if __name__ == "__main__":
    app = MyApp()
    time.sleep(.2) ##Give it just a second to create everything
    app.boot()
    
        