from tkinter import *

window = Tk()
TopFrame = Frame(window)
TopFrame.pack(side=TOP)

TextBox = Text(TopFrame,height=2 , pady=40)
TextBox.pack()
output = ''


#----------------------------------------------------------

def Click(number):
    global output
    if (number != 'del') and (number != 'Exe'):
        output += '{}'.format(number)
        TextBox.insert(END , '{}'.format(number))
        print(output)

    elif number == 'del':
        output = output[:-1]
        TextBox.delete("end-2c")
        print(output)

    elif number == 'Exe':
        sumup = str(eval(output))
        TextBox.delete(1.0 , END)
        TextBox.insert(END , sumup)
#----------------------------------------------------------------



BottomFrame = Frame(window)
BottomFrame.pack(side=BOTTOM)

bouton7 = Button(BottomFrame,text='7' , command=lambda: Click(7))
bouton7.grid(row = 1 , column=0 , ipadx=20 , ipady=20)

bouton8 = Button(BottomFrame,text='8' , command=lambda: Click(8))
bouton8.grid(row = 1, column=1, ipadx=20, ipady=20)

bouton9 = Button(BottomFrame,text='9' , command=lambda: Click(9))
bouton9.grid(row = 1 , column=2 , ipadx=20 , ipady=20 )

bouton4 = Button(BottomFrame,text='4' , command=lambda: Click(4))
bouton4.grid(row = 2 , column=0 , ipadx=20 , ipady=20 )

bouton5 = Button(BottomFrame,text='5' , command=lambda: Click(5))
bouton5.grid(row = 2 , column=1 , ipadx=20 , ipady=20 )

bouton6 = Button(BottomFrame,text='6' , command=lambda: Click(6))
bouton6.grid(row = 2 , column=2 , ipadx=20 , ipady=20 )

bouton1 = Button(BottomFrame,text='1' , command=lambda: Click(1))
bouton1.grid(row = 3 , column=0 , ipadx=20 , ipady=20 )

bouton2 = Button(BottomFrame,text='2' , command=lambda: Click(2))
bouton2.grid(row = 3 , column=1 , ipadx=20 , ipady=20)

bouton3 = Button(BottomFrame,text='3' , command=lambda: Click(2))
bouton3.grid(row = 3 , column=2 , ipadx=20 , ipady=20 )

boutonX = Button(BottomFrame, text='*' , command=lambda: Click(' * '))
boutonX.grid(row = 0 , column=1 , ipadx=18.5 , ipady=20)

boutonDIV = Button(BottomFrame , text='%' , command=lambda: Click(' / '))
boutonDIV.grid(row = 0 , column=2 , ipadx=18.5 , ipady=20)

boutonPARTH1= Button(BottomFrame , text='(' , command=lambda: Click('('))
boutonPARTH1.grid(row  = 1 , column = 3 , ipadx=20 ,ipady=20 )

boutonPARTH2 = Button(BottomFrame ,text=')' , command=lambda : Click(')'))
boutonPARTH2.grid(row = 0 , column = 3 , ipadx = 20 , ipady = 20)

boutonPOINT = Button(BottomFrame , text='.' , command=lambda: Click('.'))
boutonPOINT.grid(row  = 2 , column = 3 , ipadx=20 ,ipady=20 )

boutonADD= Button(BottomFrame , text='+' , command=lambda: Click(' + '))
boutonADD.grid(row  = 1 , column = 4 , ipadx=20 ,ipady=20 )

boutonDEL = Button(BottomFrame ,text='del' , command=lambda : Click('del'))
boutonDEL.grid(row = 0 , column = 0 , ipadx = 20 , ipady = 20)

boutonSOUS = Button(BottomFrame , text='_' , command=lambda: Click(' - '))
boutonSOUS.grid(row  = 2 , column = 4 , ipadx=20 ,ipady=20 )

boutonEXE = Button(BottomFrame , text ='Exe' , bg = 'red' , command=lambda : Click('Exe'))
boutonEXE.grid( row=3 ,column=3 , ipadx = 15 , ipady = 20)

window.mainloop()