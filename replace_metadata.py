import os
import re
import random as rd
import string


# Define list of random possible replacement for occurences of "enron" in the emails
replacement = []
while len(replacement)<100:
    a = ''
    for i in range(rd.randint(4,6)):
        a= a + rd.choice(string.ascii_letters).upper()
    replacement.append(a)


# Define variables for the paths of the datasets and create the output folder
dataset_path = "./"
mails_path = os.path.join(dataset_path,"21000 textes v2")

output_path = "21000 textes v3"
os.makedirs(output_path,exist_ok=True)


# Define the subfunction that will replace the old years by newer ones
def replace_year(line):
    # Regular expression to match the date pattern
    date_pattern = r'Date: (\w{3}, \d{2} \w{3} (?:19\d{2}|20(?:0[0-2]|09)) \d{2}:\d{2}:\d{2} [+-]\d{4} \(\w{3}\))'

    # Define a function to replace the year with a random year betwee 2015 and 2022 if the year is before 2009
    def replace_year_func(match):
        date_string = match.group(0)
        year = int(re.search(r'\d{4}', date_string).group(0))  # Extract the year
        if year < 2003:
            new_year = rd.randint(2015,2022)
            return date_string.replace(str(year), str(new_year))
        else:
            return date_string

    # Use re.sub to replace the year in the line
    return re.sub(date_pattern, replace_year_func, line)


# Main function to replace the metadata that could create a bias
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
        content = f.readlines()
        
        # Replace the year
        modified_content = [replace_year(line) for line in content]
        
        # Replace the metadatas that contain "enron" and that are common
        for j in range(len(modified_content)):
            while "</O=ENRON" in modified_content[j]:
                i = rd.randint(0,len(replacement)-1)
                modified_content[j] = modified_content[j].replace("</O=ENRON", "</O=" + replacement[i] ,1)
        
        # Save the modified email
        with open(outpath, 'w') as f:
            f.writelines(modified_content)
        n+=1
        
        # To follow the progress and debug
        print(n)
#        print(file)
