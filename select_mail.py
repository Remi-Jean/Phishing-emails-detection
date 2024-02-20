import os
import random as rd
import shutil

# Define variables for the paths of the datasets and create the output folder
directory="./enron_mail_20150507"

output ="./enron10K"
os.makedirs(output,exist_ok=True)


# Main function to randomly select a certain number of email from the enron dataset
i = 0
j = 0

# Numbers of emails
nb_to_select = 10678
nb_total = 517401

# Randomly choose which email to select
tocopy = rd.sample(range(1, nb_total), nb_to_select)
while i != nb_to_select:
    for root, subdirs, files in os.walk(directory):
        for file in files:
            j = j+1
            
            # Copy the email if its number is one of the selected one
            if j in tocopy:
                path = os.path.join(root,file)
                path = os.path.relpath(path, "./")
                i = i+1
                out = os.path.join(output,path.split("/")[-3] + "-" + path.split("/")[-2] + "-" + path.split("/")[-1] + str(i+1))
                shutil.copyfile(path,out)
                
                # To follow the progress
                print("nb copied:", i)
                print("nb mails:", j)

    