from tkinter import *
root= Tk()

import RPi.GPIO as GPIO

# Define Buttons
Button1_PIN = 11
Button2_PIN = 13
Button3_PIN = 15
Button4_PIN = 29
Button5_PIN = 31
Button6_PIN = 37
Button7_PIN = 16
Button8_PIN = 18


#Set up the GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Button1_PIN, GPIO.OUT)
GPIO.setup(Button2_PIN, GPIO.OUT)
GPIO.setup(Button3_PIN, GPIO.OUT)
GPIO.setup(Button4_PIN, GPIO.OUT)
GPIO.setup(Button5_PIN, GPIO.OUT)
GPIO.setup(Button6_PIN, GPIO.OUT)
GPIO.setup(Button7_PIN, GPIO.OUT)
GPIO.setup(Button8_PIN, GPIO.OUT)



#GPIO.output(Button1,FALSE)
#GPIO.output(in2,FALSE)



#define grid
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)

#Creating a label widget
Button1 = Button(root,text="HEADLIGHT", padx=30,pady=64, activebackground="green", 
font=("Sans medium", 24),relief="raised", fg="white", bg="blue", bd="6", highlightcolor="black")
Button2 = Button(root,text="TAILLIGHTS", padx=30,pady=64, activebackground="green", 
font=("Sans medium", 24),relief="raised", fg="white", bg="blue", bd="6", highlightcolor="black")
Button3 = Button(root,text="OFFROAD LIGHTs", padx=30,pady="47", activebackground="green", 
font=("Sans medium", 24),relief="raised", fg="white", bg="blue", bd="6", highlightcolor="black", wraplength="160")
Button4 = Button(root,text="ROCK LIGHTS", padx=30,pady="50", activebackground="green", 
font=("Sans medium", 24),relief="raised", fg="white", bg="blue", bd="6", highlightcolor="black", wraplength="160")
Button5 = Button(root,text="START", padx=60,pady=70, activebackground="green", 
font=("Sans medium", 24),relief="raised", fg="white", bg="blue", bd="6", highlightcolor="black")
Button6 = Button(root,text="INTERIOR LIGHTS", padx=30,pady="50", activebackground="green", 
font=("Sans medium", 24),relief="raised", fg="white", bg="blue", bd="6", highlightcolor="black", wraplength="160")
Button7 = Button(root,text="STEREO", padx=30,pady=64, activebackground="green", 
font=("Sans medium", 24),relief="raised", fg="white", bg="blue", bd="6", highlightcolor="black")
Button8 = Button(root,text="DOME LIGHT", padx=30,pady="50", activebackground="green", 
font=("Sans medium", 24),relief="raised", fg="white", bg="blue", bd="6", highlightcolor="black", wraplength="160")

#shoving it onto the screen
Button1.grid(row=0,column=0)
Button2.grid(row=0,column=1)
Button3.grid(row=0,column=2)
Button4.grid(row=0,column=3)
Button5.grid(row=1,column=0)
Button6.grid(row=1,column=1)
Button7.grid(row=1,column=2)
Button8.grid(row=1,column=3)

root.mainloop()