#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
os.chdir('/content/drive/MyDrive/viact')
get_ipython().system('ls')


# In[3]:


# install dependencies: 
get_ipython().system('pip install pyyaml==5.1')
import torch, torchvision
print(torch.__version__, torch.cuda.is_available())
get_ipython().system('gcc --version')
# opencv is pre-installed on colab


# In[4]:


# install detectron2: (Colab has CUDA 10.1 + torch 1.8)
# See https://detectron2.readthedocs.io/tutorials/install.html for instructions
import torch
assert torch.__version__.startswith("1.8")   # need to manually install torch 1.8 if Colab changes its default version
get_ipython().system('pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.8/index.html')
# exit(0)  # After installation, you need to "restart runtime" in Colab. This line can also restart runtime


# In[5]:


import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
# import some common libraries
import numpy as np
import cv2
import random
import os
import torch

from detectron2.data import detection_utils as utils
import detectron2.data.transforms as T
import copy

from detectron2.engine import DefaultTrainer
from detectron2.data import build_detection_test_loader, build_detection_train_loader

# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
from detectron2.data.catalog import DatasetCatalog
from detectron2.data import DatasetMapper
from detectron2.data.datasets import register_coco_instances


# In[6]:


register_coco_instances("qi_train", {}, "/content/drive/MyDrive/viact/train.json", "/content/drive/MyDrive/viact/image")


# In[7]:


from detectron2.data.catalog import DatasetCatalog
qi_train_metadata = MetadataCatalog.get("qi_train")
dataset_dicts = DatasetCatalog.get("qi_train")

print(qi_train_metadata)


# In[32]:


get_ipython().system('ls')


# In[33]:


cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"))
cfg.DATASETS.TRAIN = ("qi_train",)
cfg.DATASETS.TEST = ("qi_test",)

cfg.MODEL.WEIGHTS = '/content/drive/MyDrive/viact/model_final.pth'
cfg.DATALOADER.NUM_WORKERS = 2
cfg.SOLVER.IMS_PER_BATCH = 2
cfg.SOLVER.BASE_LR = 0.001
cfg.SOLVER.MOMENTUM = 0.9
cfg.SOLVER.WEIGHT_DECAY = 0.001

cfg.MODEL.BACKBONE.FREEZE_AT = 2

cfg.SOLVER.WARMUP_FACTOR = 1.0/1000
cfg.SOLVER.WARMUP_ITERS = 1000
cfg.SOLVER.MAX_ITER = 10000 #adjust up if val mAP is still rising, adjust down if overfit
cfg.SOLVER.STEPS = (1000, 1500)
cfg.SOLVER.GAMMA = 0.05
cfg.SOLVER.CHECKPOINT_PERIOD = 5000

cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 128
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 4
cfg.MODEL.RPN.POST_NMS_TOPK_TEST = 10000 #added 1
cfg.MODEL.RPN.POST_NMS_TOPK_TEST = 10000 #added 2


# In[9]:


from detectron2.engine import DefaultTrainer
from detectron2.evaluation import COCOEvaluator


# In[34]:


os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)
trainer = DefaultTrainer(cfg)
trainer.resume_or_load(resume=False)+
trainer.train()


# In[57]:


cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "model_final.pth")  # path to the model we just trained
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.6   # set a custom testing threshold
predictor = DefaultPredictor(cfg)


# In[58]:


im = cv2.imread('/content/44.jpg')
outputs = predictor(im)
from google.colab.patches import cv2_imshow
v = Visualizer(im[:, :, ::-1],
                   metadata=qi_train_metadata, 
                   scale=0.5   # remove the colors of unsegmented pixels. This option is only available for segmentation models
    )
out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
cv2_imshow(out.get_image()[:, :, ::-1])


# In[ ]:




