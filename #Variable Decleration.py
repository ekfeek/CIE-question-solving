#Variable Decleration
Contacts = [
    [],
    []
]
Currentsize = int()
Cont = bool()
Choice = int(input())
Newcontacts = int(input())
Count = int()
Count2 = int()
Flag = bool()
Temp1 = str()
Temp2 = str()

#Number of contacts in array
Currentsize = 0

#Allow program to run infinitely
Cont = True
while Cont==True:
    print('Please choose one of the following: ')
    print('Press 1 to enter new contacts ')
    print('Press 2 to display your contacts ')
    print('Press 3 to delete all contacts ')
    print(Choice)

#Validation of choices as 1,2 and 3
if Choice==1 and Currentsize==100:
    print('Your contacts are full, please select another option')  
    print(Choice)

#Enter new contacts
if Choice == 1:
    print('How many contacts to be printed (Limit is 5)?')
    print(Newcontacts)
    # Validation of new input
    while Newcontacts < 1 or Newcontacts > 5:
        print('There is a limit of 1 contact or 5 contacts')
        print(Newcontacts)
    #Checking maximum size
    while Currentsize + Newcontacts > 100:
        print('Not enough space, maximum is 100')
    for Count in range(Currentsize + 1, Currentsize + Newcontacts + 1):
        print('Enter the contacts last and first name')
        input_value = input(f"Enter value for Contacts[{Count}][1]: ")
        Contacts[Count][1] = input_value
        print('Enter the phone number')
        input_value1 = input(f"Enter value for Contacts[{Count}][2]: ")
        Contacts[Count][2] = input_value1
        Currentsize = Currentsize + Newcontacts
    # Bubble Sorting the array for 2 or more contacts
    if Currentsize >=2:
        while True:
            Flag = False
            for Count in range(Count == 1, Currentsize-1 ):
                if Contacts[Count + 1][1] < Contacts[Count][1]:
                    Flag=True
                    Temp1 = Contacts[Count][1]
                    Temp2 - Contacts[Count][2]
                    Contacts[Count][1] = Contacts[Count + 1][1]
                    Contacts[Count][2] = Contacts[Count + 1][2]
                    Contacts[Count + 1][1] = Temp1
                    Contacts[Count + 1][2] = Temp2

#Display all Contacts
if Choice == 2:
    if Currentsize > 0:
        print('Name and Number')
        for Count in range(1, Currentsize + 1):
            print(Contacts[Count, 1],' ', Contacts[Count, 2])
            print(f'Count is now: {Count}')

#delete all contacts
if Choice == 3:
    for Count in range(1, 100):
        for Count2 in range(1, 2):
            Contacts[Count][Count2] = ""
        print(f'Count2 is now: {Count2}')
    print(f'Count is now {Count}')


                
            












