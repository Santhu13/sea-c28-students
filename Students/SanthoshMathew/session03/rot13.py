
def rot13(rotme):
    #if len(rotme) <=1:
    #    return rotme 
    
    rotted = ""

    for letter in rotme:
        
        Ucode = ord(letter) # for each char return # representing the Unicode of that letter
        #print Ucode 

        if Ucode >= ord('a') and Ucode <= ord('z'):  # hence a small letter a-z 
            if Ucode > ord('m'): # greater than half way so subtract 13 
                Ucode -= 13
            else:
                Ucode += 13
        elif Ucode >= ord('A') and Ucode <= ord('Z'):
            if Ucode > ord('M'):
                Ucode -= 13
            else:
                Ucode += 13
    
        rotted += chr(Ucode)  # Adding to the output ... .

    return rotted

#import string 
#s1=string.digits
#sp=string.punctuation 
#nonalf=s1+sp+' ' # complete set of non-alphabetic characters 
#print nonalf

if __name__ == "__main__":
# Testing ... validating 
    rotme=str("Do YOU think this will work?? eh !!")  
    x=rot13(rotme)
    y=rot13(rot13(rotme))
    if rotme==y:  
        print "that was a rot-ing success!" 

#print(rot13(rotme))
#print(rot13(rot13(rotme)))


