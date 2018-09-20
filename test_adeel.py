import hashlib

hash1, salt1, fileName, fileText = "", "", "password_file.txt", ""
lineCount = 0

def hash_with_sha256(str):
 
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()      
    return hex_dig

def letsPlay(n):
    if n == 5:
        print("Job completed!")
        return
    else:
        words = fileText[n].split(',') # split current line to words
        hash1, salt1 = words[2], words[1]
        print(hash1)
        #print("Cracking->", words[0], "# Hash->", hash1, "# Salt->", salt1)

        i, stop, zeros = 941, 943, 3 # increment, where to stop, number of zeros
        while i < stop:
            
            hex_dig = hash_with_sha256('942neguch')
            #print('{:d}'.format(i).zfill(zeros)+salt1,hex_dig)
            
            if (hash1 == '5372c991ea3b3c9b8eb0e094188d985dba415099687c3d60ca230aedcc3b740b'):
            
                print("match");
#                print("###############################################################################\nPassword Cracked!!!\n",
#                      words[0], ",password:", '{:d}'.format(i).zfill(zeros), ",salt:", salt1, "\nhash:", hex_dig,
#                      "\n###############################################################################")
            else:
                print(str(hex_dig))
                print(str(hash1))
                print("mismatch")
            i += 1
            if i == 1000 and zeros == 3:
                #print("Ending 3 digit combinations - Restarting with 4")
                i = 0
                zeros += 1  # increase number of zeros
#            if i == 10000 and zeros == 4:
#                print("Ending 4 digit combinations - Restarting with 5")
#                i = 0
#                zeros += 1  # increase number of zeros
#            if i == 100000 and zeros == 5:
#                print("Ending 5 digit combinations - Restarting with 6")
#                i = 0
#                zeros += 1  # increase number of zeros
#            if i == 1000000 and zeros == 6:
#                print("Ending 6 digit combinations - Restarting with 7")
#                i = 0
#                zeros += 1  # increase number of zeros
#            if i == 1000000 and zeros == 7:
#                break

        return letsPlay(n + 1)

with open(fileName, "r") as f: # getting file content
    fileText = f.readlines()

for line in fileText: # getting line count
    lineCount += 1
# print(fileText[99], lineCount) # get a particular line and line count

letsPlay(4) # start from line 0, minimum password length 3, max length 7
