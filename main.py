import os
import SQLManager
import shutil
import subprocess

from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import *
from Address import *
from Customer import *
from Deed import *
from Project import *
from Employee import *
from Template import *
from tkinter import filedialog
from Report import *

def ChangeMenu(newFrame : Frame, button : Button = False):
    global curWindow, curBtn

    if button:
        curBtn['relief'] = 'groove'
        curBtn['bg']='light grey'
        button['relief'] = 'flat'
        button['bg'] = '#F0F0F0'
        curBtn = button

    curWindow.destroy()
    curWindow = newFrame
    curWindow.grid(row=1, column=0, sticky='news')

def Login():
    def click_login(c):
        global curWindow, curBtn
        if c:
            curWindow.destroy()
            Window.rowconfigure(0,weight=1)
            Window.rowconfigure(1,weight=15)
            Head().grid(row=0, column=0, sticky='news')
            frame = Main()
            curBtn = m1
            ChangeMenu(frame, m1)
            curWindow = frame
            curWindow.grid(row=1, column=0, sticky='news')

    frame = Frame(Window)
    
    frame.columnconfigure(0,weight=1)
    Label(frame, text = 'JRS House Constructor', font=("bold 50"),fg="#6C63FF").grid(row=0, column=0,pady=20)
    Label(frame, text = 'ชื่อผู้ใช้', font=("bold 20")).grid(row=1, column=0, sticky='w',pady=20,padx=20)
    Entry(frame, font=("30"),width=40).grid(row=2, column=0,pady=10,sticky="wnes", ipady=20)
    Label(frame, text = 'รหัสผ่าน', font=("bold 20")).grid(row=3, column=0, sticky='w',pady=20,padx=20)
    Entry(frame, font=("30"),width=40).grid(row=4, column=0,pady=10,sticky="wnes", ipady=20)
    Button(frame,text='เข้าสู่ระบบ', command=lambda:click_login(True),font=("bold 20"),fg="white",bg="#6C63FF").grid(row=5, column=0,sticky="news",pady=20)
    return frame

def Head():
    global m1,m2,m3,m4,m5,m6
    frameM = Frame(Window)
    frameM.columnconfigure(0, weight=3)
    frameM.columnconfigure(1, weight=1)
    frame = Frame(frameM)
    #frame.rowconfigure(0, weight=1)
    frame.columnconfigure((0,1,2,3,4,5),weight=1)
    m1 = Button(frame, bg='light grey',image=employeeIcon , compound=TOP, relief='groove', text='หน้าหลัก', command=lambda:ChangeMenu(Main(),m1), width=10)
    m2 = Button(frame, bg='light grey',image=employeeIcon ,compound=TOP, relief='groove', text='ข้อมูลโครงการ', command=lambda:ChangeMenu(ProjectManagement(),m2), width=10)
    m3 = Button(frame, bg='light grey',image=employeeIcon ,compound=TOP, relief='groove', text='แบบก่อสร้าง\nแบบรื้อถอน', command=lambda:ChangeMenu(TemplateManagement(),m3), width=10)
    m4 = Button(frame, bg='light grey',image=employeeIcon ,compound=TOP, relief='groove', text='การชำระเงิน', command=lambda:ChangeMenu(PaymentManagement(),m4), width=10)
    m5 = Button(frame, bg='light grey',image=employeeIcon ,compound=TOP, relief='groove', text='ทะเบียนพนักงาน',command=lambda:ChangeMenu(EmployeeManagement(),m5), width=10)
    m6 = Button(frame, bg='light grey',image=employeeIcon ,compound=TOP, relief='groove', text='ทะเบียนลูกค้า', command=lambda:ChangeMenu(CustomerManagement(),m6), width=10)
    m1.grid(row=0, column=0, sticky='news')
    m2.grid(row=0, column=1, sticky='news')
    m3.grid(row=0, column=2, sticky='news')
    m4.grid(row=0, column=3, sticky='news')
    m5.grid(row=0, column=4, sticky='news')
    m6.grid(row=0, column=5, sticky='news')
    frame.grid(row=0,column=0, sticky='news')
    return frameM

def Main():
    frame = Frame(Window,bg="#A5D8FF")
    frame.rowconfigure((0,1), weight=1)
    frame.columnconfigure((0,1,2), weight=1)
    Label(frame, text = 'JRS House Constructor\nระบบจัดการข้อมูลการก่อสร้าง',font="bold 30",bg="#A5D8FF").grid(row=0, column=0,columnspan=3,padx=10)
    aboutFrame = Frame(frame,bg="white")

    TotalProjectsVar = StringVar()
    NotStartProjectsVar = StringVar()
    BuildingProjectsVar = StringVar()
    FinishProjectsVar = StringVar()

    def Dashboard():
        TotalProjectsVar.set(len(Projects))
        NotStart, Building, Finish = 0, 0, 0
        for Project in Projects.values():
            if Project.Status == "ยังไม่ดำเนินการ":
                NotStart += 1
            elif Project.Status == "กำลังดำเนินการ":
                Building += 1
            elif Project.Status == "ดำเนินการเสร็จสิ้น":
                Finish += 1
        NotStartProjectsVar.set(NotStart)
        BuildingProjectsVar.set(Building)
        FinishProjectsVar.set(Finish)

    Dashboard()

    Label(aboutFrame, text = 'โครงการ',font="bold 20",bg="white").grid(row=0, columnspan=2,padx=10,pady=10)
    Label(aboutFrame, text = 'โครงการทั้งหมด',font="14",bg="white").grid(row=1, column=0,sticky="w",padx=10,pady=10)
    Label(aboutFrame, text = 'โครงการที่เสร็จสิ้น',font="14",bg="white").grid(row=2, column=0,padx=10,sticky="w",pady=10)
    Label(aboutFrame, text = 'โครงการที่อยู่ระหว่างก่อสร้าง',font="14",bg="white").grid(row=3, column=0,padx=10,sticky="w",pady=10)
    Label(aboutFrame, text = 'โครงการที่ยังไม่ดำเนินการ',font="14",bg="white").grid(row=4, column=0,padx=10,sticky="w",pady=10)
    Label(aboutFrame, textvariable=TotalProjectsVar,font="14",bg="white").grid(row=1, column=1,padx=10,sticky="w",pady=10)
    Label(aboutFrame, textvariable=FinishProjectsVar,font="14",bg="white").grid(row=2, column=1,padx=10,sticky="w",pady=10)
    Label(aboutFrame, textvariable=BuildingProjectsVar,font="14",bg="white").grid(row=3, column=1,padx=10,sticky="w",pady=10)
    Label(aboutFrame, textvariable=NotStartProjectsVar,font="14",bg="white").grid(row=4, column=1,padx=10,sticky="w",pady=10)

    aboutFrame.grid(row=1, column=0,padx=20,sticky="n")

    currentFrame = Frame(frame,bg="white")
    currentFrame.grid(row=1, column=1,padx=20,sticky="n",columnspan=2) 
    Label(currentFrame, text = 'โครงการล่าสุด',font="bold 20",bg="white").grid(row=0, column=0,columnspan=3,padx=10,pady=10)
    Count = 3 if len(Projects) > 2 else len(Projects)
    for i in range(Count):
        Project = list(Projects.values())[i]
        if Project:
            p1Frame = Frame(currentFrame,bg="#4DABF7")
            Label(p1Frame, text = 'รหัสโครงการ :',font="14",bg="#4DABF7").grid(row=0, column=0,padx=5,sticky="w",pady=10)
            Label(p1Frame, text = 'ผู้ดูแลโครงการ :',font="14",bg="#4DABF7").grid(row=1, column=0,padx=5,sticky="w",pady=10)
            Label(p1Frame, text = 'ลูกค้า :',font="14",bg="#4DABF7").grid(row=2, column=0,padx=5,sticky="w",pady=10)
            Label(p1Frame, text = 'เปอร์เซ็นการดำเนินการ :',font="14",bg="#4DABF7").grid(row=3, column=0,padx=5,sticky="w",pady=10)   
            Label(p1Frame, text = f'#{Project.ID}',font="14",bg="#4DABF7").grid(row=0, column=1,sticky="w")
            Employee = Employees.get(Project.EmployeeID)
            if Employee:
                Label(p1Frame, text = f'{Employee.Firstname} {Employee.Lastname}',font="14",bg="#4DABF7").grid(row=1, column=1,sticky="w")
            Customer = Customers.get(Project.CustomerID)
            if Customer:
                Label(p1Frame, text = f'{Customer.Firstname} {Customer.Lastname}',font="14",bg="#4DABF7").grid(row=2, column=1,sticky="w")
            Label(p1Frame, text = f'{int(Project.GetProgress())} %',font="14",bg="#4DABF7").grid(row=3, column=1,sticky="w")
            p1Frame.grid(row=1, column=i,padx=10,pady=10,sticky="nwes")
    return frame

def PaymentManagement():
    global tablePayment, btnAddProve, btnSave, EntryAmount
    frame = Frame(Window)
    frame.rowconfigure((1), weight=1)
    frame.columnconfigure((0), weight=1)
    frame.columnconfigure((1), weight=20)
    topFrame = Frame(frame)
    Label(topFrame, text = 'ค้นหาโดย').grid(row=0, column=0,padx=10)
    Label(topFrame, text = 'คำค้นหา').grid(row=0, column=2,padx=10)

    SearchValue = StringVar()
    SelectedValue = StringVar()

    def OnSearchPayment():
        searchValue = { 'รหัสโครงการ': 'project_id',
                        'ชื่อ-ผู้ดูแลโครงการ':'emp_fname',
                        'นามสกุล-ผู้ดูแลโครงการ':'emp_lname',
                        'ชื่อ-ลูกค้า':'cus_fname',
                        'นามสกุล-ลูกค้า':'cus_lname' }
        LoadTablePayment(tablePayment, GetProjectsByState())

    selectionBox = ttk.Combobox(topFrame, textvariable=SelectedValue, state="readonly")
    columnList = ['รหัสโครงการ','ชื่อ-ผู้ดูแลโครงการ','นามสกุล-ผู้ดูแลโครงการ','ชื่อ-ลูกค้า', "นามสกุล-ลูกค้า"]
    selectionBox['values'] = columnList
    selectionBox.current(0)
    selectionBox.grid(row=0, column=1,padx=10)
    Entry(topFrame, textvariable=SearchValue).grid(row=0, column=3,padx=10)
    Button(topFrame, text = 'ค้นหา', width=5, command=OnSearchPayment).grid(row=0, column=4, sticky='w')
    Button(topFrame, text = 'รีเฟรช', width=5, command=lambda:LoadTablePayment(tablePayment, GetProjectsByState())).grid(row=0, column=5, sticky='w')
    topFrame.grid(row=0, column=0,columnspan=2, sticky="e", padx=10)

    ProjectState = GetProjectsByState()

    IDProject = IntVar()
    EmployeeVar = StringVar()
    CustomerVar = StringVar()
    PercentProject = StringVar()
    AmountPaid = IntVar()
    PaymentAmount = IntVar()
    FilePathVar = StringVar()
    CurrentPhaseID = IntVar()

    def OnSetDefault():
        IDProject.set(0)
        EmployeeVar.set("")
        CustomerVar.set("")
        PercentProject.set("")
        AmountPaid.set(0)
        PaymentAmount.set(0)
        FilePathVar.set("")
        CurrentPhaseID.set(0)
        textPhaseDescription.delete("1.0", END)
    
    def ButtonChangeState(State):
        btnAddProve["state"] = State
        btnSave["state"] = State
        EntryAmount["state"] = State

    def OnSelectedPayment(Event):
        for Item in tablePayment.selection():
            Values = tablePayment.item(Item)['values']
            Project = ProjectState.get(Values[1])
            if Project:
                IDProject.set(Project.ID)
                CurrentPhaseID.set(Project.CurrentPhase)
                Employee = Employees.get(Project.EmployeeID)
                if Employee:
                    EmployeeVar.set(f"{Employee.Firstname} {Employee.Lastname}")
                Customer = Customers.get(Project.CustomerID)
                if Customer:
                    CustomerVar.set(f"{Customer.Firstname} {Customer.Lastname}")
                PercentProject.set(f"{Project.GetProgress():.0f} %")
                Phase = Project.Phases.get(Project.CurrentPhase)
                if Phase:
                    AmountPaid.set(Phase.GetCost(Project.BudgetProject))
                    textPhaseDescription.delete("1.0", END)
                    textPhaseDescription.insert(END, Phase.DescriptionExcessCost)

                ButtonChangeState(NORMAL)
    leftFrame = Frame(frame)
    leftFrame.grid(row=1, column=0,sticky="nwes")
    leftFrame.rowconfigure((0), weight=1)
    columnList = ["No", "ProjectID", "Manager", "Customer", "Phase"]
    textList = ["No.", "รหัสโครงการ", "ผู้ดูแลโครงการ", "ลูกค้า", "เฟสการดำเนินการ"]
    tablePayment = ttk.Treeview(leftFrame, columns=columnList, show='headings')
    for i in range(len(columnList)):
        tablePayment.heading(columnList[i], text=textList[i])
        tablePayment.column("No", width=100, minwidth=100, anchor=CENTER)
        tablePayment.column("ProjectID", width=180, minwidth=180, anchor=CENTER)
        tablePayment.column("Manager", width=180, minwidth=180, anchor=CENTER)
        tablePayment.column("Customer", width=180, minwidth=180, anchor=CENTER)
        tablePayment.column("Phase", width=180, minwidth=180, anchor=CENTER)
    LoadTablePayment(tablePayment, ProjectState)
  
    scrollbar = ttk.Scrollbar(leftFrame, orient=VERTICAL, command=tablePayment.yview)
    tablePayment.configure(yscrollcommand=scrollbar.set)
    tablePayment.bind("<<TreeviewSelect>>", OnSelectedPayment)
    tablePayment.grid(row=0, column=0, sticky='news',pady=10)
    scrollbar.grid(row=0, column=1, sticky='ns')
   
    rightFrame = LabelFrame(frame)
    rightFrame.columnconfigure((0, 1), weight=1)
    Label(rightFrame, text = 'รหัสโครงการ').grid(row=0, column=0, sticky="w", pady=5)
    Label(rightFrame, text = 'ผู้ดูแลโครงการ').grid(row=1, column=0, sticky="w", pady=5)
    Label(rightFrame, text = 'ลูกค้า').grid(row=2, column=0, sticky="w", pady=5)
    Label(rightFrame, text = 'เฟสที่รอรับชำระ').grid(row=3, column=0, sticky="w", pady=5)
    Label(rightFrame, text = 'เปอร์เซ็นการดำเนินโครงการ').grid(row=4, column=0, sticky="w", pady=5)
    Label(rightFrame, text = 'ยอดที่ต้องชำระ').grid(row=5, column=0, sticky="w", pady=5)
    Label(rightFrame, text = 'ยอดการชำระ').grid(row=6, column=0, sticky="w", pady=5)
    Label(rightFrame, text = 'รายละเอียดของค่าใช้จ่าย\nส่วนเกิน (กรณีชำระเงินเกิน)').grid(row=7, column=0, sticky="w", pady=5)
    Label(rightFrame, text = 'ไฟล์หลักฐานการรับชำระเงิน').grid(row=8, column=0, sticky="w", pady=5)

    Entry(rightFrame, textvariable=IDProject, state=DISABLED).grid(row=0, column=1, sticky="we", padx=10, pady=11)
    Entry(rightFrame, textvariable=EmployeeVar, state=DISABLED).grid(row=1, column=1, sticky="we", padx=10, pady=11)
    Entry(rightFrame, textvariable=CustomerVar, state=DISABLED).grid(row=2, column=1, sticky="we", padx=10, pady=11)
    Entry(rightFrame, textvariable=CurrentPhaseID, state=DISABLED).grid(row=3, column=1, sticky="we", padx=10, pady=11)
    Entry(rightFrame, textvariable=PercentProject, state=DISABLED).grid(row=4, column=1, sticky="we", padx=10, pady=11)
    Entry(rightFrame, textvariable=AmountPaid, state=DISABLED).grid(row=5, column=1, sticky="we", padx=10, pady=11)
    EntryAmount = Entry(rightFrame, textvariable=PaymentAmount, state=DISABLED)
    EntryAmount.grid(row=6, column=1, sticky="we", padx=10, pady=11)
    textPhaseDescription = Text(rightFrame, width=30, height=10)
    textPhaseDescription.grid(row=7, column=1, sticky="we", padx=10, pady=11)
    scrollbarDes = ttk.Scrollbar(rightFrame, orient=VERTICAL, command=textPhaseDescription.yview)
    scrollbarDes.grid(row=7, column=1, sticky='nes')
    textPhaseDescription.configure(yscrollcommand=scrollbarDes.set)
    Entry(rightFrame, textvariable=FilePathVar, state=DISABLED).grid(row=8, column=1, sticky="we", padx=10, pady=11)
    def OnBrowseFile():
        file_path = filedialog.askopenfilename(filetypes=[("Selected files", "*.jpg;*.jpeg;*.png;*.pdf")], initialdir=CURRENT_DIRECTORY)
        FilePathVar.set(file_path)

    def OnSave():
        project = Projects.get(IDProject.get())
        project : Project
        if project:
            Phase = project.Phases.get(CurrentPhaseID.get())
            CreateDirectory(f"{project.ID}", "Payments")
            if Phase:
                if FilePathVar.get() != "":
                    if PaymentAmount.get() >= AmountPaid.get():
                        try:
                            Base, Extension = os.path.splitext(FilePathVar.get())
                            Phase.Payment = shutil.copy(FilePathVar.get(), os.path.join(CURRENT_DIRECTORY, "Payments", f"{project.ID}", f"Payment_{Phase.ID}_{datetime.now().strftime(DATE_FILE_FORMAT)}{Extension}"))
                        except:
                            pass
                        DueTime = datetime.strptime(Phase.DueDate, DATE_FORMAT)
                        TimeNow = datetime.strptime(datetime.now().strftime(DATE_FORMAT), DATE_FORMAT)
                        FormatTime = TimeNow.strftime(DATE_FORMAT)
                        Phase.PaymentDate = FormatTime
                        if TimeNow >= DueTime:
                            Phase.Note = "ชำระเงินล่าช้า"
                        Phase.Start = FormatTime
                        Phase.Status = PHASE_STATUS_ALL.get(4)
                        Phase.DescriptionExcessCost = textPhaseDescription.get("1.0", END)
                        Cost = Phase.GetCost(project.BudgetProject)
                        if PaymentAmount.get() > Cost:
                            Phase.ExcessCost = PaymentAmount.get() - Cost
                        Next = project.NextPhase()
                        DateNow = datetime.now()
                        OldPhase = project.Phases.get(Next - 1)
                        if OldPhase:
                            OldPhase.End = DateNow.strftime(DATE_FORMAT)
                            OldPhase.Status = PHASE_STATUS_ALL.get(6)
                        NewPhase = project.Phases.get(Next)
                        if NewPhase:
                            NewPhase.Status = PHASE_STATUS_ALL.get(4)
                            NewPhase.DueDate = (DateNow + timedelta(weeks=2)).strftime(DATE_FORMAT)
                        if NewPhase == project.PhaseCount:
                            project.Status = PROJECT_STATUS_ALL.get(2)
                            SQLManager.UpdateProjectStatus(project.ID, project.Status)
                        if SQLManager.UpdatePhase(project.ID, OldPhase) and SQLManager.UpdatePhase(project.ID, NewPhase) and SQLManager.UpdateProjectCurrentPhase(project.ID, Next):
                            LoadTablePayment(tablePayment, GetProjectsByState())
                            ButtonChangeState(DISABLED)
                            OnSetDefault()
                            messagebox.showinfo("สำเร็จ!", "ดำเนินการเสร็จสิ้น")
                    else:
                        messagebox.showwarning("คำเตือน!", "กรุณากรอกยอดเงินที่ชำระให้ถูกต้อง!\nซึ่งต้องมากกว่าหรือเท่ากับยอดที่ต้องชำระเท่านั้น")
                else:
                    messagebox.showwarning("คำเตือน!", "กรุณาเลือกไฟล์หลักฐานการชำระเงินก่อน")
        ButtonChangeState(DISABLED)
        OnSetDefault()
        tablePayment.selection_set('')
        CurrentPhaseID.set(0)

    btnAddProve = Button(rightFrame, text = 'เพิ่มหลักฐาน', font=("20"), command=OnBrowseFile, state=DISABLED)
    btnAddProve.grid(row=9, column=0, padx=10, pady=10, sticky="news")
    btnSave = Button(rightFrame, text = 'บันทึก', font=("20"), command=OnSave, state=DISABLED)
    btnSave.grid(row=9, column=1, padx=10, pady=10, sticky="news")
    rightFrame.grid(row=1, column=1,sticky="nwes",padx=10,pady=10)

    return frame

def ProjectManagement():
    global tableProject, addProject, deleteProject, phaseManagement, editProject
    CurrentProjectID.set(0)
    frame = Frame(Window)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=0)
    frame.rowconfigure(0, weight=0)
    frame.rowconfigure(1, weight=1)
    subTopFrame = Frame(frame)
    subTopFrame.columnconfigure((0,1), weight=1)
    subTopLeft = Frame(subTopFrame)
    subTopRight = Frame(subTopFrame)
    Label(subTopLeft, text='เลือก').grid(row=0, column=0, pady=5)
    Entry(subTopLeft, textvariable=CurrentProjectID, state=DISABLED, justify=CENTER).grid(row=0, column=1, columnspan=3, padx=5, pady=5)
    addProject = Button(subTopLeft, text='เพิ่มโครงการ', command=lambda : OnAddOrEditProject(False))
    addProject.grid(row=0, column=4, rowspan=2, sticky='news', pady=5)
    deleteProject = Button(subTopLeft, text='ลบโครงการ', command=lambda : OnDeleteProject(CurrentProjectID.get()), state=DISABLED)
    deleteProject.grid(row=0, column=5, rowspan=2, sticky='news', pady=5)
    editProject = Button(subTopLeft, text='แก้ไขโครงการ', command=lambda : OnAddOrEditProject(True), state=DISABLED)
    editProject.grid(row=0, column=6, rowspan=2, sticky='news', pady=5)
    phaseManagement = Button(subTopLeft, text='เฟสการดำเนินการ', command=lambda : ChangeMenu(PhaseManagement(CurrentProjectID.get())), state=DISABLED)
    phaseManagement.grid(row=0, column=7, rowspan=2, sticky='news', pady=5)
    Button(subTopLeft, text="จัดพิมพ์รายงานความคืบหน้าโครงการ", command=ProjectReport).grid(row=0, column=8, rowspan=2, sticky='news', pady=5)

    SearchValue = StringVar()
    SelectedValue = StringVar()

    def OnSearchProject():
        searchValue = { 'ไอดีโครงการ': 'id',
                        'ชื่อ-ผู้รับผิดชอบ':'emp_fname',
                        'นามสกุล-ผู้รับผิดชอบ':'emp_lname',
                        'ชื่อ-ลูกค้า':'cus_fname',
                        'นามสกุล-ลูกค้า':'cus_lname',
                        'สถานะ':'status',
                        'เฟสล่าสุด':'current_phase' }
        Result = SQLManager.SearchProject(searchValue[SelectedValue.get()], SearchValue.get())
        LoadTableProject(tableProject, Result)

    Label(subTopLeft).grid(row=1)
    Label(subTopRight, text = 'ค้นหาโดย').grid(row=0, column=5)
    Label(subTopRight, text = 'คำค้นหา').grid(row=1, column=5)
    searchValues = ['ไอดีโครงการ', 'ชื่อ-ผู้รับผิดชอบ', 'นามสกุล-ผู้รับผิดชอบ', 'ชื่อ-ลูกค้า', 'นามสกุล-ลูกค้า', 'สถานะ', 'เฟสล่าสุด']
    selectionBox = ttk.Combobox(subTopRight, values=searchValues, textvariable=SelectedValue, state="readonly")
    selectionBox.current(0)
    selectionBox.grid(row=0, column=6, padx=5)
    Entry(subTopRight, textvariable=SearchValue).grid(row=1, column=6, sticky='ew', padx=5)
    Button(subTopRight, text = 'ค้นหา', command=OnSearchProject).grid(row=0, column=7, sticky='news', rowspan=2, ipadx=10)
    Button(subTopRight, text = 'รีเฟรช', command=lambda:LoadTableProject(tableProject, Projects)).grid(row=0, column=8, sticky='news', rowspan=2, ipadx=10)
    subTopLeft.grid(row=0,column=0, sticky='nws')
    subTopRight.grid(row=0,column=1, sticky='nes')

    def OnSelectedProject(Event):
        for Item in tableProject.selection():
            Values = tableProject.item(Item)['values']
            Project = Projects.get(Values[1])
            if Project:
                CurrentProjectID.set(Project.ID)
                phaseManagement["state"] = NORMAL
                deleteProject["state"] = NORMAL
                editProject["state"] = NORMAL

    columnList = ["No", "ProjectID", "Employee", "Customer", "Status", "CurrentPhase"]
    textList = ["No.", "รหัสโครงการ", "ผู้รับผิดชอบ", "ชื่อลูกค้า", "สถานะ", "เฟสล่าสุด"]
    tableProject = ttk.Treeview(frame, columns=columnList, show='headings', height=10)
    for i in range(len(columnList)):
        tableProject.heading(columnList[i], text=textList[i])
        tableProject.column("No", width=50, minwidth=50, anchor=CENTER)
        tableProject.column("ProjectID", width=100, minwidth=100, anchor=CENTER)
        tableProject.column("Employee", width=100, minwidth=100, anchor=CENTER)
        tableProject.column("Customer", width=100, minwidth=100, anchor=CENTER)
        tableProject.column("Status", width=100, minwidth=100, anchor=CENTER)
        tableProject.column("CurrentPhase", width=100, minwidth=100, anchor=CENTER)
    LoadTableProject(tableProject, Projects)
    scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=tableProject.yview)
    tableProject.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')
    subTopFrame.grid(row=0, sticky='news')
    tableProject.bind("<<TreeviewSelect>>", OnSelectedProject)
    tableProject.grid(row=1, column=0, sticky='news')
    return frame

def TemplateManagement():
    global tableTemplate, btnEdit, btnDelete, btnOpenFile
    frame = Frame(Window)
    frame.rowconfigure(0,weight=1)
    frame.columnconfigure((0),weight=1)
    frame.columnconfigure((1),weight=30)
    leftframe = Frame(frame)
    leftframe.rowconfigure(0,weight=0)
    leftframe.rowconfigure(1,weight=1)
    leftframe.grid(row=0,column=0, sticky='nwes')
    subTopFrame = Frame(leftframe)
    subTopFrame.grid(row=0,column=0, sticky='nwes')
    subTopFrame.columnconfigure((0,1,2,3,4,5), weight=1)

    SearchValue = StringVar()
    SelectedValue = StringVar()

    def OnSearchTemplate():
        searchValue = { 'รหัสแบบ': 'id',
                        'ประเภท':'type',
                        'ผู้เขียนแบบ':'draftman' }
        Result = SQLManager.SearchTemplate(searchValue[SelectedValue.get()], SearchValue.get())
        LoadTableTemplate(tableTemplate, Result)

    Label(subTopFrame, text = 'ค้นหาโดย').grid(row=0, column=0, sticky='nwes')
    Label(subTopFrame, text = 'คำค้นหา').grid(row=0, column=2, sticky='nwes')
    selectionBox = ttk.Combobox(subTopFrame, textvariable=SelectedValue, state="readonly")
    columnList = ["รหัสแบบ", "ประเภท", "ผู้เขียนแบบ"]
    selectionBox['values'] = columnList
    selectionBox.current(0)
    selectionBox.grid(row=0, column=1, sticky='nwes')
    searchEntry = Entry(subTopFrame, textvariable=SearchValue)
    searchEntry.grid(row=0, column=3, sticky='nwes')
    Button(subTopFrame, text = 'ค้นหา', command=OnSearchTemplate).grid(row=0, column=4, sticky='nwes')
    Button(subTopFrame, text = 'รีเฟรช', command=lambda:LoadTableTemplate(tableTemplate, Templates)).grid(row=0, column=5, sticky='nwes')

    IDValue = IntVar()
    TypeValue = StringVar()
    DraftmanValue = StringVar()
    CreateDateValue = StringVar()
    ProjectIDValue = StringVar()
    FilePathVar = StringVar()

    def SetDefaultValue():
        IDValue.set(0)
        TypeValue.set("")
        DraftmanValue.set("")
        CreateDateValue.set("")
        ProjectIDValue.set("")
        FilePathVar.set("")

    CurrentTemplateID = IntVar()

    def OnSelectedTemplate(Event):
        for Item in tableTemplate.selection():
            Values = tableTemplate.item(Item)['values']
            ID = Values[1]
            Template = Templates.get(ID)
            if Template:
                ChangeButtonState(NORMAL)
                CurrentTemplateID.set(ID)
                IDValue.set(ID)
                TypeValue.set(Template.Type)
                DraftmanValue.set(Template.Draftman)
                CreateDateValue.set(Template.CreateDate)
                if Template.Path != "":
                    btnOpenFile["state"] = NORMAL
                else:
                    btnOpenFile["state"] = DISABLED
                FilePathVar.set(Template.Path)
                if int(Template.ProjectID) > 0:
                    Project = SQLManager.GetProjectByID(Template.ProjectID)
                    if Project:
                        ProjectIDValue.set(f"โครงการที่ {Project.ID}")
                    else:
                        ProjectIDValue.set("ไม่พบข้อมูลโครงการ")
                else:
                    ProjectIDValue.set("")
    
    columnList = ["No", "ID", "Type", "Project", "Draftman", "CreateDate", "Amount"]
    textList = ["No.", "รหัสแบบ", "ประเภท", "โครงการ", "ผู้เขียนแบบ", "วันที่เพิ่ม", "จำนวนการแก้ไข"]
    tableTemplate = ttk.Treeview(leftframe, columns=columnList, show='headings', height=10)
    for i in range(len(columnList)):
        tableTemplate.heading(columnList[i], text=textList[i])
        tableTemplate.column("No", width=50, minwidth=50, anchor=CENTER)
        tableTemplate.column("ID", width=150, minwidth=150, anchor=CENTER)
        tableTemplate.column("Type", width=150, minwidth=150, anchor=CENTER)
        tableTemplate.column("Project", width=150, minwidth=150, anchor=CENTER)
        tableTemplate.column("Draftman", width=150, minwidth=150, anchor=CENTER)
        tableTemplate.column("CreateDate", width=150, minwidth=150, anchor=CENTER)
        tableTemplate.column("Amount", width=150, minwidth=150, anchor=CENTER)
    LoadTableTemplate(tableTemplate, Templates)
    tableTemplate.bind("<<TreeviewSelect>>", OnSelectedTemplate)
    tableTemplate.grid(row=1, column=0, sticky='news',pady=10)

    scrollbar = ttk.Scrollbar(leftframe, orient=VERTICAL, command=tableTemplate.yview)
    tableTemplate.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')
    rightframe = Frame(frame)
    rightframe.grid(row=0, column=1, sticky='news')
    rightframe.columnconfigure((0), weight=1)
    rightframe.rowconfigure((0), weight=2)
    rightframe.rowconfigure((1), weight=1)
    Label(rightframe,height=15).grid(row=0, column=0,sticky="w",columnspan=3)
    detailFrame = LabelFrame(rightframe, text="ข้อมูลแบบ")
    detailFrame.columnconfigure((0, 1, 2, 3), weight=1)
    detailFrame.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
    Label(detailFrame, text = 'รหัสแบบ').grid(row=0, column=0,sticky="w",padx=10)
    Label(detailFrame, text = 'ประเภท').grid(row=1, column=0,sticky="w",padx=10)
    Label(detailFrame, text = 'ผู้เขียนแบบ').grid(row=2, column=0,sticky="w",padx=10)
    Label(detailFrame, text = 'เลือกโครงการ').grid(row=3, column=0,sticky="w",padx=10)
    Label(detailFrame, text = 'เส้นทางไฟล์').grid(row=4, column=0,sticky="w",padx=10)
    Entry(detailFrame, state=DISABLED, textvariable=IDValue).grid(row=0, column=1,columnspan=3,sticky="nwes",pady=10,padx=10)
    EntryType = Entry(detailFrame, textvariable=TypeValue)
    EntryType.grid(row=1, column=1,columnspan=3,sticky="nwes",pady=10,padx=10)
    EntryDraftman = Entry(detailFrame, textvariable=DraftmanValue)
    EntryDraftman.grid(row=2, column=1,columnspan=3,sticky="nwes",pady=10,padx=10)
    selectionBox = ttk.Combobox(detailFrame, textvariable=ProjectIDValue, values=[f"โครงการที่ {Project.ID}" for Project in Projects.values()], state="readonly")
    selectionBox.current(0)
    selectionBox.grid(row=3, column=1, columnspan=3,sticky="nwes",pady=10,padx=10)
    EntryPath = Entry(detailFrame, textvariable=FilePathVar, state=DISABLED)
    EntryPath.grid(row=4, column=1, columnspan=2,sticky="nwes",pady=10,padx=10)
    btnOpenFile  = Button(detailFrame, text="เปิดไฟล์", state=DISABLED, command=lambda:OpenFileByPath(FilePathVar.get()))
    btnOpenFile.grid(row=4, column=3,sticky="nwes",pady=10,padx=10)

    def OnAddTemplate():
        IDSplit = ProjectIDValue.get().split(" ")
        ProjectID = int(-1)
        if len(IDSplit) > 1:
            ProjectID = int(IDSplit[1])
        Temp = Template()
        Temp.Type = TypeValue.get()
        Temp.Draftman = DraftmanValue.get()
        Temp.ProjectID = ProjectID
        Temp.CreateDate = datetime.now().strftime(DATE_FORMAT)

        if not Temp.check():
            return

        TemplateID = SQLManager.CreateTemplate(Temp)
        if TemplateID != 0:
            Temp.ID = TemplateID
            CreateDirectory(f"{Temp.ID}", "Templates")
            if FilePathVar.get() != "":
                try:
                    Base, Extension = os.path.splitext(FilePathVar.get())
                    Path = shutil.copy(FilePathVar.get(), os.path.join(CURRENT_DIRECTORY, os.path.join("Templates", f"{Temp.ID}"), f"Template_{Temp.ID}_{datetime.now().strftime(DATE_FILE_FORMAT)}{Extension}"))
                    if SQLManager.UpdateTemplatePath(Temp.ID, Path):
                        Temp.Path = Path
                except:
                    pass
            Project = Projects.get(Temp.ProjectID)
            if Project:
                if SQLManager.IsExistTemplateCountByProjectID(Project.ID):
                    if SQLManager.UpdateProjectTemplateID(Project.ID, Temp.ID):
                        Project.TemplateID = Temp.ID
                        messagebox.showerror('สำเร็จ!', f'เพิ่มแบบก่อสร้าง-แบบรื้อถอนสำเร็จ\nและเพิ่มไอดีแบบที่ {Temp.ID} ลงในโครงการสำเร็จ')
                    else:
                        messagebox.showerror('ล้มเหลว!', f'ไม่สามารถเพิ่มไอดีแบบที่ {Temp.ID} ลงในโครงการได้')
                else:
                    if SQLManager.UpdateTemplateProjectID(Temp.ID, -1):
                        Temp.ProjectID = -1
                        messagebox.showerror('ล้มเหลว!', f'เพิ่มแบบก่อสร้าง-แบบรื้อถอนสำเร็จ\nแต่ไม่สามารถเพิ่มแบบซ้ำลงในโครงการได้')
                    else:
                        messagebox.showerror('ล้มเหลว!', f'SQL Error!')
            else:
                messagebox.showinfo("สำเร็จ!", "เพิ่มแบบก่อสร้าง-แบบรื้อถอนสำเร็จ")
        Templates.update({ Temp.ID : Temp })
        LoadTableTemplate(tableTemplate, Templates)
        SetDefaultValue()

    def OnDeleteTemplate(ID : int, Type : str, Draftman : str):
        if not bool(tableTemplate.selection()):
            messagebox.showwarning('ลบแบบก่อสร้าง-แบบรื้อถอน','โปรดเลือกข้อมูลที่ต้องการลบก่อน')
            frame.focus()
            return
        if messagebox.askquestion('ลบแบบก่อสร้าง-แบบรื้อถอน',f'คุณแน่ใจที่ต้องการจะลบใช่ไหม?\nไอดีแบบ : {ID} ประเภท : {Type} ผู้เขียนแบบ : {Draftman} ') == 'yes':
            Template = Templates.get(ID)
            if Template:
                Project = Projects.get(Template.ProjectID)
                if Project:
                    if SQLManager.UpdateProjectTemplateID(Project.ID, -1):
                        Project.TemplateID = -1
                    else:
                        messagebox.showerror('ล้มเหลว!', f'ไม่สามารถลบไอดีแบบที่ {ID} ได้')
                if SQLManager.DeleteTemplate(ID):
                    Templates.pop(ID)
                    RemoveDirectory(f"{ID}", "Templates")
                    LoadTableTemplate(tableTemplate, Templates)
                    ChangeButtonState(DISABLED)
                    messagebox.showinfo('สำเร็จ!', f'ไอดีแบบ: {ID} ถูกลบเรียบร้อย')
            else:
                messagebox.showerror('ล้มเหลว!', f'ไม่พบไอดีแบบที่ {ID}')
        SetDefaultValue()

    def OnSaveTemplate():
        IDSplit = ProjectIDValue.get().split(" ")
        ProjectID = int(-1)
        if len(IDSplit) > 1:
            ProjectID = int(IDSplit[1])
        Select = tableTemplate.focus()
        Index = tableTemplate.index(Select)
        template = Templates.get(CurrentTemplateID.get())
        if template:
            template.Type = TypeValue.get()
            CreateDirectory(f"{template.ID}", "Templates")
            if FilePathVar.get() != "":
                try:
                    Base, Extension = os.path.splitext(FilePathVar.get())
                    Path = shutil.copy(FilePathVar.get(), os.path.join(CURRENT_DIRECTORY, os.path.join("Templates", f"{template.ID}"), f"Template_{template.ID}_{datetime.now().strftime(DATE_FILE_FORMAT)}{Extension}"))
                    if SQLManager.UpdateTemplatePath(template.ID, Path):
                        template.Path = Path
                except shutil.SameFileError:
                    pass
            template.Draftman = DraftmanValue.get()
            template.AmountOfEdited += 1
            if SQLManager.UpdateTemplate(template):
                Project = Projects.get(ProjectID)
                if Project:
                    if SQLManager.IsExistTemplateCountByProjectID(Project.ID):
                        if SQLManager.UpdateTemplateProjectID(template.ID, ProjectID) and SQLManager.UpdateProjectTemplateID(Project.ID, template.ID):
                            template.ProjectID = ProjectID
                            Project.TemplateID = template.ID
                            messagebox.showinfo('สำเร็จ!', f'ไอดีแบบ: {template.ID} ถูกบันทึกลงโครงงานที่ {Project.ID} สำเร็จ')
                        else:
                            messagebox.showerror('ล้มเหลว!', f'ไอดีแบบ: {template.ID} แก้ไขโครงงานไม่สำเร็จ')
                    else:
                        messagebox.showwarning("คำเตือน!", f"ไอดีแบบ: {template.ID} ไม่สามารถเพิ่มแบบลงซ้ำในโครงการที่ {Project.ID}")
                        
                LoadTableTemplate(tableTemplate, Templates)
                tableTemplate.selection_set(tableTemplate.get_children()[Index])
                tableTemplate.focus(tableTemplate.get_children()[Index])
                messagebox.showinfo('สำเร็จ!', f'ไอดีแบบ: {template.ID} แก้ไขโครงงานสำเร็จ')

    def ChangeButtonState(State):
        btnEdit["state"] = State
        btnDelete["state"] = State

    def OnBrowseFile():
        file_path = filedialog.askopenfilename(filetypes=[("Selected files", "*.jpg;*.jpeg;*.png;*.pdf")], initialdir=CURRENT_DIRECTORY)
        FilePathVar.set(file_path)

    Button(detailFrame, text = 'เพิ่มไฟล์', command=OnBrowseFile).grid(row=5, column=0,pady=10,padx=10,sticky="nwes")
    Button(detailFrame, text = 'เพิ่ม', command=OnAddTemplate).grid(row=5, column=1,pady=10,padx=10,sticky="nwes")
    btnEdit = Button(detailFrame, text = 'บันทึก', command=OnSaveTemplate, state=DISABLED)
    btnEdit.grid(row=5, column=2,pady=10,padx=10,sticky="nwes")
    btnDelete = Button(detailFrame, text = 'ลบ', command=lambda:OnDeleteTemplate(CurrentTemplateID.get(), TypeValue.get(), DraftmanValue.get()), state=DISABLED)
    btnDelete.grid(row=5, column=3,pady=10,padx=10,sticky="nwes")
    detailFrame.grid(row=1, column=0, sticky='news', padx=10, pady=10)
    return frame

def PhaseManagement(ProjectID : int):
    global tablePhase, btnOpenTemplate, btnOpenPath, btnAddFile
    CurrentProjectID.set(0)
    Project = Projects.get(ProjectID)
    frame = Frame(Window)
    frame.rowconfigure(2, weight=1)
    frame.columnconfigure((0, 1), weight=1)
    Label(frame, text=f"โครงการ : " + (f"#{Project.ID}" if Project != None else "ไม่มีข้อมูล"), font=("28")).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    Button(frame, text="ย้อนกลับ", command=lambda:ChangeMenu(ProjectManagement())).grid(row=0, column=1, sticky="e", padx=20, pady=5)
    if Project == None:
        messagebox.showwarning("คำเตือน!", "ไม่พบข้อมูลของโครงการ")
        frame.focus()
        return frame
    
    def projectReportClick():
        pro = Project
        cus = SQLManager.GetCustomerByID(pro.CustomerID)
        emp = SQLManager.GetEmployeeByID(pro.EmployeeID)
        di = filedialog.askdirectory(initialdir=CURRENT_DIRECTORY)
        if di != "":
            try:
                if saveReport(projectFinalReport(pro,cus,emp),di,f'Project_Final_Report_ID_{pro.ID}_{date.today()}'):
                    messagebox.showinfo('สำเร็จ!','พิมรายงานข้อมูลโครงการสำเร็จ')
                else:
                    messagebox.showerror('ล้มเหลว!','พิมพ์รายงานข้อมูลโครงการไม่สำเร็จ')
            except:
                messagebox.showerror('ล้มเหลว!','พิมพ์รายงานข้อมูลโครงการไม่สำเร็จ')
        
    def projectPaymentClick():
        pro = Project
        cus = SQLManager.GetCustomerByID(pro.CustomerID)
        di = filedialog.askdirectory(initialdir=CURRENT_DIRECTORY)
        if di != "":
            try:
                if saveReport(projectPaymentReport(cus, pro),di,f'Project_Payment_Report_ID_{pro.ID}_{date.today()}'):
                    messagebox.showinfo('สำเร็จ!','พิมรายงานการรับชำเงินโครงการสำเร็จ')
                else:
                    messagebox.showerror('ล้มเหลว!','พิมพ์รายงานการรับชำเงินโครงการไม่สำเร็จ')
            except:
                messagebox.showerror('ล้มเหลว!','พิมพ์รายงานการรับชำเงินโครงการไม่สำเร็จ')
    
    CurrentPhaseID = IntVar()
    CurrentPhaseID.set(Project.CurrentPhase - 1)
    
    EmployeeName = StringVar()
    TemplateName = StringVar()
    PhaseStatus = StringVar()
    PhaseStart = StringVar()
    PhaseEnd = StringVar()
    PhaseTitle = StringVar()
    PhasePath = StringVar()
    PhaseTemplate = StringVar()
    PhasePaymentDate = StringVar()
    PhaseDueDate = StringVar()
    PhasePayment = StringVar()
    PaymentPath = StringVar()

    detailFrame = Frame(frame)
    detailFrame.rowconfigure(0, weight=1)
    detailFrame.columnconfigure(1, weight=1)
    phaseFrame = Frame(detailFrame)
    phaseFrame.columnconfigure((0, 1), weight=1)
    if Project.Phases == None or len(Project.Phases) == 0:
        Label(phaseFrame, text="ไม่พบข้อมูลของเฟส", font=("20")).grid(row=0, columnspan=2, pady=20)
    else:
        Label(phaseFrame, text="เลือกเฟส", font=("20")).grid(row=0, columnspan=2, pady=20)
        columnList = ["เฟส"]
        textList = ["เฟส"]
        tablePhase = ttk.Treeview(phaseFrame, columns=columnList, show='headings', height=10)
        for i in range(len(columnList)):
            tablePhase.heading(columnList[i], text=textList[i])
            tablePhase.column("เฟส", width=300, minwidth=300, anchor=CENTER)
        tablePhase.grid(row=1, columnspan=2, padx=20, sticky='news')
        LoadTablePhase(tablePhase, Project)
        tablePhase.selection_set(tablePhase.get_children()[CurrentPhaseID.get()])
        #Button(phaseFrame, text="สิ้นสุดโครงการ").grid(row=2, columnspan=2, sticky="news", ipady=10, padx=5, pady=10)
        Button(phaseFrame, text="จัดพิมพ์รายงานข้อมูลโครงการ", command=projectReportClick).grid(row=2, column=0, sticky="news", ipady=10, padx=5, pady=10)
        Button(phaseFrame, text="จัดพิมพ์รายงานการรับชำเงินโครงการ", command=projectPaymentClick).grid(row=2, column=1, sticky="news", ipady=10, padx=5, pady=10)
    phaseFrame.grid(row=0, column=0, padx=10, pady=10, sticky="news")
    manageFrame = Frame(detailFrame)
    #manageFrame.columnconfigure((0, 1, 2, 3), weight=1)
    Label(manageFrame, text="เฟส :", font=("20")).grid(row=0, column=0, sticky="e", padx=10, pady=10)
    Label(manageFrame, textvariable=PhaseTitle, font=("20")).grid(row=0, column=1, sticky="w", padx=10, pady=10)
    Label(manageFrame, text="วันที่เริ่ม :", font=("20")).grid(row=1, column=0, sticky="e", padx=10, pady=10)
    Label(manageFrame, textvariable=PhaseStart, font=("20")).grid(row=1, column=1, sticky="w", padx=10, pady=10)
    Label(manageFrame, text="วันที่สิ้นสุด :", font=("20")).grid(row=1, column=2, sticky="w", padx=10, pady=10)
    Label(manageFrame, textvariable=PhaseEnd, font=("20")).grid(row=1, column=3, sticky="e", padx=10, pady=10)
    Label(manageFrame, text="ชื่อผู้ดูแลเฟส :", font=("20")).grid(row=2, column=0, sticky="e", padx=10, pady=10)
    Label(manageFrame, textvariable=EmployeeName, font=("20")).grid(row=2, column=1, sticky="w", padx=10, pady=10)
    Label(manageFrame, text="จำนวนเงินที่ต้องชำระ :", font=("20")).grid(row=2, column=2, sticky="w", padx=10, pady=10)
    Label(manageFrame, textvariable=PhasePayment, font=("20")).grid(row=2, column=3, sticky="e", padx=10, pady=10)
    Label(manageFrame, text="วันที่กำหนดชำระ :", font=("20")).grid(row=3, column=0, sticky="e", padx=10, pady=10)
    Label(manageFrame, textvariable=PhaseDueDate, font=("20")).grid(row=3, column=1, sticky="w", padx=10, pady=10)
    Label(manageFrame, text="วันที่ชำระ :", font=("20")).grid(row=3, column=2, sticky="w", padx=10, pady=10)
    Label(manageFrame, textvariable=PhasePaymentDate, font=("20")).grid(row=3, column=3, sticky="e", padx=10, pady=10)
    Label(manageFrame, text="แบบก่อสร้าง-แบบรื้อถอน :", font=("20")).grid(row=4, column=0, sticky="e", padx=10, pady=10)
    Label(manageFrame, textvariable=TemplateName, font=("20")).grid(row=4, column=1, sticky="w", padx=10, pady=10)
    btnOpenTemplate = Button(manageFrame, text="เปิดแบบ", font=("20"), command=lambda:OpenFileByPath(PhaseTemplate.get()), state=DISABLED)
    btnOpenTemplate.grid(row=4, column=2, sticky="news", padx=10, pady=10)
    Label(manageFrame, text="รายละเอียดของเฟส :", font=("20")).grid(row=5, column=0, sticky="ne", padx=10, pady=10)
    descriptionFrame = Frame(manageFrame)
    textPhaseDescription = Text(descriptionFrame, width=40, height=10, font=("20"))
    textPhaseDescription.grid(row=0, column=0, pady=5)
    scrollbarDes = ttk.Scrollbar(descriptionFrame, orient=VERTICAL, command=textPhaseDescription.yview)
    scrollbarDes.grid(row=0, column=1, sticky='ns')
    textPhaseDescription.configure(yscrollcommand=scrollbarDes.set)
    descriptionFrame.grid(row=5, column=1, columnspan=2, sticky="news")

    def SetCurrentPhase(Index : int):
        Phase = Project.Phases.get(Index)
        if Phase:
            textPhaseDescription.insert(END, Phase.Description)
            CurrentPhaseID.set(Phase.ID)
            PhaseStatus.set(Phase.Status)
            PhaseStart.set(Phase.Start)
            PhaseEnd.set(Phase.End)
            PhaseTitle.set(Phase.Title)
            PhasePaymentDate.set(Phase.PaymentDate)
            PhaseDueDate.set(Phase.DueDate)
            PhasePayment.set(f"{Phase.GetCost(Project.BudgetProject):.2f} บาท")
            if Phase.Status == "ยังไม่เริ่มเฟส":
                btnAddFile["state"] = DISABLED
            else:
                btnAddFile["state"] = NORMAL
            if Phase.Path != "":
                PhasePath.set(Phase.Path)
                btnOpenPath["state"] = NORMAL
            else:
                btnOpenPath["state"] = DISABLED
            if Phase.Payment != "":
                PaymentPath.set(Phase.Payment)
                btnOpenPayment["state"] = NORMAL
            else:
                btnOpenPayment["state"] = DISABLED
            Employee = SQLManager.GetEmployeeByID(Phase.EmployeeID)
            if Employee:
                EmployeeName.set(f"{Employee.Firstname} {Employee.Lastname}")
        Template = Templates.get(Project.TemplateID)
        if Template:
            TemplateName.set(f"#{Template.ID} ผู้เขียนแบบ : {Template.Draftman}")
            if Template.Path != "":
                PhaseTemplate.set(Template.Path)
                btnOpenTemplate["state"] = NORMAL
            else:
                btnOpenTemplate["state"] = DISABLED
        else:
            TemplateName.set("ไม่พบข้อมูลแบบก่อสร้าง-แบบรื้อถอน")

    def OnBrowseFile():
        file_path = filedialog.askopenfilename(initialdir=CURRENT_DIRECTORY)
        try:
            Base, Extension = os.path.splitext(file_path)
            Path = shutil.copy(file_path, os.path.join(CURRENT_DIRECTORY, PhasePath.get(), f"Phase_{CurrentPhaseID.get()}_{datetime.now().strftime(DATE_FILE_FORMAT)}{Extension}"))
            if Path != "":
                messagebox.showinfo("สำเร็จ!", "เพิ่มไฟล์สำเร็จ")
                Window.focus()
        except:
            pass

    def OnSaveDescription():
        PhaseDescription = textPhaseDescription.get("1.0", END)
        Phase = Project.Phases.get(CurrentPhaseID.get())
        if Phase:
            Phase.Status = PHASE_STATUS_ALL.get(1) if Phase.Status != PHASE_STATUS_ALL.get(6) else PHASE_STATUS_ALL.get(6)
            PhaseStatus.set(Phase.Status)
            if SQLManager.UpdatePhaseDescription(Project.ID, CurrentPhaseID.get(), PhaseDescription) and SQLManager.UpdatePhaseStatus(Project.ID, Phase.ID, Phase.Status):
                Phase.Description = PhaseDescription
                textPhaseDescription.delete('1.0', END)
                textPhaseDescription.insert(END, PhaseDescription)
                messagebox.showinfo("สำเร็จ!", "บันทึกข้อมูลรายละเอียดของเฟสสำเร็จ")
            else:
                messagebox.showerror("ล้มเหลว!", "บันทึกข้อมูลรายละเอียดของเฟสไม่สำเร็จ")
        else:
            messagebox.showwarning("คำเตือน!", f"ไม่พบข้อมูลของเฟสที่ {Phase.ID} ของโครงการ")

    def OnOpenPaymentPath():
        Phase = Project.Phases.get(CurrentPhaseID.get())
        if Phase:
            OpenFileByPath(Phase.Payment)

    Label(manageFrame, text=f"สถานะเฟส :", font=("20")).grid(row=7, column=0, sticky="e", padx=10, pady=10)
    Label(manageFrame, textvariable=PhaseStatus, font=("20"), fg="red").grid(row=7, column=1, sticky="w", padx=10, pady=10)
    btnOpenPayment = Button(manageFrame, text="ดูหลักฐานการชำระเงิน", font=("20"), command=OnOpenPaymentPath)
    btnOpenPayment.grid(row=7, column=2, sticky="w", padx=10, pady=10)
    Label(manageFrame, text="เอกสารประกอบ :", font=("20")).grid(row=8, column=0, sticky="e", padx=10, pady=10)
    btnAddFile = Button(manageFrame, text="เพิ่มไฟล์", font=("20"), command=OnBrowseFile)
    btnAddFile.grid(row=8, column=1, sticky="news", padx=10, pady=10)
    btnOpenPath = Button(manageFrame, text="เปิด Path", font=("20"), command=lambda:subprocess.Popen(f'explorer /open, "{PhasePath.get()}"'), state=DISABLED)
    btnOpenPath.grid(row=8, column=2, sticky="news", padx=10, pady=10)
    Button(manageFrame, text="บันทึก", font=("20"), command=OnSaveDescription).grid(row=9, column=1, columnspan=2, sticky="news", padx=10, pady=10)

    SetCurrentPhase(CurrentPhaseID.get())

    def OnSelectedPhase(Event):
        textPhaseDescription.delete('1.0', END)
        for Item in tablePhase.selection():
            Values = tablePhase.item(Item)['values']
            Index = Values[0]
            SetCurrentPhase(Index)

    tablePhase.bind("<<TreeviewSelect>>", OnSelectedPhase)
    manageFrame.grid(row=0, column=1, padx=10, pady=10, sticky="news")
    detailFrame.grid(row=1, columnspan=2, sticky="news")
    return frame

def EmployeeManagement():
    global tableEmployee
    frame = Frame(Window)
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0,weight=2)
    frame.rowconfigure(1,weight=1)
    fnameVar = StringVar()
    positionVar = StringVar()
    lnameVar = StringVar()
    phoneVar = StringVar()
    citizenIDVar= StringVar()
    dobVar = StringVar()
    checkVar = BooleanVar()
    AddressNoVar = StringVar()
    MooVar = StringVar()
    alleyVar = StringVar()
    roadVar = StringVar()
    cityVar = StringVar()
    districtVar = StringVar()
    provinceVar = StringVar()
    zipcodeVar = StringVar() 
    searchVar = StringVar()
    selectSearchVar = StringVar()

    def EntriesChangeState():
        inputList = [fname, position, phone, lname, citizen_id, cal, saveButton,
                     NoEnt,mooEnt,roadEnt,cityEnt,alleyEnt,districtEnt,zipcodeEnt, provinceEnt]
        if checkVar.get():
            for i in inputList:
                i['state'] = NORMAL
        else:
            for i in inputList:
                i['state'] = DISABLED
    

    def OnSelectedEmployee(eve):
        checkButton['state'] = NORMAL
        checkVar.set(FALSE)
        EntriesChangeState()
        for Item in tableEmployee.selection():
            Values = tableEmployee.item(Item)['values']
            ID = Values[1]
            Employee = Employees.get(ID)
            if Employee != None:
                fnameVar.set(Employee.Firstname)
                lnameVar.set(Employee.Lastname)
                positionVar.set(Employee.Position)
                citizenIDVar.set(Employee.CitizenID)
                phoneVar.set(Employee.Phone)
                dobVar.set(Employee.Birthday)
                if Employee.Address != None:
                    AddressNoVar.set(Employee.Address.No)
                    MooVar.set(Employee.Address.Mu)
                    alleyVar.set(Employee.Address.Alley)
                    roadVar.set(Employee.Address.Road)
                    cityVar.set(Employee.Address.City)
                    districtVar.set(Employee.Address.District)
                    provinceVar.set(Employee.Address.Province)
                    zipcodeVar.set(Employee.Address.ProvinceZip)

    def onClickSaveEdit():
        select = tableEmployee.focus()
        index = tableEmployee.index(select)
        for Item in tableEmployee.selection():
            Values = tableEmployee.item(Item)['values']

        ID = Values[0]
        employee = Employees.get(ID)
        if employee:
            employee.Firstname = fnameVar.get()
            employee.Lastname = lnameVar.get()
            employee.Position = positionVar.get()
            employee.CitizenID = citizenIDVar.get()
            employee.Phone = phoneVar.get()
            employee.Birthday = dobVar.get()
            address = employee.Address
            if address:
                address.No = AddressNoVar.get()
                address.Mu = MooVar.get()
                address.Alley = alleyVar.get()
                address.Road = roadVar.get()
                address.City = cityVar.get()
                address.District = districtVar.get()
                address.Province = provinceVar.get()
                address.ProvinceZip = zipcodeVar.get()

            if not employee.check():
                return

        if SQLManager.UpdateEmployee(ID, employee) and SQLManager.UpdateAddress('EMP', address):
            LoadTableEmployee(tableEmployee, Employees)
            tableEmployee.selection_set(tableEmployee.get_children()[index])
            tableEmployee.focus(tableEmployee.get_children()[index])
            messagebox.showinfo('สำเร็จ!', f'ไอดีพนักงาน: {ID} ถูกอัพเดตแล้ว')

    def onClickSearch():

        searchValue = { 'ไอดี': 'id',
                        'ตำแหน่ง':'position',
                        'ชื่อ':'fname',
                        'นามสกุล':'lname',
                        'เบอร์โทร':'phone',
                        'เลขบัตรประชาชน':'citizen_id' }
        Result = SQLManager.SearchEmployee(searchValue[selectSearchVar.get()], searchVar.get())
        LoadTableEmployee(tableEmployee, Result)

    columnList = ["No", "ID",'Position', "FullName", "Phone"]
    textList = ["No.", "ไอดี",'ตำแหน่ง', "ชื่อ - นามสกุล", "เบอร์โทร"]
    tableEmployee = ttk.Treeview(frame, columns=columnList, show='headings', height=10)
    tableEmployee.column("No", width=50, minwidth=50, anchor=CENTER)
    tableEmployee.column("ID", width=50, minwidth=50, anchor=CENTER)
    tableEmployee.column("Position", width=50, minwidth=200, anchor=CENTER)
    tableEmployee.column("FullName", width=100, minwidth=100, anchor=CENTER)
    tableEmployee.column("Phone", width=100, minwidth=100, anchor=CENTER)
    for i in range(len(columnList)):
        tableEmployee.heading(columnList[i], text=textList[i])
    tableEmployee.bind("<<TreeviewSelect>>", OnSelectedEmployee)
    tableEmployee.grid(row=0, column=0, sticky='news')

    LoadTableEmployee(tableEmployee, Employees)

    scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=tableEmployee.yview)
    tableEmployee.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    #FRAME2 INFO
    frame2 = Frame(frame)
    frame2.grid(row=1,column=0, sticky='news', columnspan=2)

    frame2.columnconfigure(0, weight=1)
    frame2.columnconfigure(1, weight=1)
    frame2.rowconfigure((0,1), weight=1)

    detailFrame = LabelFrame(frame2, text="รายละเอียดพนักงาน")
    detailFrame.columnconfigure((0,2), weight=1)
    detailFrame.columnconfigure((1,3), weight=10)

    checkButton = Checkbutton(detailFrame, text='แก้ไข', state=DISABLED, variable=checkVar, command=EntriesChangeState)
    checkButton.grid(row=0,column=3, sticky='e', padx=10)
    saveButton = Button(detailFrame, text='บันทึกแก้ไข', state=DISABLED, command=onClickSaveEdit, bg='light grey', relief='groove')
    saveButton.grid(row=0,column=3,sticky='e', padx=80)

    Label(detailFrame, text="ชื่อ : ").grid(row=1,column=0, sticky='e')
    Label(detailFrame, text="ตำแหน่ง : ").grid(row=2,column=0, sticky='e')
    Label(detailFrame, text="เบอร์โทรศัพท์ : ").grid(row=3,column=0, sticky='e')
    Label(detailFrame, text="นามสกุล : ").grid(row=1,column=2, sticky='e')
    Label(detailFrame, text="เลขบัตรประชาชน : ").grid(row=2,column=2, sticky='e')
    Label(detailFrame, text="วันเกิด : ").grid(row=3,column=2, sticky='e')

    fname = Entry(detailFrame, textvariable=fnameVar)
    fname.grid(row=1,column=1, sticky='we')
    position = ttk.Combobox(detailFrame, textvariable=positionVar, values=POSITION_ALL, state="readonly")
    position.current(0)
    position.grid(row=2,column=1, sticky='we')
    phone = Entry(detailFrame, textvariable=phoneVar)
    phone.grid(row=3,column=1, sticky='we')
    lname = Entry(detailFrame, textvariable=lnameVar)
    lname.grid(row=1,column=3, sticky='we', padx=10, pady=5)
    citizen_id = Entry(detailFrame, textvariable=citizenIDVar)
    citizen_id.grid(row=2,column=3, sticky='we', padx=10, pady=5)
    cal = DateEntry(detailFrame, bd=2, date_pattern=ENTRY_DATE_FORMAT, state='readonly')
    cal['textvariable'] = dobVar
    cal.grid(row=3, column=3,
            sticky='ew', padx=10)
    addressFrame = LabelFrame(frame2, text="ที่อยู่")
    subFrame = Frame(addressFrame)

    addressFrame.columnconfigure(0,weight=1)
    addressFrame.columnconfigure(1,weight=5)
    addressFrame.columnconfigure(2, weight=1)
    addressFrame.columnconfigure(3, weight=5)

    Label(addressFrame, text="บ้านเลขที่ : ").grid(row=0, column=0, sticky='e')
    Label(addressFrame, text="ถนน : ").grid(row=1,column=0, sticky='e', ipady=5)
    subFrame.columnconfigure((0,2), weight=4)
    subFrame.columnconfigure((1), weight=1)
    subFrame.rowconfigure(0, weight=1)
    Label(subFrame, text="หมู่ที่ : ").grid(row=0, column=1, sticky='e')
    NoEnt = Entry(subFrame,textvariable=AddressNoVar)
    NoEnt.grid(row=0, column=0, sticky='ew')
    Label(subFrame, text='ตำบล : ').grid(row=1, column=1, sticky='e')

    mooEnt = Entry(subFrame, textvariable=MooVar)
    mooEnt.grid(row=0, column=2, columnspan=2, sticky='ew')
    roadEnt = Entry(subFrame, textvariable=roadVar)
    roadEnt.grid(row=1, column=0, sticky='ew')
    cityEnt = Entry(subFrame, textvariable=cityVar)
    cityEnt.grid(row=1, column=2, sticky='ew')
    subFrame.grid(row=0, column=1, columnspan=1, sticky='ew', ipady=5, rowspan=2)

    Label(addressFrame, text="จังหวัด : ").grid(row=2,column=0, sticky='e', ipady=5)
    Label(addressFrame, text="ตรอก/ซอย : ").grid(row=0,column=2, sticky='e')
    Label(addressFrame, text="อำเภอ : ").grid(row=1,column=2, sticky='e')
    Label(addressFrame, text="รหัสไปรษณีย์ : ").grid(row=2,column=2, sticky='e',ipady=5)
    provinceEnt = ttk.Combobox(addressFrame, values=PROVINCES, textvariable=provinceVar, state="readonly")
    provinceEnt.current(1)
    provinceEnt.grid(row=2,column=1, sticky='ew')
    alleyEnt = Entry(addressFrame, textvariable=alleyVar)
    alleyEnt.grid(row=0,column=3, sticky='ew', padx=10)
    districtEnt = Entry(addressFrame, textvariable=districtVar)
    districtEnt.grid(row=1,column=3, sticky='ew', padx=10)
    zipcodeEnt = Entry(addressFrame, textvariable=zipcodeVar)
    zipcodeEnt.grid(row=2,column=3, sticky='ew', padx=10)

    EntriesChangeState()

    searchFrame = LabelFrame(frame2, text="ค้นหา")
    searchFrame.rowconfigure((0,1), weight=1)
    searchFrame.columnconfigure((0,2), weight=1)
    searchFrame.columnconfigure((1), weight=4)
    Label(searchFrame, text="ค้นหาโดย : ").grid(row=0, column=0)
    Label(searchFrame, text="คำค้นหา : ").grid(row=1, column=0)
    searchValues = ['ไอดี', 'ตำแหน่ง', 'ชื่อ', 'นามสกุล', 'เบอร์โทร', 'เลขบัตรประชาชน']
    selectionBox = ttk.Combobox(searchFrame, state='readonly', textvariable=selectSearchVar, values=searchValues)
    selectionBox.current(0)
    selectionBox.grid(row=0, column=1 , sticky='ew')
    Entry(searchFrame, textvariable=searchVar).grid(row=1, column=1, sticky='ew')
    Button(searchFrame, text='รีเฟรช', command = lambda:LoadTableEmployee(tableEmployee, Employees), bg='light grey', relief='groove').grid(row=0, column=2)
    Button(searchFrame, text='ค้นหา', command=onClickSearch, bg='light grey', relief='groove').grid(row=1, column=2)

    arFrame = LabelFrame(frame2, text="เพิ่ม/ลบ")
    arFrame.columnconfigure((0,1), weight=1)
    arFrame.rowconfigure(0, weight=1)
    Button(arFrame, text = 'เพิ่ม', command=lambda:OnAddEmployee(), bg='light grey', relief='groove').grid(row=0, column=0, sticky='news', pady=10, padx=10)
    Button(arFrame, text = 'ลบที่เลือก', command=lambda:OnDeleteEmployee(), bg='light grey', relief='groove').grid(row=0, column=1, sticky='news', pady=10, padx=10)
    # Button(arFrame, text = 'บันทึกแก้ไข').grid(row=0, column=2, sticky='news', pady=10, padx=10)

    # detailFrame = DetailFrame()
    # addressFrame = AddressFrame()
    detailFrame.grid(row=0, column=0, sticky='news', ipadx=10, ipady=10, padx=5, pady=5)
    addressFrame.grid(row=1, column=0, sticky='news', ipadx=10, ipady=10, padx=5, pady=5)
    searchFrame.grid(row=0,column=1, sticky='news', ipadx=10, ipady=10, padx=5, pady=5)
    arFrame.grid(row=1, column=1, sticky='news', ipadx=10, ipady=10, padx=5, pady=5)
    return frame

def CustomerManagement():
    global tableCustomer
    frame = Frame(Window)
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0,weight=2)
    frame.rowconfigure(1,weight=1)

    fnameVar = StringVar()
    emailVar = StringVar()
    lnameVar = StringVar()
    phoneVar = StringVar()
    citizenIDVar= StringVar()
    dobVar = StringVar()
    checkVar = BooleanVar()
    AddressNoVar = StringVar()
    MooVar = StringVar()
    alleyVar = StringVar()
    roadVar = StringVar()
    cityVar = StringVar()
    districtVar = StringVar()
    provinceVar = StringVar()
    zipcodeVar = StringVar() 
    searchVar = StringVar()
    selectSearchVar = StringVar()

    def EntriesChangeState():
        inputList = [fname, email, phone, lname, citizen_id, cal, saveButton,
                     NoEnt, mooEnt, roadEnt, cityEnt, alleyEnt, districtEnt, zipcodeEnt, provinceEnt]
        if checkVar.get():
            for i in inputList:
                i['state'] = NORMAL
        else:
            for i in inputList:
                i['state'] = DISABLED
    
    def onSelectCustomer(eve):
        checkButton['state'] = NORMAL
        checkVar.set(FALSE)
        EntriesChangeState()
        for Item in tableCustomer.selection():
            Values = tableCustomer.item(Item)['values']
            ID = Values[1]
            Customer = Customers.get(ID)
            if Customer != None:
                fnameVar.set(Customer.Firstname)
                lnameVar.set(Customer.Lastname)
                emailVar.set(Customer.Email)
                citizenIDVar.set(Customer.CitizenID)
                phoneVar.set(Customer.Phone)
                dobVar.set(Customer.Birthday)
                if Customer.Address:
                    AddressNoVar.set(Customer.Address.No)
                    MooVar.set(Customer.Address.Mu)
                    alleyVar.set(Customer.Address.Alley)
                    roadVar.set(Customer.Address.Road)
                    cityVar.set(Customer.Address.City)
                    districtVar.set(Customer.Address.District)
                    provinceVar.set(Customer.Address.Province)
                    zipcodeVar.set(Customer.Address.ProvinceZip)

    def onClickSaveEdit():
        select = tableCustomer.focus()
        index = tableCustomer.index(select)
        for Item in tableCustomer.selection():
            Values = tableCustomer.item(Item)['values']
            ID = Values[1]
            customer = Customers.get(ID)
            if customer:
                customer.Firstname = fnameVar.get()
                customer.Lastname = lnameVar.get()
                customer.Email = emailVar.get()
                customer.CitizenID = citizenIDVar.get()
                customer.Phone = phoneVar.get()
                customer.Birthday = dobVar.get()
                address = customer.Address
                if address:
                    address.No = AddressNoVar.get()
                    address.Mu = MooVar.get()
                    address.Alley = alleyVar.get()
                    address.Road = roadVar.get()
                    address.City = cityVar.get()
                    address.District = districtVar.get()
                    address.Province = provinceVar.get()
                    address.ProvinceZip = zipcodeVar.get()

                    if not customer.check():
                        return

                    if SQLManager.UpdateCustomer(ID, customer) and SQLManager.UpdateAddress('CUS', address):
                        LoadTableCustomer(tableCustomer, Customers)
                        tableCustomer.selection_set(tableCustomer.get_children()[index])
                        tableCustomer.focus(tableCustomer.get_children()[index])
                        messagebox.showinfo('สำเร็จ!', f'ไอดีลูกค้า: {ID} ถูกอัพเดตแล้ว')

    def onClickSearch():
        searchValue = { 'ไอดี' : 'id', 
                        'ชื่อ' : 'fname', 
                        'นามสกุล' : 'lname', 
                        'เบอร์โทร' : 'phone', 
                        'เลขบัตรประชาชน' : 'citizen_id', 
                        'อีเมล' : 'email' }
        
        Result = SQLManager.SearchCustomer(searchValue[selectSearchVar.get()], searchVar.get())
        LoadTableCustomer(tableCustomer, Result)
        
    columnList = ["No", "ID", "FullName", "Email", "Phone"]
    textList = ["No.", "ไอดี", "ชื่อ - นามสกุล", "อีเมล", "เบอร์โทร"]
    tableCustomer = ttk.Treeview(frame, columns=columnList, show='headings', height=10)
    tableCustomer.column("No", width=50, minwidth=50, anchor=CENTER)
    tableCustomer.column("ID", width=50, minwidth=50, anchor=CENTER)
    tableCustomer.column("FullName", width=100, minwidth=100, anchor=CENTER)
    tableCustomer.column("Email", width=100, minwidth=100, anchor=CENTER)
    tableCustomer.column("Phone", width=100, minwidth=100, anchor=CENTER)
    for i in range(len(columnList)):
        tableCustomer.heading(columnList[i], text=textList[i])
    tableCustomer.bind("<<TreeviewSelect>>", onSelectCustomer)
    tableCustomer.grid(row=0, column=0, sticky='news')
    LoadTableCustomer(tableCustomer, Customers)
    scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=tableCustomer.yview)
    tableCustomer.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')
    frame2 = Frame(frame)
    frame2.grid(row=1,column=0, sticky='news', columnspan=2)
    frame2.columnconfigure(0, weight=1)
    frame2.columnconfigure(1, weight=1)
    frame2.rowconfigure((0,1), weight=1)
    detailFrame = LabelFrame(frame2, text="รายละเอียดลูกค้า")
    detailFrame.columnconfigure((0,2), weight=1)
    detailFrame.columnconfigure((1,3), weight=10)
    checkButton = Checkbutton(detailFrame, text='แก้ไข', state=DISABLED, variable=checkVar, command=EntriesChangeState)
    checkButton.grid(row=0,column=3, sticky='e', padx=10)
    saveButton = Button(detailFrame, text='บันทึกแก้ไข', state=DISABLED, command=onClickSaveEdit)
    saveButton.grid(row=0,column=3,sticky='e', padx=80)
    Label(detailFrame, text="ชื่อ : ").grid(row=1,column=0, sticky='e')
    Label(detailFrame, text="อีเมล : ").grid(row=2,column=0, sticky='e')
    Label(detailFrame, text="เบอร์โทรศัพท์ : ").grid(row=3,column=0, sticky='e')
    Label(detailFrame, text="นามสกุล : ").grid(row=1,column=2, sticky='e')
    Label(detailFrame, text="เลขบัตรประชาชน : ").grid(row=2,column=2, sticky='e')
    Label(detailFrame, text="วันเกิด : ").grid(row=3,column=2, sticky='e')
    fname = Entry(detailFrame, textvariable=fnameVar)
    fname.grid(row=1,column=1, sticky='we')
    email = Entry(detailFrame, textvariable=emailVar)
    email.grid(row=2,column=1, sticky='we')
    phone = Entry(detailFrame, textvariable=phoneVar)
    phone.grid(row=3,column=1, sticky='we')
    lname = Entry(detailFrame, textvariable=lnameVar)
    lname.grid(row=1,column=3, sticky='we', padx=10, pady=5)
    citizen_id = Entry(detailFrame, textvariable=citizenIDVar)
    citizen_id.grid(row=2,column=3, sticky='we', padx=10, pady=5)
    cal = DateEntry(detailFrame, bd=2, date_pattern=ENTRY_DATE_FORMAT, state='readonly')
    cal['textvariable'] = dobVar
    cal.grid(row=3, column=3,
            sticky='ew', padx=10)
    addressFrame = LabelFrame(frame2, text="ที่อยู่")
    subFrame = Frame(addressFrame)
    addressFrame.columnconfigure(0,weight=1)
    addressFrame.columnconfigure(1,weight=5)
    addressFrame.columnconfigure(2, weight=1)
    addressFrame.columnconfigure(3, weight=5)
    Label(addressFrame, text="บ้านเลขที่ : ").grid(row=0, column=0, sticky='e')
    Label(addressFrame, text="ถนน : ").grid(row=1,column=0, sticky='e', ipady=5)
    subFrame.columnconfigure((0,2), weight=4)
    subFrame.columnconfigure((1), weight=1)
    subFrame.rowconfigure(0, weight=1)
    Label(subFrame, text="หมู่ที่ : ").grid(row=0, column=1, sticky='e')
    NoEnt = Entry(subFrame,textvariable=AddressNoVar)
    NoEnt.grid(row=0, column=0, sticky='ew')
    Label(subFrame, text='ตำบล : ').grid(row=1, column=1, sticky='e')
    mooEnt = Entry(subFrame, textvariable=MooVar)
    mooEnt.grid(row=0, column=2, columnspan=2, sticky='ew')
    roadEnt = Entry(subFrame, textvariable=roadVar)
    roadEnt.grid(row=1, column=0, sticky='ew')
    cityEnt = Entry(subFrame, textvariable=cityVar)
    cityEnt.grid(row=1, column=2, sticky='ew')
    subFrame.grid(row=0, column=1, columnspan=1, sticky='ew', ipady=5, rowspan=2)
    Label(addressFrame, text="จังหวัด : ").grid(row=2,column=0, sticky='e', ipady=5)
    Label(addressFrame, text="ตรอก/ซอย : ").grid(row=0,column=2, sticky='e')
    Label(addressFrame, text="อำเภอ : ").grid(row=1,column=2, sticky='e')
    Label(addressFrame, text="รหัสไปรษณีย์ : ").grid(row=2,column=2, sticky='e',ipady=5)
    provinceEnt = ttk.Combobox(addressFrame, values=PROVINCES, textvariable=provinceVar, state="readonly")
    provinceEnt.current(1)
    provinceEnt.grid(row=2,column=1, sticky='ew')
    alleyEnt = Entry(addressFrame, textvariable=alleyVar)
    alleyEnt.grid(row=0,column=3, sticky='ew', padx=10)
    districtEnt = Entry(addressFrame, textvariable=districtVar)
    districtEnt.grid(row=1,column=3, sticky='ew', padx=10)
    zipcodeEnt = Entry(addressFrame, textvariable=zipcodeVar)
    zipcodeEnt.grid(row=2,column=3, sticky='ew', padx=10)
    EntriesChangeState()

    searchFrame = LabelFrame(frame2, text="ค้นหา")
    searchFrame.rowconfigure((0,1), weight=1)
    searchFrame.columnconfigure((0,2), weight=1)
    searchFrame.columnconfigure((1), weight=4)
    Label(searchFrame, text="ค้นหาโดย : ").grid(row=0, column=0)
    Label(searchFrame, text="คำค้นหา : ").grid(row=1, column=0)
    # Entry(searchFrame).grid(row=0, column=1, sticky='ew')
    valuesSearch = ['ไอดี', 'ชื่อ', 'นามสกุล', 'เบอร์โทร', 'อีเมล', 'เลขบัตรประชาชน']
    selectionBox = ttk.Combobox(searchFrame, state='readonly', textvariable=selectSearchVar, values=valuesSearch)
    selectionBox.current(0)
    selectionBox.grid(row=0, column=1 , sticky='ew')
    Entry(searchFrame, textvariable=searchVar).grid(row=1, column=1, sticky='ew')
    Button(searchFrame, text='รีเฟรช', command = lambda:LoadTableCustomer(tableCustomer, Customers)).grid(row=0, column=2)
    Button(searchFrame, text='ค้นหา', command=onClickSearch).grid(row=1, column=2)

    arFrame = LabelFrame(frame2, text="เพิ่ม/ลบ")
    arFrame.columnconfigure((0,1), weight=1)
    arFrame.rowconfigure(0, weight=1)
    Button(arFrame, text = 'เพิ่ม', command=lambda:OnAddCustomer()).grid(row=0, column=0, sticky='news', pady=10, padx=10)
    # Button(arFrame, text = 'ลบที่เลือก', command=lambda:deleteCustomer(customer_id)).grid(row=0, column=1, sticky='news', pady=10, padx=10)
    Button(arFrame, text = 'ลบที่เลือก', command=lambda:OnDeleteCustomer()).grid(row=0, column=1, sticky='news', pady=10, padx=10)
    # Button(arFrame, text = 'บันทึกแก้ไข').grid(row=0, column=2, sticky='news', pady=10, padx=10)

    # detailFrame = DetailFrame()
    # addressFrame = AddressFrame()
    detailFrame.grid(row=0, column=0, sticky='news', ipadx=10, ipady=10, padx=5, pady=5)
    addressFrame.grid(row=1, column=0, sticky='news', ipadx=10, ipady=10, padx=5, pady=5)
    searchFrame.grid(row=0,column=1, sticky='news', ipadx=10, ipady=10, padx=5, pady=5)
    arFrame.grid(row=1, column=1, sticky='news', ipadx=10, ipady=10, padx=5, pady=5)
    return frame

def LoadTableCustomer(Table : ttk.Treeview, Customers : list):
    for i in Table.get_children():
        Table.delete(i)
    Counter = 0
    for i in Customers:
        Customer = Customers[i]
        Values = [Counter + 1, Customer.ID, f"{Customer.Firstname} {Customer.Lastname}", Customer.Email, Customer.Phone]
        Table.insert('', END, values=Values)
        Counter += 1

def LoadTableEmployee(Table : ttk.Treeview, Employees : list):
    for i in Table.get_children():
        Table.delete(i)
    Counter = 0
    for i in Employees:
        Employee = Employees[i]
        Values = [Counter + 1, Employee.ID, Employee.Position, f"{Employee.Firstname} {Employee.Lastname}", Employee.Phone]
        Table.insert('', END, values=Values)
        Counter += 1

def LoadTableProject(Table : ttk.Treeview, Projects : list):
    CurrentProjectID.set(0)
    for i in Table.get_children():
        Table.delete(i)
    Counter = 0
    for i in Projects:
        Project = Projects[i]
        CustomerName = "ไม่มีข้อมูล"
        Customer = SQLManager.GetCustomerByID(Project.CustomerID)
        if Customer != None:
            CustomerName = f"{Customer.Firstname} {Customer.Lastname}"
        EmployeeName = "ไม่มีข้อมูล"
        Employee = SQLManager.GetEmployeeByID(Project.EmployeeID)
        if Employee != None:
            EmployeeName = f"{Employee.Firstname} {Employee.Lastname}"
        Values = [f"{Counter + 1}", f"{Project.ID}", f"{EmployeeName}", f"{CustomerName}", f"{Project.Status}", f"เฟสที่ {Project.CurrentPhase}"]
        tableProject.insert('', END, values=Values)
        Counter += 1

def LoadTablePhase(Table : ttk.Treeview, Project : Project):
    for i in Table.get_children():
        Table.delete(i)
    for i in Project.Phases:
        Values = [Project.Phases[i].ID]
        Table.insert('', END, values=Values)

def LoadTableTemplate(Table : ttk.Treeview, Templates : list):
    for i in Table.get_children():
        Table.delete(i)
    Counter = 0
    for i in Templates:
        Template = Templates[i]
        Values = [f"{Counter + 1}", f"{Template.ID}", f"{Template.Type}", f"โครงการ {Template.ProjectID}" if int(Template.ProjectID) > 0 else "ไม่มีโครงการ", f"{Template.Draftman}", f"{Template.CreateDate}", f"{Template.AmountOfEdited}"]
        Table.insert('', END, values=Values)
        Counter += 1

def LoadTablePayment(Table : ttk.Treeview, Projects : list):
    for i in Table.get_children():
        Table.delete(i)
    Counter = 0
    for i in Projects:
        Project = Projects[i]
        EmployeeName = ""
        CustomerName = ""
        Employee = Employees.get(Project.EmployeeID)
        if Employee:
            EmployeeName = f"{Employee.Firstname} {Employee.Lastname}"
        else:
            EmployeeName = "ไม่พบข้อมูลผู้ดูแลโครงการ"
        Customer = Customers.get(Project.CustomerID)
        if Customer:
            CustomerName = f"{Customer.Firstname} {Customer.Lastname}"
        else:
            CustomerName = "ไม่พบข้อมูลลูกค้า"
        Values = [f"{Counter + 1}", f"{Project.ID}", f"{EmployeeName}", f"{CustomerName}", f"เฟสที่ {Project.CurrentPhase}"]
        Table.insert('', END, values=Values)
        Counter += 1

def OnAddCustomer():
    win = Toplevel(Window)
    win.title('เพิ่มลูกค้าใหม่')
    win.resizable(False,False)

    def OnClick():
        customer = Customer()
        customer.Firstname = fnameVar.get()
        customer.Lastname = lnameVar.get()
        customer.Email = emailVar.get()
        customer.CitizenID = citizenIDVar.get()
        customer.Phone = phoneVar.get()
        customer.Birthday = dobVar.get()

        address = Address()
        address.Type = "CUS"
        address.No = AddressNoVar.get()
        address.Mu = MooVar.get()
        address.Alley = alleyVar.get()
        address.Road = roadVar.get()
        address.City = cityVar.get()
        address.District = districtVar.get()
        address.Province = provinceVar.get()
        address.ProvinceZip = zipcodeVar.get()

        if not customer.check():
            return
        
        CustomerID = SQLManager.CreateCustomer(customer)
        customer.ID = CustomerID
        address.ID = CustomerID
        if SQLManager.UpdateCustomerAddressID(customer.ID, address.ID) and SQLManager.CreateAddress(address):
            customer.Address = address
            Customers.update({ customer.ID : customer })
            LoadTableCustomer(tableCustomer, Customers)
            messagebox.showinfo('สำเร็จ!',f'เพิ่มลูกค้าเข้าในระบบเรียบร้อยแล้ว')
            win.destroy()

    fnameVar = StringVar()
    lnameVar = StringVar()
    phoneVar = StringVar()
    citizenIDVar= StringVar()
    dobVar = StringVar()
    emailVar = StringVar()
    AddressNoVar = StringVar()
    MooVar = StringVar()
    alleyVar = StringVar()
    roadVar = StringVar()
    cityVar = StringVar()
    districtVar = StringVar()
    provinceVar = StringVar()
    zipcodeVar = StringVar()

    frame2 = Frame(win)
    frame2.grid(row=1,column=0, sticky='news', columnspan=2)
    frame2.columnconfigure(0, weight=1)
    frame2.columnconfigure(1, weight=1)
    frame2.rowconfigure((0,1), weight=1)
    detailFrame = LabelFrame(frame2, text=f"รายละเอียดลูกค้า")
    detailFrame.columnconfigure((0,2), weight=1)
    detailFrame.columnconfigure((1,3), weight=10)
    Label(detailFrame, text="ชื่อ : ").grid(row=1,column=0, sticky='e')
    Label(detailFrame, text="อีเมล : ").grid(row=2,column=0, sticky='e')
    Label(detailFrame, text="เบอร์โทรศัพท์ : ").grid(row=3,column=0, sticky='e')
    Label(detailFrame, text="นามสกุล : ").grid(row=1,column=2, sticky='e')
    Label(detailFrame, text="เลขบัตรประชาชน : ").grid(row=2,column=2, sticky='e')
    Label(detailFrame, text="วันเกิด : ").grid(row=3,column=2, sticky='e')
    fname = Entry(detailFrame, textvariable=fnameVar)
    fname.grid(row=1,column=1, sticky='we')
    email = Entry(detailFrame, textvariable=emailVar)
    email.grid(row=2,column=1, sticky='we')
    phone = Entry(detailFrame, textvariable=phoneVar)
    phone.grid(row=3,column=1, sticky='we')
    lname = Entry(detailFrame, textvariable=lnameVar)
    lname.grid(row=1,column=3, sticky='we', padx=10, pady=5)
    citizen_id = Entry(detailFrame, textvariable=citizenIDVar)
    citizen_id.grid(row=2,column=3, sticky='we', padx=10, pady=5)
    cal = DateEntry(detailFrame, bd=2, date_pattern=ENTRY_DATE_FORMAT, state='readonly')
    cal['textvariable'] = dobVar
    cal.grid(row=3, column=3,
            sticky='ew', padx=10)
    addressFrame = LabelFrame(frame2, text="ที่อยู่")
    subFrame = Frame(addressFrame)
    addressFrame.columnconfigure(0,weight=1)
    addressFrame.columnconfigure(1,weight=5)
    addressFrame.columnconfigure(2, weight=1)
    addressFrame.columnconfigure(3, weight=5)
    Label(addressFrame, text="บ้านเลขที่ : ").grid(row=0, column=0, sticky='e')
    Label(addressFrame, text="ถนน : ").grid(row=1,column=0, sticky='e', ipady=5)
    subFrame.columnconfigure((0,2), weight=4)
    subFrame.columnconfigure((1), weight=1)
    subFrame.rowconfigure(0, weight=1)
    Label(subFrame, text="หมู่ที่ : ").grid(row=0, column=1, sticky='e')
    NoEnt = Entry(subFrame,textvariable=AddressNoVar)
    NoEnt.grid(row=0, column=0, sticky='ew')
    Label(subFrame, text='ตำบล : ').grid(row=1, column=1, sticky='e')
    mooEnt = Entry(subFrame, textvariable=MooVar)
    mooEnt.grid(row=0, column=2, columnspan=2, sticky='ew')
    roadEnt = Entry(subFrame, textvariable=roadVar)
    roadEnt.grid(row=1, column=0, sticky='ew')
    cityEnt = Entry(subFrame, textvariable=cityVar)
    cityEnt.grid(row=1, column=2, sticky='ew')
    subFrame.grid(row=0, column=1, columnspan=1, sticky='ew', ipady=5, rowspan=2)
    Label(addressFrame, text="จังหวัด : ").grid(row=2,column=0, sticky='e', ipady=5)
    Label(addressFrame, text="ตรอก/ซอย : ").grid(row=0,column=2, sticky='e')
    Label(addressFrame, text="อำเภอ : ").grid(row=1,column=2, sticky='e')
    Label(addressFrame, text="รหัสไปรษณีย์ : ").grid(row=2,column=2, sticky='e',ipady=5)
    provinceEnt = ttk.Combobox(addressFrame, values=PROVINCES, textvariable=provinceVar, state="readonly")
    provinceEnt.current(1)
    provinceEnt.grid(row=2,column=1, sticky='ew')
    alleyEnt = Entry(addressFrame, textvariable=alleyVar)
    alleyEnt.grid(row=0,column=3, sticky='ew', padx=10)
    districtEnt = Entry(addressFrame, textvariable=districtVar)
    districtEnt.grid(row=1,column=3, sticky='ew', padx=10)
    zipcodeEnt = Entry(addressFrame, textvariable=zipcodeVar)
    zipcodeEnt.grid(row=2,column=3, sticky='ew', padx=10)
    arFrame = LabelFrame(frame2, text="เพิ่ม/ลบ")
    arFrame.columnconfigure((0,1), weight=1)
    arFrame.rowconfigure(0, weight=1)
    Button(arFrame, text = 'เพิ่ม', width=10, command=OnClick).grid(row=0, column=0, sticky='news', pady=10, padx=10)
    Button(arFrame, text = 'ปิด', width=10, command=lambda:win.destroy()).grid(row=0, column=1, sticky='news', pady=10, padx=10)
    detailFrame.grid(row=0, column=0, sticky='news', ipadx=10, ipady=10, padx=5, pady=5)
    addressFrame.grid(row=1, column=0, sticky='news', ipadx=10, ipady=10, padx=5, pady=5)
    arFrame.grid(row=1, column=1, sticky='news', ipadx=10, ipady=10, padx=5, pady=5)

def OnAddEmployee():
    win = Toplevel(Window)
    win.title('เพิ่มพนักงานใหม่')
    win.resizable(False,False)

    def OnClick():
        employee = Employee()
        employee.Firstname = fnameVar.get()
        employee.Lastname = lnameVar.get()
        employee.Position = positionVar.get()
        employee.CitizenID = citizenIDVar.get()
        employee.Phone = phoneVar.get()
        employee.Birthday = dobVar.get()

        address = Address()
        address.Type = "EMP"
        address.No = AddressNoVar.get()
        address.Mu = MooVar.get()
        address.Alley = alleyVar.get()
        address.Road = roadVar.get()
        address.City = cityVar.get()
        address.District = districtVar.get()
        address.Province = provinceVar.get()
        address.ProvinceZip = zipcodeVar.get()

        if not employee.check():
            return
        
        EmployeeID = SQLManager.CreateEmployee(employee)
        employee.ID = EmployeeID
        address.ID = EmployeeID
        if SQLManager.UpdateEmployeeAddressID(employee.ID, address.ID) and SQLManager.CreateAddress(address):
            employee.Address = address
            Employees.update({ employee.ID : employee })
            LoadTableEmployee(tableEmployee, Employees)
            messagebox.showinfo('สำเร็จ!',f'เพิ่มพนักงานเข้าในระบบเรียบร้อยแล้ว')
            win.destroy()

    fnameVar = StringVar()
    lnameVar = StringVar()
    phoneVar = StringVar()
    citizenIDVar= StringVar()
    dobVar = StringVar()
    positionVar = StringVar()
    AddressNoVar = StringVar()
    MooVar = StringVar()
    alleyVar = StringVar()
    roadVar = StringVar()
    cityVar = StringVar()
    districtVar = StringVar()
    provinceVar = StringVar()
    zipcodeVar = StringVar()

    frame2 = Frame(win)
    frame2.grid(row=1,column=0, sticky='news', columnspan=2)
    frame2.columnconfigure(0, weight=1)
    frame2.columnconfigure(1, weight=1)
    frame2.rowconfigure((0,1), weight=1)
    detailFrame = LabelFrame(frame2, text=f"รายละเอียดพนักงาน")
    detailFrame.columnconfigure((0,2), weight=1)
    detailFrame.columnconfigure((1,3), weight=10)
    Label(detailFrame, text="ชื่อ : ").grid(row=1,column=0, sticky='e')
    Label(detailFrame, text="ตำแหน่ง : ").grid(row=2,column=0, sticky='e')
    Label(detailFrame, text="เบอร์โทรศัพท์ : ").grid(row=3,column=0, sticky='e')
    Label(detailFrame, text="นามสกุล : ").grid(row=1,column=2, sticky='e')
    Label(detailFrame, text="เลขบัตรประชาชน : ").grid(row=2,column=2, sticky='e')
    Label(detailFrame, text="วันเกิด : ").grid(row=3,column=2, sticky='e')
    fname = Entry(detailFrame, textvariable=fnameVar)
    fname.grid(row=1,column=1, sticky='we')
    position = ttk.Combobox(detailFrame, textvariable=positionVar, values=POSITION_ALL, state="readonly")
    position.current(0)
    position.grid(row=2,column=1, sticky='we')
    phone = Entry(detailFrame, textvariable=phoneVar)
    phone.grid(row=3,column=1, sticky='we')
    lname = Entry(detailFrame, textvariable=lnameVar)
    lname.grid(row=1,column=3, sticky='we', padx=10, pady=5)
    citizen_id = Entry(detailFrame, textvariable=citizenIDVar)
    citizen_id.grid(row=2,column=3, sticky='we', padx=10, pady=5)
    cal = DateEntry(detailFrame, bd=2, date_pattern=ENTRY_DATE_FORMAT, state='readonly')
    cal['textvariable'] = dobVar
    cal.grid(row=3, column=3,
            sticky='ew', padx=10)
    addressFrame = LabelFrame(frame2, text="ที่อยู่")
    subFrame = Frame(addressFrame)
    addressFrame.columnconfigure(0,weight=1)
    addressFrame.columnconfigure(1,weight=5)
    addressFrame.columnconfigure(2, weight=1)
    addressFrame.columnconfigure(3, weight=5)
    Label(addressFrame, text="บ้านเลขที่ : ").grid(row=0, column=0, sticky='e')
    Label(addressFrame, text="ถนน : ").grid(row=1,column=0, sticky='e', ipady=5)
    subFrame.columnconfigure((0,2), weight=4)
    subFrame.columnconfigure((1), weight=1)
    subFrame.rowconfigure(0, weight=1)
    Label(subFrame, text="หมู่ที่ : ").grid(row=0, column=1, sticky='e')
    NoEnt = Entry(subFrame,textvariable=AddressNoVar)
    NoEnt.grid(row=0, column=0, sticky='ew')
    Label(subFrame, text='ตำบล : ').grid(row=1, column=1, sticky='e')
    mooEnt = Entry(subFrame, textvariable=MooVar)
    mooEnt.grid(row=0, column=2, columnspan=2, sticky='ew')
    roadEnt = Entry(subFrame, textvariable=roadVar)
    roadEnt.grid(row=1, column=0, sticky='ew')
    cityEnt = Entry(subFrame, textvariable=cityVar)
    cityEnt.grid(row=1, column=2, sticky='ew')
    subFrame.grid(row=0, column=1, columnspan=1, sticky='ew', ipady=5, rowspan=2)
    Label(addressFrame, text="จังหวัด : ").grid(row=2,column=0, sticky='e', ipady=5)
    Label(addressFrame, text="ตรอก/ซอย : ").grid(row=0,column=2, sticky='e')
    Label(addressFrame, text="อำเภอ : ").grid(row=1,column=2, sticky='e')
    Label(addressFrame, text="รหัสไปรษณีย์ : ").grid(row=2,column=2, sticky='e',ipady=5)
    provinceEnt = ttk.Combobox(addressFrame, values=PROVINCES, textvariable=provinceVar, state="readonly")
    provinceEnt.current(1)
    provinceEnt.grid(row=2,column=1, sticky='ew')
    alleyEnt = Entry(addressFrame, textvariable=alleyVar)
    alleyEnt.grid(row=0,column=3, sticky='ew', padx=10)
    districtEnt = Entry(addressFrame, textvariable=districtVar)
    districtEnt.grid(row=1,column=3, sticky='ew', padx=10)
    zipcodeEnt = Entry(addressFrame, textvariable=zipcodeVar)
    zipcodeEnt.grid(row=2,column=3, sticky='ew', padx=10)
    arFrame = LabelFrame(frame2, text="เพิ่ม/ลบ")
    arFrame.columnconfigure((0,1), weight=1)
    arFrame.rowconfigure(0, weight=1)
    Button(arFrame, text = 'เพิ่ม', width=10, command=OnClick).grid(row=0, column=0, sticky='news', pady=10, padx=10)
    Button(arFrame, text = 'ปิด', width=10, command=lambda:win.destroy()).grid(row=0, column=1, sticky='news', pady=10, padx=10)
    detailFrame.grid(row=0, column=0, sticky='news', ipadx=10, ipady=10, padx=5, pady=5)
    addressFrame.grid(row=1, column=0, sticky='news', ipadx=10, ipady=10, padx=5, pady=5)
    arFrame.grid(row=1, column=1, sticky='news', ipadx=10, ipady=10, padx=5, pady=5)

def OnAddOrEditProject(EditProject = False):
    win = Toplevel(Window)
    win.resizable(False,False)
    frame = Frame(win)
    ProjectID = CurrentProjectID.get()
    checkVar = BooleanVar()
    IsEdit = Checkbutton(frame, text="แก้ไขข้อมูล", variable=checkVar)
    Title = "เพิ่มโครงการ"
    if EditProject:
        Title = f'ดู/แก้ไขโครงการ : {ProjectID}'
        win.title(Title)
        Label(frame,text = Title).grid(row=0, column=0)
        IsEdit.grid(row=0, column=0, sticky="e", padx=20)
        checkVar.set(False)
    else:
        Label(frame,text = Title).grid(row=0, column=0)
        win.title(Title)
        checkVar.set(True)
    phaseFrame = Frame(frame)
    phaseFrame.grid(row=1, column=0, sticky='w',padx=10,pady=5)
    phaseFrame.columnconfigure((0,1,2,3), weight=1)

    phaseCount = IntVar()
    customerID = StringVar()
    dateProject = StringVar()
    budgetProject = DoubleVar()
    deedID = StringVar()
    portion = StringVar()
    no = StringVar()
    page = StringVar()
    province = StringVar()
    district = StringVar()
    city = StringVar()
    rai = StringVar()
    ngan = StringVar()
    wah = StringVar()
    employeeID = StringVar()
    buildingType = StringVar()
    demolishTime = StringVar()
    buildingTime = StringVar()
    company = StringVar()
    juristicID = StringVar()
    juristicPerson = StringVar()
    adrNo = StringVar()
    adrMu = StringVar()
    adrAlley = StringVar()
    adrRoad = StringVar()
    adrCity = StringVar()
    adrDistrict = StringVar()
    adrProvince = StringVar()
    adrProvinceZip = StringVar()

    project = SQLManager.GetProjectByID(ProjectID)
    if project != None and EditProject:
        phaseCount.set(project.PhaseCount)
        dateProject.set(project.DateProject)
        budgetProject.set(project.BudgetProject)
        deedID.set(project.DeedID)
        buildingType.set(project.BuildingType)
        demolishTime.set(project.DemolishTime)
        buildingTime.set(project.BuildingTime)
        company.set(project.Company)
        juristicID.set(project.JuristicID)
        juristicPerson.set(project.JuristicPerson)
        Customer = SQLManager.GetCustomerByID(project.CustomerID)
        if Customer:
            customerID.set(f"{Customer.ID:02}, {Customer.Firstname} {Customer.Lastname}")
        Employee = SQLManager.GetEmployeeByID(project.EmployeeID)
        if Employee:
            employeeID.set(f"{Employee.ID:02}, {Employee.Position}, {Employee.Firstname} {Employee.Lastname}")
        if project.Deed:
            portion.set(project.Deed.Portion)
            no.set(project.Deed.No)
            page.set(project.Deed.Page)
            province.set(project.Deed.Province)
            district.set(project.Deed.District)
            city.set(project.Deed.City)
            rai.set(project.Deed.Rai)
            ngan.set(project.Deed.Ngan)
            wah.set(project.Deed.Wah)
        if project.Address:
            adrNo.set(project.Address.No)
            adrMu.set(project.Address.Mu)
            adrAlley.set(project.Address.Alley)
            adrRoad.set(project.Address.Road)
            adrCity.set(project.Address.City)
            adrDistrict.set(project.Address.District)
            adrProvince.set(project.Address.Province)
            adrProvinceZip.set(project.Address.ProvinceZip)
    
    Label(phaseFrame, text = 'จำนวนเฟส').grid(row=1, column=0, sticky='w',padx=10)
    selectPhaseCount = ttk.Combobox(phaseFrame, textvariable=phaseCount, values=PHASE_ALL, state="readonly")
    if project == None or not EditProject:
        selectPhaseCount.current(0)
    selectPhaseCount.grid(row=1, column=1,padx=10)

    LENGTH_PHASE_ALL = int(PHASE_ALL[len(PHASE_ALL) - 1])
    PhasesTitle = [StringVar() for i in range(LENGTH_PHASE_ALL)]
    PhasesPercent = [DoubleVar() for i in range(LENGTH_PHASE_ALL)]

    settingPhase = Button(phaseFrame, text="ตั้งค่าเฟส", command=lambda:OnSettingPhase(phaseCount.get(), PhasesTitle, PhasesPercent), state=DISABLED if EditProject else NORMAL)
    settingPhase.grid(row=1, column=2, sticky='w',padx=10)
    customerFrame = LabelFrame(frame, text='ผู้ว่าจ้าง')
    customerFrame.columnconfigure((0,1,2,3), weight=0)

    Label(customerFrame, text = 'ค้นหาลูกค้า').grid(row=0, column=0, sticky='w',padx=10)
    Label(customerFrame, text = 'วันที่').grid(row=0, column=1, sticky='w',padx=10)
    Label(customerFrame, text = 'งบประมาณ').grid(row=0, column=2, columnspan=2, sticky='w',padx=10)
    selectCustomer = ttk.Combobox(customerFrame, values=[f"{Customer.ID:02}, {Customer.Firstname} {Customer.Lastname}" for Customer in Customers.values()], textvariable=customerID, state='readonly')
    selectCustomer.current(0)
    selectCustomer.grid(row=1, column=0,padx=10,pady=5)
    entryDateProject = DateEntry(customerFrame, bd=2, date_pattern=ENTRY_DATE_FORMAT, state='readonly')
    entryDateProject["textvariable"] = dateProject
    entryDateProject.grid(row=1, column=1,padx=10,pady=5)
    entryBudgetProject = Entry(customerFrame, textvariable=budgetProject)
    entryBudgetProject.grid(row=1, column=2, columnspan=2,padx=10,pady=5,sticky="nwes")

    Label(customerFrame, text = 'หมวดอาคาร').grid(row=2, column=0, sticky='w',padx=10)
    Label(customerFrame, text = 'ที่ดินโฉนดเลขที่').grid(row=2, column=1, sticky='w',padx=10)
    Label(customerFrame, text = 'ระวาง').grid(row=2, column=2, sticky='w',padx=10)
    Label(customerFrame, text = 'เลขที่ดิน').grid(row=2, column=3, sticky='w',padx=10)

    entryBuildingType = Entry(customerFrame, textvariable=buildingType)
    entryBuildingType.grid(row=3, column=0,padx=10,pady=5)
    entryDeedID = Entry(customerFrame, textvariable=deedID)
    entryDeedID.grid(row=3, column=1,padx=10,pady=5)
    entryPortion = Entry(customerFrame, textvariable=portion)
    entryPortion.grid(row=3, column=2,padx=10,pady=5)
    entryNo = Entry(customerFrame, textvariable=no)
    entryNo.grid(row=3, column=3,padx=10,pady=5)

    Label(customerFrame, text = 'หน้าสำรวจ').grid(row=4, column=0, sticky='w',padx=10)
    Label(customerFrame, text = 'จังหวัด').grid(row=4, column=1, sticky='w',padx=10)
    Label(customerFrame, text = 'อำเภอ/เขต').grid(row=4, column=2, sticky='w',padx=10)
    Label(customerFrame, text = 'ตำบล/แขวง').grid(row=4, column=3, sticky='w',padx=10)

    entryPage = Entry(customerFrame, textvariable=page)
    entryPage.grid(row=5, column=0,padx=10,pady=5)
    entryProvince = ttk.Combobox(customerFrame, values=PROVINCES, textvariable=province, state="readonly")
    entryProvince.current(1)
    entryProvince.grid(row=5, column=1,padx=10,pady=5)
    entryDistrict = Entry(customerFrame, textvariable=district)
    entryDistrict.grid(row=5, column=2,padx=10,pady=5)
    entryCity = Entry(customerFrame, textvariable=city)
    entryCity.grid(row=5, column=3,padx=10,pady=5)

    areaFrame = LabelFrame(customerFrame, text='เนื้อที่ประมาณ')
    areaFrame.columnconfigure((0,1,2), weight=1)

    Label(areaFrame, text = '\nไร่').grid(row=0, column=0, sticky='w',padx=10)
    Label(areaFrame, text = '\nงาน').grid(row=0, column=1, sticky='w',padx=10)
    Label(areaFrame, text = '\nตารางวา').grid(row=0, column=2, sticky='w',padx=10)
  
    entryRai = Entry(areaFrame, textvariable=rai)
    entryRai.grid(row=1, column=0,padx=10,pady=5, sticky='news')
    entryNgan = Entry(areaFrame, textvariable=ngan)
    entryNgan.grid(row=1, column=1,padx=10,pady=5, sticky='news')
    entryWah = Entry(areaFrame, textvariable=wah)
    entryWah.grid(row=1, column=2,padx=10,pady=5, sticky='news')
    areaFrame.grid(row=6, column=0,columnspan=4,padx=10,pady=5, sticky='news')

    customerFrame.grid(row=2, column=0, sticky='news',padx=22,pady=5)
    
    contractorFrame = LabelFrame(frame, text='ผู้ว่าจ้าง')
    contractorFrame.columnconfigure((0,1), weight=1)

    Label(contractorFrame, text = '\nบริษัท').grid(row=0, column=0, sticky='w',padx=10)
    Label(contractorFrame, text = '\nผู้ดูแลโครงการ').grid(row=0, column=1, sticky='w',padx=10)

    entryCompany = Entry(contractorFrame, textvariable=company)
    entryCompany.grid(row=1, column=0,padx=10,pady=5, sticky='news')
    selectEmployee = ttk.Combobox(contractorFrame, values=[f"{Employee.ID:02}, {Employee.Position}, {Employee.Firstname} {Employee.Lastname}" for Employee in Employees.values()], textvariable=employeeID, state='readonly')
    selectEmployee.grid(row=1, column=1,padx=10,pady=5, sticky='news')

    Label(contractorFrame, text = 'ระยะเวลายื่นแบบ').grid(row=2, column=0, sticky='w',padx=10)
    Label(contractorFrame, text = 'ระยะเวลาที่ใช้ในการดำเนินการก่อสร้าง').grid(row=2, column=1, sticky='w',padx=10)

    entryDemolishTime = Entry(contractorFrame, textvariable=demolishTime)
    entryDemolishTime.grid(row=3, column=0,padx=10,pady=5, sticky='news')
    entryBuildingTime = Entry(contractorFrame, textvariable=buildingTime)
    entryBuildingTime.grid(row=3, column=1,padx=10,pady=5, sticky='news')

    Label(contractorFrame, text = 'ทะเบียนนิติบุคคล เลขที่').grid(row=4, column=0, sticky='w',padx=10)
    Label(contractorFrame, text = 'กรรมการผู้มีอำนาจ').grid(row=4, column=1, sticky='w',padx=10)

    entryJuristicID = Entry(contractorFrame, textvariable=juristicID)
    entryJuristicID.grid(row=5, column=0,padx=10,pady=5, sticky='news')
    entryJuristicPerson = Entry(contractorFrame, textvariable=juristicPerson)
    entryJuristicPerson.grid(row=5, column=1,padx=10,pady=5, sticky='news')

    locationFrame = LabelFrame(contractorFrame, text='ที่อยู่สำนักงาน')
    locationFrame.columnconfigure((0,1,2,3), weight=1)

    Label(locationFrame, text = '\nเลขที่').grid(row=0, column=0, sticky='w',padx=10)
    Label(locationFrame, text = '\nหมู่ที่').grid(row=0, column=1, sticky='w',padx=10)
    Label(locationFrame, text = '\nตรอก/ซอย').grid(row=0, column=2, sticky='w',padx=10)
    Label(locationFrame, text = '\nถนน').grid(row=0, column=3, sticky='w',padx=10)

    entryAdrNo = Entry(locationFrame, textvariable=adrNo)
    entryAdrNo.grid(row=1, column=0,padx=10,pady=5)
    entryAdrMu = Entry(locationFrame, textvariable=adrMu)
    entryAdrMu.grid(row=1, column=1,padx=10,pady=5)
    entryAdrAlley = Entry(locationFrame, textvariable=adrAlley)
    entryAdrAlley.grid(row=1, column=2,padx=10,pady=5)
    entryAdrRoad = Entry(locationFrame, textvariable=adrRoad)
    entryAdrRoad.grid(row=1, column=3,padx=10,pady=5)

    Label(locationFrame, text = 'ตำบล/แขวง').grid(row=2, column=0, sticky='w',padx=10)
    Label(locationFrame, text = 'อำเภอ/เขต').grid(row=2, column=1, sticky='w',padx=10)
    Label(locationFrame, text = 'จังหวัด').grid(row=2, column=2, sticky='w',padx=10)
    Label(locationFrame, text = 'รหัสไปรษณีย์').grid(row=2, column=3, sticky='w',padx=10)

    entryAdrCity = Entry(locationFrame, textvariable=adrCity)
    entryAdrCity.grid(row=3, column=0,padx=10,pady=5)
    entryAdrDistrict = Entry(locationFrame, textvariable=adrDistrict)
    entryAdrDistrict.grid(row=3, column=1,padx=10,pady=5)
    entryAdrProvince = ttk.Combobox(locationFrame, values=PROVINCES, textvariable=adrProvince, state="readonly")
    entryAdrProvince.current(1)
    entryAdrProvince.grid(row=3, column=2,padx=10,pady=5)
    entryAdrProvinceZip = Entry(locationFrame, textvariable=adrProvinceZip)
    entryAdrProvinceZip.grid(row=3, column=3,padx=10,pady=5)

    EntriesAll = [selectPhaseCount, selectCustomer, entryDateProject, entryBudgetProject, entryBuildingType, 
                   entryDeedID, entryPortion, entryNo, entryPage, entryProvince, entryDistrict, entryCity, 
                   entryRai, entryNgan, entryWah, entryCompany, selectEmployee, entryDemolishTime, entryBuildingTime, 
                   entryJuristicID, entryJuristicPerson, entryAdrNo, entryAdrMu, entryAdrAlley, entryAdrRoad, 
                   entryAdrCity, entryAdrDistrict, entryAdrProvince, entryAdrProvinceZip]
    
    EntriesEnabled = [selectCustomer, entryDateProject, entryBudgetProject, entryBuildingType, 
                   entryDeedID, entryPortion, entryNo, entryPage, entryProvince, entryDistrict, entryCity, 
                   entryRai, entryNgan, entryWah, entryCompany, selectEmployee, entryDemolishTime, entryBuildingTime, 
                   entryJuristicID, entryJuristicPerson, entryAdrNo, entryAdrMu, entryAdrAlley, entryAdrRoad, 
                   entryAdrCity, entryAdrDistrict, entryAdrProvince, entryAdrProvinceZip]

    locationFrame.grid(row=6, column=0,columnspan=2,padx=10,pady=5)
    contractorFrame.grid(row=3, column=0, sticky='news',padx=22,pady=5)
    buttonFrame = Frame(frame)
    if EditProject:
        btnPrint = Button(buttonFrame, text = 'พิมพ์สัญญา', width=20, command=lambda:saveContact())
        btnPrint.grid(row=0, column=0, sticky='e')
    btnSave = Button(buttonFrame, text = 'บันทึก', width=20, command=lambda:OnCreateOrSaveProject(EditProject), state=DISABLED)
    btnSave.grid(row=0, column=1, sticky='e')
    buttonFrame.grid(row=4, column=0, sticky="e", padx=20, pady=10)

    def EntriesChangeState(Entries : list):
        if checkVar.get():
            for Entry in Entries:
                Entry["state"] = NORMAL
            btnSave["state"] = NORMAL
        else:
            for Entry in Entries:
                Entry["state"] = DISABLED
            btnSave["state"] = DISABLED
    
    EntriesChangeState(EntriesAll)

    def OnClickCheckbox():
        EntriesChangeState(EntriesEnabled)
            

    IsEdit["command"] = OnClickCheckbox

    def saveContact():
        projectID = CurrentProjectID.get()
        project_info = SQLManager.GetProjectByID(projectID)
        customer_info = SQLManager.GetCustomerByID(project_info.CustomerID)
        di = filedialog.askdirectory(initialdir=CURRENT_DIRECTORY)
        if projectContact(customer_info, project_info,di):
            messagebox.showinfo('สำเร็จ!','พิมสัญญาสำเร็จ')
        else:
            messagebox.showerror('ล้มเหลว!','พิมสัญญาไม่สำเร็จ')

    def OnCreateOrSaveProject(Edited = False):
        listValue = [phaseCount.get(), customerID.get(), dateProject.get(), budgetProject.get(),deedID.get(), portion.get(), no.get(), page.get(), province.get(), district.get(), 
                     city.get(), rai.get(), ngan.get(), wah.get(), employeeID.get(), buildingType.get(), demolishTime.get(), buildingTime.get(), company.get(), juristicID.get(), 
                     juristicPerson.get(), adrNo.get(), adrMu.get(), adrAlley.get(), adrRoad.get(), adrRoad.get(), adrDistrict.get(), adrProvince.get(), adrProvinceZip.get()]
        listValuePhase = [[PhasesTitle[i].get() for i in range(phaseCount.get())], [PhasesPercent[i].get() for i in range(phaseCount.get())]]

        entryCounter, entryPhaseCounter = 0, 0
        for i in listValuePhase:
            for j in i:
                if isinstance(j, str) and (j == "" or len(j) == 0):
                    entryPhaseCounter += 1
                elif isinstance(j, float) and float(j) == 0.0:
                    entryPhaseCounter += 1 
        for i in listValue:
            if isinstance(i, str) and (i == "" or len(i) == 0):
                entryCounter += 1
            elif isinstance(i, float) and float(i) == 0.0:
                entryCounter += 1
            elif isinstance(i, int) and int(i) == 0:
                entryCounter += 1
        if not EditProject and entryPhaseCounter != 0 or len(PhasesTitle) == 0 or len(PhasesPercent) == 0:
            messagebox.showwarning("คำเตือน!", "กรุณากรอกข้อมูลการตั้งค่าของเฟสให้ครบถ้วน")
            win.focus()
            return
        
        if entryCounter != 0:
            messagebox.showwarning("คำเตือน!", "กรุณากรอกข้อมูลของโครงการให้ครบถ้วน")
            win.focus()
            return

        cusID = int(customerID.get().split(", ")[0])
        empID = int(employeeID.get().split(", ")[0])

        if not Edited:
            project = Project()
            project.CustomerID = cusID
            project.DateProject = dateProject.get()
            project.BuildingType = buildingType.get()
            project.BudgetProject = budgetProject.get()
            project.DeedID = deedID.get()
            project.EmployeeID = empID
            project.DemolishTime = demolishTime.get()
            project.BuildingTime = buildingTime.get()
            project.JuristicID = juristicID.get()
            project.JuristicPerson = juristicPerson.get()
            project.PhaseCount = phaseCount.get()
            project.Company = company.get()
            project.Status = PROJECT_STATUS_ALL.get(1)
            project.CurrentPhase = 1

            deed = Deed()
            deed.ID = deedID.get()
            deed.Portion = portion.get()
            deed.No = no.get()
            deed.Page = page.get()
            deed.Province = province.get()
            deed.District = district.get()
            deed.City = city.get()
            deed.Rai = rai.get()
            deed.Ngan = ngan.get()
            deed.Wah = wah.get()

            address = Address()
            address.Type = "PRO"
            address.No = adrNo.get()
            address.Mu = adrMu.get()
            address.Alley = adrAlley.get()
            address.Road = adrRoad.get()
            address.City = adrCity.get()
            address.District = adrDistrict.get()
            address.Province = adrProvince.get()
            address.ProvinceZip = adrProvinceZip.get()

            project.Address = address
            project.Deed = deed

            if not project.check():
                return

            ProjectID = SQLManager.CreateProject(project)
            if ProjectID > 0:
                project.ID = ProjectID
                project.AddressID = ProjectID
                address.ID = project.AddressID
                ProjectRoot = CreateDirectory(f"{project.ID}", "Projects")
                if SQLManager.UpdateProjectAddressID(project.ID, project.AddressID):
                    if SQLManager.CreateDeed(deed) and SQLManager.CreateAddress(address):
                        Phases = {}
                        PhaseRoot = CreateDirectory("Phases", ProjectRoot)
                        for i in range(project.PhaseCount):
                            phase = Phase()
                            phase.ID = i + 1
                            phase.ProjectID = ProjectID
                            phase.EmployeeID = project.EmployeeID
                            phase.Path = CreateDirectory(f"{i + 1}", PhaseRoot)
                            phase.Start = "-"
                            phase.End = "-"
                            phase.Title = PhasesTitle[i].get()
                            phase.CollectionPercent = PhasesPercent[i].get()
                            if i == 0:
                                phase.Status = PHASE_STATUS_ALL.get(1)
                                phase.DueDate = (datetime.now() + timedelta(weeks=2)).strftime(DATE_FORMAT)
                            else:
                                phase.Status = PHASE_STATUS_ALL.get(0)
                            SQLManager.CreatePhase(project, phase)
                            Phases.update({ phase.ID : phase })
                        project.Phases = Phases
                        Projects.update({ project.ID : project })
                        messagebox.showinfo("สำเร็จ!", "เพิ่มโครงงานสำเร็จ")
        else:
            ProjectID = CurrentProjectID.get()
            project = Projects.get(ProjectID)
            if project:
                OldDeedID = project.DeedID
                project.CustomerID = cusID
                project.DateProject = dateProject.get()
                project.BuildingType = buildingType.get()
                project.BudgetProject = budgetProject.get()
                project.DeedID = deedID.get()
                project.EmployeeID = empID
                project.DemolishTime = demolishTime.get()
                project.BuildingTime = buildingTime.get()
                project.JuristicID = juristicID.get()
                project.JuristicPerson = juristicPerson.get()
                project.PhaseCount = phaseCount.get()
                project.Company = company.get()
                deed = project.Deed
                if deed:
                    deed.ID = deedID.get()
                    deed.Portion = portion.get()
                    deed.No = no.get()
                    deed.Page = page.get()
                    deed.Province = province.get()
                    deed.District = district.get()
                    deed.City = city.get()
                    deed.Rai = rai.get()
                    deed.Ngan = ngan.get()
                    deed.Wah = wah.get()
                address = project.Address
                if address:
                    address.No = adrNo.get()
                    address.Mu = adrMu.get()
                    address.Alley = adrAlley.get()
                    address.Road = adrRoad.get()
                    address.City = adrCity.get()
                    address.District = adrDistrict.get()
                    address.Province = adrProvince.get()
                    address.ProvinceZip = adrProvinceZip.get()

                if not project.check():
                    return
                
                if SQLManager.UpdateProject(project) and SQLManager.UpdateAddress("PRO", address) and SQLManager.UpdateDeed(deed, OldDeedID) and SQLManager.UpdateDeedID(OldDeedID, deed.ID):
                    project.DeedID = deed.ID
                    messagebox.showinfo("สำเร็จ!", "แก้ไขโครงงานสำเร็จ")
        LoadTableProject(tableProject, Projects)
        win.destroy()
        win.update()
    frame.grid(row=0, column=0, sticky='news')

def OnDeleteCustomer():
    if not bool(tableCustomer.selection()):
        messagebox.showwarning('ลบลูกค้า','โปรดเลือกข้อมูลที่ต้องการลบก่อน')
        return
    for Item in tableCustomer.selection():
        Values = tableCustomer.item(Item)['values']
        ID = Values[1]
        Name = Values[2]
        if messagebox.askquestion('ลบลูกค้า',f'คุณแน่ใจที่ต้องการจะลบใช่ไหม?\nไอดีลูกค้า : {ID} ชื่อ : {Name} ') == 'yes':
            if SQLManager.DeleteCustomer(ID) and SQLManager.DeleteAddress(ID, "CUS"):
                Customers.pop(ID)
                LoadTableCustomer(tableCustomer, Customers)
                messagebox.showinfo('สำเร็จ!', f'ไอดีลูกค้า: {ID} ถูกลบเรียบร้อย')

def OnDeleteEmployee():
    if not bool(tableEmployee.selection()):
        messagebox.showwarning('ลบพนักงาน','โปรดเลือกข้อมูลที่ต้องการลบก่อน')
        return
    for Item in tableEmployee.selection():
        Values = tableEmployee.item(Item)['values']
        ID = Values[1]
        Name = Values[3]
        if messagebox.askquestion('ลบพนักงาน',f'คุณแน่ใจที่จะลบข้อมูลนี้?\nไอดีพนักงาน : {ID} ชื่อ : {Name} ') == 'yes':
            if SQLManager.DeleteEmployee(ID) and SQLManager.DeleteAddress(ID, "EMP"):
                Employees.pop(ID)
                LoadTableEmployee(tableEmployee, Employees)
                messagebox.showinfo('สำเร็จ!', f'ไอดีพนักงาน: {ID} ถูกลบเรียบร้อย')

def OnDeleteProject(ID : int):
    if ID == 0:
        messagebox.showwarning("คำเตือน!", "กรุณาเลือกโครงการก่อน")
    if messagebox.askquestion('ลบโครงการ',f'คุณแน่ใจที่จะลบข้อมูลนี้?\nไอดีโครงการ : {ID}') == 'yes':
        Project = SQLManager.GetProjectByID(ID)
        if Project != None and SQLManager.DeleteProject(ID) and SQLManager.DeleteDeed(Project.DeedID) and SQLManager.DeletePhase(ID) and SQLManager.DeleteAddress(Project.AddressID, "PRO"):
            Template = Templates.get(Project.TemplateID)
            if Template:
                if SQLManager.UpdateTemplateProjectID(Template.ID, -1):
                    Template.ProjectID = -1
            Projects.pop(ID)
            RemoveDirectory(f"{ID}", "Projects")
            LoadTableProject(tableProject, Projects)
            CurrentProjectID.set(0)
            phaseManagement["state"] = DISABLED
            deleteProject["state"] = DISABLED
            editProject["state"] = DISABLED
            messagebox.showinfo('สำเร็จ!', f'ไอดีโครงงาน: {ID} ถูกลบเรียบร้อย')

def OnSettingPhase(PhaseCount : int, PhasesTitle : list, PhasesPercent : list):
        win = Toplevel(Window)
        win.title("ตั้งค่าเฟสของโครงการ")
        win.resizable(False, False)
        Setting = Frame(win)
        Setting.columnconfigure((0, 1, 2), weight=1)
        Row, Column = 0, 0
        for i in range(PhaseCount):
            Block = LabelFrame(Setting, text=f"เฟสที่ {i + 1} : ")
            Block.columnconfigure((0, 1), weight=1)
            Label(Block, text="ชื่อเฟส").grid(row=i, column=0, pady=5)
            Label(Block, text="เปอร์เซ็นในการเรียกเก็บเงิน").grid(row=i, column=1, padx=5)
            Entry(Block, textvariable=PhasesTitle[i]).grid(row=i + 1, column=0, padx=5, pady=5)
            Entry(Block, textvariable=PhasesPercent[i]).grid(row=i + 1, column=1, padx=5, pady=5)
            Block.grid(row=Row, column=Column, padx=10, pady=10)
            Column += 1
            if Column == 3:
                Row += 1
                Column = 0

        def OnSave():
            EntryCounter = 0
            for i in range(PhaseCount):
                if isinstance(PhasesTitle[i].get(), str) and (PhasesTitle[i].get() == "" or len(PhasesTitle[i].get()) == 0):
                    EntryCounter += 1
            for i in range(PhaseCount):
                if isinstance(PhasesPercent[i].get(), float) and float(PhasesPercent[i].get()) == 0.0:
                    EntryCounter += 1
            if EntryCounter != 0:
                messagebox.showwarning("คำเตือน!", "กรุณากรอกข้อมูลการตั้งค่าของเฟสให้ครบถ้วน")
                win.focus()
            else:
                Maximum = 0
                for i in range(PhaseCount):
                    Maximum += PhasesPercent[i].get()
                if Maximum == 100:
                    messagebox.showinfo("สำเร็จ!", "บันทึกข้อมูลการตั้งค่าเฟสสำเร็จ")
                    win.destroy()
                else:
                    messagebox.showwarning("คำเตือน!", "กรุณากรอกข้อมูลการตั้งค่าเปอร์เซ็นของเฟสให้เท่ากับ 100%")
                    win.focus()

        Button(Setting, text="บันทึก", command=OnSave).grid(row=Row + 1, column=1, sticky="news", padx=10, ipady=10)
        Setting.grid(row=0, column=0, sticky="news", padx=10, pady=10)

def CreateDirectoryAll():
    for Directory in DIRECTORY_LIST:
        CreateDirectory(Directory)

def CreateDirectory(Name : str, Path : str = ""):
    try:
        current_directory = os.path.join(CURRENT_DIRECTORY, Path)
        final_directory = os.path.join(current_directory, Name)
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)
        return final_directory
    except OSError as ex:
        print(f"Error occured: {Path}\{Name} : {ex.strerror}")

def RemoveDirectory(Name : str, Path : str = ""):
    try:
        current_directory = os.path.join(CURRENT_DIRECTORY, Path)
        final_directory = os.path.join(current_directory, Name)
        if os.path.exists(final_directory):
            shutil.rmtree(final_directory)
    except OSError as ex:
        messagebox.showerror("พบข้อผิดพลาด!", f"Error occured: {Path}\{Name} : {ex.strerror}")

def OpenFileByPath(Path : str):
    if Path == "":
        return
    os.startfile(Path)

def GetProjectsByState():
    Result = {}
    for Project in Projects.values():
        Phase = Project.Phases.get(Project.CurrentPhase)
        if Phase and Phase.Status == PHASE_STATUS_ALL.get(1):
            Result.update({ Project.ID : Project })
    return Result

def ProjectReport():
    a = Toplevel()
    a.geometry('400x100')
    a.resizable(0,0)
    a.rowconfigure(0, weight=0)
    a.rowconfigure(1, weight=1)
    a.columnconfigure(0, weight=1)
    frame = Frame(a)
    frame.rowconfigure((0,1), weight=1)
    frame.columnconfigure((0), weight=1)
    frame.columnconfigure((1), weight=2)
    frame.columnconfigure((2), weight=1)

    date_start = StringVar()
    durationVar = IntVar(value=3)
    Label(frame, text='วันที่เริ่มต้น : ').grid(row=0, column = 0, sticky='news')
    cal = DateEntry(frame, bd=2, date_pattern=ENTRY_DATE_FORMAT, state='readonly')
    cal['textvariable'] = date_start
    cal.grid(row=0,column=1, sticky='ew')
    box = ttk.Combobox(frame, values=[3,6,9,12], textvariable=durationVar, state='readonly')
    box.grid(row=1, column =1, sticky='ew')


    pathVar = StringVar()
    def getD():
        pathVar.set(filedialog.askdirectory(initialdir=CURRENT_DIRECTORY))
    pathVar.set(CURRENT_DIRECTORY)
    Button(frame, text='เลือก Path', command = getD).grid(row=2, column=0, padx=2, pady=2)
    Entry(frame, state='readonly', textvariable=pathVar,).grid(row=2, column=1, sticky='ew')



    def PrintReport():
        data = [date_start.get(),durationVar.get(),pathVar.get()]
        if data[0] == '':
            return messagebox.showerror('ล้มเหลว!','ข้อมูลการจัดพิมพ์รายงานไม่ครบถ้วน\nกรุณาเช็คข้อมูลอีกครั้ง')
        try:
            report = projectProgressionReport(data[0], data[1])
            if saveReport(report, pathVar.get(),f'Project_Progreesion_Report_{date.today()}'):
                messagebox.showinfo('สำเร็จ!','พิมรายงานความคืบหน้าโครงการสำเร็จ')
        except:
            messagebox.showerror('ล้มเหลว!','พิมพ์รายงานล้มเหลว')
        

    Button(frame, text='พิมพ์', command =PrintReport).grid(row=0, column = 2, sticky='news', rowspan=3, ipadx=10, padx=10, pady=10)
    
    Label(a, text='พิมพ์รายงานความคืบหน้าโครงการ').grid(row=0,column=0)
    frame.grid(row=1, column=0, padx=5,pady=5, sticky='news')

Employees = SQLManager.LoadEmployees()
Customers = SQLManager.LoadCustomers()
Projects = SQLManager.LoadProjects()
Templates = SQLManager.LoadTemplates()

DATE_FORMAT = "%Y-%m-%d"
DATE_FILE_FORMAT = "%Y-%m-%d_%H-%M-%S"
ENTRY_DATE_FORMAT = "yyyy-MM-dd"
POSITION_ALL = ["กรรมการ", "ผู้จัดการ", "บัญชี", "วิศวกร", "ผู้ดูแลระบบ", "ช่างไฟ", "ช่างไม้", "ช่างประปา", "ช่างปูน"]
PHASE_ALL = ["3", "4", "5", "6", "7", "8", "9", "10"]
PROJECT_STATUS_ALL = { 0 : "ยังไม่ดำเนินการ", 1 : "กำลังดำเนินการ", 2 : "ดำเนินการเสร็จสิ้น"}
PHASE_STATUS_ALL = { 0 : "ยังไม่เริ่มเฟส", 1 : "รอการชำระเงิน", 2 : "รับชำระเงิน", 3 : "เริ่มเฟส", 4 : "อยู่ระหว่างการดำเนินการ", 5 : "ดำเนินการงานเฟสเสร็จสิ้น", 6 : "สิ้นสุดเฟส" }
DIRECTORY_LIST = ["Templates", "Projects", "Reports", "Payments"]
PROVINCES = ["กระบี่", "กรุงเทพมหานคร", "กาญจนบุรี", "กาฬสินธุ์", "กำแพงเพชร",
             "ขอนแก่น", "จันทบุรี", "ฉะเชิงเทรา", "ชลบุรี", "ชัยนาท", "ชัยภูมิ",
             "ชุมพร", "เชียงราย", "เชียงใหม่", "ตรัง", "ตราด", "ตาก", "นครนายก",
             "นครปฐม", "นครพนม", "นครราชสีมา", "นครศรีธรรมราช", "นครสวรรค์", "นนทบุรี",
             "นราธิวาส", "น่าน", "บึงกาฬ", "บุรีรัมย์", "ปทุมธานี", "ประจวบคีรีขันธ์",
             "ปราจีนบุรี", "ปัตตานี", "พระนครศรีอยุธยา", "พะเยา", "พังงา", "พัทลุง",
             "พิจิตร", "พิษณุโลก", "เพชรบุรี", "เพชรบูรณ์", "แพร่", "ภูเก็ต", "มหาสารคาม",
             "มุกดาหาร", "แม่ฮ่องสอน", "ยโสธร", "ยะลา", "ร้อยเอ็ด", "ระนอง", "ระยอง",
             "ราชบุรี", "ลพบุรี", "ลำปาง", "ลำพูน", "เลย", "ศรีสะเกษ", "สกลนคร",
             "สงขลา", "สตูล", "สมุทรปราการ", "สมุทรสงคราม", "สมุทรสาคร", "สระแก้ว",
             "สระบุรี", "สิงห์บุรี", "สุโขทัย", "สุพรรณบุรี", "สุราษฎร์ธานี",
             "สุรินทร์", "หนองคาย", "หนองบัวลำภู", "อ่างทอง", "อุดรธานี","อุทัยธานี","อุตรดิตถ์",
             "อุบลราชธานี","อำนาจเจริญ"]

CURRENT_DIRECTORY = os.getcwd()

Window = Tk()
Width = 1280
Height = 720
X = Window.winfo_screenwidth() / 2 - Width / 2
Y = Window.winfo_screenheight() / 2 - Height / 2
Window.title("JRS House Constructor")
Window.geometry("%dx%d+%d+%d" % (Width, Height, X, Y))
CurrentProjectID = IntVar()
employeeIcon = PhotoImage(file = './Picture/Icon/employee.png').subsample(11,11)
CreateDirectoryAll()
curWindow = Login()
curWindow.grid(row=0, column=0)
Window.columnconfigure(0,weight=1)
Window.rowconfigure(0,weight=1)
Window.mainloop()