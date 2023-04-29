from datetime import datetime, timedelta
import sqlite3
from Address import *
from Customer import *
from Employee import *
from Phase import *
from Project import *
from Deed import *
from Template import *

def Connect():
    return sqlite3.connect("Database/JRSConstructor.db")

def LoadEmployees():
    Employees = {}
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute("SELECT * FROM Employee ORDER BY id ASC")
        Lists = Cursor.fetchall()
        if Lists:
            for Data in Lists:
                Emp = Employee()
                Emp.ID = Data[0]
                Emp.Position = Data[1]
                Emp.CitizenID = Data[2]
                Emp.Firstname = Data[3]
                Emp.Lastname = Data[4]
                Emp.AddressID = Data[5]
                Emp.Phone = Data[6]
                Emp.Username = Data[7]
                Emp.Password = Data[8]
                Emp.Birthday = Data[9]
                Emp.Address = GetAddressByID(Emp.AddressID, "EMP")
                Employees.update({ Emp.ID : Emp })
        Lists.clear()
        Cursor.close()
    return Employees

def LoadCustomers():
    Customers = {}
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute("SELECT * FROM Customer ORDER BY id ASC")
        Lists = Cursor.fetchall()
        if Lists:
            for Data in Lists:
                Cus = Customer()
                Cus.ID = Data[0]
                Cus.Firstname = Data[1]
                Cus.Lastname = Data[2]
                Cus.Email = Data[3]
                Cus.CitizenID = Data[4]
                Cus.AddressID = Data[5]
                Cus.Phone = Data[6]
                Cus.Birthday = Data[7]
                Cus.Address = GetAddressByID(Cus.AddressID, "CUS")
                Customers.update({ Cus.ID : Cus })
        Lists.clear()
        Cursor.close()
    return Customers

def CreateCustomer(Customer : Customer):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"INSERT INTO Customer (fname, lname, email, citizen_id, phone, birthday) VALUES ('{Customer.Firstname}', '{Customer.Lastname}', '{Customer.Email}', '{Customer.CitizenID}', '{Customer.Phone}', '{Customer.Birthday}') RETURNING id")
        LastID = Cursor.lastrowid
        Cursor.close()
        return LastID
    
def CreateEmployee(Employee : Employee):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"INSERT INTO Employee (position, citizen_id, fname, lname, phone, birthday) VALUES ('{Employee.Position}', '{Employee.CitizenID}', '{Employee.Firstname}', '{Employee.Lastname}', '{Employee.Phone}', '{Employee.Birthday}') RETURNING id")
        LastID = Cursor.lastrowid
        Cursor.close()
        return LastID

def GetEmployeeByID(ID : int):
    Emp = Employee
    if ID == 0:
        return None
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"SELECT * FROM Employee WHERE id='{ID}'")
        Data = Cursor.fetchone()
        Emp.ID = Data[0]
        Emp.Position = Data[1]
        Emp.CitizenID = Data[2]
        Emp.Firstname = Data[3]
        Emp.Lastname = Data[4]
        Emp.AddressID = Data[5]
        Emp.Phone = Data[6]
        Emp.Username = Data[7]
        Emp.Password = Data[8]
        Emp.Birthday = Data[9]
        Emp.Address = GetAddressByID(Emp.AddressID, "EMP")
        Cursor.close()
    return Emp

def SearchCustomer(Selected : str, Keyword : str):
    Customers = {}
    with Connect() as Session:
        cur = Session.cursor()
        if Selected == 'id':
            cur.execute(f"SELECT * FROM Customer WHERE {Selected} = '{Keyword}' ORDER BY id ASC")
        else:
            cur.execute(f"SELECT * FROM Customer WHERE {Selected} LIKE '%{Keyword}%' ORDER BY id ASC")
        List = cur.fetchall()
        if List:
            for Data in List:
                Cus = Customer()
                Cus.ID = Data[0]
                Cus.Firstname = Data[1]
                Cus.Lastname = Data[2]
                Cus.Email = Data[3]
                Cus.CitizenID = Data[4]
                Cus.AddressID = Data[5]
                Cus.Phone = Data[6]
                Cus.Birthday = Data[7]
                Cus.Address = GetAddressByID(Cus.AddressID, "CUS")
                Customers.update({ Cus.ID : Cus })
        List.clear()
        cur.close()
    return Customers

def SearchEmployee(Selected : str, Keyword : str):
    Employees = {}
    with Connect() as Session:
        cur = Session.cursor()
        if Selected == 'id':
            cur.execute(f"SELECT * FROM Employee WHERE {Selected} LIKE '{Keyword}' ORDER BY id ASC")
        else:
            cur.execute(f"SELECT * FROM Employee WHERE {Selected} LIKE '%{Keyword}%' ORDER BY id ASC")
        List = cur.fetchall()
        for Data in List:
            Emp = Employee()
            Emp.ID = Data[0]
            Emp.Position = Data[1]
            Emp.CitizenID = Data[2]
            Emp.Firstname = Data[3]
            Emp.Lastname = Data[4]
            Emp.AddressID = Data[5]
            Emp.Phone = Data[6]
            Emp.Username = Data[7]
            Emp.Password = Data[8]
            Emp.Birthday = Data[9]
            Emp.Address = GetAddressByID(Emp.AddressID, "EMP")
            Employees.update({ Emp.ID : Emp })
        List.clear()
        cur.close()
    return Employees

def UpdateCustomer(id : str, Customer : Customer):
    with Connect() as Session:
        cur = Session.cursor()
        cur.execute(f"UPDATE Customer SET fname='{Customer.Firstname}', lname='{Customer.Lastname}',email='{Customer.Email}', citizen_id='{Customer.CitizenID}', phone='{Customer.Phone}',birthday='{Customer.Birthday}' WHERE id='{id}'")
        cur.close()
        return True
    
def UpdateEmployee(id : str, Employee : Employee):
    with Connect() as Session:
        cur = Session.cursor()
        cur.execute(f"UPDATE Employee SET fname='{Employee.Firstname}', lname='{Employee.Lastname}',position='{Employee.Position}', citizen_id='{Employee.CitizenID}', phone='{Employee.Phone}',birthday='{Employee.Birthday}' WHERE id='{id}'")
        cur.close()
        return True

def DeleteCustomer(ID : int):
    with Connect() as Session:
        cur = Session.cursor()
        cur.execute(f"DELETE FROM Customer WHERE id = '{ID}'")
        cur.close()
        return True
    
def DeleteEmployee(ID : int):
    with Connect() as Session:
        cur = Session.cursor()
        cur.execute(f"DELETE FROM Employee WHERE id = '{ID}'")
        cur.close()
        return True
    
def UpdateAddress(Type : str, Address : Address):
    with Connect() as Session:
        cur = Session.cursor()
        cur.execute(f"UPDATE Address SET no='{Address.No}', mu='{Address.Mu}', alley='{Address.Alley}', road='{Address.Road}', city='{Address.City}', district='{Address.District}', province='{Address.Province}', province_zip='{Address.ProvinceZip}' WHERE id='{Address.ID}' AND type = '{Type}'")
        cur.close()
        return True
    
def DeleteAddress(ID : int, Type : str):
    with Connect() as Session:
        cur = Session.cursor()
        cur.execute(f"DELETE FROM Address WHERE id = '{ID}' AND type = '{Type}'")
        cur.close()
        return True

def GetAddressByID(ID : int, Type : str):
    Adr = None
    if ID == 0:
        return Adr
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"SELECT * FROM Address WHERE id = '{ID}' AND type = '{Type}'")
        Data = Cursor.fetchone()
        if Data:
            Adr = Address()
            Adr.ID = Data[0]
            Adr.Type = Data[1]
            Adr.No = Data[2]
            Adr.Mu = Data[3]
            Adr.Alley = Data[4]
            Adr.Road = Data[5]
            Adr.City = Data[6]
            Adr.District = Data[7]
            Adr.Province = Data[8]
            Adr.ProvinceZip = Data[9]
            Cursor.close()
    return Adr

def SelectCustomer(customerID : str):
    with Connect() as Session:
        cur = Session.cursor()
        cur.execute(f"SELECT * FROM Customer WHERE id='{customerID}'")
        data = cur.fetchone()
        cur.close()
        return data
    
def LoadProjects():
    Projects = {}
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute('SELECT * FROM Project ORDER BY id ASC')
        List = Cursor.fetchall()
        if List:
            for Data in List:
                Pro = Project()
                Pro.ID = Data[0]
                Pro.CustomerID = Data[1]
                Pro.DateProject = Data[2]
                Pro.BuildingType = Data[3]
                Pro.BudgetProject = Data[4]
                Pro.DeedID = Data[5]
                Pro.EmployeeID = Data[6]
                Pro.DemolishTime = Data[7]
                Pro.BuildingTime = Data[8]
                Pro.JuristicID = Data[9]
                Pro.JuristicPerson = Data[10]
                Pro.AddressID = Data[11]
                Pro.TemplateID = Data[12]
                Pro.PhaseCount = Data[13]
                Pro.Status = Data[14]
                Pro.Company = Data[15]
                Pro.CurrentPhase = Data[16]
                Pro.Deed = GetDeedByID(Pro.DeedID)
                Pro.Address = GetAddressByID(Pro.AddressID, "PRO")
                Pro.Phases = GetAllPhaseByProjectID(Pro.ID)
                Projects.update({ Pro.ID : Pro })
        List.clear()
        Cursor.close()
    return Projects

def CreateProject(Project : Project):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"INSERT INTO Project (customer_id, date_project, building_type, budget_project, deed_id, employee_id, demolish_time, building_time, juristic_id, juristic_person, phase_count, company, status, current_phase) VALUES ('{Project.CustomerID}', '{Project.DateProject}', '{Project.BuildingType}', '{Project.BudgetProject}', '{Project.DeedID}', '{Project.EmployeeID}', '{Project.DemolishTime}', '{Project.BuildingTime}', '{Project.JuristicID}', '{Project.JuristicPerson}', '{Project.PhaseCount}', '{Project.Company}', '{Project.Status}', '{Project.CurrentPhase}') RETURNING id")
        ProjectID = Cursor.lastrowid
        Cursor.close()
        return ProjectID
    
def CreateDeed(Deed : Deed):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"INSERT INTO Deed (id, portion, no, page, province, district, city, rai, ngan, wah) VALUES ('{Deed.ID}', '{Deed.Portion}', '{Deed.No}', '{Deed.Page}', '{Deed.Province}', '{Deed.District}', '{Deed.City}', '{Deed.Rai}', '{Deed.Ngan}', '{Deed.Wah}')")
        Cursor.close()
        return True
    
def CreateAddress(Address : Address):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"INSERT INTO Address (id, type, no, mu, alley, road, city, district, province, province_zip) VALUES ('{Address.ID}', '{Address.Type}', '{Address.No}', '{Address.Mu}', '{Address.Alley}', '{Address.Road}', '{Address.City}', '{Address.District}', '{Address.Province}', '{Address.ProvinceZip}')")
        Cursor.close()
        return True
    
def UpdateProjectAddressID(ID : int, AddressID : int):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"UPDATE Project SET address_id = '{AddressID}' WHERE id = '{ID}'")
        Cursor.close()
        return True
    
def UpdateCustomerAddressID(ID : int, AddressID : int):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"UPDATE Customer SET address_id = '{AddressID}' WHERE id = '{ID}'")
        Cursor.close()
        return True
    
def UpdateEmployeeAddressID(ID : int, AddressID : int):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"UPDATE Employee SET address_id = '{AddressID}' WHERE id = '{ID}'")
        Cursor.close()
        return True
    
def GetCustomerByID(ID : int):
    Cus = None
    if ID == 0:
        return Cus
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"SELECT * FROM Customer WHERE id = {ID}")
        Data = Cursor.fetchone()
        if Data:
            Cus = Customer()
            Cus.ID = Data[0]
            Cus.Firstname = Data[1]
            Cus.Lastname = Data[2]
            Cus.Email = Data[3]
            Cus.CitizenID = Data[4]
            Cus.AddressID = Data[5]
            Cus.Phone = Data[6]
            Cus.Birthday = Data[7]
            Cus.Address = GetAddressByID(Cus.AddressID, "CUS")
        Cursor.close()
    return Cus

def GetEmployeeByID(ID : int):
    Emp = None
    if ID == 0:
        return Emp
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"SELECT * FROM Employee WHERE id = {ID}")
        Data = Cursor.fetchone()
        if Data:
            Emp = Employee()
            Emp.ID = Data[0]
            Emp.Position = Data[1]
            Emp.CitizenID = Data[2]
            Emp.Firstname = Data[3]
            Emp.Lastname = Data[4]
            Emp.AddressID = Data[5]
            Emp.Phone = Data[6]
            Emp.Username = Data[7]
            Emp.Password = Data[8]
            Emp.Birthday = Data[9]
            Emp.Address = GetAddressByID(Emp.AddressID, "EMP")
        Cursor.close()
    return Emp

def GetProjectByID(ID : int):
    Pro = None
    if ID == 0:
        return Pro
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"SELECT * FROM Project WHERE id = '{ID}'")
        Data = Cursor.fetchone()
        if Data:
            Pro = Project()
            Pro.ID = Data[0]
            Pro.CustomerID = Data[1]
            Pro.DateProject = Data[2]
            Pro.BuildingType = Data[3]
            Pro.BudgetProject = Data[4]
            Pro.DeedID = Data[5]
            Pro.EmployeeID = Data[6]
            Pro.DemolishTime = Data[7]
            Pro.BuildingTime = Data[8]
            Pro.JuristicID = Data[9]
            Pro.JuristicPerson = Data[10]
            Pro.AddressID = Data[11]
            Pro.TemplateID = Data[12]
            Pro.PhaseCount = Data[13]
            Pro.Status = Data[14]
            Pro.Company = Data[15]
            Pro.CurrentPhase = Data[16]
            Pro.Deed = GetDeedByID(Pro.DeedID)
            Pro.Address = GetAddressByID(Pro.AddressID, "PRO")
            Pro.Phases = GetAllPhaseByProjectID(Pro.ID)
        Cursor.close()
    return Pro

def DeleteProject(ID : int):
    with Connect() as Session:
        cur = Session.cursor()
        cur.execute(f"DELETE FROM Project WHERE id = '{ID}'")
        cur.close()
        return True
    
def UpdateProject(Project : Project):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"UPDATE Project SET customer_id='{Project.CustomerID}', date_project='{Project.DateProject}', building_type='{Project.BuildingType}', budget_project='{Project.BudgetProject}', deed_id='{Project.DeedID}', employee_id='{Project.EmployeeID}', demolish_time='{Project.DemolishTime}', building_time='{Project.BuildingTime}', juristic_id='{Project.JuristicID}', juristic_person='{Project.JuristicPerson}', company='{Project.Company}' WHERE id = '{Project.ID}'")
        Cursor.close()
        return True
    
def DeleteDeed(ID : int):
    with Connect() as Session:
        cur = Session.cursor()
        cur.execute(f"DELETE FROM Deed WHERE id = '{ID}'")
        cur.close()
        return True

def GetAllPhaseByProjectID(ID : int):
    Phases = {}
    if ID == 0:
        return Phases
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"SELECT * FROM Phase WHERE project_id = '{ID}'")
        List = Cursor.fetchall()
        if List:
            for Data in List:
                Pha = Phase()
                Pha.ProjectID = Data[0]
                Pha.Title = Data[1]
                Pha.ID = Data[2]
                Pha.EmployeeID = Data[3]
                Pha.Start = Data[4]
                Pha.End = Data[5]
                Pha.Status = Data[6]
                Pha.Path = Data[7]
                Pha.Payment = Data[8]
                Pha.PaymentDate = Data[9]
                Pha.DueDate = Data[10]
                Pha.Description = Data[11]
                Pha.DescriptionExcessCost = Data[12]
                Pha.CollectionPercent = Data[13]
                Pha.ExcessCost = Data[14]
                Pha.Note = Data[15]
                Phases.update({ Pha.ID : Pha })
        Cursor.close()
    return Phases

def CreatePhase(Project : Project, Phase : Phase):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"INSERT INTO Phase (project_id, title, id, employee_id, status, path, due_date, collection_percent) VALUES ('{Project.ID}', '{Phase.Title}', '{Phase.ID}', '{Project.EmployeeID}', '{Phase.Status}', '{Phase.Path}', '{Phase.DueDate}', '{Phase.CollectionPercent}')")
        Cursor.close()

def DeletePhase(ProjectID : int):
    with Connect() as Session:
        cur = Session.cursor()
        cur.execute(f"DELETE FROM Phase WHERE project_id = '{ProjectID}'")
        cur.close()
        return True
    
def GetDeedByID(ID : int):
    deed = None
    if ID == 0:
        return deed
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"SELECT * FROM Deed WHERE id = '{ID}'")
        Data = Cursor.fetchone()
        if Data:
            deed = Deed()
            deed.ID = Data[0]
            deed.Portion = Data[1]
            deed.No = Data[2]
            deed.Page = Data[3]
            deed.Province = Data[4]
            deed.District = Data[5]
            deed.City = Data[6]
            deed.Rai = Data[7]
            deed.Ngan = Data[8]
            deed.Wah = Data[9]
        Cursor.close()
    return deed
    
def UpdateDeed(Deed : Deed, OldID : int):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"UPDATE Deed SET portion='{Deed.Portion}', no='{Deed.No}', page='{Deed.Page}', province='{Deed.Province}', district='{Deed.District}', city='{Deed.City}', rai='{Deed.Rai}', ngan='{Deed.Ngan}', wah='{Deed.Wah}' WHERE id = '{OldID}'")
        Cursor.close()
        return True

def UpdateDeedID(OldID : int, NewID : int):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"UPDATE Deed SET id = '{NewID}' WHERE id = '{OldID}'")
        Cursor.close()
        return True
    
def SearchProject(Selected : str, Keyword : str):
    Projects = {}
    with Connect() as Session:
        Cursor = Session.cursor()
        if Selected == 'id' and Selected == 'current_phase':
            Cursor.execute(f"SELECT * FROM Project WHERE {Selected} = '{Keyword}' ORDER BY id ASC")
        elif Selected == 'emp_fname' or Selected == 'emp_lname':
            Column = "fname" if Selected == "emp_fname" else "lname"
            Employees = SearchEmployee(Column, Keyword)
            if Employees:
                Values = ", ".join([str(Employee.ID) for Employee in Employees.values()])
                Cursor.execute(f"SELECT * FROM Project WHERE employee_id IN ({Values}) ORDER BY id ASC")
        elif Selected == 'cus_fname' or Selected == 'cus_lname':
            Column = "fname" if Selected == "cus_fname" else "lname"
            Customers = SearchCustomer(Column, Keyword)
            if Customers:
                Values = ", ".join([str(Customer.ID) for Customer in Customers.values()])
                Cursor.execute(f"SELECT * FROM Project WHERE customer_id IN ({Values}) ORDER BY id ASC")
        else:
            Cursor.execute(f"SELECT * FROM Project WHERE {Selected} LIKE '%{Keyword}%' ORDER BY id ASC")
        List = Cursor.fetchall()
        if List:
            for Data in List:
                Pro = Project()
                Pro.ID = Data[0]
                Pro.CustomerID = Data[1]
                Pro.DateProject = Data[2]
                Pro.BuildingType = Data[3]
                Pro.BudgetProject = Data[4]
                Pro.DeedID = Data[5]
                Pro.EmployeeID = Data[6]
                Pro.DemolishTime = Data[7]
                Pro.BuildingTime = Data[8]
                Pro.JuristicID = Data[9]
                Pro.JuristicPerson = Data[10]
                Pro.AddressID = Data[11]
                Pro.TemplateID = Data[12]
                Pro.PhaseCount = Data[13]
                Pro.Status = Data[14]
                Pro.Company = Data[15]
                Pro.CurrentPhase = Data[16]
                Pro.Deed = GetDeedByID(Pro.DeedID)
                Pro.Address = GetAddressByID(Pro.AddressID, "PRO")
                Pro.Phases = GetAllPhaseByProjectID(Pro.ID)
                Projects.update({ Pro.ID : Pro })
        List.clear()
        Cursor.close()
    return Projects

def LoadTemplates():
    Templates = {}
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute("SELECT * FROM Template ORDER BY id ASC")
        Lists = Cursor.fetchall()
        if Lists:
            for Data in Lists:
                Tem = Template()
                Tem.ID = Data[0]
                Tem.Type = Data[1]
                Tem.Path = Data[2]
                Tem.Draftman = Data[3]
                Tem.ProjectID = Data[4]
                Tem.CreateDate = Data[5]
                Tem.AmountOfEdited = Data[6]
                Templates.update({ Tem.ID : Tem })
        Lists.clear()
        Cursor.close()
    return Templates

def GetProjectsByDate(DateString : str, Months : int = 1):
    DATE_FORMAT = "%Y-%m-%d"
    Start = (datetime.strptime(DateString, DATE_FORMAT)).strftime(DATE_FORMAT)
    End = (datetime.strptime(DateString, DATE_FORMAT) + timedelta(weeks=Months * 4)).strftime(DATE_FORMAT)
    Projects = {}
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"SELECT * FROM Project WHERE '{Start}' <= date_project AND date_project < '{End}' ORDER BY id ASC")
        List = Cursor.fetchall()
        if List:
            for Data in List:
                Pro = Project()
                Pro.ID = Data[0]
                Pro.CustomerID = Data[1]
                Pro.DateProject = Data[2]
                Pro.BuildingType = Data[3]
                Pro.BudgetProject = Data[4]
                Pro.DeedID = Data[5]
                Pro.EmployeeID = Data[6]
                Pro.DemolishTime = Data[7]
                Pro.BuildingTime = Data[8]
                Pro.JuristicID = Data[9]
                Pro.JuristicPerson = Data[10]
                Pro.AddressID = Data[11]
                Pro.TemplateID = Data[12]
                Pro.PhaseCount = Data[13]
                Pro.Status = Data[14]
                Pro.Company = Data[15]
                Pro.CurrentPhase = Data[16]
                Pro.Deed = GetDeedByID(Pro.DeedID)
                Pro.Address = GetAddressByID(Pro.AddressID, "PRO")
                Pro.Phases = GetAllPhaseByProjectID(Pro.ID)
                Projects.update({ Pro.ID : Pro })
        List.clear()
        Cursor.close()
    return Projects

def CreateTemplate(Template : Template):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"INSERT INTO Template (type, path, draftman, project_id, create_date, amount) VALUES ('{Template.Type}', '{Template.Path}', '{Template.Draftman}', '{Template.ProjectID}', '{Template.CreateDate}', '{Template.AmountOfEdited}') RETURNING id")
        LastID = Cursor.lastrowid
        Cursor.close()
        return LastID

def UpdateTemplateProjectID(ID : int, ProjectID : int):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"UPDATE Template SET project_id='{ProjectID}' WHERE id = '{ID}'")
        Cursor.close()
        return True
    
def UpdateTemplate(Template : Template):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"UPDATE Template SET type='{Template.Type}', path='{Template.Path}', draftman='{Template.Draftman}', project_id='{Template.ProjectID}', amount='{Template.AmountOfEdited}' WHERE id = '{Template.ID}'")
        Cursor.close()
        return True
    
def DeleteTemplate(ID : int):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"DELETE FROM Template WHERE id = '{ID}'")
        Cursor.close()
        return True
    
def UpdateProjectTemplateID(ID : int, TemplateID : int):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"UPDATE Project SET template_id='{TemplateID}' WHERE id = '{ID}'")
        Cursor.close()
        return True
    
def SearchTemplate(Selected : str, Keyword : str):
    Templates = {}
    with Connect() as Session:
        cur = Session.cursor()
        if Selected == 'id':
            cur.execute(f"SELECT * FROM Template WHERE {Selected} LIKE '{Keyword}' ORDER BY id ASC")
        else:
            cur.execute(f"SELECT * FROM Template WHERE {Selected} LIKE '%{Keyword}%' ORDER BY id ASC")
        List = cur.fetchall()
        for Data in List:
            Tem = Template()
            Tem.ID = Data[0]
            Tem.Type = Data[1]
            Tem.Path = Data[2]
            Tem.Draftman = Data[3]
            Tem.ProjectID = Data[4]
            Tem.CreateDate = Data[5]
            Tem.AmountOfEdited = Data[6]
            Templates.update({ Tem.ID : Tem })
        List.clear()
        cur.close()
    return Templates

def UpdateTemplatePath(ID : int, Path : str):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"UPDATE Template SET path='{Path}' WHERE id = '{ID}'")
        Cursor.close()
        return True
    
def IsExistTemplateCountByProjectID(ID : int):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"SELECT COUNT(*) FROM Template WHERE project_id = '{ID}'")
        Counter = Cursor.fetchone()[0]
        Cursor.close()
        return not Counter > 0
    
def UpdatePhaseDescription(ProjectID : int, PhaseID : int, PhaseDescription : str):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"UPDATE Phase SET description='{PhaseDescription}' WHERE project_id = '{ProjectID}' AND id='{PhaseID}'")
        Cursor.close()
        return True

def UpdatePhase(ProjectID : int, Phase : Phase):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"UPDATE Phase SET start='{Phase.Start}', end='{Phase.End}', status='{Phase.Status}', payment='{Phase.Payment}', payment_date='{Phase.PaymentDate}', due_date='{Phase.DueDate}', description_excess_cost='{Phase.DescriptionExcessCost}', excess_cost='{Phase.ExcessCost}', note='{Phase.Note}' WHERE project_id = '{ProjectID}' AND id='{Phase.ID}'")
        Cursor.close()
        return True
    
def UpdateProjectCurrentPhase(ID : int, CurrentPhase : int):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"UPDATE Project SET current_phase='{CurrentPhase}' WHERE id = '{ID}'")
        Cursor.close()
        return True
    
def UpdateProjectStatus(ID : int, Status : int):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"UPDATE Project SET status='{Status}' WHERE id = '{ID}'")
        Cursor.close()
        return True
    
def UpdatePhaseStatus(ProjectID : int, PhaseID : int, Status : int):
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute(f"UPDATE Phase SET status='{Status}' WHERE project_id='{ProjectID}' AND id='{PhaseID}'")
        Cursor.close()
        return True
    
def LoadLastProjects():
    Projects = {}
    with Connect() as Session:
        Cursor = Session.cursor()
        Cursor.execute("SELECT * FROM Project WHERE status != 'ดำเนินการเสร็จสิ้น' ORDER BY id DESC")
        List = Cursor.fetchall()
        if List:
            for Data in List:
                Pro = Project()
                Pro.ID = Data[0]
                Pro.CustomerID = Data[1]
                Pro.DateProject = Data[2]
                Pro.BuildingType = Data[3]
                Pro.BudgetProject = Data[4]
                Pro.DeedID = Data[5]
                Pro.EmployeeID = Data[6]
                Pro.DemolishTime = Data[7]
                Pro.BuildingTime = Data[8]
                Pro.JuristicID = Data[9]
                Pro.JuristicPerson = Data[10]
                Pro.AddressID = Data[11]
                Pro.TemplateID = Data[12]
                Pro.PhaseCount = Data[13]
                Pro.Status = Data[14]
                Pro.Company = Data[15]
                Pro.CurrentPhase = Data[16]
                Pro.Deed = GetDeedByID(Pro.DeedID)
                Pro.Address = GetAddressByID(Pro.AddressID, "PRO")
                Pro.Phases = GetAllPhaseByProjectID(Pro.ID)
                Projects.update({ Pro.ID : Pro })
        List.clear()
        Cursor.close()
    return Projects

def SearchPayment(Selected : str, Keyword : str):
    Projects = {}
    with Connect() as Session:
        Cursor = Session.cursor()
        if Selected == 'id':
            Cursor.execute(f"SELECT * FROM Project WHERE {Selected} = '{Keyword}' AND status='รอการชำระเงิน' ORDER BY id ASC")
        elif Selected == 'emp_fname' or Selected == 'emp_lname':
            Column = "fname" if Selected == "emp_fname" else "lname"
            Employees = SearchEmployee(Column, Keyword)
            if Employees:
                Values = ", ".join([str(Employee.ID) for Employee in Employees.values()])
                Cursor.execute(f"SELECT * FROM Project WHERE employee_id IN ({Values}) AND status='รอการชำระเงิน' ORDER BY id ASC")
        elif Selected == 'cus_fname' or Selected == 'cus_lname':
            Column = "fname" if Selected == "cus_fname" else "lname"
            Customers = SearchCustomer(Column, Keyword)
            if Customers:
                Values = ", ".join([str(Customer.ID) for Customer in Customers.values()])
                Cursor.execute(f"SELECT * FROM Project WHERE customer_id IN ({Values}) AND status='รอการชำระเงิน' ORDER BY id ASC")
        else:
            Cursor.execute(f"SELECT * FROM Project WHERE {Selected} LIKE '%{Keyword}%' AND status='รอการชำระเงิน' ORDER BY id ASC")
        List = Cursor.fetchall()
        if List:
            for Data in List:
                Pro = Project()
                Pro.ID = Data[0]
                Pro.CustomerID = Data[1]
                Pro.DateProject = Data[2]
                Pro.BuildingType = Data[3]
                Pro.BudgetProject = Data[4]
                Pro.DeedID = Data[5]
                Pro.EmployeeID = Data[6]
                Pro.DemolishTime = Data[7]
                Pro.BuildingTime = Data[8]
                Pro.JuristicID = Data[9]
                Pro.JuristicPerson = Data[10]
                Pro.AddressID = Data[11]
                Pro.TemplateID = Data[12]
                Pro.PhaseCount = Data[13]
                Pro.Status = Data[14]
                Pro.Company = Data[15]
                Pro.CurrentPhase = Data[16]
                Pro.Deed = GetDeedByID(Pro.DeedID)
                Pro.Address = GetAddressByID(Pro.AddressID, "PRO")
                Pro.Phases = GetAllPhaseByProjectID(Pro.ID)
                Projects.update({ Pro.ID : Pro })
        List.clear()
        Cursor.close()
    return Projects