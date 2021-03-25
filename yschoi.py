from tkinter import *
from tkinter import messagebox


window = Tk()
window.title('시급 계산기 ver1.2')
window.geometry('600x500')

label1 = Label(window, text="받게 될 세전 금액을 알려주세요", font=('나눔스퀘어',15), fg='black')
label2 = Label(window, text="이번달 예상 근무 일수를 적어주세요", font=("나눔스퀘어", 15), fg="black", height=5)
label3 = Label(window, text="하루동안 근무하게 될 시간을 적어주세요", font=("나눔스퀘어", 15), fg="black", height=5)

label1.pack()
upFrame = Frame(window)
upFrame.pack()
editBox = Entry(upFrame, width = 30, bg = 'white')
editBox.pack(padx = 10, pady = 10)
label2.pack()
upFrame = Frame(window)
upFrame.pack()
editBox2 = Entry(upFrame, width = 30, bg = 'white')
editBox2.pack(padx = 10, pady = 10)
label3.pack()
upFrame = Frame(window)
upFrame.pack()
editBox3 = Entry(upFrame, width = 30, bg = 'white')
editBox3.pack(padx = 10, pady = 10)

def clickButton() :
    messagebox.showinfo('당신의 시급은?', str(int(int(editBox.get())/int(editBox2.get())/int(editBox3.get())/100*93.4))+'원                           \n\n\n')
button1 = Button(window, text="나의 시급 계산하기", fg="black", bg="white", command=clickButton)
button1.pack(expand = 1)




window.mainloop()




print('시급 계산기 ver.1.0')
########################################
paytotal =  int(input('받게 될 세전 금액을 알려주세요'))
month2 = input('이번달 예상 근무 일수를 적어주세요')
hour = int(input('하룻동안 근무하게 될 시간을 적어주세요'))
month3 = int(month2)
print('세전시급:',paytotal/month3/hour)
print('세후시급:', paytotal/month3/hour/100*93.4)
