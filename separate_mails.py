import os
import re



# The folder that contains the files extracted from the .zip file
directory="./bruts/"


# Create the output folder
path="./Separes/"
os.makedirs(path,exist_ok=True)

    
# List the files that contain the emails to separate 
f = []
for file in os.listdir(directory):
    if not (file.endswith(".txt")) and not (file.endswith(".py")):
        f.append(file)


# Separate the emails from each file
for j in range(len(f)):
    fi = f[j]    
    
    # Get the name of the file
    if fi.endswith(".mbox"):
        path = os.path.join(path,fi[0:-5])
        os.mkdir(path)
    else:
        path = os.path.join(path,fi)
        path = path + "rep"
        os.mkdir(path)
    path = path + "/0"
    
    # Open the file
    with open(os.path.join(directory,fi), 'r') as file:
        
        # mail contains one mail that will be saved in a file
        mail = file.readline()
        
        # buff is the buffer that will store each line one by one in order to verify that it is not the beginning of a new mail
        buff = file.readline()
        i = 0
        while len(buff) > 0:
            
            # Continue to read a new line until we arrive on a new email
            while re.search('^From .*@',buff) == None and len(buff) >0:
                mail = mail + buff
                #print(buff)
                buff = file.readline()

            # If we wrote 1000 emails in the previous folder, we create a new folder to store the following emails
            if i%1000 == 0:
                subpath = path[:-1] + str(i//1000)
                os.mkdir(subpath)
            pathf = subpath + "/" + str(j+0) + "-" + str(i)
            
            # Write the email in its own file
            nf = open(pathf,"w")
            nf.write(mail)
            nf.close()
            i+=1
            mail = file.readline()
            buff = file.readline()
            
