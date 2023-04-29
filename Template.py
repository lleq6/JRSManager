from tkinter import messagebox
from regexCheck import *

class Template:
    ID = 0
    Type = ""
    Path = ""
    Draftman = ""
    ProjectID = 0
    CreateDate = ""
    AmountOfEdited = 0

    def check(self):
        if not checkJuristic(self.Draftman) or not checkJuristic(self.Type):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก  ประเภทและผู้เขียนแบบ')
            return False
        elif not checkJuristic(self.Draftman) or not checkJuristic(self.Type):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก ประเภทและผู้เขียนแบบ ด้วยตัวอักษร')
            return False
        
        return True