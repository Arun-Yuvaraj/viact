#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import xml.etree.cElementTree as ET
tree = ET.ElementTree(file='C:\\Users\\Arun Yuvaraj\\Desktop\\new\\wheat\\new\\Regan - Full Time AI Engineer - Technical test\\interview\\task2\\dataset\\annotations.xml')


# In[ ]:


tree.getroot()
root = tree.getroot()


# In[ ]:


def create_xml(bbox, folder, filename, width, height, j):
    t = []
    for i in range(len(bbox)):
        t.append(bbox[i])

    annotation = ET.Element('annotation')
    ET.SubElement(annotation, 'folder').text = folder
    ET.SubElement(annotation, 'filename').text = filename
    ET.SubElement(annotation, 'segmented').text = '0'
    size = ET.SubElement(annotation, 'size')
    ET.SubElement(size, 'width').text = str(width)
    ET.SubElement(size, 'height').text = str(height)
    ET.SubElement(size, 'depth').text = '3'
    print(len(bbox))
    for k in range(len(bbox)):

        xmin = t[k][0]
        ymin = t[k][1]
        xmax = t[k][2]
        ymax = t[k][3]
        cl = t[k][4]

        ob = ET.SubElement(annotation, 'object')
        ET.SubElement(ob, 'name').text = str(cl)
        ET.SubElement(ob, 'pose').text = 'Unspecified'
        ET.SubElement(ob, 'truncated').text = '0'
        ET.SubElement(ob, 'difficult').text = '0'
        bbox = ET.SubElement(ob, 'bndbox')
        ET.SubElement(bbox, 'xmin').text = str(xmin)
        ET.SubElement(bbox, 'ymin').text = str(ymin)
        ET.SubElement(bbox, 'xmax').text = str(xmax)
        ET.SubElement(bbox, 'ymax').text = str(ymax)
        print('done')
    tree = ET.ElementTree(annotation)
    save =  'C:\\Users\\Arun Yuvaraj\\Desktop\\viact\\' + str(j) + '.xml'
    tree.write(save, encoding='utf8')


# In[ ]:


for x in root.iter('image'):
    bbox = []
    root1=ET.Element('root')
    root1=x
#     print(x.attrib)
    filename = x.attrib['id'] + '.jpg'
    width = x.attrib['width']
    height = x.attrib['height']
    folder = '/home/'
    
    for supply in root1.iter('box'):
        box = []
        root2=ET.Element('root')
        if supply.attrib['label'] != 'head':
            continue
        x1 = int(float(supply.attrib['xtl']))
        y1 = int(float(supply.attrib['ytl']))
        x2 = int(float(supply.attrib['xbr']))
        y2 = int(float(supply.attrib['ybr']))
        box.append(x1)
        box.append(int(y1))
        box.append(int(x2))
        box.append(int(y2))
#         print(supply.attrib)
        root2=(supply)
        temp = []
        h = 0
        m = 0
        for tech in root2.iter('attribute'):
#             h = 0
#             m = 0
#             print(tech.attrib['name'])
#             print(tech.text)
            root3 = ET.Element('root')
            if (tech.attrib['name']) == 'has_safety_helmet' and tech.text == 'yes':
                h = 1
            elif (tech.attrib['name']) == 'mask' and tech.text == 'yes':
                m = 1
#             temp.append(tech.text)
        if h == 1 and m == 0:
            obj = 'Safety Helmet present'
        elif h == 1 and m == 1:
            obj = 'Helmet and Mask present'
        elif h == 0 and m == 1:
            obj = 'Mask available'
        elif h == 0 and m == 0:
            obj = 'No Helmet and Mask present'
        box.append(obj)
        bbox.append(box)

    create_xml(bbox,folder, filename, width, height, filename[:-4])

