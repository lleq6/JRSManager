class Phase:
    ProjectID = 0
    ID = 0
    EmployeeID = 0
    Title = ""
    Start = ""
    End = ""
    Status = ""
    Path = ""
    Payment = ""
    PaymentDate = ""
    DueDate = ""
    Description = ""
    DescriptionExcessCost = ""
    CollectionPercent = 0
    ExcessCost = 0
    Note = ""

    def GetCost(self, Budget : int):
        return int((Budget * self.CollectionPercent) / 100)