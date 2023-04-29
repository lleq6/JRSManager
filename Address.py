from tkinter import messagebox
from regexCheck import *


class Address:
    ID = 0
    Type = ""
    No = ""
    Mu = ""
    Alley = ""
    Road = ""
    City = ""
    District = ""
    Province = ""
    ProvinceZip = 0

    def check(this):
        if not checkEmpty(this.No):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก บ้านเลขที่')
            return False
        if not checkEmpty(this.Mu):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก หมู่ที่')
            return False
        elif not checkInt(this.Mu):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก หมู่ที่ด้วยตัวเลข')
            return False
        if not checkEmpty(this.Alley):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก ตรอก/ซอย')
            return False
        
        for i in [this.Road, this.City, this.District]:
            if not checkEmpty(i):
                messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก  ถนน, ตำบลและอำเภอ')
                return False
            elif not checkThaiLanguage(i):
                messagebox.showerror('ข้อมูลผิดพลาด','กรุณา ถนน, ตำบลและอำเภอ  ด้วยตัวอักษรภาษาไทย')
                return False
        
        if not checkEmpty(this.ProvinceZip):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก   รหัสไปรษณีย์')
            return False
        if not checkZip(this.ProvinceZip):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอกรหัสไปรษณีย์ 5 หลัก')
            return False
        
        return True