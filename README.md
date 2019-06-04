# X-ray

Hola profe, 

Profe el proyecto es un poco sencillo, pero la idea es saber si una persona, por medio de radiografías, tiene o no neumonía. El entrenamiento es igual al del video que nos envio, con el cambio que nos hiciste en la parte de agregar más convulusiones ya que no nos detectaba las epocas que le colocabamos, al final del entrenamiento la perdida que tuvimos fue de 0.12 (lo cual consideramos bastante buena).En la parte del "main.py", llamamos el modelo, los pesos y creamos una función para predecir, en ese mismo código está la creación de la página web con flask. En la carpeta templates estan las vistas, hay una de inicio, otra para subir la radiografía y por ultimo la pestaña que muestra la predicción, dependiendo cual sea el resultado muestra diferente información. 

Para saber que tan bien predecía hicimos la matriz de confusión manualmente, como te los mostramos el viernes, y le agregamos
otros resultados que nos dio el fin de semana. También separamos el data-set en entrenamiento y prueba, con estas ultimas hicimos paquetes
de a 10 imagenes para ver que tan bien predecía, en ese paquete fallaba en 1 o en 2 predicciones. Finalmente le pedimos el favor a un
familiar que nos enviara radiografias de neumonia y las probamos, cabe aclarar que las imagenes estaban tomadas desde un celular a una
pantalla (las puedes ver en la carpeta de pruebas/nuevas), al final de 6 imagenes acertó en 5.
