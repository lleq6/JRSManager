from fpdf import FPDF
import Customer,Project
from Project import Project
from Customer import Customer
from Utils import *
from fpdf.fonts import FontFace
from PIL import Image
from bahttext import bahttext
from datetime import date
from pypdf import PdfReader,PdfWriter

b = 0

def contractPDF(customer : Customer, project : Project):
    data = [project.ID,'บริษัท อาร์เจเอสเอส คอนสตรัคชั่น จำกัด', date.today()]
    pdf = FPDF('portrait', format='A4')
    pdf.set_margin(25)
    pdf.add_font('Sarabun', '', r".\Font\THSarabunNew.ttf")
    pdf.add_font('Sarabun', 'B', r".\Font\THSarabunNew Bold.ttf")
    pdf.set_font('Sarabun','',14)
    pdf.add_page()
    pdf.cell(110, 10, f"", new_x="LMARGIN", new_y="NEXT",border=0)
    pdf.cell(119, 10, f"", new_x="RIGHT", new_y="LAST",border=0)
    pdf.cell(0, 10, f"{data[0]}", new_x="LMARGIN", new_y="NEXT",border=0)
    for i in range(1, 3):
            pdf.cell(110, 10, f"", new_x="RIGHT", new_y="LAST",border=0)
            pdf.cell(0, 10, f"{data[i]}", new_x="LMARGIN", new_y="NEXT",border=0)
    pdf.cell(0,0,'', new_x= 'LMARGIN', new_y='NEXT')
    #r1
    pdf.cell(85, 10.2, f"", new_x="RIGHT", new_y="LAST",border=0)
    pdf.cell(36, 10.2, f"{customer.Firstname}", new_x="RIGHT", new_y="LAST",border=0)
    pdf.cell(40, 10.2, f"{customer.Lastname}", new_x="LMARGIN", new_y="NEXT",border=0)
    #r2
    pdf.cell(6, 10.2, f"", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(7, 10.2, f"{getAge(customer.Birthday)}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(43, 10.2, f"", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(59, 10.2, f"{customer.CitizenID}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(20, 10.2, f"{customer.Address.No}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(20, 10.2, f"{customer.Address.Mu}", new_x="LMARGIN", new_y="NEXT",border=b)
    #r3
    pdf.cell(14, 10.2, f"", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(31, 10.2, f"{customer.Address.Alley}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(55, 10.2, f"{customer.Address.Road}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(55, 10.2, f"{customer.Address.City}", new_x="LMARGIN", new_y="NEXT",border=b)
    #r4
    pdf.cell(15, 10.2, f"", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(48, 10.2, f"{customer.Address.District}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(49, 10.2, f"{customer.Address.Province}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(49, 10.2, f"{customer.Address.ProvinceZip}", new_x="LMARGIN", new_y="NEXT",border=b)
    #r5
    pdf.cell(96, 10.2, f"", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(0, 10.2, f"{project.Company}", new_x="LMARGIN", new_y="NEXT",border=b)
    #r6
    pdf.cell(33, 10.2, f"", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(43, 10.2, f"{project.JuristicID}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(0, 10.2, f"{project.JuristicPerson}", new_x="LMARGIN", new_y="NEXT",border=b)
    #r7
    pdf.cell(36, 10.2, f"", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(46, 10.2, f"{project.Address.No}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(27, 10.2, f"{project.Address.Alley}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(0, 10.2, f"{project.Address.Road}", new_x="LMARGIN", new_y="NEXT",border=b)   
    #r7
    pdf.cell(16, 10.2, f"", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(37, 10.2, f"{project.Address.City}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(37, 10.2, f"{project.Address.District}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(44, 10.2, f"{project.Address.Province}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(0, 10.2, f"{project.Address.ProvinceZip}", new_x="LMARGIN", new_y="NEXT",border=b)   
    #
    for i in range(7):
        pdf.cell(0, 10.2, f"", new_x="LMARGIN", new_y="NEXT",border=b)
    #
    pdf.cell(113, 10.2, f"", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(0, 10.2, f"{project.BuildingType}", new_x="LMARGIN", new_y="NEXT",border=b)  
    #
    pdf.cell(0, 10.2, f"", new_x="LMARGIN", new_y="NEXT",border=b)
    #
    pdf.cell(21, 10.2, f"", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(31, 10.2, f"{project.Deed.ID}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(39, 10.2, f"{project.Deed.Portion}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(28, 10.2, f"{project.Deed.No}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(0, 10.2, f"{project.Deed.Page}", new_x="LMARGIN", new_y="NEXT",border=b)  
    #
    pdf.cell(16, 10.2, f"", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(39, 10.2, f"{project.Deed.City}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(37, 10.2, f"{project.Deed.District}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(50, 10.2, f"{project.Deed.Province}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(0, 10.2, f"{project.Deed.Rai}", new_x="LMARGIN", new_y="NEXT",border=b)  
    #
    pdf.cell(3, 10.2, f"", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(11, 10.2, f"{project.Deed.Ngan}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(0, 10.2, f"{project.Deed.Rai}", new_x="LMARGIN", new_y="NEXT",border=b)      

    pdf.add_page()
    pdf.cell(0, 35, f"", new_x="LMARGIN", new_y="NEXT",border=b)

    pdf.cell(58, 10.2, f"", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(58, 10.2, f"{project.DemolishTime}", new_x="LMARGIN", new_y="NEXT",border=b)
    pdf.cell(0, 15, f"", new_x="LMARGIN", new_y="NEXT",border=b)
    pdf.cell(82, 10.2, f"", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(0, 10.2, f"{project.BuildingTime}", new_x="LMARGIN", new_y="NEXT",border=b)
    pdf.cell(0, 131, f"", new_x="LMARGIN", new_y="NEXT",border=b)
    pdf.cell(14, 10.2, f"", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(0, 10.2, currencyFormat(project.BudgetProject), new_x="LMARGIN", new_y="NEXT",border=b)
    pdf.cell(75, 10.2, "", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(0, 10.2, f"{project.Phases[1].CollectionPercent}", new_x="LMARGIN", new_y="NEXT",border=b)

    pdf.cell(0, 10.2, "", new_x="LMARGIN", new_y="NEXT",border=b)
    pdf.cell(125, 10.2, "", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(0, 14, currencyFormat(int(getPaymentP(project.Phases[1].CollectionPercent, project.BudgetProject))), new_x="LMARGIN", new_y="NEXT",border=b)
    #
    pdf.add_page()
    pdf.cell(130, 5, f"", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(0, 5, currencyFormat(int(getPaymentP(project.Phases[1].CollectionPercent, project.BudgetProject))), new_x="LMARGIN", new_y="NEXT",border=b)
    pdf.cell(75, 10.2, "", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(45, 10.2, f"{100-int(project.Phases[1].CollectionPercent)}", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(0, 10.2, currencyFormat(int(project.BudgetProject)-int(getPaymentP(project.Phases[1].CollectionPercent, project.BudgetProject))), new_x="LMARGIN", new_y="NEXT",border=b)
    pdf.cell(95, 5, f"", new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(0, 5, f"{currencyFormat(int(project.BudgetProject)-int(getPaymentP(project.Phases[1].CollectionPercent, project.BudgetProject)))}", new_x="LMARGIN", new_y="NEXT",border=b)
    pdf.cell(95, 27, f"", new_x="LMARGIN", new_y="NEXT",border=b)
    p = project.Phases.copy()
    for i in range(2,project.PhaseCount):
        pdf.cell(8, 10.2,'',new_x="RIGHT", new_y="LAST",border=b)
        pdf.cell(35, 10.2,f'{i}',new_x="RIGHT", new_y="LAST",border=b)
        pdf.cell(33, 10.2,f'{project.Phases[i].CollectionPercent}',new_x="RIGHT", new_y="LAST",border=b)
        pdf.cell(0, 10.2,f'{currencyFormat(getPaymentP(project.Phases[i].CollectionPercent, project.BudgetProject))}',new_x="LMARGIN", new_y="NEXT",border=b)  
        pdf.cell(60, 10.2,f'',new_x="RIGHT", new_y="LAST",border=b)
        pdf.cell(0, 10.2,f'text',new_x="LMARGIN", new_y="NEXT",border=b)  
    for i in range(10-project.PhaseCount):
        pdf.cell(0, 10.2,f'',new_x="LMARGIN", new_y="NEXT",border=b)  
        pdf.cell(0, 10.2,f'',new_x="LMARGIN", new_y="NEXT",border=b)  
    
    pdf.cell(8, 10.2,'',new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(35, 10.2,f'',new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(33, 11.2,f'{project.Phases[project.PhaseCount].CollectionPercent}',new_x="RIGHT", new_y="LAST",border=b)
    pdf.cell(0, 11.2,f'{currencyFormat(getPaymentP(project.Phases[project.PhaseCount].CollectionPercent, project.BudgetProject))}',new_x="LMARGIN", new_y="NEXT",border=b)  
    pdf.cell(0, 10.2,f'',new_x="LMARGIN", new_y="LAST",border=b)  
    pdf.cell(60, 10.2,f'test',new_x="RIGHT", new_y="LAST",border=b)

    return pdf

def projectPaymentReport(customer : Customer, project : Project):
    b = 1
    pdf = FPDF('portrait', format='A4')
    pdf.add_font('Sarabun', '', r".\Font\THSarabunNew.ttf")
    pdf.add_font('Sarabun', 'B', r".\Font\THSarabunNew Bold.ttf")
    pdf.add_page()
    pdf.set_font('Sarabun','',24)

    pdf.cell(0, 20,f'รายงานการรับชำระเงินโครงการ',new_x="LMARGIN", new_y="NEXT", border=0, align='C')

    pdf.set_font('Sarabun','',16)
    t = datetime.now()
    pdf.cell(0, 10.2,('%32s'%(f'วันที่พิมพ์รายงาน : {t.day}-04-{t.year}')),new_x="LMARGIN", new_y="NEXT", border=0, align='R')

    pdf.set_font('Sarabun','',18)
    pdf.cell(40, 10.2,f'เลขที่โครงการ',new_x="RIGHT", new_y="LAST", border=b,)
    pdf.cell(0,10.2, f'{project.ID}',new_x="LMARGIN", new_y="NEXT", border=b)

    pdf.cell(40, 10.2,f'ชื่อลูกค้า',new_x="RIGHT", new_y="LAST", border=b,)
    pdf.cell(0,10.2, f'{customer.Firstname} {customer.Lastname}',new_x="LMARGIN", new_y="NEXT", border=b)

    pdf.cell(40, 10.2,f'ที่อยู่ปัจจุบัน',new_x="RIGHT", new_y="LAST", border=b,)
    text = f'{customer.Address.No} หมู่ที่ {customer.Address.Mu} {customer.Address.City} {customer.Address.District} จังหวัด{customer.Address.Province} {customer.Address.ProvinceZip}'
    pdf.cell(0,10.2, text, new_x="LMARGIN", new_y="NEXT", border=b)

    pdf.cell(40, 10.2,f'เบอร์โทรศัพท์',new_x="RIGHT", new_y="LAST", border=b,)
    text = f'{customer.Phone}'
    pdf.cell(0,10.2, text, new_x="LMARGIN", new_y="NEXT", border=b)

    pdf.cell(40, 20.4,f'ข้อมูลพื้นที่ก่อสร้าง',new_x="RIGHT", new_y="LAST", border=b,)
    text = f'ที่ดินโฉนดเลขที่ {project.Deed.ID}  ระวาง {project.Deed.Portion}  เลขที่ดิน {project.Deed.No}  หน้าสำรวจ {project.Deed.Page}'
    text2 = f'เนื้อที่ประมาณ {project.Deed.Rai} ไร่ {project.Deed.Ngan} งาน {project.Deed.Wah} ตารางวา'
    pdf.cell(0,10.2, text, new_x='LEFT',  new_y="NEXT", border='LTR')
    pdf.cell(0,10.2, text2, new_x="LMARGIN", new_y="NEXT", border='LBR')

    pdf.cell(40, 10.2,f'ข้อมูลอาคารก่อสร้าง',new_x="RIGHT", new_y="LAST", border=b,)
    text = f'{project.BuildingType}'
    pdf.cell(0,10.2, text, new_x="LMARGIN", new_y="NEXT", border=b)

    pdf.cell(40, 10.2,f'จำนวนงวดการทำงาน',new_x="RIGHT", new_y="LAST", border=b,)
    text = f'{project.PhaseCount}'
    pdf.cell(0,10.2, text, new_x="LMARGIN", new_y="NEXT", border=b)
    pdf.cell(0,10.2, '', new_x="LMARGIN", new_y="NEXT", border=b)
    
    TABLE_DATA = [
    ("งวดที่", "เปอร์เซนต์", "จำนวนเงินที่ต้องชำระ", "ค่าใช้จ่ายที่เกินมา", "ยอดที่ต้องชำระ", "วันที่ต้องชำระ", "สถานะ", 'หมายเหตุ'),
    ]
    total = 0
    for i in project.Phases:
        phase = project.Phases[int(i)]
        no = i
        percent = phase.CollectionPercent
        cost = currencyFormat((project.BudgetProject/100)*int(phase.CollectionPercent))
        other_cost = currencyFormat(phase.ExcessCost)
        total_cost = currencyFormat((project.BudgetProject/100)*int(phase.CollectionPercent)+phase.ExcessCost)
        day = phase.DueDate
        status = phase.Status
        other = phase.Note
        total += int(phase.ExcessCost)

        dataList = [str(i) for i in [no, percent, cost, other_cost, total_cost, day, status, other]]

        TABLE_DATA.append(tuple(dataList))

    pdf.set_font('Sarabun','',size=14)
    alignm = []
    for i in range(len(TABLE_DATA[0])):
        alignm.append('CENTER')

    with pdf.table(col_widths=(10,15,30,30,30,20,20,15),text_align = tuple(alignm) , headings_style = FontFace(fill_color=(170, 170, 170))) as table:
        for data_row in TABLE_DATA:
            row = table.row()
            for datum in data_row:
                row.cell(datum,)

    pdf.cell(27.95, 10.2,f'รวม',new_x="RIGHT", new_y="LAST", border=b,)
    pdf.cell(33.55, 10.2,f'{currencyFormat(project.BudgetProject)}',new_x="RIGHT", new_y="LAST", border=b,)
    pdf.cell(33.5, 10.2,f'{currencyFormat(total)}',new_x="RIGHT", new_y="LAST", border=b,)
    pdf.cell(33.5, 10.2,f'{currencyFormat(int(project.BudgetProject)+total)}',new_x="RIGHT", new_y="LAST", border=b,)
    pdf.cell(0, 10.2,f'{bahttext(int(project.BudgetProject)+total)}',new_x="RIGHT", new_y="LAST", border=b,)
    pdf.cell(0,10.2, '', new_x="LMARGIN", new_y="NEXT", border=0)
    return pdf

def projectProgressionReport(date_start, duration_month):
    b = 1
    DATE_FORMAT = "%Y-%m-%d"
    date_end = (datetime.strptime(date_start, DATE_FORMAT) + timedelta(weeks=duration_month * 4)).strftime(DATE_FORMAT)
    pdf = FPDF('portrait', format='A4')
    pdf.add_font('Sarabun', '', r".\Font\THSarabunNew.ttf")
    pdf.add_font('Sarabun', 'B', r".\Font\THSarabunNew Bold.ttf")
    pdf.add_page()
    pdf.set_font('Sarabun','B',24)

    pdf.cell(0, 20,f'รายงานความคืบหน้าโครงการ',new_x="LMARGIN", new_y="NEXT", border=0, align='C')

    pdf.set_font('Sarabun','',14)

    logo = Image.open("./Picture/JRS.jpg")
    width, height = logo.size
    logo = logo.resize((width//10, height//10))
    
    pdf.image(logo, x=20, y=20)

    pdf.cell(90, 7,f'',new_x="RIGHT", new_y="LAST", border=0,)
    pdf.cell(40, 7,f'จาก',new_x="RIGHT", new_y="LAST", border=1,)
    pdf.cell(0, 7,f'{date_start}',new_x="LMARGIN", new_y="NEXT", border=1,)

    pdf.cell(90, 7,f'',new_x="RIGHT", new_y="LAST", border=0,)
    pdf.cell(40, 7,f'ถึง',new_x="RIGHT", new_y="LAST", border=1,)
    pdf.cell(0, 7,f'{date_end}',new_x="LMARGIN", new_y="NEXT", border=1,)
    pdf.cell(0, 7,f'1 = กำลังดำเนินการ 2 = ดำเนินการเสร็จสิ้น',new_x="LMARGIN", new_y="NEXT", border=0,)
    TABLE_DATA = [
    ("สถานะ", "เปอร์เซนต์", "เลขที่โครงการ", "ผู้ดูแลโครงการ", "วันที่เริ่มโครงการ", "ชื่อลูกค้า", "ที่ตั้งโครงการ", ),
    ]
    

    project_dict = projectSummaryFormat(GetProjectsByDate(date_start, duration_month))
    c,n = project_dict[1]
    TABLE_DATA.extend(project_dict[0])
    pdf.set_font('Sarabun','',size=10)
    alignm = []
    for i in range(len(TABLE_DATA[0])):
        alignm.append('CENTER')

    with pdf.table(col_widths=(12,17,14,30,30,30,40),text_align = tuple(alignm) , headings_style = FontFace(fill_color=(170, 170, 170))) as table:
        for data_row in TABLE_DATA:
            row = table.row()
            for datum in data_row:
                row.cell(datum,)


    pdf.cell(113.1, 7,f'',new_x="RIGHT", new_y="LAST", border=0,)
    pdf.cell(33, 7,f'โครงการที่เสร็จสิ้นแล้ว',new_x="RIGHT", new_y="LAST", border=1,)
    pdf.cell(0, 7,f'{c} โครงการ',new_x="LMARGIN", new_y="NEXT", border=1, align='R')

    pdf.cell(113.1, 7,f'',new_x="RIGHT", new_y="LAST", border=0,)
    pdf.cell(33, 7,f'โครงการที่อยู่ระหว่างก่อสร้าง',new_x="RIGHT", new_y="LAST", border=1,)
    pdf.cell(0, 7,f'{n} โครงการ',new_x="LMARGIN", new_y="NEXT", border=1, align='R')

    pdf.cell(113.1, 7,f'',new_x="RIGHT", new_y="LAST", border=0,)
    pdf.cell(33, 7,f'โครงการทั้งหมด',new_x="RIGHT", new_y="LAST", border=1,)
    pdf.cell(0, 7,f'{n+c} โครงการ',new_x="LMARGIN", new_y="NEXT", border=1, align='R')

    t = datetime.now()
    pdf.cell(0, 10.2,('%32s'%(f'วันที่พิมพ์รายงาน : {t.year}-{t.month}-{t.day}')),new_x="LMARGIN", new_y="NEXT", border=0, align='R')
    return pdf

def projectFinalReport(project : Project, customer : Customer, employee : Employee):
    class PDF(FPDF):
        def header(self) -> None:
                self.add_font('Sarabun', '', r".\Font\THSarabunNew.ttf")
                self.add_font('Sarabun', 'B', r".\Font\THSarabunNew Bold.ttf")
                self.set_font('Sarabun','B',24)
                logo = Image.open("./Picture/JRS.jpg")
                width, height = logo.size
                logo = logo.resize((width//10, height//10))
                self.image(logo, x=10, y=10)
                self.cell(0, 10.2,f'รายงานข้อมูลโครงการ',new_x="LMARGIN", new_y="NEXT", border=0, align='C')
                self.set_font('Sarabun','',18)

                t = datetime.now()

                self.cell(0, 10.2,('%-32s'%(f'เลขที่โครงการ : {project.ID}')),new_x="LMARGIN", new_y="NEXT", border=0, align='R')
                self.cell(0, 10.2,('%32s'%(f'วันที่พิมพ์รายงาน : {t.day}-04-{t.year}')),new_x="LMARGIN", new_y="NEXT", border=0, align='R')
                self.cell(0, 10.2,('%32s'%(f'วันที่เริ่มโครงการ : {t.day}-04-{t.year}')),new_x="RMARGIN", new_y="LAST", border=0, align='L')
                self.cell(0, 10.2,('%32s'%(f'วันที่สิ้นสุดโครงการ : {t.day}-04-{t.year}')),new_x="LMARGIN", new_y="NEXT", border=0, align='R')
            
                return super().header()
    b=1
    pdf = PDF('portrait', format='A4')
    pdf.add_page()
    pdf.set_font('Sarabun','',18)
    pdf.cell(0, 10.2,f'ข้อมูลผู้ว่าจ้าง',new_x="LMARGIN", new_y="NEXT", border=0, align='L')
    pdf.cell(16, 10.2,f'ชื่อลูกค้า',new_x="RIGHT", new_y="LAST", border=b)
    pdf.cell(70, 10.2,f' {customer.Firstname} {customer.Lastname}',new_x="RIGHT", new_y="LAST", border=b)
    pdf.cell(29, 10.2,f' เบอร์โทรศัพท์',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(0, 10.2,f' {customer.Phone}',new_x="LMARGIN", new_y="NEXT", border=b, align='L')
    pdf.cell(16, 20.4,'ที่อยู่',new_x="RIGHT", new_y="LAST", border=1,)

    addressText = f'{customer.Address.No} หมู่ที่{customer.Address.Mu} {customer.Address.City}'
    addressText2 = f'{customer.Address.District} จังหวัด{customer.Address.Province} {customer.Address.Province}'
    pdf.cell(0, 10.2,addressText,new_x="LEFT", new_y="NEXT", border='LTR',)
    pdf.cell(0, 10.2,addressText2,new_x="LMARGIN", new_y="NEXT", border='LBR',)
    pdf.cell(0, 10.2,f'ข้อมูลผู้รับจ้าง',new_x="LMARGIN", new_y="NEXT", border=0, align='L')
    pdf.cell(16, 10.2,f'บริษัท',new_x="RIGHT", new_y="LAST", border=b)
    pdf.cell(70, 10.2,f' {project.Company}',new_x="RIGHT", new_y="LAST", border=b)
    pdf.cell(29, 10.2,f' เบอร์โทรศัพท์',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(0, 10.2,f' 092-991-2666',new_x="LMARGIN", new_y="NEXT", border=b, align='L')

    pdf.cell(29, 20.4,'ที่อยู่',new_x="RIGHT", new_y="LAST", border=1, align='C')
    addressText = f' {project.Address.No} หมู่ที่{project.Address.Mu} {project.Address.City}'
    addressText2 = f' {project.Address.District} จังหวัด{project.Address.Province} {project.Address.Province}'
    pdf.cell(0, 10.2,addressText,new_x="LEFT", new_y="NEXT", border='LTR',)
    pdf.cell(0, 10.2,addressText2,new_x="LMARGIN", new_y="NEXT", border='LBR',)

    pdf.cell(42, 10.2,f'ทะเบียนนิติบุคคลเลขที่',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(0, 10.2,f'{project.JuristicID}',new_x="LMARGIN", new_y="NEXT", border=b, align='L')
    pdf.cell(42, 10.2,f'ชื่อผู้ดูแลโครงการ',new_x="RIGHT", new_y="LAST", border=b, align='C')
    pdf.cell(0, 10.2,f'นาย สมพงษ์ บุตรชน',new_x="LMARGIN", new_y="NEXT", border=b, align='L')

    pdf.cell(42, 10.2,f'ผู้ดูแลโครงการ', new_x="RIGHT", new_y="LAST", border=b, align='C')
    pdf.cell(70, 10.2,f'{employee.Firstname} {employee.Lastname}',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(27, 10.2,f'เบอร์โทรศัพท์', new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(0, 10.2,f'{employee.Phone}',new_x="LMARGIN", new_y="NEXT", border=b, align='L')
    pdf.cell(42, 10.2,f'วิศวะกรผู้คุมงาน', new_x="RIGHT", new_y="LAST", border=b, align='C')
    pdf.cell(70, 10.2,f'{employee.Firstname} {employee.Lastname}',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(27, 10.2,f'เบอร์โทรศัพท์', new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(0, 10.2,f'{employee.Phone}',new_x="LMARGIN", new_y="NEXT", border=b, align='L')
    pdf.cell(0, 10.2,f'ข้อมูลพื้นที่ก่อสร้าง',new_x="LMARGIN", new_y="NEXT", border=0, align='L')
    pdf.cell(32, 10.2,f'ที่ดินโฉนดเลขที่',new_x="RIGHT", new_y="LAST", border=b)
    pdf.cell(40, 10.2,f' {project.Deed.ID}',new_x="RIGHT", new_y="LAST", border=b)
    pdf.cell(15, 10.2,f'ระวาง',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(15, 10.2,f'{project.Deed.Portion}',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(16, 10.2,f'เลขที่ดิน',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(20, 10.2,f'{project.Deed.No}',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(20, 10.2,f'หน้าสำรวจ',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(0, 10.2,f'{project.Deed.Page}',new_x="LMARGIN", new_y="NEXT", border=b, align='L')

    pdf.cell(15, 10.2,f'ตำบล',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(40, 10.2,f'{project.Deed.City}',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(15, 10.2,f'อำเภอ',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(40, 10.2,f'{project.Deed.District}',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(15, 10.2,f'จังหวัด',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(0, 10.2,f'{project.Deed.Province}',new_x="LMARGIN", new_y="NEXT", border=b, align='L')
    pdf.cell(43, 10.2,f'เนื้อที่ประมาณ',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(49, 10.2,f'{project.Deed.Rai} ไร่',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(49, 10.2,f'{project.Deed.Ngan} งาน ',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(49, 10.2,f'{project.Deed.Wah} วา',new_x="LMARGIN", new_y="NEXT", border=b, align='L')
    pdf.cell(43, 10.2,f'ข้อมูลอาคารก่อสร้าง',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(0, 10.2,f'{project.BuildingType}',new_x="LMARGIN", new_y="NEXT", border=b, align='L')
    pdf.cell(43, 10.2,f'งบประมาณการ',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(0, 10.2,f'{currencyFormat(project.BudgetProject)} บาท',new_x="LMARGIN", new_y="NEXT", border=b, align='L')
    pdf.cell(43, 10.2,f'ค่าใช้จ่ายที่เกินงบ',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(0, 10.2,f'{currencyFormat(project.BudgetProject)} บาท',new_x="LMARGIN", new_y="NEXT", border=b, align='L')
    pdf.cell(43, 10.2,f'งบประมาณรวมทั้งสิ้น',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(0, 10.2,f'{currencyFormat(project.BudgetProject)           } บาท',new_x="LMARGIN", new_y="NEXT", border=b, align='L')
    pdf.cell(43, 10.2,f'จำนวนงวดในการทำงาน',new_x="RIGHT", new_y="LAST", border=b, align='L')
    pdf.cell(0, 10.2,f'{project.PhaseCount} งวด',new_x="LMARGIN", new_y="NEXT", border=b, align='L')

    pdf.add_page()
    pdf.cell(0, 10.2,f'',new_x="LMARGIN", new_y="NEXT", border=0, align='L')

    for i in project.Phases:
        phase : Phase
        phase = project.Phases[i]
        pdf.set_font('Sarabun','',16)
        pdf.cell(0, 10.2,f'งวดที่ {i}',new_x="LMARGIN", new_y="NEXT", border=0, align='C')
        pdf.cell(0, 10.2,f'ชื่อเฟส {phase.Title}',new_x="LMARGIN", new_y="NEXT", border=0, align='C')
        pdf.set_font('Sarabun','',14)
        pdf.cell(0, 10.2,f'วันที่เริ่ม : {phase.Start}',new_x="RIGHT", new_y="LAST", border=0, align='L')
        pdf.cell(0, 10.2,f'วันที่สิ้นสุด : {phase.End}',new_x="RIGHT", new_y="LAST", border=0, align='R')
        pdf.cell(0, 10.2,f'',new_x="LMARGIN", new_y="NEXT", border=0, align='C')
        pdf.cell(40, 10.2,f'เปอร์เซนต์',new_x="RIGHT", new_y="LAST", border=1, align='C')
        pdf.cell(60, 10.2,f'{phase.CollectionPercent}',new_x="RIGHT", new_y="LAST", border=1, align='C')
        pdf.cell(40, 10.2,f'วันที่กำหนดชำระ',new_x="RIGHT", new_y="LAST", border=1, align='C')
        pdf.cell(0, 10.2,f'{phase.DueDate}',new_x="LMARGIN", new_y="NEXT", border=1, align='C')


        pdf.cell(40, 10.2,f'ค่าใช้จ่ายที่เกินมา',new_x="RIGHT", new_y="LAST", border=1, align='C')
        pdf.cell(60, 10.2,f'{currencyFormat(phase.ExcessCost)} บาท',new_x="RIGHT", new_y="LAST", border=1, align='C')
        pdf.cell(40, 10.2,f'วันที่ชำระ',new_x="RIGHT", new_y="LAST", border=1, align='C')
        pdf.cell(0, 10.2,f'{phase.PaymentDate}',new_x="LMARGIN", new_y="NEXT", border=1, align='C')


        emp = GetEmployeeByID(phase.EmployeeID)

        pdf.cell(40, 10.2,f'จํานวนเงินที่ ต้องชําระ',new_x="RIGHT", new_y="LAST", border=1, align='C')
        pdf.cell(60, 10.2,f'{currencyFormat(getPaymentP(phase.CollectionPercent,project.BudgetProject)+phase.ExcessCost)}',new_x="RIGHT", new_y="LAST", border=1, align='C')
        pdf.cell(40, 10.2,f'พนักงานผู้รับชำระ',new_x="RIGHT", new_y="LAST", border=1, align='C')
        pdf.cell(0, 10.2,f'{emp.Firstname} {emp.Lastname}',new_x="LMARGIN", new_y="NEXT", border=1, align='C')

        text1 = phase.Description.replace('\n',' ')
        text2 = phase.DescriptionExcessCost.replace('\n',' ')
        pdf.multi_cell(40, 10.2,f'รายละเอียด',new_x="RIGHT", new_y="LAST", border=1, align='C')
        pdf.multi_cell(0, 10.2,f'{text1}',new_x="LMARGIN", new_y="NEXT", border=1, align='C')
        
        pdf.cell(40, 10.2,f'รายละเอียดค่าใช้จ่ายที่เกินมา',new_x="RIGHT", new_y="LAST", border=1, align='C')
        pdf.cell(0, 10.2,f'{text2}test',new_x="LMARGIN", new_y="NEXT", border=1, align='C')

        pdf.cell(0, 27.2,f'',new_x="LMARGIN", new_y="NEXT", border=0, align='C')

    return pdf

def saveReport(pdf,path, filename = 'Default.pdf'):
    try:
        pdf.output(f"{path}/{filename}.pdf")
        return True
    except:
        return False
    
def run(id,path):
    reader = PdfReader('./PDF/Example.pdf')
    reader2 = PdfReader('./PDF/Form.pdf')
    writer = PdfWriter()
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    page2 = reader2.pages[0]
    page.merge_page(page2)
    page = reader.pages[1]
    page2 = reader2.pages[1]
    page.merge_page(page2)
    page = reader.pages[2]
    page2 = reader2.pages[2]
    page.merge_page(page2)
    writer.add_page(reader.pages[0])
    writer.add_page(reader.pages[1])
    writer.add_page(reader.pages[2])
    writer.add_page(reader.pages[3])
    writer.add_page(reader.pages[4])
    writer.add_page(reader.pages[5])
    writer.add_page(reader.pages[6])
    writer.add_page(reader.pages[7])

    writer.write(f'{path}/Project_Contact_ID_{id}.pdf')
    
def projectContact(customer : Customer, project : Project,path):
    try:
        saveReport(contractPDF(customer, project),'.',f'/PDF/Form')
        run(project.ID,path)
        return True
    except:
        return False