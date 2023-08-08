# --------------------------------------------------
# importing the libraries and packages
# --------------------------------------------------

try:
    from tkinter import *
except:
    from Tkinter import *
from tkinter import messagebox
import cv2
import PIL.Image
import PIL.ImageTk
from tkinter import ttk
from keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array 
import tensorflow
import pyttsx3
engine = pyttsx3.init()
  
# This module is imported so that we can 
# play the converted audio
import os
# --------------------------------------------------------------------------------------------------
# Class that contains all the class variables and methods which are used to create user interface
# --------------------------------------------------------------------------------------------------


class SignLanguageDetector:

    # --------------------------------------------------
    # Initializing class variables and UI components
    # --------------------------------------------------

    # main window
    __window = Tk()

    # Logo for main window
    __photo = PhotoImage(file="img/LogoNew.png")
    __window.iconphoto(False, __photo)

    # Frames in the main window
    __canvas = Canvas(__window, width=450, height=400)
    __thisframe = Frame(__window, width=450, height=400,
                        highlightbackground='black', highlightthickness=1, bg='black')
    __canvas1 = Canvas(__thisframe, width=270, height=270, bg="black")

    # Progress bar
    __progress = ttk.Progressbar(
        __window, orient=HORIZONTAL, length=945, mode='determinate')

    # Label to display prediction
    __geslabel = Label(__thisframe, fg='yellow', bg='black',
                       font=('times new roman', 40, 'bold'))

    # Images used for button widgets
    __photo1 = PhotoImage(file=r"img/button_start.png")
    __photo2 = PhotoImage(file=r"img/button_adjust.png")
    __photo3 = PhotoImage(file=r"img/button_close.png")

    # ----------------------------------------------------------
    # Constructor method to initialize and place UI components
    # ----------------------------------------------------------

    def __init__(self):
        
        # Window properties
        self.__window.title('Sign Language Detector')
        self.__window.configure(bg='#F8B850')
        self.__window.geometry("990x560+0+0")
        self.__window.resizable(False, False)

        # Built-in device camera
        self.vid = cv2.VideoCapture(0)

        # Create a canvas that can fit the above video source size
        self.__canvas.grid(row=0, column=0, padx=20, pady=20)
        self.__thisframe.grid(row=0, column=1, padx=20)
        self.__canvas.grid_propagate(0)
        self.__thisframe.grid_propagate(0)
        self.__canvas1.grid_propagate(0)
        self.__geslabel.place(x=10, y=320)

        # initialize weight for running average
        self.aWeight = 0.5
        # initialize num of frames
        self.num_frames = 0

        self.run_once = 0
        self.bg = None

        # Load model from memory
        self.classifier = load_model('Trained_model.h5')

        # Buttons Used
        self.__b1 = Button(self.__window, text='Scan', image=self.__photo1,
                           bg='#F8B850', activebackground='#F8B850', bd=0, command=self.on_start)
        self.__b1.place(x=104, y=480)
        self.__b2 = Button(self.__window, text='Scan', image=self.__photo2,
                           bg='#F8B850', activebackground='#F8B850', bd=0, command=self.on_adjust)
        self.__b2.place(x=418, y=480)
        self.__b3 = Button(self.__window, text='Scan', image=self.__photo3,
                           bg='#F8B850', activebackground='#F8B850', bd=0, command=self.on_stop)
        self.__b3.place(x=749, y=480)

    # --------------------------------------------------
    # To find the running average over the background
    # --------------------------------------------------
    def run_avg(self, image, aWeight):
        """ To find the running average over the background. """

        # initialize the background
        if self.bg is None:
            self.bg = image.copy().astype("float")
            return

        # compute weighted average, accumulate it and update the background
        cv2.accumulateWeighted(image, self.bg, aWeight)

    # ---------------------------------------------
    # To segment the region of hand in the image
    # ---------------------------------------------
    def segment(self, image, threshold=25):
        """ To segment the region of hand in the image """
        # find the absolute difference between background and current frame
        diff = cv2.absdiff(self.bg.astype("uint8"), image)

        # threshold the diff image so that we get the foreground
        thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]

        # get the contours in the thresholded image
        (cnts, _) = cv2.findContours(thresholded.copy(),
                                     cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # return None, if no contours detected
        if len(cnts) == 0:
            return
        else:
            # based on contour area, get the maximum contour which is the hand
            segmented = max(cnts, key=cv2.contourArea)
            return (thresholded, segmented)

    # --------------------------------------------------
    # To predict the gesture
    # --------------------------------------------------
    def predictor(self):
        """ Depending on model loaded, prediction is made by checking array """
        import numpy as np
        from tensorflow.keras.utils import load_img, img_to_array
        test_image = tensorflow.keras.utils.load_img('1.png', target_size=(64, 64))
        test_image = tensorflow.keras.utils.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = self.classifier.predict(test_image)
        if result[0][0] == 1:
            engine.say("A")
            engine.runAndWait()
            return 'A'
        elif result[0][1] == 1:
            engine.say("B")
            engine.runAndWait()
            return 'B'
        elif result[0][2] == 1:
            engine.say("C")
            engine.runAndWait()
            return 'C'
        elif result[0][3] == 1:
            engine.say("D")
            engine.runAndWait()
            return 'D'
        elif result[0][4] == 1:
            engine.say("E")
            engine.runAndWait()
            return 'E'
        elif result[0][5] == 1:
            engine.say("F")
            engine.runAndWait()
            return 'F'
        elif result[0][6] == 1:
            engine.say("G")
            engine.runAndWait()
            return 'G'
        elif result[0][7] == 1:
            engine.say("H")
            engine.runAndWait()
            return 'H'
        elif result[0][8] == 1:
            engine.say("I")
            engine.runAndWait()
            return 'I'
        elif result[0][9] == 1:
            engine.say("J")
            engine.runAndWait()
            return 'J'
        elif result[0][10] == 1:
            engine.say("K")
            engine.runAndWait()
            return 'K'
        elif result[0][11] == 1:
            engine.say("L")
            engine.runAndWait()
            return 'L'
        elif result[0][12] == 1:
            engine.say("M")
            engine.runAndWait()
            return 'M'
        elif result[0][13] == 1:
            engine.say("N")
            engine.runAndWait()
            return 'N'
        elif result[0][14] == 1:
            engine.say("O")
            engine.runAndWait()
            return 'O'
        elif result[0][15] == 1:
            engine.say("hey victory")
            engine.runAndWait()
            return 'hey victory '
        elif result[0][16] == 1:
            engine.say("Punch")
            engine.runAndWait()
            return 'Punch'
        elif result[0][17] == 1:
            engine.say("Gud morning")
            engine.runAndWait()
            return 'Gud morning'
        elif result[0][18] == 1:
            engine.say("Hands up")
            engine.runAndWait()
            return 'Hands up'
        elif result[0][19] == 1:
            engine.say("T")
            engine.runAndWait()
            return 'T'
        elif result[0][20] == 1:
            engine.say("U")
            engine.runAndWait()
            return 'U'
        elif result[0][21] == 1:
            engine.say("Victory")
            engine.runAndWait()
            return 'Victory'
        elif result[0][22] == 1:
            engine.say("W")
            engine.runAndWait()
            return 'W'
        elif result[0][23] == 1:
            engine.say("X")
            engine.runAndWait()
            return 'X'
        elif result[0][24] == 1:
            engine.say("Hello How are you")
            engine.runAndWait()
            return 'Hello How are you'
        elif result[0][25] == 1:
            engine.say("good")
            engine.runAndWait()
            return 'good'
    
    # --------------------------------------------------
    # To destroy all windows on closing application 
    # --------------------------------------------------

    def on_closing(self):
        self.vid.release()
        cv2.destroyAllWindows()
        self.__window.destroy()
    
    # --------------------------------------------------
    # To start the application 
    # --------------------------------------------------

    def on_start(self):
        if self.run_once == 0:
            self.delay = 10
            self.__canvas1.grid(row=0, column=1, padx=174)
            self.__progress.place(x=20, y=440)
            self.update()
            self.run_once += 1
    
    # --------------------------------------------------
    # To ask user if he/she wants to quit application 
    # --------------------------------------------------

    def on_stop(self):
        if self.run_once > 0:
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.vid.release()
                cv2.destroyAllWindows()
                self.__window.destroy()

    # -------------------------------------------------------
    # To find the running average over the background again
    # -------------------------------------------------------

    def on_adjust(self):
        if self.run_once > 0:
            self.vid.release()
            self.num_frames = 0
            self.__progress['value'] = 0
            self.__progress.place(x=20, y=440)
            self.vid = cv2.VideoCapture(0)
    
    # -------------------------------------------------------
    # To update user interface continuously...
    # -------------------------------------------------------

    def update(self):
        """ To update user interface continuously... """
        # Get a frame from the video source
        ret, frame = self.vid.read()
        frame = cv2.flip(frame, 1)
        clone = frame.copy()
        top, right, bottom, left = 30, 170, 300, 440
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        if ret:
            img = clone
            roi = frame[top:bottom, right:left]
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (7, 7), 0)
            self.__geslabel['text'] = 'None' if self.num_frames > 30 else 'Loading...'
            if self.num_frames < 30:
                self.run_avg(gray, self.aWeight)
                self.__progress['value'] += self.num_frames

            else:
                # segment the hand region
                hand = self.segment(gray)
                if self.__progress.winfo_exists() == 1:
                    self.__progress.place_forget()

                # check whether hand region is segmented
                if hand is not None:
                    # if yes, unpack the thresholded image and
                    # segmented region
                    (thresholded, segmented) = hand

                    # draw the segmented region and display the frame
                    cv2.drawContours(
                        clone, [segmented + (right, top)], -1, (0, 0, 255))
                    cv2.imwrite('1.png', thresholded)
                    img1 = thresholded
                    self.photo1 = PIL.ImageTk.PhotoImage(
                        image=PIL.Image.fromarray(img1))
                    self.__canvas1.create_image(
                        0, 0, image=self.photo1, anchor=NW)
                    gesture = self.predictor()
                    self.__geslabel['text'] = gesture

            # draw the segmented hand
            cv2.rectangle(clone, (left, top), (right, bottom), (0, 255, 0), 2)

            # increment the number of frames
            self.num_frames += 1

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
            self.__canvas.create_image(0, 0, image=self.photo, anchor=NW)
        self.__window.after(self.delay, self.update)
    
    # -------------------------------------------------------
    # To run the application
    # -------------------------------------------------------

    def run(self):
        self.__window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.__window.mainloop()
        

detector = SignLanguageDetector()
detector.run()
