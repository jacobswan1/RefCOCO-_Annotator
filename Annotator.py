import os
import pickle
import numpy as np
from tkinter import *
from PIL import ImageTk,Image  



class MainWindow():

    def __init__(self, main, root, image_list):
        
        # Program stop listener goes here
        def on_closing():
            save_annotations()
            print('Total annotated:', len(self.result))
            print('To be annotated:', len(self.image_dict.keys()))
            main.destroy()
        
        # Result saver
        def save_annotations():
            with open('ca_annotations', 'wb') as fp:
                pickle.dump(self.result, fp)
            with open('counterfactual_grounding', 'wb') as fp:
                pickle.dump(self.image_dict, fp)
        
        # Load previous annotations
        def load_annotations():
            if os.path.exists('ca_annotations'):
                with open ('ca_annotations', 'rb') as fp:
                    result = pickle.load(fp)
                return result
            else:
                return {}
        
        main.protocol("WM_DELETE_WINDOW", on_closing)

        # Canvas for image
        self.canvas = Canvas(main, width=400, height=400)
        self.canvas.grid(row=0, column=0, rowspan=20, columnspan=1, )
        
        self.image_keys = list(image_list.keys())
        self.image_dict = image_list
        
        # Loading images
        self.my_images = []
        for item in image_list.keys():
            self.my_images.append(ImageTk.PhotoImage(Image.open(
                os.path.join(root, item)).resize((400, 400))))
            
        self.my_image_number = 0

        # Set first image on canvas
        self.image_on_canvas = self.canvas.create_image(
            20, 20, anchor = NW, image = self.my_images[self.my_image_number])

        # button to change image
        self.button = Button(main, text="NEXT", command=self.onButton)
        self.button.grid(row=1, column=0)

        MODES = [
            ("Man", "1"),("Woman", "1"),("Boy", "1"),("Girl", "1"),
            ("black", "1"),("blue", "1"),("brown", "1"),("green", "1"),("grey", "1"),("orange", "1"),
            ("pink", "1"),("purple", "1"),("red", "1"),("white", "1"),("yellow", "1")
        ]
        
        # Store all var and checkbox objects, and final annotations
        checkbox_list = []
        var_list = []
        result = load_annotations()
        
        # Creating checkbox groups
        count = 0
        for text, mode in MODES:
            var = StringVar()
            var.set(0) # initialize
            radio = Checkbutton(main, text=text, variable=var, font=2, 
                                     activebackground='blue', disabledforeground='red')
            radio.grid(row=count+1, column=2)
            checkbox_list.append(radio)
            var_list.append(var)
            count += 1
            
        self.checkbox_list = checkbox_list
        self.var_list = var_list
        self.result = result
        self.modes = MODES
        self.main = main
        

    def onButton(self):
        one_hot = np.zeros(len(self.modes))
        count = 0
        for var in self.var_list:
            if int(var.get()) == 1:
                one_hot[count] = 1
            count += 1
        print(one_hot)
        
        # Save new annotations and remove the annotated one from annotations
        self.result[self.image_keys[self.my_image_number]] = one_hot
        del self.image_dict[self.image_keys[self.my_image_number]]
        
        # New images
        self.my_image_number += 1
        
        # Extract the one_hot in original annotations
        one_hot = self.image_dict[self.image_keys[self.my_image_number]]    
        
        # Updata the checkbox selection according to the annotations
        for count, chb in enumerate(self.checkbox_list):
            if one_hot[count] == 1:
                chb.select()
            else:
                chb.deselect()
        # change image
        self.canvas.itemconfig(self.image_on_canvas,anchor=NW, image = self.my_images[self.my_image_number])


    def onBreakButton(self):
        # New images
        next_image()
        


image_root = '/media/drive1/Data/refer/data/images'
# Loading the image list and previous attributes in caption
with open ('counterfactual_grounding', 'rb') as fp:
    ca_annotation = pickle.load(fp, encoding='bytes')
    
root = Tk()
a = MainWindow(root, image_root, ca_annotation)
root.mainloop()
