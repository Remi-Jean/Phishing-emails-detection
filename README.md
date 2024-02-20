# Phishing-emails-detection

This repository contains the different script used to prepare the datasets used in order to train and evaluate the capacity of the model to detect phishing emails.
It also contains the kaggle notebook used to create the model and to carry out the experimentation.


## Preparation of the datasets
#### Base datasets
This project mainly used two datasets: the [Enron Email Dataset](http://www.cs.cmu.edu/~enron/) that contains more than 500,000 legitimate emails and [Jose Nazario's dataset](http://www.monkey.org/~jose/phishing) that contains 10,678 phishing emails.
<br/>
Another dataset has been used at the beginning, the dataset from the [Spam Assassin Project](http://spamassassin.apache.org/old/publiccorpus/) that contains 4,000 legitimate emails and nearly 2,000 spam emails

#### Transformations of the datasets
##### Enron dataset
As the Enron dataset is huge and as we want to have as many legitimate emails as phishing emails, we need to randomly select select some emails from the dataset. This is the task of the *select_mail.py* script.
During the experience, we decided to look for possible bias to get rid of them, and we found that all of the emails of the enron dataset included email addresses ending in '@enron.com' so we decided to change those domain names by random ones using the *replace_domain.py* script. After looking a bit deeper, we found that all those emails were sent before 2003 and that some common metadata were including the name of the company ENRON, so we decided to test our model with those possible bias removed using the *replace_metadata.py* script.
##### Nazario dataset
When we download Jose Nazario's dataset, we get ten or so files, each containing many phishing emails one after another. However to be able to use those emails, we need to separate them and save each one in its own file, this is the task of the *separate_mails.py* script.

#### Creation of the new datasets
The datasets that will be used by the model are all made using the following structure:
[](dataset_structure.png)
We'll be using a ratio of 80% of the total emails for the training dataset and 20% for the testing dataset and we'll make sure that in each of those two datasets, there will be as many ham emails as phishing ones.
Later on, the training dataset will be split in two subsets, one for the training (80% of the training dataset, 64% of the total number of emails) and one for the validation (20% of the training dataset, 16% of the total number of emails).

#### Composition of the new datasets
To test our models, we'll be using two datasets:
<br/>
**Dataset 1:** made of 10,678 phishing emails from Nazario's dataset and 10,678 ham emails from the Enron dataset for a total of 21,356 emails. The emails are used as they were in the original datasets.
The training and validation dataset is made of 17,086 emails and the testing dataset of 4,270 emails.
<br/>
**Dataset 2:** same dataset as before, but the metadata from the emails of the enron dataset have been replaced using the replace_domains.py and replace_metadata.py scripts

#### Transformation of the emails in images
Our model will not be working on the emails as texts but as images, so we need to convert the emails in image. This can be done using the *to_image.py* script.
Afterward, we can use the *repart_size.py* script to get graphs of the repartition of size of the images and see the differences that would appear by deleting the 10 biggest images.


## CNN model
#### First model: VGG16 with transfer learning
In the *VGG_Frozen.ipynb* python notebook can be found the python code to use a first model that uses the VGG16 CNN model pre-trained on the imagenet dataset. To this model was added a layer at the end to get 2 outputs as we only have two classes, this layer is the only one that we have trained.

#### Second model: VGG16 entirely trained
In the *VGG_Unfrozen.ipynb* python notebook, the same VGG16 model is used, however this time it is entirely trained to see the differences in performances between the model pre-trained and the model trained on our dataset.

#### Third model: VGG16 + LightGBM
In the *VGG_LGBM.ipynb* python notebook, a new model is used. This model also use the VGG16 CNN pre-trained on the imagenet dataset, but this time it is used to extract features from the datasets. Afterward, a LightGBM classifier, which is based on a random forest, is used to classify the emails using the extracted features.
