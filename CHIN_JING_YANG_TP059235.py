# Chin Jing Yang
# TP059235
# Special statue WT = waiting for testing
## All strings with "center()" is only for the needs of keeping the file neatly
def getHeader():
    return "ID".center(8," ")+"\t"+"Name".center(20," ")+"\t"+"Group Code".center(10," ")+"\t"+"Zone".center(6," ")+"\t"+"Contact Number".center(15," ") + "\t"+"Email Address".center(20," ")+"\t"+"CheckDate".center(10," ")+ "\t" +"Action".center(10," ") + "\t" + "Status".center(10," ")+"\t"+"Remark".center(20," ")+"\t"+"Case Code".center(10," ") + "\t" + "DiagDate".center(10," ") + "\n"
def replaceFileDetails(patientOld,patientNew):
    file = open("Name_List.txt","r")
    replacement = ""
    counter = 0
    for lines in file:
        if counter == 0:
            counter = 1
            continue
        if patientOld in lines:
            replacement = replacement + patientNew
            continue
        replacement = replacement + lines
    file.close()
    fileWriter = open("Name_List.txt","w")
    fileWriter.write(getHeader())
    fileWriter.write(replacement)
    fileWriter.close()
#1st Question
import datetime #Autogenerate datetime
def dateGenerator():
    date = datetime.datetime.now()
    return str(date)[:10] #Ignore the details(time) after the date


def idGenerator(group,zone):#This function is to check is there any same id in the file
    count = 1
    id = zone + str(count) + group
    checker = open("Name_List.txt","r")
    for lines in checker:
        if id in lines:
            count +=1
            id = zone + str(count) + group
    checker.close()
    return count

def idGeneratorCheckList(detailList,group,zone):#This function is to check is there any sam id in the list. It is combined with idGenerator to perform a unique id
    count = idGenerator(group,zone)
    id = zone + str(count) + group
    for iDs in detailList:
        if id in iDs[0]:
            count +=1
            id = zone + str(count) + group
    return id

#The main design part for Question 1 is here
def registration():
    header = getHeader()
    try: #To prevent causing error if the Name_List.txt is missing
        file = open("Name_List.txt","r")
        first = file.read(1)
        file.close() #The purpose of these two line is to check is Name_List.txt really there, so I open a file to read and close it immediately
        file = open("Name_List.txt","a")
        #These lines are existed to check the header. if the file is empty means there is no header
        if not first:#If the file is empty, the first character must be null, so "first"will be false
            file.write(header)#Write the header for the file
            
    except IOError: #If the file is missing, then the user should register again
        file = open("Name_List.txt","w")
        print("Since this is the first time you've been here, please kindly register all of the patients :D\n")
        file.write(header)
        

    number_of_patient = input("Please enter the number of patients you want to register :")
    while(not number_of_patient.isdigit()): #Validate the input is only positive and int
        number_of_patient = input("Sorry, only positive integer please :")
        
    patientList = [] #Creating a list of patients for list of patient's details
    for x in range(0,int(number_of_patient)):
        patient = []
        print("Please enter patient's detail......Current patient no:"+str(x+1))
        zone = input("Which zone do patient belong to? Please enter the zone code to proceed :\nA: East\nB: West\nC: North\nD: South\nYour Choice here: ")
        zone = zone.upper() #Make the strings in variable zone uppercased, easier in validatoin
        while (zone != "A" and zone !="B" and zone!="C" and zone != "D"):
            zone = input("Invalid zone! Please enter the zone code(A/B/C/D) again :")
            zone = zone.upper() #Same as above, Allow user to enter code in either uppercase or lowercase
        #The print is to descript the details for all the groups
        print("There are several group for patients. As below :\nATO stands for asymptimatic individuals with history of travelling overseas.",
              "\n\nACC stands for asymptomatic individuals with history of contact with known case of COVID-19.",
              "\n\nAEO stands for asymptomatic individuals who had attended event associated with known COVID-19 outbreak.",
              "\n\nSID stands for Symptomatic individuals.","\n\nAHS stands for Aymptomatic hospical staff.")
        group = input("Which groups of patient do patient belong to? Please enter the Group Code :")
        group = group.upper() #Same idea as the zone variable
        while(group != "ATO" and group != "ACC" and group != "AEO" and group != "SID" and group != "AHS"):
            group = input("Invalid group code! Please your group code (ATO/ACC/AEO/SID/AHS) again :")
            group = group.upper() #Same as above
        name = input("Patient's name please :")
        contact = input("Patient's Number please: ")
        while(not contact.isdigit() or  len(contact) < 10 or len(contact) > 11):
            contact = input("Invalid phone number. Please enter again: ")
        email = input("Patient's email please: ")
        while(not email.endswith(".com") or not "@" in email):
            email = input("Invalid email. Please enter patient's email again: ")
        id = idGeneratorCheckList(patientList,group,zone) #The id of the current patient
        #Arranging patient's information in the correct order
        patient.append(id)
        patient.append(name)
        patient.append(group)
        patient.append(zone)
        patient.append(contact)
        patient.append(email)
        patient.append(dateGenerator())
        patient.append("WT")
        patient.append("Undiagnosed")
        patient.append("Test 1 required")
        patient.append("N/A")
        patient.append("-")
        patientList.append(patient)
    for patients in patientList:
        counter = 1
        for information in patients:
            if counter == 1:
                file.write(information.center(8," ")+"\t")
            elif counter == 2 or counter == 6 or counter == 10:
                file.write(information.center(20," ")+"\t")
            elif counter == 4:
                file.write(information.center(6," ")+"\t")
            elif counter == 5:
                file.write(information.center(15," ")+"\t")
            else:
                file.write(information.center(10," ")+"\t")
            counter +=1
        file.write("\n")
    file.close()
    
# 2nd Question
def askRegistration(): #For emergyncy registration
    register = input("Any emergency patient to be registered? Type 'y' for registration else for continue testing: ")
    register = register.lower()
    if register == "y":
        registration()
#Case Number Generator is a part of Question 3
#For Convinience, I created it in question 2
#So when the patient is detected positive, it will automatically generate a case code
def caseNumberGenerator():
    infec = open("Infected_Name_List.txt","r")
    counter = 0
    first = infec.read(1)
    if not first:
        counter = 1
    for lines in infec:
        counter +=1
    if counter < 10:
        return "000"+str(counter)
    elif counter < 100:
        return "00"+str(counter)
    elif counter < 1000:
        return  "0"+str(counter)
    infec.close()
    return str(counter)
#This function is to write in all the infected patient into the file in sequence
def infected(patient,test):
    try:
        checker = open("Infected_Name_List.txt","r")
        file = open("Infected_Name_List.txt","a")
        first = checker.read(1)
        if not first:
            file.write(getHeader())
        checker.close()
    except IOError :
        file = open("Infected_Name_List.txt","w")
        file.write(getHeader())
    patientOld = patient
    if "Phase1" in patient:
        patient = patient.replace("   Phase1   ","Admitted ICU")
    elif "Phase2" in patient :
        patient = patient.replace("   Phase2  ","Admitted NW")
    elif "Phase3" in patient:
        patient = patient.replace("   Phase3  ","Admitted NW")
    #patient = patient.replace("\n","\t")
    patient = patient.replace(" N/A",caseNumberGenerator())
    patient = patient.replace("    -     ",dateGenerator())
    file.write(patient)
    file.close()
    replaceFileDetails(patientOld,patient) #Change the data in the Original data file
#Ensure the patient is in file
def identification(fileName,mode,patient):
    checker = open(fileName,mode)
    flag = 0
    for lines in checker:
        if patient in lines:
            flag = 1
            break
    checker.close()
    return flag == 1
#Ensure the patient is in file.
def manualIdentification(fileName,mode,patient):
    checker = open(fileName,mode)
    flag = 0
    patientDetails = ""
    for lines in checker:
        if patient in lines:
            identifier = input("Are you looking for this person?\n"+getHeader()+lines+"\nPlease enter y or n: ") #This line is to prevent some accident like sometimes people will have the same name
            identifier = identifier.lower()
            while (identifier != "y" and identifier != "n"): #so if the user enter no, the system will continue find another person that suits the requirement
                identifier = input("Wrong option! y for yes and n for no: ")
            if identifier == "y":
                flag = 1
                patientDetails = lines
                break
    checker.close()
    return flag == 1, patientDetails #patientDetails return the full details of the current patient to prevent the system use the user's searching data to do testing

def testPhase1(patient):
    try:
        checker = open("Test_Result_1.txt","r")
        first = checker.read(1)
        checker.close()
        file = open("Test_Result_1.txt","a")
        if not first:
            file.write(getHeader())
    except IOError :
        file = open("Test_Result_1.txt","w")
        file.write(getHeader())
    result = input("Test Phase 1\nIs this patient infected?\n"+getHeader()+patient+"\nPlease enter POSITIVE or NEGATIVE: ") # Since importing function is not legalled, so I can't use random to automatically decide whether the patient is inffected or not
    result= result.upper()
    patientOld = patient
    while(result != "POSITIVE" and result != "NEGATIVE"):
        result = input("Invalid Option. Failed to identify! Please enter the result again. POSITIVE or NEGATIVE: ")
        result = result.upper()
    if result == "POSITIVE":#Each group of patients has different action to be taken
        if "AHS" in patient:
            patient = patient.replace(" WT ","HQNF")
        else:
            patient = patient.replace(" WT ","QHNF")

        patient = patient.replace("Undiagnosed","   Active  ")
        patient = patient.replace("Test 1 required","     Phase1    ") #Phase 1 is a marking for the other function to decide where should the patient stay
        file.write(patient)
        file.close()
        replaceFileDetails(patientOld,patient)
        infected(patient,1)
    else:#Same as above, different group of patient have different action to be taken
        if "SID" in patient:
            patient = patient.replace(" WT ","HQFR")
        elif "AHS" in patient:
            patient = patient.replace(" WT ","CWFR")
        else:
            patient = patient.replace(" WT ","QDFR")

        patient = patient.replace("Test 1 required","Test 2 required")
        file.write(patient)
        file.close()
        replaceFileDetails(patientOld,patient)
    askRegistration()
        
    
        
def testPhase2(patient):
    try:
        checker = open("Test_Result_2.txt","r")
        first = checker.read(1)
        checker.close
        file = open("Test_Result_2.txt","a")
        if not first:
            file.write(getHeader())
    except IOError:
        file = open("Test_Result_2.txt","w")
        file.write(getHeader())
    try:
        if not identification("Test_Result_1.txt","r",patient):
            print("Certain patient has not tested in testing 1..... Sending to testing 1...")
            testPhase1(patient)
            return "" #Break the function if patient is not tested in phase 1
    except IOError:
        print("Certain pacient has not tested in testing 1..... Sending to testing 1...")
        testPhase1(patient)
        return "" #Break the loop if exception detected
    patientOld = patient
    result = input("Test Phase 2\nIs this patient infected?\n"+getHeader()+patient+"\nPlease enter POSITIVE or NEGATIVE: ") # Same as testPhase 1
    result= result.upper()
    while(result != "POSITIVE" and result != "NEGATIVE"):
        result = input("Invalid Option. Failed to identify! Please enter the result again. POSITIVE or NEGATIVE: ")
        result = result.upper()
    if result == "POSITIVE":
        if "AHS" in patient:#Same as testPhase 1
            patient = patient.replace("CWFR","HQNF")
        elif "SID" in patient:
            patient = patient.replace("HQFR","QHNF")
        else :
            patient = patient.replace("QDFR","QHNF")
        patient = patient.replace("Undiagnosed","   Active  ")
        patient = patient.replace("Test 2 required","     Phase2    ") #"Phase 2 is a marking for the other function to decide where should the patient stay
        file.write(patient)
        file.close()
        replaceFileDetails(patientOld,patient)
        infected(patient,2)
    else:#Since they are still negative, the only thing to be changed is only the next remark section
        patient = patient.replace("Test 2 required","Test 3 required")
        file.write(patient)
        file.close()
        replaceFileDetails(patientOld,patient)
    askRegistration()
        
def testPhase3(patient):
    try:
        checker = open("Test_Result_3.txt","r")
        first = checker.read(1)
        checker.close
        file = open("Test_Result_3.txt","a")
        if not first:
            file.write(getHeader())
    except IOError:
        file = open("Test_Result_3.txt","w")
        file.write(getHeader())
    try:
        if not identification("Test_Result_2.txt","r",patient):
            print("Certain pacient has not tested in testing 2..... Sending to testing 2...")
            testPhase2(patient)
            return "" #Break the loop if the patient is not tested in Test 2
    except IOError:
        print("Certain pacient has not tested in testing 2..... Sending to testing 2...")
        testPhase2(patient)
        return "" #Break the loop if Exception Detected
    patientOld = patient
    result = input("Test Phase 3\nIs this patient infected?\n"+getHeader()+patient+"\nPlease enter POSITIVE or NEGATIVE") # Same as testPhase 1
    result= result.upper()
    while(result != "POSITIVE" and result != "NEGATIVE"):
        result = input("Invalid Option. Failed to identify! Please enter the result again. POSITIVE or NEGATIVE: ")
        result = result.upper()
    if result == "POSITIVE":#Same situation as Test Phase 1. Different groups of patient take different action
        if "AHS" in patient:
            patient = patient.replace("CWFR","HQNF")
        elif "SID" in patient:
            patient = patient.replace("HQFR","QHNF")
        else :
            patient = patient.replace("QDFR","QHNF")
        patient = patient.replace("Undiagnosed","   Active  ")#The space added is to prevent the format of alignment being destroyed
        patient = patient.replace("Test 3 required","     Phase3    ") #Phase 3 is a marking for the other function to decide where should the patient stay
        file.write(patient)
        file.close()
        replaceFileDetails(patientOld,patient)
        infected(patient,3)
    else:#Same situation as TestPhase 1. Different groups of patient takes different action
        if "SID" in patient:
            patient = patient.replace("HQFR","RU")

        elif "AHS" in patient:
            patient = patient.replace("CWFR","CW")
        else:
            patient = patient.replace("QDFR","RU")
        patient = patient.replace(" Test 3 required ", "Patient may leave")
        patient = patient.replace("Undiagnosed", "   Safety  ")
        file.write(patient)
        file.close()
        replaceFileDetails(patientOld,patient)
    askRegistration()
    
def testing():
    try:
        checker = open("Name_List.txt","r")
        head = checker.read(1)
        checker.close()
        if not head:
            print("Sorry no patients here!\nPlease do registration before testing")
            registration()
            return ""
    except IOError:
        print("Sorry no file existed!\nPlease do registration first!")
        registration()
        return ""
    selection = input("Do you want to test all patients accordingly or test the specific person only? Enter 1 for accordingly and 2 for testing specific patient:")
    while (selection != "2" and selection != "1"):
        selection = input("Wrong option. Please enter again: ")
    if selection == "1":
        fullList = []
        counter = 1
        file = open("Name_List.txt","r")
        for lines in file:
            if counter == 1:#avoid adding the header into the patientList
                counter += 1
                continue
            fullList.append(lines)
        for patients in fullList:
            if "Test 1 required" in patients:
                testPhase1(patients)
            elif "Test 2 required" in patients:
                testPhase2(patients)
            elif "Test 3 required" in patients:
                testPhase3(patients)
            elif "Not Infected" in patients:
                print("All test procedure for particular patient\n"+getHeader()+patients+"have been completed")
            else:
                print(patients[10:30].strip() + " has been tested positive.")#[10:30] is the range for the patient's name. It's been set
        file.close()
        
    else: #
        patient = input("Please enter the name or the patient's ID to test: ")
        flag, patientDetails = manualIdentification("Name_List.txt","r",patient)
        while not flag:
            patient = input("Sorry, the particular patient is not available in the namelist.\nPlease look for another one: ")
            flag, patientDetails = manualIdentification("Name_List.txt","r",patient)

        phase = input("Select testing phase(1/2/3) :")
        while (phase != "1" and phase != "2" and phase != "3"):
            phase = input("Sorry! No such option available here! Please choose again (1/2/3):")
        if phase == "1": #To ensure that the patient is not getting the same testing and prevent the patient to skip one of the test
            if "Test 1 required" in patientDetails:
                testPhase1(patientDetails)
            else:
                print("Current service not available for " + patientDetails[10:30].strip())#[10:30] is the range of patient's name.
        elif phase == "2":
            if "Test 2 required" in patientDetails:
                testPhase2(patientDetails)
            else:
                print("Current service not available for " + patientDetails[10:30].strip())
        else:
            if "Test 3 required" in patientDetails:
                testPhase3(patientDetails)
            else:
                print("Current service not available for " + patientDetails[10:30].strip())
# Question 3 here
def replaceInfectedNameList(oldDetails,newDetails):#Everytime the details is changed, the Infected name list should be changed. Replacing it is an easy way for me
    infected = open("Infected_Name_List.txt","r")
    replacement = ""
    for lines in infected:
        if oldDetails in lines:
            replacement = replacement + newDetails
            continue
        replacement = replacement + lines
    infected.close()
    rewrite = open("Infected_Name_List.txt","w")
    rewrite.write(replacement)
    rewrite.close()
    
def recovered(patientDetails):
    patient = patientDetails.replace("  Active ","Recovered")
    if "Admitted ICU" in patient:
        patient = patient.replace("Admitted ICU"," Discharged ")
    else:
        patient = patient.replace("Admitted NW"," Discharged")
    replaceFileDetails(patientDetails,patient)
    replaceInfectedNameList(patientDetails,patient)
    
def decease(patientDetails):
    patient = patientDetails.replace(" Active ","Deceased")
    if "Admitted ICU" in patient:
        patient = patient.replace("Admitted ICU","   Heaven   ")
    else:
        patient = patient.replace("Admitted NW","   Heaven  ")
    replaceFileDetails(patientDetails,patient)
    replaceInfectedNameList(patientDetails,patient)
    
def healing():
    try:
        infected = open("Infected_Name_List.txt","r")
        counter = 0
        first = infected.read(1)
        if not first:
            print("No Infected Patients Here!")
            return ""
        for patient in infected:
            if counter == 0: #Prevent taking action to the header
                counter = 1
                continue
            if "Active" in patient: # Deciding the patient's situation manually:D
                patientSituation = input("Did this patient recovered, staying active or this patient didn't make it?\n"+getHeader()+patient+" Type 'a' for staying active,'r' for recovered and 'd' for deceased: ")
                patientSituation = patientSituation.lower()
                while(patientSituation != "a" and patientSituation !="r" and patientSituation != "d"):
                    patientSituation = input("Situation unknown. Please do a proper check: ")
                    patientSituation = patientSituation.lower()
                if patientSituation == "a":
                    continue
                elif patientSituation == "r":
                    recovered(patient)
                else:
                    decease(patient)
            elif "Recovered" in patient:
                print("Current patient\n"+getHeader()+patient+"has already recovered. No need healing anymore.")
            else:
                print("We felt so sorry that \n"+getHeader()+patient+"didn't make it :(")
    except IOError:
        print("No Infected Patients Here!")

# Q4 Statistics Information On Tests Carried Out
def totalTest():
    count = 0
    lineCount = 1
    try:#Check if the Test1 file exist
        file = open("Test_Result_1.txt","r")
        for lines in file:
            if lineCount == 1:
                lineCount = 2
                continue
            count += 1
        file.close()
        file = open("Test_Result_2.txt","r")
        for lines in file:
            if lineCount == 2:
                lineCount = 3
                continue
            count += 1
        file.close()
        file = open("Test_Result_3.txt","r")
        for lines in file:
            if lineCount == 3:
                lineCount = 0
                continue
            count += 1
        file.close()
        return str(count)
    except IOError: #Catching exception if the file is missing or no test result at all.
        if lineCount == 1: #LineCount equal to the file currently counting the patient tested
            print("File for Test Result 1 is missing. No Counts at all.")

        elif lineCount == 2:#As I set the linecount number same as the test result number above
            print("You have only tested Phase 1. Please do the follow up test.")

        else: # So if linecount==1 and throws an error. Means that file1 is not existed. If linecount == 2 and throws and error means file2 is not existed
            print("You have only tested Phase 1 and Phase 2. Please do the final test.")
        return str(count)
        
def patientTest():
    try:
        nameList = open("Name_List.txt","r")
        counter = 0
        for lines in nameList:
            if ("Test 1 required" in lines or "Remark" in lines):
                continue
            counter += 1
        nameList.close()
        return str(counter)
    except IOError: #If the file didnt exits. Means the test hasn't been started yet. So the count must be 0
        print("Sorry you are not even registered any patient yet.")
        return "0"
    
def recoveredTotal():
    try:
        infected = open("Infected_Name_List.txt","r")
        counter = 0
        for lines in infected:
            if "Recovered" in lines:
                counter += 1
        infected.close()
        return str(counter)
    except IOError:
        print("Sorry no infected patient found. Did you do registration or testing on patient?")
        return"0"#No infected means no recovery.
    
def positiveGroup():
    atoCount, accCount, aeoCount, sidCount, ahsCount = 0,0,0,0,0
    try:
        nameList = open("Name_List.txt","r")
        for lines in nameList:#All positive patient will be divided into three groups, which is recovered, deceased, and active.
            if ("Active" in lines or "Recovered" in lines or "Deceased" in lines):
                if "ATO" in lines:
                    atoCount +=1
                elif "ACC" in lines:
                    accCount +=1
                elif "AEO" in lines:
                    aeoCount += 1
                elif "SID" in lines:
                    sidCount +=1
                elif "AHS" in lines:
                    ahsCount +=1
        nameList.close()
        return str(atoCount),str(accCount),str(aeoCount),str(sidCount),str(ahsCount)
    except IOError:
        print("No Registration done.")
        return "0","0","0","0","0" #It suppose to be no one when the file is missing. 
def zones():
    a,b,c,d = 0,0,0,0
    try:
        nameList = open("Name_List.txt","r")
        for lines in nameList:#Only show the active patient in different zone
            lines = lines.strip()
            if "Active" in lines:
                if lines.startswith("A"): #The first letter of the patient's id is set to their zone.
                    a += 1
                elif lines.startswith("B"):#For example, if the patient is from zone b, then their id must start with B
                    b += 1
                elif lines.startswith("C"):#if the patient is from zone c, then their id must start with C
                    c += 1
                elif lines.startswith("D"):
                    d += 1
        nameList.close()
        return str(a),str(b),str(c),str(d) #Only strings can be written into text file, so I do typecast here.
    except IOError:
        print("No Registration has been done,")
        return "0","0","0","0"
def statistics():
    file = open("Statistics.txt","w") #I didn't check the file is exist or not and straightly rewrite it.
    total = totalTest() #This is because everytime the statistics function is called, the statistics must be different
    patient = patientTest()
    recover = recoveredTotal()
    ATO, ACC, AEO, SID, AHS = positiveGroup()
    A, B, C, D = zones()
    file.write("Total Test: "+total+"\n")
    file.write("Total Patient Tested: " + patient+ "\n")
    file.write("Total Patient Recovered: " + recover + "\n")
    file.write("Total result of positive case in Group:\nATO: "+ATO+"\nACC: "+ACC+"\nAEO: "+AEO+"\nSID: "+SID+"\nAHS: " + AHS +"\n")
    file.write("Current Active cases in Zone:\nA: " + A + "\nB: "+ B + "\nC: "+ C + "\nD: " + D + "\n")
    file.close()# The purpose of having code above is to ensure that the statistics is the latest one.
    reopen = open("Statistics.txt","r")#So the program first rewrite all the data and presents it to the user.
    for line in reopen:
        print(line.strip())
    reopen.close()

#Question 5
def searchID(detail):
    try:
        nameList = open("Name_List.txt","r")
        gui = ""
        found = False
        for line in nameList:
            if detail in line[:29]: #[:29] is the range from id to name. So the system will not presents something unrelated with the patient's name
                found = True
                gui += line
                nameList.close()
                return getHeader() + gui
        nameList.close()
        return getHeader()+gui if found else "No such patients"
    except IOError:
        return "Sorry. No files for patient are found. Have you done registration?"

def searchCaseID(caseID):
    try:
        nameList = open("Name_List.txt","r")
        for line in nameList:
            if caseID in line[139:149]:#[139:149] is the position of the patient's id.
                nameList.close()
                return "CaseID: "+caseID + "\tStatus: "+line[109:119].strip() #[109:119] is the position of the patient's status
        nameList.close()
        return "Patients of CaseID: " + caseID + " not found."
    except IOError:
        return "Sorry. No files for patient are found. Have you done registration?"

def statusSearch():
    try:
        nameList = open("Name_List.txt","r")
        flag = False
        gui = getHeader()
        selection = input("Which status of patient are you looking for?\n1.Active\n2.Discharged\n3.Deceased\nPlease enter your option in number: ")
        while(not selection.isdigit() or int(selection) < 1 or int(selection) > 3):
            selection = input("Wrong option. Please enter again: ")
        if selection == "1":
            selection = "Active"
        elif selection == "2":
            selection = "Discharged"
        else:
            selection = "Deceased"
        for line in nameList:
            if selection in line:
                gui += line
                flag = True
        nameList.close()
        return  gui if flag else "No patiet is " + selection + " now." # if flag is true, then the result will be returned. else the system will notify the user that nobody is in the situation
    except IOError:
        return "Sorry. No files for patient are found. Have you done registration?"

def search():
    options = input("What do you want to search?\n1.Search with name or ID\n2.Search with CaseID\n3.Search using Patient Stauts\nPlease enter your option in number: ")
    reply = "" #Declaring a string
    while(not options.isdigit() or int(options) > 3 or int(options) < 1):
        options = input("Sorry. No such Option. Please enter again: ")
    if options == "1":
        name = input("Please enter patient's name or patient's id to search: ")
        reply = searchID(name)
    elif options == "2":
        case = input("Please enter patient's case ID to search: ")
        reply = searchCaseID(case)
    else:
        reply = statusSearch()
    print(reply)
#Program begins here
def deleteFile():
    choice = input("Are you sure you want to clear the records?\nPlease enter 'y' for yes: ")
    if choice == "y":
        print("File Cleaning in progress......")
        nameList = open("Name_List.txt", "w")#The characteristic of "w" is that it will clear all the data in the file first before writing data.
        nameList.close()
        print("Name_List is empty now.")
        test1 = open("Test_Result_1.txt", "w")#So I use"w" to do a clearing progress
        test1.close()
        print("Test_Result_1 is empty now.")#All the print operation is non-essential.
        test2 = open("Test_Result_2.txt", "w")
        test2.close()
        print("Test_Result_2 is empty now.")#I just put them here to tell the user that all data is cleared
        test3 = open("Test_Result_3.txt", "w")
        test3.close()
        print("Test_Result_3 is empty now.")#It is weird if nothing happens when you choose to delete right?
        sta = open("Statistics.txt", "w")
        sta.close()
        print("Statistics is empty now")
        inf = open("Infected_Name_List.txt", "w")
        inf.close()
        print("Infected_Name_List is empty now.")
    else:
        print("Wise choise. File Kept")

print("Welcome to Hospital APU".center(100,"*"))
while(True):
    service = input("Please choose the service you want listed below:\n0.Exit\n1.Registration\n2.Testing\n3.Healing\n4.Statistics\n5.Searching Patient\n6.Delete Patient's Record\n7.Show Record\nReply is required in number: ")
    while(not service.isdigit() or int(service) > 7):#Using the input as strings instead of integer can prevent the system to throw exception if the user enter strings.
        service = input("No such Option. Please choose again: ")
    print("\n")
    if service == "0":
        print("Good bye")
        print("COVID-19 Patient Management System turning off....".center(100,"*"))
        break
    elif service == "1":
        registration()#Calling the registration system
    elif service == "2":
        testing()#Calling the testing system
    elif service == "3":
        healing()#calling the healing system
    elif service == "4":
        statistics()#Calling the statistics system
    elif service == "5":
        search()# Calling the search system
    elif service == "6":
        deleteFile()# Calling the delete file system

    else:
        select = input("Which record do you want to see?\n1.Name list\n2.Infected Name list\nPlease enter your option in number: ")
        while (select != "1" and select != "2"):
            select = input("Sorry! No such option\nPlease enter again: ")
        try:
            if select == "1":
                file = open("Name_List.txt","r")
            else:
                file = open("Infected_Name_List.txt","r")
            first = file.read(1)
            if not first:
                print("The file is empty.")
                file.close()
            else:
                for lines in file:
                    print(lines.strip())
                file.close()
        except IOError:
            if select == "1":#If user enters 1, when the exception is thrown, the program can specific which file is missing
                print("Sorry. The Name_List file is missing.")
            else:#If user enters 2, the system will come to this part to tell the user that the Infected_Name_List.txt is missing
                print("Sorry. The Infected_Name_List file is meaning.")
                    
    print("\n")
