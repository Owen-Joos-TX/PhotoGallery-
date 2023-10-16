from kivy.app import App
from kivy.uix.screenmanager import Screen



images = ["dogs.png", "dogs2.png","dogs3.png"]
index = 0
class PhotoGalleryApp(App):
    pass


class Display(Screen):
    def displayImage(self):
        return images[index]


    def advanceImage(self):
        global index
        if index < len(images)-1:
            index +=1
        else:
            index = 0
        self.ids.image.source =self.displayImage()


    def subImage(self):
        global index
        if index < len(images)-1:
            index -=1
        else:
            index = 3
        self.ids.image.source =self.displayImage()









PhotoGalleryApp().run()