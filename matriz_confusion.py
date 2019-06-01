from sklearn.metrics import confusion_matrix

y_true = ["Neumonia","Neumonia","Neumonia","Neumonia","Neumonia","Neumonia","Neumonia","Neumonia","Neumonia","Neumonia"]
y_pred = ["Neumonia","Neumonia","Normal","Neumonia","Neumonia","Neumonia","Neumonia","Neumonia","Neumonia","Neumonia"]

y_verdad= ["Normal",
"Normal",
"Normal",
"Normal",
"Neumonia",
"Neumonia",
"Neumonia",
"Normal",
"Normal",
"Neumonia",
"Neumonia"]

y_prueba = ["Normal",
"Normal",
"Normal",
"Normal",
"Neumonia",
"Neumonia",
"Neumonia",
"Normal",
"Normal",
"Neumonia",
"Neumonia"]

print(confusion_matrix(y_verdad, y_prueba))