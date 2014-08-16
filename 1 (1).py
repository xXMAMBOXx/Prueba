from tkinter import *

lbl=Label(ventana,image="1.gif").pack()
lbl=Label(ventana,image="2.gif").pack()

#img1 = PhotoImage(file="1.gif")
#img2 = PhotoImage(file="2.gif")
#img3 = PhotoImage(file="3.gif")
#img4 = PhotoImage(file="4.gif")
#img5 = PhotoImage(file="5.gif")
#img6 = PhotoImage(file="6.gif")
#img7 = PhotoImage(file="7.gif")
#img8 = PhotoImage(file="8.gif")
#img9 = PhotoImage(file="9.gif")
#img0 = PhotoImage(file="0.gif")
#imgsuma = PhotoImage(file="+.gif")
#imgresta = PhotoImage(file="-.gif")
#imgmulti = PhotoImage(file="multi.gif")
#imgdivi = PhotoImage(file="divi.gif")
#imgexpo = PhotoImage(file="expo.gif")



elementos = [["0","img0"],["1","img1"],["2","img2"],["3","img3"],["4","img4"],["5","img5"],["6","img6"],["7","img7"],["8","img8"],["9","img9"],["+","imgsuma"],["-","imgresta"],["*","imgmulti"],["/","imgdiv"],["^","imgexpo"]]

def determinarelementos(expresion_str):
    iele=0
    jope=0
    operacion = list(expresion_str)
    largo= len (operacion)-1
    largo2 = 15
    nuevalista = []
    while jope < largo:
        iele=0
        while iele <=  largo:
            if operacion.get [jope]==elementos [iele][0]:
                nuevalista = nuevalista +[elementos [iele][1]]
            else:
                iele = iele +1
        jope = jope +1
    print (nuevalista)
                
frame_width = 900
frame_height =900

master = Tk()

frame = Frame(master, 
           width=frame_width, 
           height=frame_height)
frame.pack()

expresion_label = Label(frame,text="Expresion Numerica:")
expresion_label.place(x=100,y=56)
expresion_str = StringVar()
expresion_entry = Entry(frame,textvariable=expresion_str)
expresion_entry.place(x=300, y=55)
convertir=Button(frame,text="convertir",font=("Calibri",12), command=lambda: determinarelementos(expresion_str.get())).place(x=100,y=100)






mainloop()

        
    



