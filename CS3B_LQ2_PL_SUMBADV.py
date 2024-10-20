"""
Student Name: Vinico Sumbad
Course, Year and Section: BSCS - 3B
Quiz No. : 2
Date: Oct 13, 2024

"""
# REFRACTORED

studentName = "Lewis Fonci"
studentAddress = "City of Candon, Ilocos Sur"
studentFavNum1 = 25                             #Declare the value as 25 as an Integer#Declare the value as 25 as an Integer
studentAge = 25                                 #Declare the value as 25 as an Integer
studentAllowance = float(500)                   #Declare the value as 500 as an float with typecasting

classmateName = "Andrea Andres"
classmateAddress = "City of Vigan, Ilocos Sur"
classmateFavNum1 = "18"                         #Declare the value as 18 as an string
classmateAge = "21"                             #Declare the value as 21 as an string
classmateAllowance = "700"                      #Declare the value as 700 as an string

studentDict = {                                 # Store the name of student name and classmate name in dictionary
    "student" : studentName,
    "classmate" : classmateName
}

sName_Length = len(studentDict["student"].replace(" ","")) #get the length of the studentName
cName_Length = len(studentDict["classmate"].replace(" ","")) #get the length of the classmateName

nameLen = [sName_Length, cName_Length]          # using Set to store the name lengths

def func():           # Creating a fuction contains if, elif, else from previous quiz Q2
    if "Ilocos Sur" in studentAddress and "Ilocos Sur" in classmateAddress: #use as a condition if "Ilocos Sur" is in studentAddress AND classmateAddress
        print(studentDict["student"], "is from", studentAddress)                       #Output: LEWIS FONSI is from City of Candon, Ilocos Sur - call and format your variables with concatenation techniques except fstring formatter
        print(studentDict["classmate"], "is from", classmateAddress)                   #Output: andrea andres is from City of Vigan, Ilocos Sur - call and format your variables with concatenation techniques except fstring formatter                    


        if sName_Length > cName_Length: #use the condition where sName_Length > cName_Length
            print(f"{studentDict['student']} has a longer name than {studentDict['classmate']} with {nameLen[0]} letters over {nameLen[1]} letters") #Output: andrea andres has a longer name than LEWIS FONSI with 13 letters over 11 letters
        else:
            print(f"{studentDict['classmate']} has a longer name than {studentDict['student']} with {nameLen[1]} letters over {nameLen[0]} letters") #The opposite result of the IF condition.

    elif "Ilocos Sur" in studentAddress and "Ilocos Sur" in classmateAddress: #use as a condition for elif "Ilocos Sur" is in studentAddress AND classmateAddress   
        sName = studentName.split(" ")                                        #split the studentName with " " - a space as identifier of the splitter
        cName = classmateName.split(" ")                                      #split the classmateName with " " - a space as identifier of the splitter

        print(f"One among {sName[0]} or {cName[0]} lives in Ilocos Sur")      #Output: "One among Lewis or Andrea lives in Ilocos Sur" use the sName_Split and cName_Split and use indexing
    else:
        print("None of them lives in Ilocos Sur")                             #"None of the Students live in Ilocos Sur"

func() # Calling the function that contains if, elif, else

print(f"\nThe added age of {studentDict['student']} and {studentDict['classmate']} is {studentAge + int(classmateAge)}")                              #print using the fstring format: the added age of studentAge and classmateAge, in addition to perform a mathematical
print(f"The subtracted value of fav Num of {studentDict['student']} and {studentDict['classmate']} is {studentFavNum1 - int(classmateFavNum1)}")    #print using the fstring format: the subtracted studentFavNum and classmateFavNum, in addition to perform a mathematical

combineWeeklyallowance = studentAllowance + float(classmateAllowance)                                                           #Add both allowances of the student and classmates.
print(f"The weekly allowance of {studentName} and {classmateName} is {combineWeeklyallowance:.2f} pesos\n")                     #print using the fstring format: the added allowances of the allowance make sure it is in 2 decimal form

classList = [studentDict["student"],studentDict["classmate"]]                             #Create a list containing the value of the student and classmate name
classList_Ext = [studentAddress,classmateAddress]                   #Create a list containing the addresses of the student and classmate

for x in classList:                                                 #Print out the value of the classList using the for loop
    print(x)

classNumbers = [studentAge, int(studentAllowance), studentFavNum1]  #Create a list containing all the numerical vars of the student, asure that all var are int
classNumbers.append(int(classmateAge))                              #append the classmateAge, Note that the list must contain int var only
classNumbers.append(int(classmateFavNum1))                          #append the classmateFavNum1, Note that the list must contain int var only
classNumbers.append(int(classmateAllowance))                        #append the classmateAllowance, Note that the list must contain int var only

classNumbers.sort(reverse=True)                                                 #Sort the list (reversed)

for x in classNumbers:                                              #Print out the value of the classNumbers using the for loop
    print(x)

def quizTwo(studentNameCS):                                         #Create a simple function for quizTwo() which receives a parameter studentNameCS 
    print(f"\nCongratulations on Quiz 2 {studentNameCS}")           #Print with fstring format Output: Congratulations on Quiz 2 {passed variable - student name}

studentNameCS = input("Name of the User: ")                                     

quizTwo(studentNameCS)                                              #Call the function quizTwo() passing a variable value of the Name of the Student of CS3B

# REFRACTORED