# Proyecto de Ciencia de Datos

### Objetivo
En este caso el cliente al finalizar la semana registraba sus ventas semanales en kg de helado para tener un segumiento y ver como le estaba yendo al negocio, su problema surgue que con el tiempo se volvio dificultoso ver y poder analizar sus metricas, por lo que en este trabajo genere dos formas de visualizar sus ventas:
  - Historico: donde puede ver como han sido las ventas mensuales, junto con dos graicos, uno para ver las ventas individuales, y otro de barras para ver las ventas totales por mes.
  - Semanal: Como mecione anteriormente el cliente al finalizar la semana necesita ver sus ventas para poder  realizar su compra de materia prima semanal, por lo tanto genere un dataframe el cual recibe fechas como input.
 
### Desde cero hasta aplicacion web.
En este proyecto realice un analisis de datos sencillo, partiendo de un dataset de las ventas semanales de una heladeria. Como dije anteriormente el dataset 'ventas.xlsx' es un archivo excel de las ventas semanales el cual se actualiza cada domingo al terminar la semana, las medidas se encuentan en kilogramos, inicalmente sus columnas eran las fechas y su fila los sabores.

El primer problema que surgio fue la disposicion del archivo .xlsx, se encontraba en un formato dificl de extraer y utilizar los datos:
![image](https://user-images.githubusercontent.com/70445613/222978117-93158d8a-c274-47f6-9770-94cc3b7a7cf4.png)

Luego de procesar el dataframe logre crear un dataframe con un formato mas adecudado, en el cual cada fila es una fecha y sus columnas son lo sabores.
  
![image](https://user-images.githubusercontent.com/70445613/222978139-fab68d50-a659-4e48-a530-cbdf3a951792.png)

Despues utilice la funcion describe() para ver un resumen rapido de los datos y me di cuenta que algunos gustos contaban con desviaciones y medias demasiado altas, por ejemplo la columna 'ANANA' tenia una venta media de 131kg lo cual es imposible realizar semanalmente. 
![image](https://user-images.githubusercontent.com/70445613/222978162-6590dba0-f8d3-4b2d-aebb-1051dec37bf5.png)

Decidi realizar un histograma para ver como estaban distribuidos los datos y descubri que habia algunso datos particularmente grandes:
  ![image](https://user-images.githubusercontent.com/70445613/222977673-6841fe6f-c68e-453c-8103-26e314a64813.png)

Revisando un poco mas el excel me di cuenta que era un error durante la carga de datos por parte de los empleados al confundir comas y puntos, por ejemplo 9000kg de helado, signfica que se vendieron 9Kg, entonce dividi numeros >50 por 100 y mayores a 1000 por 100.
Luego de esto la disstribucion: 
![image](https://user-images.githubusercontent.com/70445613/222977782-417262a4-c885-43e9-8078-a4c2d529c0e4.png)

Despues genere una archivo func.ipynb en el cual cuenta con las funciones de agrupamiento y ordenamiento de datos, realice un analisis historico de los datos, es decir los agrupe por mes, y cree dos dataframes, uno es el dataframe agrupado por mes(ventas totales de cada columna por mes) y el segundo es la suma de las ventas totales. Ademas, partiendo del datafarme  creado, llamado: 'VentasTabla.xlsx' genere visualizciones de las ventas ordenas de manera descendente(mas vendios a menos).

Para terminar con el proyecto genere atravez de la libreria 'Streamlit' una aplicacion web,  para poder facilitar la visualizacion de los resultados para personas sin conocimientos de programacion. Todos los archivos de la aplicacion de encuentran en la carpeta Apliacion, el enlace web es: https://share.streamlit.io/app/fowardelcac-projecto-heladeria-aplicacionapp-7uopw6/

### Capturas de pantalla
![image](https://user-images.githubusercontent.com/70445613/229180413-714b50ff-ad1f-49a9-9df0-7e514d34c604.png)
![image](https://user-images.githubusercontent.com/70445613/229180603-6dcb485e-c231-4c7a-8daf-4d617fa1e535.png)
![image](https://user-images.githubusercontent.com/70445613/229180647-d5c51dc3-f811-41c6-8019-28e94cbeb404.png)
![image](https://user-images.githubusercontent.com/70445613/229180899-d677cb6f-91d0-4099-abaa-a385d753a1ab.png)
![image](https://user-images.githubusercontent.com/70445613/229180354-d1eef535-bb56-4083-8a5c-c4db6128e60d.png)
