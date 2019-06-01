import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from sklearn.metrics import confusion_matrix

from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform

#----- Predicción -----
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
        y = "Normal"
        print("Normal")
  elif answer == 1:
        y = "Neumonia"
        print("Neumonia")

  return y



print("---- xd? ---")
predict('./probar/Neumonia/Virus/person1676_virus_2892.jpeg')



#----- Pagina web -----

from flask import Flask, render_template, request, make_response, session,escape,redirect,url_for,flash, jsonify,send_from_directory
import os

UPLOAD_FOLDER = os.path.abspath("./uploads/")

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/",methods=["GET","POST"])
def home():
    return render_template("inicio.html")

@app.route("/subirImagen",methods=["GET","POST"])
def subir_imagen():
    if request.method == "POST":
        f = request.files["ourfile"]
        filename = f.filename
        f.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
        x = './uploads/'+filename
        print(x)
        res = predict(x)
        print("La predicción es: " + res)
        return render_template("prediccion.html", res = res)

    return render_template("subir_imagen.html")















@app.route("/IrSubirImagen",methods=["GET","POST"])
def IrSubirImagen():
      if request.method == "POST":
            return redirect("/subirImagen")

@app.route("/IrInicio",methods=["GET","POST"])
def IrInicio():
      if request.method == "POST":
            return redirect("/")

@app.route("/IrPrediccion",methods=["GET","POST"])
def IrPrediccion():
      if request.method == "POST":
            return redirect("/")
















if __name__=="__main__":
    app.run(debug=True)
