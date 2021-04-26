**Task 1**

  Please find code for task1 in code folder with the name - task1.py.
  In input folder, in addition to the given files, I have downloaded one more file from Open Image 6 with the name of **class-descriptions-boxable.csv**.
  In output folder, there are 2 csv's, First csv is **Class Details.csv**, where parent, ancestor and sibling classes of all the classes metioned in **class-descriptions-boxable.csv** is created, Second csv is **ancestor_match.csv**, in which 2 classes with same ancestor are mentioned with ancestor name.

**Task 2**

 The code for this task is present in code folder with the name - task2.ipynb and create xml.py. Example xml is placed in xml folder.
 You can get the model file from here - https://drive.google.com/file/d/1pPAsOaYTSElMAKI97yv0paZ-CdUPOxpM/view?usp=sharing
 Process - 
 
  I used create xml.py to create xmls for all the images that have heads. Example xml is present in the xml folder.
  I have used 4 classes for this task - **Helmet and Mask present, Safety Helmet Present, Mask available, No Helmet and Mask present**
  I converted all the xml's to json for training a detectron model.
  The code for training detectron model and sample output is given in task2.ipynb
  
  **mAP at 50% is 81%**
  You can check AP for different threshold in task2.ipynb
 Future works (Due to time constraints, I was not able to incorporate below points) -
 
  By using more images, we can have better model for this task.
  By using different types of augmentations.
  
 **Important Question - Evaluation Metric**
 
 As the problem at hand is a object detection task, I will use **mAP**(mean average precision) metric for evaluation. The reason being, average precision gives you precision at different threshold. And by defination, it gives how many of the predictions are correct and that is what we need to check.
