from datetime import date
from Project import Project
from SQLManager import *

def age(birthdate : date):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def getAge(strDate : str):
    df = [int(i) for i in strDate.split('-')]
    bd = date(day=df[2], month=df[1], year=df[0])
    return age(bd)

def getPaymentP(percent : int, budget : int):
    return(budget/100*percent)

def currencyFormat(num : int):
    return "{:,.2f}".format(num)

def getProgressionPercent(project : Project):
    return (100/int(project.PhaseCount))*(int(project.CurrentPhase)-1)

def projectSummaryFormat(projectList : list[Project]):
    percent = {0:[],
               10:[],
               20:[],
               30:[],
               40:[],
               50:[],
               60:[],
               70:[],
               80:[],
               90:[],
               100:[]
               }
    for i in projectList:
        pro: Project
        pro = projectList[i]
        a = getProgressionPercent(projectList[i])
        if pro.Status == "สิ้นสุดเฟส":
            percent[100].append(projectList[i])
        else:
            percent[int((a//10)*10)].append(projectList[i])

    c = 0
    n = 0
    strList = []

    for i in percent:
        check = 0
        status = '1'
        if i == 100:
            status = '2'
        textList = [status,str(i),'','','','','']
        for j in percent[i]:
            check = 1
            emp = GetEmployeeByID(j.EmployeeID)
            cus = GetCustomerByID(j.CustomerID)
            textList[0] += '\n-'
            textList[1] += '\n-'
            textList[2] += f'{j.ID}\n'
            textList[3] += f'{emp.Firstname} {emp.Lastname}\n'
            textList[4] += f'{j.DateProject}\n'
            textList[5] += f'{cus.Firstname} {cus.Lastname}\n'
            textList[6] += f'{j.Address.City} {j.Address.District}\n'
            if i == 100:
                c+=1
            else:
                n+=1
        textList[0] = textList[0][:-1]
        textList[1] = textList[1][:-1]
        textList[2] = textList[2][:-1]
        textList[3] = textList[3][:-1]
        textList[4] = textList[4][:-1]
        textList[5] = textList[5][:-1]
        textList[6] = textList[6][:-1]
        if check == 1:
            strList.append(textList.copy())
    strList.reverse()
    return (strList,[c,n])