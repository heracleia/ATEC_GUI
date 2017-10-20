#!python
#!/usr/bin/env python
from kivy.app import App
from kivy.uix.bubble import Bubble
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.graphics.instructions import CanvasBase
from kivy.uix.progressbar import ProgressBar



Builder.load_string('''
#template for menu items
[ListButton@ToggleButton]
    background_normal: 'button_normal_cmenu.jpg'
    background_down: 'button_normal_cmenu_d.jpg'
    #background_color: ctx.background_color if hasattr(ctx, 'background_color') else [1, 1, 1, 1]
    group: 'context_menue_root'
    on_release: ctx.on_release(self) if hasattr(ctx, 'on_release') else None
    size_hint: ctx.size_hint if hasattr(ctx, 'size_hint') else (1, 1)
    width: ctx.width if hasattr(ctx, 'width') else 1
    text: ctx.text if hasattr(ctx, 'text') else ''
    

<Button>:
    font_size: self.texture_size[1]/6 
    size_hint: 0.25,0.130
    color: (0, 0, 0, 1)
    #background_color: (0.81, 0.20, 0.81, 1)
    #width: self.texture_size[0]
    #height: self.texture_size[1]
    text_size: self.width,self.height
    halign: 'center'
    valign: 'middle'
    background_down: 'button_down.png'
    #background_down: 'atlas://data/images/defaulttheme/bubble_btn'
    background_normal: 'button_normal.jpg'

<MainScreen>
    id: "main"
    pos_hint: {"right":1,"top":1} 
    size_hint: 0.75, 1
    canvas:
        Rectangle:
            source: 'main_canvas2.jpg'
            pos: self.pos
            size: self.size
   



   

<MainMenu>
    canvas:
        Rectangle:
            source: 'button_back.jpg'
            pos: self.pos
            size: self.size
    
    MainScreen:
         
        Label:
            id: label
            text:"ATEC \\n\\nINTRODUCTION:\\n[Begin with child standing.]\\n\\nSCRIPT:\\nWe are going to play games today that involve using your body in lots of different ways.\\n\\nSometimes, you will do movements that are familiar to you; sometimes you will do movements you may not have done before.\\n\\nWe will always make sure to tell you exactly what to do and sometimes we will show you how to do them. And we always play safe.\\n\\nAre you ready to play the games?"
            text_size: root.width-root.width*0.45,  root.height
            font_size: self.texture_size[1]/28 
            size: self.texture_size
            pos_hint: {"right":0.92,"top":01} 
            color: (1, 1, 1, 1)
            halign: 'left'
            valign: 'top'

        Button:
            #text: "START"
            on_release:  root.on_control(args[0],"start")
            pos_hint: {"right":1,"top":0.8} 
            background_normal: "start2.png"
            size_hint: 0.15,0.15
            background_down: 'record_pressed.png'

        Button:
            #text: "PAUSE"
            on_release:  root.on_control(args[0],"pause")
            pos_hint: {"right":1,"top":0.6}   
            background_normal: "pause.png"
            size_hint: 0.15,0.15
            background_down: 'pause_pressed.png'

        Button:
            #text: "STOP"
            on_release:  root.on_control(args[0],"stop")
            pos_hint: {"right":1,"top":0.4}  
            background_normal: "stop.png"
            size_hint: 0.15,0.15
            background_down: 'stop_pressed.png'

        Button:
            #text: "Task Copleted"
            on_release:  root.on_control(args[0],"complete")
            pos_hint: {"right":1,"top":1}  
            background_normal: "complete2.png"
            background_down: 'complete.png'
            size_hint: 0.15,0.15
        
        

    Button:
        id: "sdsd"
        text: "Gross Motor \\nGait and Balance"
        on_release:  root.add_menu(args[0],1)
        pos_hint: {"right":0.25,"top":1}  


    Button:
        on_release:  root.add_menu(args[0],2)
        text: "Synchronous Movements"
        pos_hint: {"right":0.25,"top":0.873}

    Button:
        on_release:  root.add_menu(args[0],3)
        text: "Bilateral Coordination &\\n Response Inhibition"
        pos_hint: {"right":0.25,"top":0.745}

    Button:
        on_release:  root.add_menu(args[0],4)
        text: "Bilateral Coordination &\\n Response Inhibition \\n(Red/Green Light)"
        pos_hint: {"right":0.25,"top":0.620}

    Button:
        on_release:  root.add_menu(args[0],5)
        text: "Visual Response\\n Inhibition"
        pos_hint: {"right":0.25,"top":0.495}

    Button:
        on_release:  root.add_menu(args[0],6)
        text: "Cross Body Game"
        pos_hint: {"right":0.25,"top":0.370}

    Button:
        on_release:  root.add_menu(args[0],7)
        text: " Finger-Nose\\n Coordination"
        pos_hint: {"right":0.25,"top":0.245}

    Button:
        on_release:  root.add_menu(args[0],8)
        text: "Rapid Sequential\\n Movements"
        pos_hint: {"right":0.25,"top":0.120}



<Cmenu1>
    id:t11
    size_hint: 0.41, 0.6
    pos_hint: {"right":0.65,"top":1}
    padding: 0.005
    #background_color: 1, 0, 0, 1
    
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Natural Walk'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Gait on Toes'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Tandem Gain'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Stand eyes closed hands outstretched'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Stand on One Foot'
                        on_release: root.menu_selected


<Cmenu2>
    size_hint: 0.41, 0.3
    pos_hint: {"right":0.65,"top":0.87}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'March Slow'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'March Fast'
                        on_release: root.menu_selected
                       

<Cmenu3>
    size_hint: 0.41, 0.3
    pos_hint: {"right":0.65,"top":0.75}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Bi-manual Bag Pass Slow'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Bi-manual Bag Pass Fast'
                        on_release: root.menu_selected

<Cmenu4>
    size_hint: 0.41, 0.6
    pos_hint: {"right":0.65,"top":0.62}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Red Light/Green Light -- Slow'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Red Light/Green Light -- Fast'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Red Light/Green Light/Yellow Light -- Slow'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Red Light/Green Light/Yellow Light -- Fast'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Red Light/Green Light/Yellow Light -- Visual Slow'
                        on_release: root.menu_selected

<Cmenu5>
    size_hint: 0.41, 0.16
    pos_hint: {"right":0.65,"top":0.50}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: ' A sailor went to Sea, Sea, Sea '
                        on_release: root.menu_selected

<Cmenu6>
    size_hint: 0.41, 0.35
    pos_hint: {"right":0.65,"top":0.37}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Cross Body Ears - Knees'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Cross Body Shoulders = Cross Body Hips'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Combined Reverse Actions'
                        on_release: root.menu_selected


<Cmenu7>
    size_hint: 0.41, 0.15
    pos_hint: {"right":0.65,"top":0.25}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Finger-Nose Coordination'
                        on_release: root.menu_selected

<Cmenu8>
    size_hint: 0.41, 0.7
    pos_hint: {"right":0.65,"top":0.68}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Foot Tap'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Foot-Heel-Toe Tap'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Hand Pat'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Hand Pronate/supinate'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Finger Tap'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Appose Finger Succession'
                        on_release: root.menu_selected                 
''')

global tast,text,intro
text =""
task=''



intro="""INTRODUCTION:\n[Begin with child standing.]\nSCRIPT: We are going to play games today that involve using your body in lots of different ways.\nSometimes, you will do movements that are familiar to you; sometimes you will do movements you may not have done before.\n"+
We will always make sure to tell you exactly what to do and sometimes we will show you how to do them. And we always play safe.\n
Are you ready to play the games?"""






class Cmenu1(Bubble):
    def __init__(self, **kwargs):
        super(Cmenu1, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self,*l):
        global text,task
        text = l[0].text

        if text == 'Natural Walk':
            task ='11'
        elif text == 'Gait on Toes':
            task ='12'
        elif text == 'Tandem Gain':
            task ='13'
        elif text == 'Stand eyes closed hands outstretched':
            task ='14'
        elif text == 'Stand on One Foot':
            task ='15'

        (r, g, b, a) = self.parent.context_menu.background_color
        print self.parent.context_menu.background_color
        def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

        for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"
                    child.color = (0, 0, 0, 1)

        anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
        anim.start(self.parent.context_menu)
        anim.bind(on_complete = on_anim_complete)
        self.parent.on_select_task(task)


class Cmenu2(Bubble):
    def __init__(self, **kwargs):
        super(Cmenu2, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self,*l):
        global text,task
       
        text = l[0].text

        (r, g, b, a) = self.parent.context_menu.background_color
        print self.parent.context_menu.background_color
        def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

        for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"
                    child.color = (0, 0, 0, 1)

        anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
        anim.start(self.parent.context_menu)
        anim.bind(on_complete = on_anim_complete)
        self.parent.on_select_task(task)





class Cmenu3(Bubble):
    
    def __init__(self, **kwargs):
        super(Cmenu3, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self,*l):
        global text
       
        text = l[0].text

        (r, g, b, a) = self.parent.context_menu.background_color
        print self.parent.context_menu.background_color
        def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

        for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"
                    child.color = (0, 0, 0, 1)

        anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
        anim.start(self.parent.context_menu)
        anim.bind(on_complete = on_anim_complete)



class Cmenu4(Bubble):

    def __init__(self, **kwargs):
        super(Cmenu4, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self,*l):
        global text
       
        text = l[0].text

        (r, g, b, a) = self.parent.context_menu.background_color
        print self.parent.context_menu.background_color
        def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

        for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"
                    child.color = (0, 0, 0, 1)

        anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
        anim.start(self.parent.context_menu)
        anim.bind(on_complete = on_anim_complete)



class Cmenu5(Bubble):

    def __init__(self, **kwargs):
        super(Cmenu5, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self,*l):
        global text
       
        text = l[0].text

        (r, g, b, a) = self.parent.context_menu.background_color
        print self.parent.context_menu.background_color
        def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

        for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"
                    child.color = (0, 0, 0, 1)

        anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
        anim.start(self.parent.context_menu)
        anim.bind(on_complete = on_anim_complete)


class Cmenu6(Bubble):

    def __init__(self, **kwargs):
        super(Cmenu6, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self,*l):
        global text
       
        text = l[0].text

        (r, g, b, a) = self.parent.context_menu.background_color
        print self.parent.context_menu.background_color
        def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

        for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"
                    child.color = (0, 0, 0, 1)

        anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
        anim.start(self.parent.context_menu)
        anim.bind(on_complete = on_anim_complete)

class Cmenu7(Bubble):

    def __init__(self, **kwargs):
        super(Cmenu7, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self,*l):
        global text
       
        text = l[0].text

        (r, g, b, a) = self.parent.context_menu.background_color
        print self.parent.context_menu.background_color
        def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

        for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"
                    child.color = (0, 0, 0, 1)

        anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
        anim.start(self.parent.context_menu)
        anim.bind(on_complete = on_anim_complete)


class Cmenu8(Bubble):

    def __init__(self, **kwargs):
        super(Cmenu8, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self,*l):
        global text
       
        text = l[0].text

        (r, g, b, a) = self.parent.context_menu.background_color
        print self.parent.context_menu.background_color
        def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

        for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"
                    child.color = (0, 0, 0, 1)

        anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
        anim.start(self.parent.context_menu)
        anim.bind(on_complete = on_anim_complete)




class MainScreen(FloatLayout) :

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        #self.ids['label'].text = self.ids['label'].text+"\n"+intro


class MainMenu(FloatLayout) :

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.context_menu = Cmenu1()
        global t1,t2,t3,t4,t5,t6,t7,t8 
        t1 = Cmenu1()
        t2 = Cmenu2()
        t3 = Cmenu3()
        t4 = Cmenu4()
        t5 = Cmenu5()
        t6 = Cmenu6()
        t7 = Cmenu7()
        t8 = Cmenu8()




    def on_touch_down(self, *l):
        #allow kids to get touch
        if super(MainMenu, self).on_touch_down(*l):
            return True
        self.remove_widget(self.context_menu)
        for child in self.children:
                #child.clear_widgets()
                child.background_normal = "button_normal.jpg"
                child.color = (0, 0, 0, 1)


    def add_menu(self, obj, submenu_id,*l):
        for child in self.children:
                #child.clear_widgets()
                child.background_normal = "button_normal.jpg"
                child.color = (0, 0, 0, 1)

        if  hasattr(self, 'context_menu'):
                self.remove_widget(self.context_menu)
        if submenu_id == 1:
            self.context_menu = t1
        elif submenu_id == 2:
            self.context_menu = t2
        elif submenu_id == 3:
            self.context_menu = t3
        elif submenu_id == 4:
            self.context_menu = t4
        elif submenu_id == 5:
            self.context_menu = t5
        elif submenu_id == 6:
            self.context_menu = t6
        elif submenu_id == 7:
            self.context_menu = t7
        elif submenu_id == 8:
            self.context_menu = t8

        if submenu_id not in ["start","stop","pause"]:
            obj.background_normal = "button_normal_is_on.jpg"
            obj.color = (1, 1, 1, 1)
            self.add_widget(self.context_menu)
            self.context_menu.pos = obj.pos[0]+ obj.width, obj.pos[1]
       
    def  on_control(self, obj, control_id,*l):
        if control_id == "start":
            print "play button pressed"
        elif control_id == "pause":
            print "pause button pressed"
        elif control_id =="complete":
            print "Task Copleted"
            print self.context_menu.ids
            for button in self.context_menu.children[1].children[0].children[0].children[0].children[0].children:
                if button.text == text:
                    button.background_normal = "button_normal_cmenu_c.jpg"
                    button.background_down = 'button_normal_cmenu_c.jpg'

        else:
            print "stopped"

    def on_select_task(self,task_id):
        print task_id
        if task_id=='11':
            self.ids['label'].text = "A. Gross Motor"
        elif task_id=='12':
            self.ids['label'].text = "aaaaaaaaa"
        elif task_id=='13':
            self.ids['label'].text = "dddddddddddd"
        elif task_id=='14':
            self.ids['label'].text = "xxxxxxxxxxx"
        elif task_id=='15':
            self.ids['label'].text = "cccccccccccc"

class MyApp(App):
    def build(self):
        return MainMenu()


if __name__ == '__main__':
    MyApp().run()