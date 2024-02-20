import os
import random as rd
import string


# Define list of random possible replacement for the domains "@enron.com" in the emails
domains = ["yahoo.com","gmail.com"]
while len(domains)<100:
    a = '@'
    for i in range(rd.randint(4,7)):
        a= a + rd.choice(string.ascii_letters)
    a = a + '.'
    for i in range(3):
        a = a + rd.choice(string.ascii_letters)
    domains.append(a)


# Define variables for the paths of the datasets and create the output folder
dataset_path = "./"
mails_path = os.path.join(dataset_path,"21000 textes")

output_path = "21000 textes v2"
os.makedirs(output_path,exist_ok=True)


# Main function to replace the domain names that could create a bias
n = 0
# Look at every email in the dataset
for root, subdirs, files in os.walk(mails_path):
    for file in files:
        filepath = os.path.join(root,file)
        fileloc = os.path.relpath(root, mails_path)
        outpath = os.path.join(output_path,fileloc)
        os.makedirs(outpath,exist_ok=True)
        outpath = os.path.join(outpath,file)
        
        # Open the email and get its content
        f = open(filepath, "r")
        content = f.read()
        
        # Replace EVERY occurence of the domain name by a random new domain name
        while "@enron.com" in content:
            i = rd.randint(0,len(domains)-1)
            content = content.replace("@enron.com", domains[i],1)
            
        # Save the modified email
        with open(outpath, 'w') as f:
            f.write(content)
        n+=1
        
        # To follow the progress and debug
        print(n)
#        print(file)