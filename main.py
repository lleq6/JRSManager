from tkinter import *
from tkinter import ttk







def changeMenu(newFrame:Frame):
    global curWindow
    curWindow.destroy()
    curWindow = newFrame
    curWindow.grid(row=1, column=0, sticky='news')

def Login():
    def click_login(c):
        global curWindow
        if c:
            curWindow.destroy()
            Window.rowconfigure(0,weight=1)
            Window.rowconfigure(1,weight=15)
            head().grid(row=0, column=0, sticky='news')
            curWindow = main()
            curWindow.grid(row=1, column=0, sticky='news')

    frame = Frame(Window, bg='red')
    frame.columnconfigure(0,weight=1)
    frame.columnconfigure(1,weight=1)
    Entry(frame).grid(row=0, column=0)
    Entry(frame).grid(row=1, column=0,)
    Button(frame,text='Login', command=lambda:click_login(True)).grid(row=0, column=1, rowspan=2, sticky='e')
    return frame


def head():
    frame = Frame(Window)
    frame.rowconfigure(0,weight=1)
    Button(frame,height=4, text='m1', command=print, width=10).grid(row=0, column=0, sticky='news')
    Button(frame,height=4, text='ข้อมูลโครงการ', command=lambda:changeMenu(ProjectManagement()), width=10).grid(row=0, column=1, sticky='news')
    Button(frame,height=4, text='m3', command=lambda:changeMenu(main2()), width=10).grid(row=0, column=2, sticky='news')
    Button(frame,height=4, text='m4', command=lambda:changeMenu(main3()), width=10).grid(row=0, column=3, sticky='news')
    Button(frame,height=4, text='m5', command=lambda:changeMenu(main2()), width=10).grid(row=0, column=4, sticky='news')
    Button(frame,height=4, text='ทะเบียนพนักงาน',command=lambda:changeMenu(EmployeeManagement()), width=10).grid(row=0, column=5, sticky='news')
    Button(frame,height=4, text='ทะเบียนลูกค้า', command=lambda:changeMenu(CustomerManagement()), width=10).grid(row=0, column=6, sticky='news')
    return frame

def main():
    frame = Frame(Window)
    return frame
def ProjectManagement():
    frame = Frame(Window, bg='red')
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=0)
    frame.rowconfigure(0, weight=0)
    frame.rowconfigure(1, weight=1)
    subTopFrame = Frame(frame)
    subTopFrame.columnconfigure((0,1), weight=1)
    subTopLeft = Frame(subTopFrame)
    subTopRight = Frame(subTopFrame)
    Label(subTopLeft, text='m2').grid(row=0, column=0)

    Label(subTopLeft, text = 'เลือก').grid(row=0, column=0)
    Entry(subTopLeft).grid(row=0, column=1, columnspan=3)

    Button(subTopLeft, text='รายละเอียดโ๕รงการ').grid(row=1, column=1)
    Button(subTopLeft, text='เฟสโครงการ', command=lambda:ProjectAddOrEdit()).grid(row=1, column=2)
    Button(subTopLeft, text='ลบโครงการ').grid(row=1, column=3)


    Label(subTopRight, text = 'ค้นหาโดย').grid(row=0, column=4)
    Label(subTopRight, text = 'คำค้นหา').grid(row=0, column=6)
    # listbox = Listbox(subTopFrame)
    selectionBox = ttk.Combobox(subTopRight)
    columnList = ['Project ID','ผู้รับผิดชอบ','ชื่อลูกค้า','สถานะ','เฟส']
    selectionBox['values'] = columnList
    selectionBox.grid(row=0, column=5)
    Entry(subTopRight).grid(row=0, column=6)
    Button(subTopRight, text = 'ค้นหา').grid(row=0, column=7, sticky='w')

    subTopLeft.grid(row=0,column=0, sticky='nws')
    subTopRight.grid(row=0,column=1, sticky='nes')
    #TABLE
    columnList = ["No", "projectID", "fname", "lname", "phone"]
    textList = ["No.", "ตำแหน่ง", "ชื่อ", "นามสกุล", "เบอร์โทร"]
    table = ttk.Treeview(frame, columns=columnList, show='headings', height=10)
    for i in range(len(columnList)):
        table.heading(columnList[i], text=textList[i])
    for i in range(30):
        textTest = textList = ["No."+str(i), "ตำแหน่ง"+str(i), "ชื่อ"+str(i), "นามสกุล"+str(i), "เบอร์โทร"+str(i)]
        table.insert('', END, values=textTest)
    scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=table.yview)
    table.configure(yscrollcommand=scrollbar.set)

    scrollbar.grid(row=1, column=1, sticky='ns')

    subTopFrame.grid(row=0, sticky='news')
    table.grid(row=1, column=0, sticky='news')
    return frame

def ProjectAddOrEdit(ProjectID = False):
    test = Toplevel(Window)
    test.resizable(False,False)
    test.geometry('600x800')

    frame = Frame(test)
    frame.columnconfigure(0, weight=0)
    if ProjectID:
        Label(frame,text = f'ดู/แก้ไขโครงการ : {ProjectID}').grid(row=0, column=0)
    else:
        Label(frame,text = f'เพิ่มโครงการ').grid(row=0, column=0)

    customerFrame = LabelFrame(frame, text='ผู้ว่าจ้าง')

    Label(customerFrame, text = 'ลูกค้า').grid(row=0, column=0)
    Label(customerFrame, text = 'วันที่').grid(row=0, column=1)
    Label(customerFrame, text = 'งบประมาณ').grid(row=0, column=2, columnspan=2)
    Entry(customerFrame).grid(row=1, column=0)
    Entry(customerFrame).grid(row=1, column=1)
    Entry(customerFrame).grid(row=1, column=2, columnspan=2)

    Label(customerFrame, text = 'หมวดอาคาร').grid(row=2, column=0)
    Label(customerFrame, text = 'ที่ดินโฉนดเลขที่').grid(row=2, column=1)
    Label(customerFrame, text = 'ระวาง').grid(row=2, column=2,)
    Label(customerFrame, text = 'เลขที่ดิน').grid(row=2, column=3)

    Entry(customerFrame).grid(row=3, column=0)
    Entry(customerFrame).grid(row=3, column=1)
    Entry(customerFrame).grid(row=3, column=2,)
    Entry(customerFrame).grid(row=3, column=3)

    customerFrame.grid(row=1, column=0, sticky='news')
    

    frame.grid(row=0, column=0, sticky='news')


    

    # Button(test,command=lambda:test.destroy()).pack()

    # frame = Frame(Window)


def main2():
    frame = Frame(Window, bg='green')
    Label(frame, text='m1').grid(row=0, column=0)

    return frame

def main3():
    frame = Frame(Window, bg='yellow')
    Label(frame, text='m3').grid(row=0, column=0)

    return frame

def EmployeeManagement():
    frame = Frame(Window, bg='yellow')
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0,weight=2)
    frame.rowconfigure(1,weight=1)
    # Label(frame, text='m3').grid(row=0, column=0)

    #TABLE ONLY
    columnList = ["No", "pos", "fname", "lname", "phone"]
    textList = ["No.", "ตำแหน่ง", "ชื่อ", "นามสกุล", "เบอร์โทร"]
    table = ttk.Treeview(frame, columns=columnList, show='headings', height=10)
    for i in range(len(columnList)):
        table.heading(columnList[i], text=textList[i])
    table.grid(row=0, column=0, sticky='news')

    for i in range(30):
        textTest = textList = ["No."+str(i), "ตำแหน่ง"+str(i), "ชื่อ"+str(i), "นามสกุล"+str(i), "เบอร์โทร"+str(i)]

        table.insert('', END, values=textTest)

    scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=table.yview)
    table.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    #FRAME2 INFO
    frame2 = Frame(frame, background='red')
    frame2.grid(row=1,column=0, sticky='news', columnspan=2)

    frame2.columnconfigure(0, weight=1)
    frame2.columnconfigure(1, weight=1)
    frame2.rowconfigure((0,1), weight=1)

    detailFrame = LabelFrame(frame2, text="รายละเอียดพนักงาน")
    detailFrame.columnconfigure((0,2), weight=1)
    detailFrame.columnconfigure((1,3), weight=10)

    Checkbutton(detailFrame, text='แก้ไข', state=DISABLED).grid(row=0,column=3, sticky='e', padx=10)
    Button(detailFrame, text='บันทึกแก้ไข', state=DISABLED).grid(row=0,column=3,sticky='e', padx=80)

    Label(detailFrame, text="ตำแหน่ง").grid(row=1,column=0)
    Label(detailFrame, text="ชื่อ").grid(row=2,column=0)
    Label(detailFrame, text="เบอร์โทรศัพท์").grid(row=3,column=0)
    Label(detailFrame, text="เลขบัตรประชาชน").grid(row=1,column=2)
    Label(detailFrame, text="นามสกุล").grid(row=2,column=2)
    Label(detailFrame, text="วันเกิด").grid(row=3,column=2)

    Entry(detailFrame).grid(row=1,column=1, sticky='we')
    Entry(detailFrame).grid(row=2,column=1, sticky='we')
    Entry(detailFrame).grid(row=3,column=1, sticky='we')
    Entry(detailFrame).grid(row=1,column=3, sticky='we', padx=10, pady=5)
    Entry(detailFrame).grid(row=2,column=3, sticky='we', padx=10, pady=5)
    Entry(detailFrame).grid(row=3,column=3, sticky='we', padx=10, pady=5)


    #ADDRESSFRAME
    addressFrame = LabelFrame(frame2, text="ที่อยู่")
    subFrame = Frame(addressFrame)

    addressFrame.columnconfigure(0,weight=1)
    addressFrame.columnconfigure(1,weight=5)
    addressFrame.columnconfigure(2, weight=1)
    addressFrame.columnconfigure(3, weight=5)
    # addressFrame.rowconfigure(0, weight=1)
    # addressFrame.rowconfigure((0,1,2), weight=1)

    subFrame.columnconfigure((0,2), weight=1)
    subFrame.columnconfigure((1,3), weight=4)
    subFrame.rowconfigure(0, weight=1)
    Label(addressFrame, text="บ้านเลขที่").grid(row=0, column=0, sticky='e')
    Label(subFrame, text="หมู่ที่").grid(row=0, column=1, sticky='ew')
    Entry(subFrame).grid(row=0, column=0, sticky='ew')
    Entry(subFrame).grid(row=0, column=2, columnspan=2, sticky='ew')

    subFrame.grid(row=0, column=1, columnspan=1, sticky='ew', ipady=5)
    Label(addressFrame, text="ตำบล").grid(row=1,column=0, sticky='w', ipady=5)
    Label(addressFrame, text="จังหวัด").grid(row=2,column=0, sticky='ew', ipady=5)
    Entry(addressFrame).grid(row=1,column=1, sticky='ew')
    Entry(addressFrame).grid(row=2,column=1, sticky='ew')
    Label(addressFrame, text="ตรอก/ซอย").grid(row=0,column=2, sticky='ew')
    Label(addressFrame, text="อำเภอ").grid(row=1,column=2, sticky='ew')
    Label(addressFrame, text="รหัสไปรษณีย์").grid(row=2,column=2, sticky='ew',ipady=5)
    Entry(addressFrame).grid(row=0,column=3, sticky='ew', padx=10)
    Entry(addressFrame).grid(row=1,column=3, sticky='ew', padx=10)
    Entry(addressFrame).grid(row=2,column=3, sticky='ew', padx=10)


    #SEARCHFRAME

    searchFrame = LabelFrame(frame2, text="ค้นหา")
    searchFrame.rowconfigure((0,1), weight=1)
    searchFrame.columnconfigure((0,2), weight=1)
    searchFrame.columnconfigure((1), weight=4)
    Label(searchFrame, text="ค้นหาโดย : ").grid(row=0, column=0)
    Label(searchFrame, text="คำค้นหา : ").grid(row=1, column=0)
    Entry(searchFrame).grid(row=0, column=1, sticky='ew')
    Entry(searchFrame,state =DISABLED).grid(row=1, column=1, sticky='ew')
    Button(searchFrame, text='รีเฟรช').grid(row=0, column=2)
    Button(searchFrame, text='ค้นหา').grid(row=1, column=2)

    arFrame = LabelFrame(frame2, text="เพิ่ม/ลบ")
    arFrame.columnconfigure((0,1), weight=1)
    arFrame.rowconfigure(0, weight=1)
    Button(arFrame, text = 'เพิ่ม').grid(row=0, column=0, sticky='news', pady=10, padx=10)
    Button(arFrame, text = 'ลบที่เลือก').grid(row=0, column=1, sticky='news', pady=10, padx=10)
    # Button(arFrame, text = 'บันทึกแก้ไข').grid(row=0, column=2, sticky='news', pady=10, padx=10)

    
    detailFrame.grid(row=0, column=0, sticky='news', ipadx=10, ipady=10)
    addressFrame.grid(row=1, column=0, sticky='news', ipadx=10, ipady=10)
    searchFrame.grid(row=0,column=1, sticky='news', ipadx=10, ipady=10)
    arFrame.grid(row=1, column=1, sticky='news', ipadx=10, ipady=10)

    return frame

def CustomerManagement():
    frame = Frame(Window, bg='yellow')
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0,weight=2)
    frame.rowconfigure(1,weight=1)
    # Label(frame, text='m3').grid(row=0, column=0)

    #TABLE ONLY
    columnList = ["No", "pos", "fname", "lname", "phone"]
    textList = ["No.", "ตำแหน่ง", "ชื่อ", "นามสกุล", "เบอร์โทร"]
    table = ttk.Treeview(frame, columns=columnList, show='headings', height=10)
    for i in range(len(columnList)):
        table.heading(columnList[i], text=textList[i])
    table.grid(row=0, column=0, sticky='news')

    for i in range(30):
        textTest = textList = ["No."+str(i), "ตำแหน่ง"+str(i), "ชื่อ"+str(i), "นามสกุล"+str(i), "เบอร์โทร"+str(i)]

        table.insert('', END, values=textTest)

    scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=table.yview)
    table.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    #FRAME2 INFO
    frame2 = Frame(frame, background='red')
    frame2.grid(row=1,column=0, sticky='news', columnspan=2)

    frame2.columnconfigure(0, weight=1)
    frame2.columnconfigure(1, weight=1)
    frame2.rowconfigure((0,1), weight=1)
    detailFrame = LabelFrame(frame2, text="รายละเอียดลูกค้า")
    Label(detailFrame, text="ชื่อ").grid(row=0,column=0)
    Label(detailFrame, text="Email").grid(row=1,column=0)
    Label(detailFrame, text="เบอร์โทรศัพท์").grid(row=2,column=0)
    Entry(detailFrame).grid(row=0,column=1)
    Entry(detailFrame).grid(row=1,column=1)
    Entry(detailFrame).grid(row=2,column=1)
    Label(detailFrame, text="นามสกุล").grid(row=0,column=2)
    Label(detailFrame, text="เลขบัตรประชาชน").grid(row=1,column=2)
    Label(detailFrame, text="วันเกิด").grid(row=2,column=2)
    Entry(detailFrame).grid(row=0,column=3)
    Entry(detailFrame).grid(row=1,column=3)
    Entry(detailFrame).grid(row=2,column=3)


    #ADDRESSFRAME
    addressFrame = LabelFrame(frame2, text="ที่อยู่")
    subFrame = Frame(addressFrame)
    Label(subFrame, text="บ้านเลขที่").grid(row=0, column=0)
    Label(subFrame, text="หมู่ที่").grid(row=0, column=2)
    Entry(subFrame).grid(row=0, column=1)
    Entry(subFrame).grid(row=0, column=3)
    subFrame.grid(row=0, column=0, columnspan=2)
    Label(addressFrame, text="ตำบล").grid(row=1,column=0)
    Label(addressFrame, text="จังหวัด").grid(row=2,column=0)
    Entry(addressFrame).grid(row=1,column=1,)
    Entry(addressFrame).grid(row=2,column=1,)
    Label(addressFrame, text="ตรอก/ซอย").grid(row=0,column=2)
    Label(addressFrame, text="อำเภอ").grid(row=1,column=2)
    Label(addressFrame, text="รหัสไปรษณีย์").grid(row=2,column=2)
    Entry(addressFrame).grid(row=0,column=3)
    Entry(addressFrame).grid(row=1,column=3)
    Entry(addressFrame).grid(row=2,column=3)


    #SEARCHFRAME

    searchFrame = LabelFrame(frame2, text="ค้นหา")
    Label(searchFrame, text="ค้นหาโดย : ").grid(row=0, column=0)
    Label(searchFrame, text="คำค้นหา : ").grid(row=1, column=0)
    Entry(searchFrame).grid(row=0, column=1)
    Entry(searchFrame,state =DISABLED).grid(row=1, column=1)
    Button(searchFrame, text='รีเฟรช').grid(row=0, column=2)
    Button(searchFrame, text='ค้นหา').grid(row=1, column=2)

    arFrame = LabelFrame(frame2, text="เพิ่ม/ลบ")
    Button(arFrame, text = 'เพิ่ม').grid(row=0, column=0)
    Button(arFrame, text = 'ลบที่เลือก').grid(row=0, column=1)

    
    detailFrame.grid(row=0, column=0, sticky='news', ipadx=10, ipady=10)
    addressFrame.grid(row=1, column=0, sticky='news', ipadx=10, ipady=10)
    searchFrame.grid(row=0,column=1, sticky='news', ipadx=10, ipady=10)
    arFrame.grid(row=1, column=1, sticky='news', ipadx=10, ipady=10)

    return frame
    

Window = Tk()
# Window.geometry('1280x720')

curWindow = Login()
curWindow.grid(row=0, column=0)
Window.columnconfigure(0,weight=1)
Window.rowconfigure(0,weight=1)



Window.mainloop()