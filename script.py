import json

currentUser = {"username" : "",
        "priviledgelevel" : ""}

#funtion to assign user privilage levels
def assignPrivilegeLevels(usertype):
    
    privilegeLevel = 0
    
    if(usertype=="Patient"):
        privilegeLevel=0
    elif(usertype=="Nurse"):
        privilegeLevel=1
    elif(usertype=="Lab Assistant"):
        privilegeLevel=2
    elif(usertype=="Doctor"):
        privilegeLevel=3
    else:
        privilegeLevel=4
    return privilegeLevel
        
    
#function to register users
def register():
    
    userdetails = {"username" : "",
        "password" : "",
        "usertype" : "",
        "priviledgelevel" : ""}
    
    print ("Enter your details here")
    
    username = input("Username : ")
    password = input("Password : ")
    usertype = input("User Type (Patient/Nurse/Lab Assistant/Doctor) : ")   
    priviledgelevel=assignPrivilegeLevels(usertype)  
    
    if(priviledgelevel==4):
        print ("Invalid User Type")
        while (priviledgelevel==4):
            usertype = input("User Type (Patient/Nurse/Lab Assistant/Doctor) : ")   
            priviledgelevel=assignPrivilegeLevels(usertype)  
        
    userdetails["username"],userdetails["password"],userdetails["usertype"],userdetails["priviledgelevel"]=username,password,usertype,priviledgelevel
    
    jsonFile = open("users.json", "r+")
    data = json.load(jsonFile)
    data['users'].append(userdetails)
    
    jrecord = json.dumps(data)
    with open('users.json','w') as f:
        f.write(jrecord)
        f.close
    
    print ("You are now registered!!!")

def login():
    username = input("Username : ")
    password = input("Password : ")
    
    jsonFile = open("users.json", "r+")
    data = json.load(jsonFile)
    for user in data['users']:
        if(user['username']==username and user['password']==password):
            print ("Hi "+username+"! You are logged in...")
            currentUser['username'],currentUser['priviledgelevel']=username,user['priviledgelevel']
    
print ("Type 'Login' if you are already log in, type 'Register' if you are a new user")

loginorregister = input("Enter your input here : ")

if (loginorregister == "Login"):
    login()
elif (loginorregister == "Register"):
    register()
else:
    print ("Invalid Input")


    