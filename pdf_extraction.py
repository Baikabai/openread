
import fitz
import os
 
filename = 'Robotics Computer Surgery - 2006 - Rayman - Long‐distance robotic telesurgery  a feasibility study for care in remote.pdf'
dir_name = filename.split('.')[0]
img_dir = os.path.join(os.getcwd(),dir_name) 
if os.path.isdir(img_dir) == False:
    os.mkdir(img_dir)
 

doc = fitz.open(filename)
 
images = []
 
for page in range(len(doc)):
    images.append(doc[page].get_images())
 
for pageNo, image in enumerate(images):
    if image != []:
        for i in range(len(image)):
            xref = image[i][0]
            smask = image[i][1]
            if image[i][8] == 'FlateDecode':
                ext = 'png'
            elif image[i][8] == 'DCTDecode':
                ext = 'jpeg'
 
            pix = fitz.Pixmap(doc.extract_image(xref)["image"])
            if smask > 0:
                mask = fitz.Pixmap(doc.extract_image(smask)["image"])
                pix = fitz.Pixmap(pix, 0) 
                pix = fitz.Pixmap(pix, mask)
 
            img_name = os.path.join(img_dir, f'image{pageNo+1}_{i}.{ext}')
            pix.save(img_name)