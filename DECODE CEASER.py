#----------------------------------------------------------
#IMPORTS
#----------------------------------------------------------
from tkinter import*
import tkinter as tk
from tkinter import font as tkFont
from tkinter import messagebox
import random
#----------------------------------------------------------
#CONSTANTS
#----------------------------------------------------------
root = Tk()
root.configure(bg="#00D5FF")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.title("Encode and Decode")
font1=tkFont.Font(family="Segoe UI",size="25")
font2=tkFont.Font(family="Agency FB",size="25")
font3=tkFont.Font(family="Segoe UI",size="15")
font4 = tkFont.Font(family="Segoe UI",size="30")
#----------------------------------------------------------
global state1,state2,shiftstate
state1 = False
state2 = False
shiftstate = False


#----------------------------------------------------------
#SUBPROGRAM
#----------------------------------------------------------
def e_ncode():
    global encode,uInput,ShiftNum,canvasButtons1
    #----------------------------------------------------------
    root.withdraw()
    encode=Toplevel()
    encode.geometry(f"{screen_width}x{screen_height}")
    encode.title("GAME")
    encode.configure(bg="#ffcd82")
    encode.update() 
    #----------------------------------------------------------
    canvasButtons1 = tk.Canvas(encode,bg="#cfaaf0",highlightthickness=2,highlightbackground="#cf98ff",bd=0)

    infoEncode = Label(encode, text = "To ENCODE:\n 1.Enter the text that need to be encoded\n 2.Enter the Shift Number choose Random\n 3.Click Ok",font=("Ariel", 20),bg="#ffcd82",fg="#0A5E6F", justify="left")
    infoEncode.place(x=50,y=25)
    uInput = Entry(encode,width="40",bg="#3f2908",fg="#00D5FF",borderwidth="5",font=font2,justify="center")
    uInput.place(x=460,y=650)
    buttonEok= Button(encode,text="OK",relief="raised",bd=2,width=10,height=1, padx=2,pady=5,command=lambda:Eok(), bg="#e6210b",fg="#FFFFFF",activebackground="#FFFFFF",activeforeground="#e6210b",font=(font1,15))
    buttonEok.place(x=700,y=710)
    ShiftNum  = Entry(encode,width="20",bg="#e0a1ff",fg="#00D5FF",borderwidth="5",font=(font2,30),justify="center")
    ShiftNum.place(x=530,y=590)
    RandShift = Button(encode,text="Random",relief="raised",bd=2,width=10,height=1, padx=2,pady=5,command=lambda:RandomShift(), bg="#9d0be6",fg="#FFFFFF",activebackground="#FFFFFF",activeforeground="#9d0be6",font=(font1,15))
    RandShift.place(x=700,y=470)
    menuButton = Button(encode,text="MENU", padx=10, pady=10,command=lambda:getstateE(), bg="#5788EB",fg="#000000",font=(font1,20))
    menuButton.place(x=1400,y=0) 
    
#---------------------------------------------------------- 
#----------------------------------------------------------
def d_ecode():
    global decode,uInput,canvasButtons2
    #----------------------------------------------------------
    root.withdraw()
    decode=Toplevel()
    decode.geometry(f"{screen_width}x{screen_height}")
    decode.title("GAME")
    decode.configure(bg="#ffcd82")
    decode.update() 
    #----------------------------------------------------------
    canvasButtons2 = tk.Canvas(decode,bg="#cfaaf0",highlightthickness=2,highlightbackground="#cf98ff",bd=0)

    infoDecode = Label(decode, text = "To DECODE:\n 1.Enter what you the text that need to be Decoded\n 3.Click Ok",font=("Ariel", 20),bg="#ffcd82",fg="#0A5E6F",justify="left")
    infoDecode.place(x=50,y=25)
    uInput = Entry(decode,width="40",bg="#3f2908",fg="#00D5FF",borderwidth="5",font=font2,justify="center")
    uInput.place(x=460,y=680)
    buttonDok= Button(decode,text="OK",relief="raised",bd=2,width=10,height=1, padx=2,pady=5,command=lambda:Dok(), bg="#e6210b",fg="#FFFFFF",activebackground="#FFFFFF",activeforeground="#e6210b",font=(font1,15))
    buttonDok.place(x=700,y=740)
    menuButton = Button(decode,text="MENU", padx=10, pady=10,command=lambda:getstateD(), bg="#5788EB",fg="#000000",font=(font1,20))
    menuButton.place(x=1400,y=0) 
    
# ------------------------------------------------------------
# ------------------------------------------------------------
def Eok():
    global userInput
    global num
    # ------------------------------------------------------------
    numx= ShiftNum.get()
    ShiftNum.delete(0,END)
    if len(numx)>0:
        num = int(numx)
        
    else:
        Valid3 = validationNoShift()
        if Valid3:
            num  = shiftBy
        else:
            tk.messagebox.showerror("Error", "\nThere need to be a number in the shift num or random need to be clicked")

    userInput = uInput.get()
    Valid = validation()
    if Valid:
        Valid2 = ValidationRnd()
        if Valid2:
            uInput.delete(0,END)
            charlist,letList = converts(userInput)
            Shift(charlist,letList)
            OutputtingcoEncode()
        elif not Valid2:
            ShiftNum.delete(0,END)
            tk.messagebox.showerror("Error", "\nNumber to be shifted cannot me more than 25 and less than 1")

        
    elif not Valid:
        uInput.delete(0,END)
        tk.messagebox.showerror("Error", "\nInvalid Input\nmake sure length of input is above 45 and below 1 characters")
    
    
def Dok():
    global userInput
    # ------------------------------------------------------------
    userInput = uInput.get()
    Valid = validation()
    if Valid:
        uInput.delete(0,END)
        charlist,letList = converts(userInput)
        Shift(charlist,letList)
        OutputtingDecode()
    elif not Valid:
        uInput.delete(0,END)
        tk.messagebox.showerror("Error", "\nInvalid Input")
# ------------------------------------------------------------
# ------------------------------------------------------------

def converts(userInp):
    listofchr = []
    for i in userInp:
        y = ord(i)
        listofchr.append(y)
    letterList = []
    for j in userInput:
        letterList.append(j)
    #print(listofchr)
    return listofchr,letterList
# ------------------------------------------------------------
# ------------------------------------------------------------
def Shift(charL,letL):
    global FinalList
    # ------------------------------------------------------------
    FinalList = []
    listX = charL
    #print(letL)
    shift = 0
    for q in range(25):
        blankL=[]
        changeL=[]
        
        for i,value1 in enumerate(listX):
            
            if letL[i].islower():           
                #print(letL[i])
                if value1<=121:
                    y = value1+1
                    blankL.append(y)
                else:
                    y = 97
                    blankL.append(y)
            elif letL[i].isupper():
                if value1<=89:
                     y = value1+1
                     blankL.append(y)
                else:
                    y=65
                    blankL.append(y)
            else:
                blankL.append(value1)
                
        #print(blankL)
            
                
        listX=blankL
        for c in listX:
            value=chr(c)
            changeL.append(value)
        #print(blankL, changeL)
        shift +=1
        string="".join(changeL)
        outPut = "Shift"+str(shift)+":"+" "+str(string)
        FinalList.append(outPut)
# ------------------------------------------------------------
# ------------------------------------------------------------
def validation():
    valid=True
    count = 0
    length = len(userInput)
    if length ==0:
        valid = False
    if length>45:
        valid = False

    while valid and count != length:
        for i in userInput:
            count+=1
            if i.isdigit():
                valid=False
            elif not i.isalpha() and not i.isdigit():
                if len(userInput)==1:
                    valid = False
        if all(not q.isalpha() and not q.isdigit() for q in userInput):
            valid = False
    return valid
# ------------------------------------------------------------
# ------------------------------------------------------------
def OutputtingDecode():
    canvas3 = tk.Canvas(decode,bg="#ffcd82",highlightthickness=0,bd=0) 
    canvas3.place(x=30,y=150,relwidth=0.95, relheight=0.60)
    canvas3.update()
    results_frame = tk.Frame(canvas3, bg="#ffcd82")
    results_frame.place(relx=0.5, rely=0, anchor="n")

    for i, value in enumerate(FinalList):
        row = i % 13      # 13 rows max before wrapping
        col = i // 13     # column 0 or 1
        lbl = tk.Label(results_frame, text=value, font=font3,bg="#ffb3f7", fg="#00D5FF", justify="left")
        lbl.grid(row=row, column=col, padx=20, pady=2)
# ------------------------------------------------------------
# ------------------------------------------------------------
def OutputtingcoEncode():
    Cnum = num-1
    outputtext = FinalList[Cnum]
    canvas4 = tk.Canvas(encode,bg="#ffcd82",highlightthickness=0,bd=0) 
    canvas4.place(x=30,y=130,relwidth=0.95, relheight=0.40)
    canvas4.update()
   
    EncodeShift = Label(canvas4, text = str(outputtext),font=font4,bg="#ffc5e2",fg="#00D5FF",justify="center")
    EncodeShift.place(x=-1000, y=-1000)
    EncodeShift.update_idletasks()
    width = EncodeShift.winfo_width()
    x1 =  (screen_width-width)//2
    EncodeShift.place(x=x1, y=200)


# ------------------------------------------------------------
# ------------------------------------------------------------
def RandomShift():
    global shiftstate
    shiftstate = True
    global shiftBy
    shiftBy = int(random.randint(1,25))
# ------------------------------------------------------------
# ------------------------------------------------------------
#def Select():
def ValidationRnd():
    valid2  = False
    if num>25:
        valid2  = False
    elif num>1 and num<=25:
        valid2 = True
    return valid2
def validationNoShift():
    valid3 = False
    if not shiftstate:
        valid3 = False
    else:
        valid3 = True
    return valid3
# ------------------------------------------------------------
# ------------------------------------------------------------
def getstateE():   
    stateIn = not state1
    menufunE(stateIn)
# ------------------------------------------------------------
# ------------------------------------------------------------
def getstateD():   
    stateIn = not state2
    menufunD(stateIn)
# ------------------------------------------------------------
# ------------------------------------------------------------
def menufunE(state_In):
    
    global state1
    state1 = state_In
    if state_In == True:
        canvasButtons1.place(x=1000, y=0, relwidth=0.20, relheight=0.15)
        canvasButtons1.update()
        homeButton=Button(canvasButtons1,text="HOME",padx=10, pady=20,command=lambda:homeFunction(), bg="#00D5FF",fg="#000000",activebackground="#000000",activeforeground="#00D5FF",font=font2)
        homeButton.place(x=110,y=10)
    elif state_In == False:
        canvasButtons1.place_forget()
# ------------------------------------------------------------
# ------------------------------------------------------------
def menufunD(state_In):
    
    global state2
    state2 = state_In
    if state_In == True:
        canvasButtons2.place(x=1000, y=0, relwidth=0.20, relheight=0.15)
        canvasButtons2.update()
        homeButton=Button(canvasButtons2,text="HOME",padx=10, pady=20,command=lambda:homeFunction(), bg="#00D5FF",fg="#000000",activebackground="#000000",activeforeground="#00D5FF",font=font2)
        homeButton.place(x=110,y=10)
    elif state_In == False:
        canvasButtons2.place_forget()
# ------------------------------------------------------------
# ------------------------------------------------------------
def homeFunction():

    if 'encode' in globals() and encode.winfo_exists():
        encode.destroy()
    elif 'decode'in globals() and decode.winfo_exists():
        decode.destroy()
    root.deiconify() 
#---------------------------------------------------------
#---------------------------------------------------------



    
#----------------------------------------------------------
#MAIN PROGRAM
#----------------------------------------------------------
 # make sure it's in the same folder

button1= Button(root,text="ENCODE",relief="raised",bd=6,width=15,height=1, padx=4,pady=10,command=lambda:e_ncode(), bg="#ff9900",fg="#FFFFFF",activebackground="#FFFFFF",activeforeground="#ff9900",font=font1)
button1.place(x=600,y=315)
button2= Button(root,text="DECODE",relief="raised",bd=6,width=15,height=1, padx=4,pady=10,command=lambda:d_ecode(), bg="#ff9900",fg="#FFFFFF",activebackground="#FFFFFF",activeforeground="#ff9900",font=font1)
button2.place(x=600,y=425)
welcome = Label(root, text = "Welcome to the Caesar Cipher!🔐🧩🕵️",font=("Ariel", 40),bg="#00D5FF",fg="#4b3412")
welcome.place(x=350,y=220)
root.mainloop()








        






