from tkinter import messagebox
from regexCheck import *

class Deed:
    ID = 0
    Portion = ""
    No = ""
    Page = ""
    Province = ""
    District = ""
    City = ""
    Rai = ""
    Ngan = ""
    Wah = ""

    def check(this):
        if not checkEmpty(this.ID) or not checkEmpty(this.Portion) or not checkEmpty(this.Portion):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก ที่ดินฉโนดเลขที่,ระวาง,เลขที่ดินและหน้าสำรวจ')
            return False
        elif not checkInt(this.ID) or not checkInt(this.Portion) or not checkInt(this.Portion):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอกที่ดินฉโนดเลขที่,ระวาง,เลขที่ดินและหน้าสำรวจที่เป็นตัวเลขเท่านั้น')
            return False
        
        if not checkEmpty(this.Province) or not checkEmpty(this.District):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก อำเภอ/เขตและตำบล/แขวง')
            return False
        
        elif not checkThaiLanguage(this.Province) or not checkThaiLanguage(this.District):
            messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอกอำเภอ/เขตและตำบล/แขวง ด้วยตัวอักษรภาษาไทย')
            return False
        
        for i in[this.Rai, this.Ngan, this.Wah]:
            if not checkEmpty(i):
                messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก  ไร่,งานและตารางวา')
                return False
            elif not checkInt(i):
                messagebox.showerror('ข้อมูลผิดพลาด','กรุณากรอก ไร่,งานและตารางวาที่เป็นตัวเลขเท่านั้น')
                return False
        
        return True