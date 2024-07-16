from tkinter import *
import tkinter as tk
from tkinter import messagebox, filedialog
import os

# PdfViewer
from tkPDFViewer import tkPDFViewer as pdf

# ScreenShot
import pyautogui

# textToSpeech
from tkinter.ttk import Combobox
import pyttsx3


# yttube
from pytube import YouTube
import customtkinter

# writeboard
from tkinter import ttk
from tkinter.colorchooser import askcolor

# clock
from time import strftime

#calendar
from tkcalendar import *

# import platform
# import psutil

root=Tk()
root.title(" Study Tools")
root.geometry("850x500+520+250")
root.resizable(False,False)
root.configure(bg='#292e2e') 

# Main Window

image_icon=PhotoImage(file="E:\\PythonGUI\\Icons\\book (4).png")
root.iconphoto(False,image_icon)

Body=Frame(root,width=900,height=600,bg='#d6d6d6')
Body.pack(pady=20,padx=20)

LHSP1=Frame(Body,width=220,height=80,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
LHSP1.place(x=10,y=10)

LHSP2=Frame(Body,width=220,height=220,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
LHSP2.place(x=10,y=100)

LHSP3=Frame(Body,width=350,height=60,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
LHSP3.place(x=10,y=390)

#------------------------

MIDP1=Frame(Body,width=225,height=80,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
MIDP1.place(x=240,y=10)

MIDP2=Frame(Body,width=225,height=220,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
MIDP2.place(x=240,y=100)

# MIDP3=Frame(Body,width=225,height=100,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
# MIDP3.place(x=240,y=350)

#-------------------------

RHSP1=Frame(Body,width=220,height=80,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
RHSP1.place(x=475,y=10)

RHSP2=Frame(Body,width=220,height=220,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
RHSP2.place(x=475,y=100)

# RHSP3=Frame(Body,width=220,height=100,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
# RHSP3.place(x=475,y=350)

#-------------------------

EHSP1=Frame(Body,width = 95,height=350,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
EHSP1.place(x=705,y=10)

EHSP2=Frame(Body,width = 95,height=80,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
EHSP2.place(x=705,y=370)

# LHS=Frame(Body,width=290,height=115,bg="#d6d6d6",highlightbackground="#adacb1",highlightthickness=1)
# LHS.place(x=15,y=15)

# Notepad - app1

def notepad():
    app1 = Toplevel()
    app1.title("Untitled - Notepad")
    app1.geometry("700x700")
    file = None

    image_icon = PhotoImage(file = "E:\\PythonGUI\\Icons\\026-notepad.png")
    app1.iconphoto(False, image_icon)
    
    def notepad():
        
        global textArea
        
        #default theme
        textArea = Text(app1, wrap = WORD,fg = "black", bg = "white", insertbackground = "black")
        textArea.pack(expand = TRUE, fill = BOTH)
        
        # textArea = Text(root)
        # textArea.grid(sticky = N + E + S + W)
        
        menuBar = Menu(app1)
        app1.config(menu = menuBar)
        
        fileMenu = Menu(menuBar, tearoff = 0)
        fileMenu.add_command(label = "New", command = newFile)
        fileMenu.add_command(label = "Open", command = openFile)
        fileMenu.add_command(label = "Save", command = saveFile)
        fileMenu.add_separator()
        fileMenu.add_command(label = "Exit", command = exit)
        menuBar.add_cascade(label = "File", menu = fileMenu)
        
        editMenu = Menu(menuBar, tearoff = 0)
        editMenu.add_command(label = "Cut", command = cut)
        editMenu.add_command(label = "Copy", command = copy )
        editMenu.add_command(label = "Paste", command = paste )
        menuBar.add_cascade(label = "Edit", menu = editMenu)
        
        helpMenu = Menu(menuBar, tearoff = 0)
        helpMenu.add_command(label = "About Notepad", command = help )
        menuBar.add_cascade(label = "Help", menu = helpMenu)
        
        # themeMenu = Menu(menuBar, tearoff = 0)
        # themeMenu.add_command(label = "Dark", command = darkTheme)
        # themeMenu.add_command(label = "Light", command = None)
        # menuBar.add_cascade(label = "Theme", menu = themeMenu)
        
    def newFile():
        global textArea
        app1.title()("Untitled - Notepad")
        file = None
        textArea.delete(1.0, END)

    def openFile():
        global textArea
        file = filedialog.askopenfile(defaultextension = ".txt", filetypes = [("All files", "*.*"), ("Text Document", "*.txt")])
        file = file.name
        
        if file == "":
            file = None
        else:
            app1.title(os.path.basename(file) + " - Notepad")
            textArea.delete(1.0, END)
            file = open(file, "rb")
            textArea.insert(1.0, file.read())
            file.close()
            
    def saveFile():
        global textArea, file
        if file == None:
            file = filedialog.asksaveasfilename(initialfile = "Untitled.txt", defaultextension = ".txt", filetypes = [("All files", "*.*"), ("Text Document", "*.txt")])
            
            if file == None:
                file = None
            else:
                file = open(file, "w")
                file.write(textArea.get(1.0, END))
                file.close()
                file = file.name
                app1.title(os.path.basename(file) + " - Notepad")
            
        else:
            file = open(file, "w")
            file.write(textArea.get(1.0, END))
            file.close()
            
    def exit():
        app1.destroy()
        
    def cut():
        global textArea
        textArea.event_generate("<<Cut>>")
        
    def copy():
        global textArea
        textArea.event_generate("<<Copy>>")
        
    def paste():
        global textArea
        textArea.event_generate("<<Paste>>")
        
    def help():
        messagebox.showinfo("Notepad", "This simple Notepad is developed by Latracal Solutions!")
        
    # def darkTheme():
    #     global textArea
    #     textArea = Text(app1, wrap = WORD,fg = "white", bg = "#292e2e", font = ("Candara", 15, "bold"), insertbackground = "white")
    #     textArea.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH)
        

    notepad()

    app1.mainloop()

#-----------------------------------------------


# Clock - app2

def clock():
    app2=Toplevel()
    app2.geometry("850x110+300+10")
    app2.title('Clock')
    app2.configure(bg='#292e2e')
    app2.resizable(False,False)

    image_icon=PhotoImage(file="E:\\PythonGUI\\Icons\\001-clock - Copy.png")
    app2.iconphoto(False,image_icon)

    def clock():
        text=strftime('%H:%M:%S %p')
        lbl.config(text=text)
        lbl.after(1000,clock)

    lbl=Label(app2,font=('Segoe UI',38,'bold'),width=21, bg='#f4f5f5',fg='#292e2e')
    lbl.pack(anchor='center',pady=20)
    clock()


    app2.mainloop()

#-------------------------------------------

# Calender - app3

def calendar():
    app3=Toplevel()
    app3.geometry("300x250+10+10")
    app3.title('Calendar')
    app3.configure(bg="#292e2e")
    app3.resizable(False,False)

    image_icon=PhotoImage(file="E:\\PythonGUI\\Icons\\001-calendar.png")
    app3.iconphoto(False,image_icon)

    mycal=Calendar(app3,setmode='day',date_pattern='d/m/yy')
    mycal.pack(padx=15,pady=35)

    app3.mainloop()
    
#--------------------------------------------

# WriteBoard - app4

def writeBoard():
    app4 = Toplevel()
    app4.title("Write Board")
    app4.geometry("700x580+150+50")
    app4.config(bg = "#f2f3f5")
    app4.resizable(False, False)

    current_x = 0
    current_y = 0
    color = "black"

    def locate_xy(work):
        
        global current_x, current_y
        
        current_x = work.x 
        current_y = work.y
        
    def addLine(work):
        
        global current_x, current_y
        
        canvas.create_line((current_x, current_y, work.x, work.y),width = get_current_value(), fill = color, capstyle = ROUND, smooth = TRUE)
        current_x, current_y = work.x, work.y 

    def show_color(new_color):
        
        global color
        
        color = new_color
        
    def new_canvas():
        
        canvas.delete("all")
        display_palatte()
        
        
    #icon
    image_icon = PhotoImage(file = "E:\\PythonGUI\\Icons\\008-blackboard.png")
    app4.iconphoto(False, image_icon)

    eraser = PhotoImage(file = "E:\\PythonGUI\\Icons\\eraser (1).png")
    Button(app4, image = eraser, bg = "#f2f3f5", command = new_canvas, bd = 0).place(x = 8, y = 340)

    colors = Canvas(app4, bg = "#ffffff", width = 80, height = 320, bd = 0)
    colors.place(x = 10, y = 10)

    def display_palatte():
        id = colors.create_rectangle((10, 10, 30, 30), fill = "black")
        colors.tag_bind(id, "<Button-1>", lambda X: show_color("black"))
        
        id = colors.create_rectangle((10, 40, 30, 60), fill = "gray")
        colors.tag_bind(id, "<Button-1>", lambda X: show_color("gray"))
        
        id = colors.create_rectangle((10, 70, 30, 90), fill = "brown4")
        colors.tag_bind(id, "<Button-1>", lambda X: show_color("brown4"))
        
        id = colors.create_rectangle((10, 100, 30, 120), fill = "red")
        colors.tag_bind(id, "<Button-1>", lambda X: show_color("red"))
        
        id = colors.create_rectangle((10, 130, 30, 150), fill = "orange")
        colors.tag_bind(id, "<Button-1>", lambda X: show_color("orange"))
        
        id = colors.create_rectangle((10, 160, 30, 180), fill = "yellow")
        colors.tag_bind(id, "<Button-1>", lambda X: show_color("yellow"))
        
        id = colors.create_rectangle((10, 190, 30, 210), fill = "green")
        colors.tag_bind(id, "<Button-1>", lambda X: show_color("green"))
        
        id = colors.create_rectangle((10, 220, 30, 240), fill = "blue")
        colors.tag_bind(id, "<Button-1>", lambda X: show_color("blue"))
        
        id = colors.create_rectangle((10, 250, 30, 270), fill = "purple")
        colors.tag_bind(id, "<Button-1>", lambda X: show_color("purple"))
        
    display_palatte()

    canvas = Canvas(app4, width = 585, height = 500, background = "white", cursor = "hand2")
    canvas.place(x = 100, y = 10)

    canvas.bind("<Button-1>", locate_xy)
    canvas.bind("<B1-Motion>", addLine)

    #--------------slider--------------#

    current_value = tk.DoubleVar()

    def get_current_value():
        return "{: .2f}".format(current_value.get())

    def slider_changed(event):
        value_label.configure(text = get_current_value())

    slider = ttk.Scale(app4, from_ = 0, to = 100, orient = "horizontal", command = slider_changed, variable = current_value)
    slider.place(x =570, y = 530)

    #value label
    value_label = ttk.Label(app4, text = get_current_value())
    value_label.place(x = 565, y = 555) 
    
    sliderLabel = Label(app4, text = "Thickness") 
    sliderLabel.place(x = 606, y = 553) 
    
    # Color Palatte Labels
    
    l1 = Label(app4, text = "Black", font = "arial 8")
    l1.place(x = 47, y = 18)
    
    l2 = Label(app4, text = "Grey", font = "arial 8") 
    l2.place(x = 47, y = 48)
    
    l3 = Label(app4, text = "Brown", font = "arial 8") 
    l3.place(x = 47, y = 78)
    
    l4 = Label(app4, text = "Red", font = "arial 8") 
    l4.place(x = 47, y = 108)
    
    l5 = Label(app4, text = "Orange", font = "arial 8") 
    l5.place(x = 47, y = 138)
    
    l6 = Label(app4, text = "Yellow", font = "arial 8") 
    l6.place(x = 47, y = 168)
    
    l7 = Label(app4, text = "Green", font = "arial 8" )
    l7.place(x = 47, y = 198)
    
    l8 = Label(app4, text = "Blue", font = "arial 8")
    l8.place(x = 47, y = 228)
    
    l9 = Label(app4, text = "Violet", font = "arial 8") 
    l9.place(x = 47, y = 258)
    
    l10 = Label(app4, text = "COLOR", font = "arial 8 bold") 
    l10.place(x = 20, y = 288)
    
    l3 = Label(app4, text = "PALETTE", font = "arial 8 bold") 
    l3.place(x = 20, y = 305)
    
    # l3 = Label(app4, text = "ERASER", font = "arial 8 bold") 
    # l3.place(x = 20, y = 430)


    app4.mainloop()

#--------------------------------------------

# YTDownloader - app5

def YTDownloader():

    
    # Our app frame

    app5 = Toplevel()
    app5.geometry("300x290")
    app5.title("YouTube")
    app5.configure(bg = "red")
    app5.resizable(False, False)

    # Set the window title logo

    app5_icon = "E:\\PythonGUI\\Icons\\001-youtube.png"
    app5.iconbitmap(app5_icon)

    image_icon = PhotoImage(file = "E:\\PythonGUI\\Icons\\001-youtube.png")
    app5.iconphoto(False, image_icon)

    # creating download function
    
    def startDownload(option):
        try:
            ytLink = link.get()
            ytObject = YouTube(ytLink, on_progress_callback = on_progress)
            if option == "highQuality":
                video = ytObject.streams.get_highest_resolution()
            elif option == "lowQuality":
                video = ytObject.streams.get_lowest_resolution()
            elif option == "audio":
                video = ytObject.streams.get_audio_only()
            else:
                return
            
            title.configure(text = ytObject.title, text_color = "black")
            finishLabel.configure(text = "")
            video.download()
            finishLabel.configure(text = "", text_color = "green")
            
        except:
            finishLabel.configure(text = "", text_color = "red")
            
    # Progress bar function

    def on_progress(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_download = total_size - bytes_remaining
        percentage_of_completion = bytes_download / total_size * 100
        per = str(int(percentage_of_completion))
        progress.configure(text = per + "%")
        progress.update()
        
        #update Progress bar
        
        progressbar.set(float(percentage_of_completion) / 100)
        
    # System Settings
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("blue")


    # Adding UI elements

    title = customtkinter.CTkLabel(app5, text = "Insert a YouTube Link", width = 200, height = 50, text_color = "white", font = ("Segoe UI", 20))
    title.pack(padx = 10, pady = 10)

    # Link input

    url_var = tk.StringVar()
    link = customtkinter.CTkEntry(app5, width = 220, height = 40, textvariable = url_var)
    link.pack()

    # Finished Downloading
    finishLabel = customtkinter.CTkLabel(app5, text = "")
    finishLabel.pack()

    # Progress Percentage
    progress = customtkinter.CTkLabel(app5, text = "0%", text_color = "black")
    progress.place(x = 120, y = 120)

    # ProgressBar

    progressbar = customtkinter.CTkProgressBar(app5, width = 215)
    progressbar.set(0)
    progressbar.pack(padx = 10, pady = 10)

    # Download High Quality Video Button

    download_hq = customtkinter.CTkButton(app5, text = "Download High Quality-Mp4", text_color = "white", command = lambda : startDownload("highQuality"))
    download_hq.pack(padx = 10, pady = 10)

    # Download Low Quality Video Buttton

    download_lq = customtkinter.CTkButton(app5, text = "Download Low Quality-Mp4", command = startDownload("lowQuality"))
    download_lq.pack(padx = 10, pady = 10) 

    # Download Audio Button 
    download_audio = customtkinter.CTkButton(app5, text = "Download Mp3", command = lambda: startDownload("audio"))
    download_audio.pack(padx = 10, pady = 10)


    # Run our App

    app5.mainloop()

#--------------------------------------------

# textToSpeech - app6

def textToSpeech():
    
    app6 = Toplevel()
    app6.title("Text to Speech")
    app6.geometry("900x450+200+200")
    app6.resizable(False,False)
    app6.configure(bg = "#305065")



    engine = pyttsx3.init()

    def speakNow():
        text = text_area.get(1.0, END)
        gender = gender_combobox.get()
        speed = speed_combobox.get()
        voices = engine.getProperty("voices")
        
        def setvoice():
            if(gender == "Male"):
                engine.setProperty("voice", voices[0].id)
                engine.say(text)
                engine.runAndWait()
            else:
                engine.setProperty("voice",voices[1].id)
                engine.say(text)
                engine.runAndWait()
                
        if(text):
            if(speed == "Fast"):
                engine.setProperty("rate", 250)
                setvoice()
            elif(speed == "Normal"):
                engine.setProperty("rate", 150)
                setvoice()
            else:
                engine.setProperty("rate", 60)
                setvoice()
                
    def download():
        print()
        
    #icon
    image_icon = PhotoImage(file = "E:\\PythonGUI\\Icons\\005-text-to-speech-1.png")
    app6.iconphoto(False, image_icon)

    #Top frame
    Top_frame = Frame(app6, bg = "white", width = 900, height = 100)
    Top_frame.place(x = 0, y = 0)

    Logo = PhotoImage(file = "speaker.png")
    Label(Top_frame, image = Logo, bg = "white").place(x = 10, y = 5)

    Label(Top_frame, text = "TEXT TO SPEECH", font = "arial 20 bold", bg = "white", fg = "black").place(x = 100, y = 30)

    #############

    text_area = Text(app6, font = "Roboto 20", bg = "white", relief = GROOVE, wrap = WORD)
    text_area.place(x = 10, y = 150, width = 500, height = 250)

    Label(app6, text = "VOICE", font = "arial 15 bold", bg = "#305065", fg = "white").place(x = 580, y = 160)
    Label(app6, text = "SPEED", font = "arial 15 bold", bg = "#305065", fg = "white").place(x = 760, y = 160)

    gender_combobox = Combobox(app6, values = ["Male", "Female"], font = "arial 14", state = "r", width = 10)
    gender_combobox.place(x = 550, y = 200)
    gender_combobox.set("Male")

    speed_combobox = Combobox(app6, values = ["Fast", "Normal", "Slow"], font = "arial 14", state = "r", width = 10)
    speed_combobox.place(x = 730, y = 200)
    speed_combobox.set("Normal")

    image_icon = PhotoImage(file = "Speak.png")
    btn = Button(app6, text = "Speak", compound = LEFT, image = image_icon, width = 130, font = "arial 14 bold", command = speakNow)
    btn.place(x = 550, y = 280)

    image_icon2 = PhotoImage(file = "download.png")
    save = Button(app6, text = "Speak", compound = LEFT, image = image_icon2, width = 130, bg = "#39c790", font = "arial 14 bold", command = download)
    save.place(x = 730, y = 280)

    app6.mainloop()
#--------------------------------------------

# ScreenShot - app7

def screenshot():
    root.iconify()

    myScreenshot=pyautogui.screenshot()
    file_path=filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)

# ScreenShot - app7

# def screenShot():
    # app7 = Toplevel()
    # # app7 = Tk()
    # # app7.geometry("250x250")
    # app7.title('ScreenShot')
    # # app7.configure(bg='#f4f5f5')
    # app7.resizable()

    # image_icon = PhotoImage(file = "E:\\PythonGUI\\Icons\\036-screenshot-1.png")
    # app7.iconphoto(False, image_icon)
    

    # def screenShot():
    #     myScreenshot = pyautogui.screenshot()
    #     file_path = filedialog.asksaveasfilename(defaultextension = ".png")
    #     myScreenshot.save(file_path)
        
    # canvas1 = Canvas(app7, width = 300, height = 300)
    # canvas1.pack()
    
    # myButton = Button(text = "Take Screenshot", command = screenShot, bg = "black", fg = "white", font = 10)
    # myButton.pack(padx = 10, pady = 10)
    # # canvas1.create_window(150, 150, window = myButton)


    # app7.mainloop()
    
#--------------------------------------------

# PdfViewer

def pdfViewer():

    app8 = Toplevel()
    app8.geometry("700x700+400+100")
    app8.title("PDF Viewer")
    app8.configure(bg = "white")
    app8.resizable(False, False)
    
    openFrame=Frame(app8,width=580,height=80,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
    openFrame.place(x=12,y=10)

    # main part of the program 

    def browseFiles():
        filename = filedialog.askopenfilename(initialdir = os.getcwd(), title = "select pdf file", filetypes = (("PDF File", ".pdf"),("PDF File", ".PDF"), ("All file", ".txt")))
        
        v1 = pdf.ShowPdf()
        v2 = v1.pdf_view(app8, pdf_location = open(filename, "r"), width = 77, height = 100)
        v2.pack(pady = (0, 0))

    openButton = Button(openFrame, text = "Browse", command = browseFiles, width = 34, font = "arial 20", bd = 1)
    openButton.pack(padx = 9, pady = 8)

    image_icon = PhotoImage(file = "E:\\PythonGUI\\Icons\\023-file.png")
    app8.iconphoto(False, image_icon)


    app8.mainloop()
    
# from tkinter import *
# from tkinter import filedialog
# from tkPDFViewer import tkPDFViewer as pdf
# import os

# # initializing tk

# root = Tk()
# root.geometry("600x700+400+100")
# root.title("PDF Viewer")
# root.configure(bg = "white")

# LHSP1=Frame(root,width=580,height=80,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
# LHSP1.place(x=12,y=10)

# # main part of the program 

# def browseFiles():
#     filename = filedialog.askopenfilename(initialdir = os.getcwd(), title = "select pdf file", filetypes = (("PDF File", ".pdf"),("PDF File", ".PDF"), ("All file", ".txt")))
    
#     v1 = pdf.ShowPdf()
#     v2 = v1.pdf_view(root, pdf_location = open(filename, "r"), width = 77, height = 100)
#     v2.pack(pady = (0, 0))



# openButton = Button(LHSP1, text = "OPEN A PDF FILE", command = browseFiles, width = 34, font = "arial 20", bd = 1)
# openButton.pack(padx = 10, pady = 10)

# image_icon = PhotoImage(file = "E:\\PythonGUI\\Icons\\023-file.png")
# root.iconphoto(False, image_icon)


# root.mainloop()
 
    
#--------------------------------------------

# switch mode


button_mode=True

def switchMode():
    global button_mode
    if button_mode:
        LHSP1.config(bg="#292e2e")
        # myimage.config(bg='#292e2e')
        # l1.config(bg="#292e2e",fg="#d6d6d6")
        # l2.config(bg="#292e2e",fg="#d6d6d6")
        # l3.config(bg="#292e2e",fg="#d6d6d6")
        # l4.config(bg="#292e2e",fg="#d6d6d6")
        # l5.config(bg="#292e2e",fg="#d6d6d6")
        # l6.config(bg="#292e2e",fg="#d6d6d6")

        RHB.config(bg="#292e2e")
        app1.config(bg="#292e2e")
        app2.config(bg="#292e2e")
        app3.config(bg="#292e2e")
        app4.config(bg="#292e2e")
        app5.config(bg="#292e2e")
        app6.config(bg="#292e2e")
        app7.config(bg="#292e2e")
        app8.config(bg="#292e2e")
        app9.config(bg="#292e2e")
        apps.config(bg="#292e2e",fg="#d6d6d6")


        button_mode=False
    else:
        LHSP1.config(bg="#f4f5f5")
        # myimage.config(bg="#f4f5f5")
        # l1.config(bg="#f4f5f5",fg="#292e2e")
        # l2.config(bg="#f4f5f5",fg="#292e2e")
        # l3.config(bg="#f4f5f5",fg="#292e2e")
        # l4.config(bg="#f4f5f5",fg="#292e2e")
        # l5.config(bg="#f4f5f5",fg="#292e2e")
        # l6.config(bg="#f4f5f5",fg="#292e2e")

        RHB.config(bg="#f4f5f5")
        app1.config(bg="#f4f5f5")
        app2.config(bg="#f4f5f5")
        app3.config(bg="#f4f5f5")
        app4.config(bg="#f4f5f5")
        app5.config(bg="#f4f5f5")
        app6.config(bg="#f4f5f5")
        app7.config(bg="#f4f5f5")
        app8.config(bg="#f4f5f5")
        app9.config(bg="#f4f5f5")
        apps.config(bg="#f4f5f5",fg="#292e2e")


        button_mode=True    

    
#--------------------------------------------

    
# RHB=Frame(Body,width=400,height=150,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
# RHB.place(x=330,y=255)

# apps=Label(RHB,text='Apps',font=('Arial Rounded MT Bold',15),bg='#f4f5f5')
# apps.place(x=10,y=10)
    
app1_image=PhotoImage(file="E:\\PythonGUI\\Icons\\032-note.png")
app1=Button(LHSP1,image=app1_image,bd=0,command=notepad)
app1.place(x=8,y=5)

app1l=Label(LHSP1,text='NOTEPAD',font=('Arial Rounded MT Bold',6),bg='#f4f5f5')
app1l.place(x=4,y=60)

app1l2=Label(LHSP1,text='Notepad is a simple text editor.\nIt creates and edits plain text   \ndocuments (bearing the ".txt"  \n filename extension) and               \ncompatible formats.                     ',font=('Arial Rounded MT Bold',5),bg='#f4f5f5')
app1l2.place(x=70,y=10)

app2_image=PhotoImage(file="E:\\PythonGUI\\Icons\\002-deadline.png")
app2=Button(EHSP1,image=app2_image,bd=0,command=clock)
app2.place(x=20,y=10)

app2l=Label(EHSP1,text='CLOCK',font=('Arial Rounded MT Bold',6),bg='#f4f5f5')
app2l.place(x=25,y=70)

app3_image=PhotoImage(file="E:\\PythonGUI\\Icons\\004-calendar-3.png")
app3=Button(EHSP1,image=app3_image,bd=0,command=calendar)
app3.place(x=22,y=95)

app3l=Label(EHSP1,text='CALENDAR',font=('Arial Rounded MT Bold',6),bg='#f4f5f5')
app3l.place(x=15,y=150)

app4_image=PhotoImage(file="E:\\PythonGUI\\Icons\\005-blackboard-1.png")
app4=Button(RHSP1,image=app4_image,bd=0,command=writeBoard)
app4.place(x=13,y=5)

app4l=Label(RHSP1,text='WRITEBOA..',font=('Arial Rounded MT Bold',6),bg='#f4f5f5')
app4l.place(x=10,y=60)

app4l2=Label(RHSP1,text='WriteBoard - Stylus is a digital     \nnote-taking app that allows you  \nto write, draw, and sketch using\na stylus with near-zero latency    \n in performance.                                 ',font=('Arial Rounded MT Bold',5),bg='#f4f5f5')
app4l2.place(x=75,y=10)

app5_image=PhotoImage(file="E:\\PythonGUI\\Icons\\001-youtube.png")
app5=Button(LHSP3,image=app5_image,bd=0,command=YTDownloader)
app5.place(x=10, y = 2)

app5l=Label(LHSP3,text='YT VIDEO  \nDOWNLO..',font=('Arial Rounded MT Bold',6),bg='#f4f5f5')
app5l.place(x=70,y=9)

app5l2=Label(LHSP3,text='Download YouTube videos in high quality with\nour free online YouTube to MP4 converter.    \nTry now — fast &easy!YouTube downloader.  ',font=('Arial Rounded MT Bold',5),bg='#f4f5f5')
app5l2.place(x=135,y=8)

app6_image=PhotoImage(file="E:\\PythonGUI\\Icons\\005-text-to-speech-1.png")
app6=Button(EHSP2,image=app6_image,bd=0,command=textToSpeech)
app6.place(x=5,y=7)

app6l=Label(EHSP2,text='TEXT  \nTO      \nSPEE..',font=('Arial Rounded MT Bold',5),bg='#f4f5f5')
app6l.place(x=58,y=12)

app6l2=Label(EHSP2,text='CONVERTOR',font=('Arial Rounded MT Bold',6),bg='#f4f5f5')
app6l2.place(x=10,y=60)

app7_image=PhotoImage(file="E:\\PythonGUI\\Icons\\034-screenshot.png")
app7=Button(EHSP1,image=app7_image,bd=0,command=screenshot)
app7.place(x=20,y=265)

app7l=Label(EHSP1,text='SCREENSHOT',font=('Arial Rounded MT Bold',6),bg='#f4f5f5')
app7l.place(x=8,y=325)

app8_image=PhotoImage(file="E:\\PythonGUI\\Icons\\023-file.png")
app8=Button(MIDP1,image=app8_image,bd=0,command=pdfViewer)
app8.place(x=8,y=5)

app8l=Label(MIDP1,text='PDF VIEW..',font=('Arial Rounded MT Bold',6),bg='#f4f5f5')
app8l.place(x=8,y=60)

app8l2=Label(MIDP1,text='A PDF viewer is an application    \nthat helps the user view PDF        \nfiles or add annotations to them.\nPDF viewers only allow viewing   \nor opening the existing PDF.        ',font=('Arial Rounded MT Bold',5),bg='#f4f5f5')
app8l2.place(x=75,y=10)

app9_image=PhotoImage(file="E:\\PythonGUI\\Icons\\021-day-and-night-3.png")
app9=Button(EHSP1,image=app9_image,bd=0)
app9.place(x=20,y=175)

app9l=Label(EHSP1,text='SWITCHMODE',font=('Arial Rounded MT Bold',6),bg='#f4f5f5')
app9l.place(x=10,y=235)

# App ScreenSHot as an image

notepadSS_image=PhotoImage(file="E:\\PythonGUI\\Icons\\notepadSS - Copy.png")
notepadSS=Button(LHSP2,image=notepadSS_image,bd=0)
notepadSS.place(x=5,y=5)

pdfviewerSS_image=PhotoImage(file="E:\\PythonGUI\\Icons\\PdfSS - Copy.png")
pdfviewerSS=Button(MIDP2,image=pdfviewerSS_image,bd=0)
pdfviewerSS.place(x=10,y=5)

writeBoardSS_image=PhotoImage(file="E:\\PythonGUI\\Icons\\whiteBoardFinalss200px.png")
writeBoardSS=Button(RHSP2,image=writeBoardSS_image,bd=0)
writeBoardSS.place(x=10,y=5)




root.mainloop()
