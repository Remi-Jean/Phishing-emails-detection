import os
from PIL import Image
import math


# Define variables for the paths of the datasets and create the output folder
dataset_path = "./"

#mails_path = os.path.join(dataset_path,"21000 textes")
#output_path = "21000 images"

#mails_path = os.path.join(dataset_path,"21000 textes v2")
#output_path = "21000 images v2"

mails_path = os.path.join(dataset_path,"21000 textes v3")
output_path = "21000 images v3"

os.makedirs(output_path,exist_ok=True)


# Main function to convert the emails in images
max_s = 0
sum = 0
n = 0
# Convert every email in the dataset
for root, subdirs, files in os.walk(mails_path):
    for file in files:
        filepath = os.path.join(root,file)
        fileloc = os.path.relpath(root, mails_path)
        outpath = os.path.join(output_path,fileloc)
        os.makedirs(outpath,exist_ok=True)
        outpath = os.path.join(outpath,file + '.png')
        
        # Open the email and get its content
        f = open(filepath, "rb")
        mail = f.read()

        # Get the size of the image (should be as small as possible to limit padding)
        s = math.ceil(len(mail)**0.5)
        
        # Get the size of the biggest image until now
        sum += s
        n += 1
        if s > max_s:
            max_s = s
        
        # Create the image and save it
        img = Image.new('L',(s,s))
        pixels = [mail[i] for i in range(0,len(mail),1)]
        img.putdata(pixels)
        img.save(outpath)


# Print the size of the biggest image and the average size of the created images
print(f"max:{max_s}")
print(f"avg:{sum/n}")
