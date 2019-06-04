import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from sklearn.metrics import confusion_matrix

from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform


longitud, altura = 150, 150
modelo = './modelo/modelo.h5'
pesos_modelo = './modelo/pesos.h5'
with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
        cnn = load_model('./modelo/modelo.h5')
cnn.load_weights(pesos_modelo)

def predict(file):
  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = cnn.predict(x)
  result = array[0]
  answer = np.argmax(result)
  if answer == 0:
        print("Normal")
  elif answer == 1:
        print("Neumonia")

  return answer


#Neumonia - Virus
predict('./probar/Neumonia/Virus/person3_virus_17.jpeg')
#Neumonia - Virus
predict('./probar/Neumonia/Virus/person8_virus_27.jpeg')
#Neumonia - Virus
predict('./probar/Neumonia/Virus/person16_virus_47.jpeg')
#Neumonia - Virus
predict('./probar/Neumonia/Virus/person1670_virus_2886.jpeg')
#Neumonia - Virus
predict('./probar/Neumonia/Virus/person1671_virus_2887.jpeg')
#Neumonia - Virus
predict('./probar/Neumonia/Virus/person1672_virus_2888.jpeg')
#Neumonia - Virus
predict('./probar/Neumonia/Virus/person1673_virus_2889.jpeg')
#Neumonia - Virus
predict('./probar/Neumonia/Virus/person1674_virus_2890.jpeg')
#Neumonia - Virus
predict('./probar/Neumonia/Virus/person1675_virus_2891.jpeg')
#Neumonia - Virus
predict('./probar/Neumonia/Virus/person1676_virus_2892.jpeg')

print("------------------------")

#Neumonia - Bacterial
predict('./probar/Neumonia/Bacterial/person78_bacteria_378.jpeg')
#Neumonia - Bacterial
predict('./probar/Neumonia/Bacterial/person78_bacteria_380.jpeg')
#Neumonia - Bacterial
predict('./probar/Neumonia/Bacterial/person134_bacteria_640.jpeg')
#Neumonia - Bacterial
predict('./probar/Neumonia/Bacterial/person134_bacteria_641.jpeg')
#Neumonia - Bacterial
predict('./probar/Neumonia/Bacterial/person134_bacteria_642.jpeg')
#Neumonia - Bacterial
predict('./probar/Neumonia/Bacterial/person134_bacteria_643.jpeg')
#Neumonia - Bacterial
predict('./probar/Neumonia/Bacterial/person134_bacteria_644.jpeg')
#Neumonia - Bacterial
predict('./probar/Neumonia/Bacterial/person135_bacteria_646.jpeg')
#Neumonia - Bacterial
predict('./probar/Neumonia/Bacterial/person135_bacteria_647.jpeg')
#Neumonia - Bacterial
predict('./probar/Neumonia/Bacterial/person173_bacteria_831.jpeg')

print("------------------------")

#Normal
predict('./probar/NORMAL/IM-0005-0001.jpeg')
#Normal
predict('./probar/NORMAL/IM-0006-0001.jpeg')
#Normal
predict('./probar/NORMAL/IM-0111-0001.jpeg')
#Normal
predict('./probar/NORMAL/NORMAL2-IM-0041-0001.jpeg')
#Normal
predict('./probar/NORMAL/NORMAL2-IM-0111-0001.jpeg')
#Normal
predict('./probar/NORMAL/NORMAL2-IM-0374-0001.jpeg')
#Normal
predict('./probar/NORMAL/NORMAL2-IM-0374-0001-0001.jpeg')
#Normal
predict('./probar/NORMAL/NORMAL2-IM-0374-0001-0002.jpeg')
#Normal
predict('./probar/NORMAL/NORMAL2-IM-0376-0001.jpeg')
#Normal
predict('./probar/NORMAL/NORMAL2-IM-0378-0001.jpeg')

print("------------------------")

#Normal
predict('./probar/NORMAL/IM-0006-0001.jpeg')
#Normal
predict('./probar/NORMAL/IM-0111-0001.jpeg')
#Normal
predict('./probar/NORMAL/NORMAL2-IM-0041-0001.jpeg')
#Normal
predict('./probar/NORMAL/NORMAL2-IM-0111-0001.jpeg')
#Neumonia - Bacterial
predict('./probar/Neumonia/Bacterial/person135_bacteria_646.jpeg')
#Neumonia - Bacterial
predict('./probar/Neumonia/Bacterial/person135_bacteria_647.jpeg')
#Neumonia - Bacterial
predict('./probar/Neumonia/Bacterial/person173_bacteria_831.jpeg')
#Normal
predict('./probar/NORMAL/NORMAL2-IM-0374-0001.jpeg')
#Normal
predict('./probar/NORMAL/NORMAL2-IM-0374-0001-0001.jpeg')
#Neumonia - Virus
predict('./probar/Neumonia/Virus/person1674_virus_2890.jpeg')
#Neumonia - Virus
predict('./probar/Neumonia/Virus/person1675_virus_2891.jpeg')


