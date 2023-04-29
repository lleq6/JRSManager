from tkinter import messagebox
from Address import *
from regexCheck import *

class Employee:
    ID = 0
    Position = "NONE"
    CitizenID = ""
    Firstname = ""
    Lastname = ""
    AddressID = 0
    Phone = ""
    Username = ""
    Password = ""
    Birthday = ""
    Address = Address()

    def check(this):
        if not checkEmpty(this.Firstname) or not checkEmpty(this.Lastname):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก ชื่อและนามสกุล')
            return False
        elif not checkENGoTH(this.Firstname) or not checkENGoTH(this.Lastname):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอกชื่อและนามสกุล ด้วยตัวอักษร')
            return False
            
        elif not (checkEng(this.Firstname)==checkEng(this.Lastname)):
            if  not (checkThaiLanguage(this.Firstname)==checkThaiLanguage(this.Lastname)):
                messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอกชื่อและนามสกุล ด้วยภาษาเดียวกัน')
                return False
            
        if not checkEmpty(this.CitizenID):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก เลขบัตรประชาชน')
            return False
        elif not checkInt(this.CitizenID):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก เลขบัตรประชาชน ที่เป็นตัวเลขเท่านั้น')
            return False
        elif not checkCitizenID(this.CitizenID):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอกเลขบัตรประชาชน 13 หลัก')
            return False

        if not checkEmpty(this.Phone):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก เบอร์โทร')
            return False
        elif not checkPhone(this.Phone):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอกเบอร์โทร 10 หลัก')
            return False

        if not this.Address.check():
            return False

        return True