from sklearn.metrics import confusion_matrix

y_true = ["Neumonia","Neumonia","Neumonia","Neumonia","Neumonia","Neumonia","Neumonia","Neumonia","Neumonia","Neumonia","Normal","Normal","Normal","Normal","Neumonia","Neumonia","Neumonia","Normal","Normal","Neumonia","Neumonia"]
y_pred = ["Neumonia","Neumonia","Normal","Neumonia","Neumonia","Neumonia","Neumonia","Neumonia","Neumonia","Neumonia","Normal","Normal","Normal","Normal","Neumonia","Neumonia","Neumonia","Normal","Normal","Neumonia","Neumonia"]


#Otra muestra
y_true1= ["Normal","Normal","Normal","Normal","Neumonia","Neumonia","Neumonia","Normal","Normal","Neumonia","Neumonia"]
y_pred1 = ["Normal","Normal","Normal","Normal","Neumonia","Neumonia","Neumonia","Normal","Normal","Neumonia","Neumonia"]

print(confusion_matrix(y_true, y_pred))
