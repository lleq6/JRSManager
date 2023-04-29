from tkinter import messagebox
from Address import Address
from regexCheck import *

class Customer:
    ID = 0
    Firstname = ""
    Lastname = ""
    Email = ""
    AddressID = 0
    Phone = ""
    Birthday = ""
    CitizenID = ""
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
            
        if not checkEmpty(this.Email):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก อีเมล')
            return False
        if not checkEmail(this.Email):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณา กรอกในรูปแบบอีเมล example@email.com')
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