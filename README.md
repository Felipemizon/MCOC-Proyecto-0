# MCOC-Proyecto-0

<b> <H1> Introducción </H1> </b>

La pérdida de significancia es un error que ocurre en los cálculos que se utiliza aritmética como en el caso de punto flotante.

<b> <H1> Perdida de Significancia en la función Coseno </H1> </b>

En este proyecto se analiza la función coseno cos(x) y como esta varía su valor debido a la perdida de significancia por la gran cantidad de datos analizados en una lista y como este error es aun mayor cuando se trabaja en dtype=np.float32 en comparación cuando se utiliza dtype=np.float64.

Para poder calcular el error relativo, se analizan los siguientes casos:
<UL>
    <LI>1. Se define el arreglo "a" con datos tipo dtype.float32 y se calcula el promedio mediante np.mean para luego calcular el coseno mediante una función creada manualmente.
    <LI>2.Se define el arreglo "a" con datos tipo dtype.float32 y se calcula el promedio mediante np.mean para luego calcular el coseno mediante la función cos(x).
    <LI>3. Se define el arreglo "a" con datos tipo dtype.float64 y se calcula el promedio mediante np.mean para luego calcular el coseno mediante una función creada manualmente.
</UL>
    
<b> <H1> Cálculos </H1> </b>
Definiendo el error como:
                            
                            error = (Calculo_obtenido - Resultado_real) / Resultado_real
   
En el siguiente gráfico se puede apreciar la perdida de significancia, y como esta aumenta según la cantidad de datos analizados y el tipo de datos que sean estos, ya sea con 32bits o 64bits.

![alt text](https://github.com/Felipemizon/MOC/blob/master/Grafico%20Definitivo.png)

Output de la consola:

    N = 65536
    -0.307332783565         2.81171149623e-07
    -0.307333               2.79960178475e-07
    -0.307332874317         1.41172978654e-08
    -0.307332869978         0.0

    N = 131072
    -0.271440092524         1.95851215505e-08
    -0.27144                5.67808994467e-09
    -0.271440092524         1.95851215505e-08
    -0.271440087208         0.0

    N = 262144
    -0.351757515668         3.82755780469e-07
    -0.351758               4.13259302803e-07
    -0.351757384385         9.53475949578e-09
    -0.351757381031         0.0

    N = 524288
    -0.37004317231          3.90907196218e-07
    -0.370043               4.28142711646e-07
    -0.370043319973         8.13495338056e-09
    -0.370043316963         0.0

    N = 1048576
    -0.337225219469         5.92339362785e-08
    -0.337225               3.23116817896e-08
    -0.337225243096         1.08279282517e-08
    -0.337225239444         0.0

    N = 2097152
    -0.259388692683         7.32079910693e-07
    -0.259389               7.03334235558e-07
    -0.259388508476         2.19228290438e-08
    -0.25938850279          0.0

    N = 4194304
    -0.280022706073         7.18688690266e-07
    -0.280023               7.34719362887e-07
    -0.28002250989          1.8091146171e-08
    -0.280022504824         0.0

    N = 8388608
    -0.0759522741521         1.90717437385e-06
    -0.0759523               1.74304741249e-06
    -0.0759521444813         1.99903754282e-07
    -0.0759521292982         0.0
    
    <b> <H1> Anexo </H1> </b>
<a href="https://github.com/96josetole/MCOC-Proyecto-0">
