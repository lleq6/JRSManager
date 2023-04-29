from datetime import *
from tkinter import messagebox
from Phase import Phase
from Deed import Deed
from Address import Address
from regexCheck import *

class Project:
    ID = 0
    CustomerID = 0
    DateProject = ""
    BuildingType = ""
    BudgetProject = 0.0
    DeedID = 0
    EmployeeID = 0
    DemolishTime = ""
    BuildingTime = ""
    JuristicID = ""
    JuristicPerson = ""
    AddressID = 0
    TemplateID = 0
    PhaseCount = 0
    Status = ""
    Company = ""
    CurrentPhase = 0
    Phases = { 0 : Phase() }
    Deed = Deed()
    Address = Address()

    def GetProgress(self):
        Counter = 0
        for Phase in self.Phases.values():
            if Phase.Status == "สิ้นสุดเฟส":
                Counter += 1
        return (Counter * 100) / len(self.Phases)
    
    def NextPhase(self):
        self.CurrentPhase += 1
        return self.CurrentPhase
    
    
    def check(this):
        if not checkEmpty(this.BudgetProject):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก งบประมาณ')
            return False
        elif not checkInt(this.BudgetProject):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอกงบประมาณที่เป็นตัวเลขเท่านั้น')
            return False
        
        if not checkEmpty(this.BuildingType):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก หมวดอาคาร ')
            return False
        
        if not checkEmpty(this.Company):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก บริษัท')
            return False
        
        if not checkEmpty(this.BuildingTime):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก ระยะเวลาที่ใช้ในการดำเนินการก่อสร้าง')
            return False
        elif not checkInt(this.BuildingTime):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอกระยะเวลาที่ใช้ในการดำเนินการก่อสร้างที่เป็นตัวเลขเท่านั้น')
            return False

        if not checkEmpty(this.JuristicID):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก ทะเบียนนิติบุคคลเลขที่')
            return False
        elif not checkInt(this.JuristicID):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอกทะเบียนนิติบุคคลเลขที่ ที่เป็นตัวเลขเท่านั้น')
            return False
        elif not checkCitizenID(this.JuristicID):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอกทะเบียนนิติบุคคล 13 หลัก')
            return False
        
        if not checkEmpty(this.JuristicPerson):
            messagebox.showerror('ข้อมูลผิดพลาด','กกรุณากรอก  กรรมการผู้มีอำนาจ')
            return False
        elif not checkJuristic(this.JuristicPerson):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก กรรมการผู้มีอำนาจ ด้วยตัวอักษร')
            return False
        
        if not this.Deed.check():
            return False
        if not this.Address.check():

            return False
    
        return True

