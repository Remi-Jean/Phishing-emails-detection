import numpy as np
import os
import matplotlib.pyplot as plt


# Define a subfunction to print and save the graph of the repartition of the size of the emails with statistical data
def hist(size,max,t,sum,n,type,i):
    moyenne = np.mean(size)
    mediane = np.median(size)
    quartiles = np.percentile(size, [25, 75])
    ecart = np.std(size)
    plt.hist(size,bins=100,color='blue',edgecolor='red')
    plt.xlabel('Values')
    plt.ylabel('Density')
    plt.title(type)

    # Show the main statistical information about the dataset on the graph
    plt.axvline(moyenne, color='red', linestyle='dashed', linewidth=1, label=f'Moyenne: {moyenne:.2f}')
    plt.axvline(mediane, color='green', linestyle='dashed', linewidth=1, label=f'Médiane: {mediane:.2f}')
    plt.axvline(ecart, color='blue', linestyle='dashed', linewidth=1, label=f'Ecart-type: {ecart:.2f}')
    plt.axvline(quartiles[0], color='orange', linestyle='dashed', linewidth=1, label=f'1er quartile: {quartiles[0]:.2f}')
    plt.axvline(quartiles[1], color='purple', linestyle='dashed', linewidth=1, label=f'3e quartile: {quartiles[1]:.2f}')
    
    # Add the legend
    plt.legend()
    
    # Show and save the graph
    nom = 'histogramme_' + type + '_' + str(i) + '.png'
    chemin_fichier = os.path.join(graph_path, nom)
    plt.savefig(chemin_fichier)
    plt.show()
    
    # Print the size of the biggest image and the average size of the created images
    print("max: ",max, t)
    print("moy: ", sum/n)


# Define variables for the paths of the datasets
#dataset_path = './21000 images'
dataset_path = './21000 images v2'
#dataset_path = './21000 images v3'
#dataset_path = './24000 images'
#dataset_path = './24000 images v2'


# For each dataset, create the graphs for real emails and phishing emails separatly
test_path = os.path.join(dataset_path,"test")
test_ham_path = os.path.join(test_path,"ham")
test_spam_path = os.path.join(test_path,"spam")

train_path = os.path.join(dataset_path,"train")
train_ham_path = os.path.join(train_path,"ham")
train_spam_path = os.path.join(train_path,"spam")   

# Create the output folder
graph_path = os.path.join(dataset_path,"histogrammes")
os.makedirs(graph_path,exist_ok=True)


# Choose which graph to make
#paths = [train_ham_path,test_ham_path]
#type = 'ham'

paths = [train_spam_path,test_spam_path]
type = 'spam'


size = []
Sum = 0
n = 0
Max = 0
t = ''

# Look at the size of every email
for directory in paths:
    for root, subdirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root,file)
            fileloc = os.path.relpath(root, directory)
            f = open(filepath, "rb")
            mail = f.read()
            s = len(mail)
            n+=1
            Sum += s
            if s>Max:
                Max = s
                t = filepath
            size.append(s)


# Create the graph for the real emails or the phishing emails
# Also create the graphs for the same emails but without the largest ones
hist(size,Max,t,Sum,n,type,0)
for i in range(10):
    print("Removed ",i+1,"th max value")
    size.remove(Max)
    n = len(size)
    Sum = sum(size)
    Max = max(size)
    hist(size,Max,t,Sum,n,type,i+1)