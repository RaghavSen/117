import os 
import cv2

path = 'Images'

images = []

for file in os.listdir(path):
    name,ext = os.path.splitext(file)
    
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file
        
        images.append(file_name)
        
count = len(images)        
frame = cv2.imread(images[0])
height,width,channels = frame.shape
size = (width,height)

output = cv2.VideoWriter('117.mp4',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(count-1, -1, -1):
    frame = cv2.imread(images[i])
    output.write(frame)

output.release()
print("Done")   
