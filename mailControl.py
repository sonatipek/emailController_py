from queue import Empty

loopContinue = True

# We continue to receive input unless the correct value is entered using an infinite loop.
while loopContinue:
    control = False
    mail = input("Please enter the email you want to have checked:\t")

    #If the value entered by navigating the string contains the '@' sign, we set the control variable to True and exit the loop.
    for search in mail:
        if (search == "@"):
            control = True
            break
    if (control == False):
        print("Your entry not e-mail. Please enter e-mail!(There must be an @ in the email.)")

    #If value passed '@' check, we check '.' and subdomain
    else:
        # .com control 
        temp = mail.split(".")
        if temp[-1] == "com":
        
            #After .com control we check subdomain 
            temp = mail.split("@")
            temp = temp[-1].split(".com")
            
            if temp[0] != Empty:
                print("Your entry is a e-mail.")
                loopContinue = False
                break
            
        
        else:      
            print("Your entry not e-mail. Please enter e-mail!(Email must have '.com' at the end or a subdomain.)")
