#Final Lab
#Muzahid Oly

def main():
    EmplDict={}
    print("Welcome to Employee Checker!\n")
    
    startProgram(EmplDict) #starts program
    addID_Department(EmplDict) #modifies the name of Employee
    add_30_percent_to_salary(EmplDict) #modifies the salary of Employee
    printD(EmplDict)

#this function starts collecting employees data
def startProgram(dict1):
    userInput=input("Would you like to start the program?(Y or N) ")
    while(userInput!="n" and userInput!="N" ):
        
        #the next five functions asks for specfic employeee information
        EmpID=employeeID(dict1)
        name(EmpID,dict1)
        eEmailAddress(EmpID,dict1)  
        eAddress(EmpID,dict1)
        eSalary(EmpID,dict1)
        
        userInput=input("Would you like to continue the program?(Y or N) ")


def employeeID(dic):
    eID=input("Enter Employee ID (Integet Value with length 7 or under): ")
    if len(eID)>7:
        employeeID(dic)

    eID=int(eID)
    dic[eID]=[]
    return eID


def name(ID,dic):
    
    eName=input("Enter Employee Name (Upper and Lowercase charaters required): ")
    #checks if input was correct
    if ("1" in eName or "2" in eName or  "3" in eName or "4"
     in eName or "5" in eName or "6" in eName or "7" in eName or "8"in eName 
     or "9" in eName or "0"in eName):
     name(ID,dic)
        
    else:
        dic[ID].append(eName)
    


def eEmailAddress(eID,dic):
    eEmailAdd=input("Enter Employee Email Address: ")
    #checks if input was correct
    if ("!" in eEmailAdd or '"' in eEmailAdd or  "'" in eEmailAdd or "#"
     in eEmailAdd or "$" in eEmailAdd or "%" in eEmailAdd or "^" in eEmailAdd or "&"in eEmailAdd 
     or "*" in eEmailAdd or "("in eEmailAdd or ")" in eEmailAdd or "="in eEmailAdd or "+"in eEmailAdd or
      ","in eEmailAdd or "<" in eEmailAdd or">"in eEmailAdd or "/"in eEmailAdd or "?"in eEmailAdd or ";"in eEmailAdd
       or ":"in eEmailAdd or "["in eEmailAdd or "]"in eEmailAdd or "{"in eEmailAdd or "}"in eEmailAdd or "\\" in eEmailAdd ):
        eEmailAddress(eID,dic)
        
    else:
        dic[eID].append(eEmailAdd)



def eAddress(eID,dic):
    eAdd=input("Enter Employee Address: ")
    #checks if input was correct
    if ("!" in eAdd or '"' in eAdd or  "'" in eAdd 
     or "#" in eAdd or "$" in eAdd or "%" in eAdd or "^" in eAdd
     or "&"in eAdd or "*"in eAdd or "_"in eAdd or "="in eAdd or "+"in eAdd 
     or "<"in eAdd or ">"in eAdd or "?"in eAdd or ";"in eAdd or ":"in eAdd 
     or "["in eAdd or "]"in eAdd or "{"in eAdd or "}"in eAdd or "\\" in eAdd ):
        eAddress(eID,dic)

    else:
        dic[eID].append(eAdd)


def eSalary(eID,dic):
    eSal=float(input("Enter Employee's Salary: "))
    #checks if input was correct
    if eSal>=18 and eSal<=27:
        dic[eID].append(eSal)
    else:
        eSalary(eID,dic)


def addID_Department(dic):
    list1=list(dic.keys())
    #here i made the keys into a list so i could interate through them and modify their values
    for i in list1:
        dic[i][0]="IT Department "+dic[i][0]

def add_30_percent_to_salary(dic):
    list1=list(dic.keys())
    #here i made the keys into a list so i could interate through them and modify their values
    for i in list1:
        dic[i][3]=1.3*dic[i][3]

    
def printD(dic):
    list1=list(dic.keys())
    #here i made the keys into a list so i could interate through them and print their values in an orderly fashion
    print("{:<15} {:<25} {:<25}{:<25}{:<25}".format( "ID", "Name", "Email","Address","New Salary"))
    for i in list1:
        print("{:<15} {:<25} {:<25}{:<25}{:<25}".format( i, dic[i][0], dic[i][1],dic[i][2],dic[i][3]))


#calls the main function to start the program
main()
