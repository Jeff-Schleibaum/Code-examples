import sys
from encryption_utilities import loadPasswordFile, savePasswordFile, passwordEncrypt

#The password list - We start with it populated for testing purposes
passwords = [["yahoo","XqffoZeo"],["google","CoIushujSetu"]]

#The password file name to store the passwords to
passwordFileName = "samplePasswordFile"

#The encryption key for the caesar cypher
encryptionKey = 16

while True:
    print("What would you like to do:")
    print(" 1. Open password file")
    print(" 2. Lookup a password")
    print(" 3. Add a password")
    print(" 4. Save password file")
    print(" 5. Print the encrypted password list (for testing)")
    print(" 6. Quit program")
    print("Please enter a number (1-4)")
    choice = input()

    if(choice == '1'): #Load the password list from a file
        passwords = loadPasswordFile(passwordFileName)

    if(choice == '2'): #Lookup at password
        print("Which website do you want to lookup the password for?")
        for keyvalue in passwords:
            print(keyvalue[0])
        passwordToLookup = input()

        ####### YOUR CODE HERE ######
        #You will need to find the password that matches the website
        found = False

        for i in range(len(passwords)): # for loop
            if passwords[i][0] == passwordToLookup: # checking list with 2 seperate stored items
                found = True
                encryptedPassword = passwords[i][1] # creating encrption
                decryptedPasword = passwordEncrypt(encryptedPassword, -encryptionKey) # decrpting password
                print(f"The password for {passwordToLookup} is {decryptedPasword} ")  # displaying the website and the decrypted password to the list
                break

        if not found:
            print (f"The password for {passwordToLookup} can not be found.") # default messege


    if(choice == '3'):
        print("What website is this password for?") # prompt for website
        website = input() # save input
        print("What is the password?") # prompt for password
        unencryptedPassword = input() # save input

        ####### YOUR CODE HERE ######
        #You will need to encrypt the password and store it in the list of passwords

        #The encryption function is already written for you
        #Step 1: You can say encryptedPassword = passwordEncrypt(unencryptedPassword,encryptionKey)]
        #the encryptionKey variable is defined already as 16, don't change this
        #Step 2: create a list of size 2, first item the website name and the second item the password.
        #Step 3: append the list from Step 2 to the password list

        # step 1
        encryptedPassword = passwordEncrypt(unencryptedPassword, encryptionKey)
        # step 2
        newEntry = [website, encryptedPassword]
        #step 3
        passwords.append(newEntry)

        print(f"The password for {website} added successfully.")
        ####### YOUR CODE HERE ######

    if(choice == '4'): #Save the passwords to a file
            savePasswordFile(passwords,passwordFileName)


    if(choice == '5'): #print out the password list
        for keyvalue in passwords:
            print(', '.join(keyvalue))

    if(choice == '6'):  #quit our program
        sys.exit()

    print()
    print()