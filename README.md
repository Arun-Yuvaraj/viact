**Task 1**

  Please find code for task1 in code folder with the name - task1.py.
  In input folder, in addition to the given files, I have downloaded one more file from Open Image 6 with the name of **class-descriptions-boxable.csv**.
  In output folder, there are 2 csv's, First csv is **Class Details.csv**, where parent, ancestor and sibling classes of all the classes metioned in **class-descriptions-boxable.csv** is created, Second csv is **ancestor_match.csv**, in which 2 classes with same ancestor are mentioned with ancestor name.

**Task 2**

 The code for this task is present in code folder with the name - task2.ipynb and create xml.py. Example xml is placed in xml folder and the model is present in model folder.
 Process - 
 
  I used create xml.py to create xmls for all the images that have heads. Example xml is present in the xml folder.
  I converted all the xml's to json for training a detectron model.
  The code for training detectron model and sample output is given in task2.ipynb
  
 Future works (Due to time constraints, I was not able to incorporate below points) -
 
  By using more images, we can have better model for this task.
  We can use face detectors like Haarcascade to detect faces and then run this model on the cropped faces.
