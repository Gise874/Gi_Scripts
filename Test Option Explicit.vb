Option Explicit

Sub ProcessEmployees()

    Dim employeeName As String
    Dim department As String
    Dim salary As Double

    employeeName = "John Smith"
    department = "IT"
    salary = 75000

    MsgBox "Employee: " & employeeName & vbCrLf & _
           "Department: " & department & vbCrLf & _
           "Salary: $" & salary

End Sub

Function CalculateBonus(baseSalary As Double, percentage As Double) As Double
    CalculateBonus = baseSalary * (percentage / 100)
End Function

Sub TestBonus()

    Dim bonus As Double

    bonus = CalculateBonus(75000, 10)

    Debug.Print "Bonus Amount: " & bonus

End Sub