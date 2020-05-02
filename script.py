import json

class User():
    username=""
    password=""
    usertype=""
    priviledgelevel=""
    
    def __init__(self,username,password,usertype):
        self.username=username
        self.password=password
        self.usertype=usertype
        self.priviledgelevel=assignPrivilegeLevels(usertype)
    def registerUser():
        pass
    def writeSicknessDetails(self):
        username = input("Enter the name of the patient : ")
        isRecorded = recordSicknessDetails(username)
        while(not isRecorded):
            username = input("Enter the name of the patient : ")
            isRecorded = recordSicknessDetails(username)
        
class Patient(User):
    pass
      
class Nurse(User):
    def registerUser(self):
        usertype = input("User Type (patient) : ")
        if(usertype=="patient"):
            register(usertype)
        else:
            print("You can add only Patients")
            while(usertype != "patient"):
                usertype = input("User Type (patient) : ")
                register(usertype)
    def writeUserDetails(self):
        username = input("Enter the name of the user : ")
        #writePersonalInfo(username)
        writePersonalData = writePersonalInfo(username)
        while(not writePersonalData):
            username = input("Enter the name of the user : ")
            writePersonalData = writePersonalInfo(username)
        
class LabAssistant(User):
    def registerUser(self):
        usertype = input("User Type (patient/nurse) : ")
        if(usertype=="patient" or usertype=="nurse"):
            register(usertype)
        else:
            isType = True
            while(isType):
                print("You can add only Patients and Nurses")
                usertype = input("User Type (patient/nurse) : ")
                if(usertype=="patient" or usertype=="nurse"):
                    isType=False
                    register(usertype)
    def writeLabTestPrescription(self):
        username = input("Enter the name of the patient : ")
        isWritten = writeLabPrescriptions(username)
        while(not isWritten):
            username = input("Enter the name of the user : ")
            isWritten = writePrescriptions(username)
            
class Doctor(User):
    def registerUser(self):
        usertype = input("User Type (patient/Nurse/lab assistant) : ")
        if(usertype=="patient" or usertype=="nurse" or usertype=="lab assistant"):
            register(usertype)
        else:
            isType = True
            while(isType):
                print("You can add only Patients, Nurses and Lab Assistants")
                usertype = input("User Type (patient/nurse) : ")
                if(usertype=="patient" or usertype=="nurse" or usertype=="lab assistant"):
                    isType=False
                    register(usertype)
    def writeDrugPrescriptions(self):
        username = input("Enter the name of the patient : ")
        isWritten = writePrescriptions(username)
        while(not isWritten):
            username = input("Enter the name of the user : ")
            isWritten = writePrescriptions(username)
        
class Admin(User):
    def registerUser(self):
        usertype = input("User Type (patient/nurse/lab assistant/doctor/admin) : ")
        if(usertype=="patient" or usertype=="nurse" or usertype=="lab assistant" or usertype=="doctor" or usertype=="admin"):
            register(usertype)
        else:
            isType = True
            while(isType):
                print ("Invalid user type, please enter a valid user type.")
                usertype = input("User Type (patient/nurse/lab assistant/doctor/admin) : ")
                if(usertype=="patient" or usertype=="nurse" or usertype=="lab assistant" or usertype=="doctor" or usertype=="admin"):
                    isType=False
                    register(usertype)
                
#funtion to assign user privilage levels
def assignPrivilegeLevels(usertype):
    
    privilegeLevel = 0
    
    if(usertype=="patient"):
        privilegeLevel=0
    elif(usertype=="nurse"):
        privilegeLevel=1
    elif(usertype=="lab assistant"):
        privilegeLevel=2
    elif(usertype=="doctor"):
        privilegeLevel=3
    elif(usertype=="admin"):
        privilegeLevel=4
    else:
        privilegeLevel=5
    return privilegeLevel
        

#function to register users
def register(utype):
    
    userdetails = {"username" : "",
        "password" : "",
        "usertype" : "",
        "priviledgelevel" : ""}
    
    print ("Enter your details here")
    
    username = input("Username : ")
    password = input("Password : ")
    usertype = utype
    priviledgelevel=assignPrivilegeLevels(utype)  
        
    userdetails["username"],userdetails["password"],userdetails["usertype"],userdetails["priviledgelevel"]=username,password,usertype,priviledgelevel
    
    jsonFile = open("users.json", "r+")
    data = json.load(jsonFile)
    data['users'].append(userdetails)
    
    jrecord = json.dumps(data)
    with open('users.json','w') as f:
        f.write(jrecord)
        f.close
    
    print (username,"is registered as a",usertype)

def login(username, password):
    
    currentUser=User("","","")

    jsonFile = open("users.json", "r+")
    data = json.load(jsonFile)
    
    for user in data['users']:
        if(user['username']==username and user['password']==password):
            if(user['usertype']=='patient'):
                currentUser = Patient(username,password,'patient')
            elif(user['usertype']=='nurse'):
                currentUser = Nurse(username,password,'nurse')
            elif(user['usertype']=='lab assistant'):
                currentUser = LabAssistant(username,password,'lab assistant')
            elif(user['usertype']=='doctor'):
                currentUser = Doctor(username,password,'doctor')
            elif(user['usertype']=='admin'):
                currentUser = Admin(username,password,'admin')
                
            print ("Hi "+currentUser.username+"! You are logged in...")
            return currentUser
            #print ("current user is : ",currentUser.username)
            #currentUser['username'],currentUser['priviledgelevel']=username,user['priviledgelevel']

def writePersonalInfo(username):
    
    jsonFile = open("users.json", "r+")
    data = json.load(jsonFile)
    
    foundUser=False
    
    userinfo = {
        "username" : "",
        "age" : "",
        "nic" : "",
        "tele" : ""
        }
    
    for user in data['users']:
        #print(user['username'])
        if(user['username']==username and user['priviledgelevel']=="0"):
            foundUser=True
            print ("Enter your user details : ")
            age = input("Age : ")
            nic = input("NIC : ")
            tele = input("Telephone : ")
            
            userinfo["username"],userinfo["age"],userinfo["nic"],userinfo["tele"]=username,age,nic,tele
            
            jsonFile1 = open("userinfo.json", "r+")
            userinfodata = json.load(jsonFile1)
            userinfodata['users'].append(userinfo)
            
            jrecord = json.dumps(userinfodata)
            with open('userinfo.json','w') as f:
                f.write(jrecord)
                f.close
                break
    if(not foundUser):
        print ("Invalid username, try again with a correct username")
        return False
    else:
        print ("User data stored successfully")
        return True

def recordSicknessDetails(username):
    
    sicknessInfo = {
        "username" : "",
        "info" : ""
        }
    
    jsonFile = open("users.json", "r+")
    data = json.load(jsonFile)
    
    foundUser=False
    
    for user in data['users']:
        if(user['username']==username and user['priviledgelevel']=="0"):
            foundUser=True
            info = input("Enter the details of the sickness : ")
            sicknessInfo['username'],sicknessInfo['info']=username,info
            
            jsonFile1 = open("sicknessdetails.json", "r+")
            usersicknessdet = json.load(jsonFile1)
            usersicknessdet['sicknessdetails'].append(sicknessInfo)
            
            jrecord = json.dumps(usersicknessdet)
            
            with open('sicknessdetails.json','w') as f:
                f.write(jrecord)
                f.close
                break
    if(not foundUser):
        print ("Invalid username, try again with a correct username")
        return False
    else:
        print ("Sickness info stored successfully")
        return True
            
def writePrescriptions(username):
        prescription = {
        "username" : "",
        "drugs" : ""
        }
        
        jsonFile = open("users.json", "r+")
        data = json.load(jsonFile)
        
        foundUser=False
        
        for user in data['users']:
            if(user['username']==username and user['priviledgelevel']=="0"):
                foundUser=True
                drugs = input("Enter the list of drugs : ")
                prescription['username'],prescription['drugs']=username,drugs
                
                jsonFile1 = open("drugprescriptions.json", "r+")
                drugprescrips = json.load(jsonFile1)
                drugprescrips['sicknessdetails'].append(prescription)
                
                jrecord = json.dumps(drugprescrips)
                
                with open('drugprescriptions.json','w') as f:
                    f.write(jrecord)
                    f.close
                    break
            
        if(not foundUser):
            print ("Invalid username, try again with a correct username")
            return False
        else:
            print ("Drug prescription stored successfully")
            return True

def writeLabPrescriptions(username):
        labprescription = {
            "username" : "",
            "result" : ""
            }
        
        jsonFile = open("users.json", "r+")
        data = json.load(jsonFile)
        
        foundUser=False
        
        for user in data['users']:
            if(user['username']==username and user['priviledgelevel']=="0"):
                foundUser=True
                result = input("Enter the results of the test : ")
                labprescription['username'],labprescription['result']=username,result
                
                jsonFile1 = open("labprescriptions.json", "r+")
                labprescrips = json.load(jsonFile1)
                labprescrips['labprescriptions'].append(labprescription)
                
                jrecord = json.dumps(labprescrips)
                
                with open('labprescriptions.json','w') as f:
                    f.write(jrecord)
                    f.close
                    break
            
        if(not foundUser):
            print ("Invalid username, try again with a correct username")
            return False
        else:
            print ("Lab prescription stored successfully")
            return True

              
print ("Type your username and password to log in to the system")

username = input("Username : ")
password = input("Password : ")

currentUser = login(username,password)

#print(currentUser.username, currentUser.password, currentUser.usertype, currentUser.priviledgelevel)

if(currentUser.usertype!="patient"):
    operation=input("Type 'Register' to register a new user, 'Write' to write records or 'Read' to read records : ")
else:
    operation=input("Type 'Read' to read records : ")


if(operation=='Register'):
    currentUser.registerUser()
elif(operation=='Write'):
    print ("Input the number relevant number : "+"\n"+"1 - personal details"
           +"\n"+ "2 - sickness details" + "\n"+ "3 - drug prescriptions"
           + "\n" + "4 - lab test prescriptions")
    number = input("Enter your input : ")
    if(number=="1"):
        if(currentUser.priviledgelevel==1):
            currentUser.writeUserDetails()
        else:
            print("Sorry, only nurses can insert personal details of patients")
    elif(number=="2"):
        if(currentUser.priviledgelevel==1 or currentUser.priviledgelevel==3):
            currentUser.writeSicknessDetails()
        else:
            print("Sorry, only doctors and nurses can insert sickness details of patients")
    elif(number=="3"):
        if(currentUser.priviledgelevel==3):
            currentUser.writeDrugPrescriptions()
        else:
            print("Sorry, only doctors can write drug prescritions for patients")
    elif(number=="4"):
        if(currentUser.priviledgelevel==2):
            currentUser.writeLabTestPrescription()
        else:
            print("Sorry, only lab assistants can write lab test prescritions")
    else:
        print ("Invalid input")
elif(operation=='Read'):
    pass


    