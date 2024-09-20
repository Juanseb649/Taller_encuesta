**Hoja de Trabajo: Una Encuesta**

**Enunciado. Analice la siguiente lectura e identiﬁque el mundo del problema, lo que se espera de la aplicación y las restricciones para desarrollarla.**

Se quiere crear una aplicación que permita realizar encuesta de opinión de un curso y manejar sus resultados. La encuesta consiste en una única pregunta, en la cual se le pide a la persona que caliﬁque la calidad de un curso dando un valor entre 0 y 10.

Se desea poder conocer los resultados de la en cuenta para diferentes sectores demográficos. Para esto se tendrá en cuenta el rango el rango de edad y el estado civil (soltero o casado) de la persona. En la encuesta se dividieron las personas en 3 rangos de edad: (1) menores de 18, (2) entre 18 y 55 y (3) mayores de 55 años.

En el momento de hacer la pregunta, la persona debe seleccionar su rango de edad, informar si es soltera o casada y agregar una nueva opinión a la encuesta.

El programa debe informar el valor total de la encuesta. Esto es, debe promediar todas las notas dadas y presentar el resultado en pantalla. También debe poder informar valores parciales de la encuesta. En ese caso se debe especificar un rango de edad y un estado civil. El programa presenta por pantalla el promedio de las caliﬁcaciones del curso dadas por todas las personas que cumplen el perﬁl pedido. Puede suponer que en el momento de calcular los resultados hay por lo menos una persona de cada perﬁl.



**Requerimientos funcionales. Describa tres requerimientos funcionales de la aplicación que haya identiﬁcado en el enunciado.**

**Requerimiento Funcional 1**

|<p>Nombre:</p><p></p>|**R1:  Añadir Opinión**|
| :- | :- |
|<p>Resumen:</p><p></p>|**Añadir Opinión del curso entre una calificación mínima de 0 y una máxima de 10**|
|<p>Entradas:</p><p></p><p></p><p></p><p></p>|<p></p><p>**Calificaciones ingresadas.**</p>|
|<p>Resultado:</p><p></p><p></p><p></p>|**Ninguno**|
|||

**Requerimiento Funcional 2**

|<p>Nombre:</p><p></p>|**R2: Calcular promedio total de la encuesta**|
| :- | :- |
|<p>Resumen:</p><p></p>|**Permite calcular el promedio de la calificación dividiendo total de calificaciones entre el total de encuestados.**|
|<p>Entradas:</p><p></p><p></p><p></p><p></p>|<p>**Ninguno.**</p><p></p><p></p>|
|<p>Resultado:</p><p></p><p></p><p></p>|**Se muestra el promedio de la calificación.**|

**Requerimiento Funcional 3**

|<p>Nombre:</p><p></p>|**R3: Calcular Promedio parcial de la encuesta.**|
| :- | :- |
|<p>Resumen:</p><p></p><p></p><p></p><p>Entradas:</p><p></p>|<p>**Permite calcular el promedio de la calificación según los criterios de búsqueda.**</p><p></p><p></p><p>**Rango Estado civil, Rango de edad**</p><p></p>|
|<p></p><p>Resultado:</p><p></p><p></p>|<p></p><p>**Se muestra el valor parcial de la encuesta.**</p>|

**Entidades del mundo. Identiﬁque las entidades del mundo y descríbalas brevemente.**

|**Entidad**|**Descripción**|
| :-: | :-: |
|<p></p><p></p><p>**Encuesta**</p><p></p><p></p><p></p>|<p>** </p><p>**Representa la encuesta en si y maneja las opiniones de los encuestados.**</p>|
|<p></p><p>**Rango**</p><p></p><p></p><p></p>|<p></p><p>**Representa la unión de solteros y casados en un rango de edad y se adiciona la suma de sus calificaciones.**</p><p>**Rango de edad:**</p><p>` `**Rango 1:** menores de 18 años</p><p>**Rango 2:** entre 18 y 55</p><p>**Rango 3:** mayores de 55)</p><p>**Estado Civil:**</p><p>(Soltero, casado)</p><p></p>|

**Características de las entidades. Identiﬁque las características de cada una de las entidades y escriba la clase en UML con el tipo de datos adecuado.**

**Entidad 1**

|**Atributo**|**Valores posibles**|**Diagrama UML**|
| :-: | :-: | :-: |
|<p></p><p>**Rango de edad**</p><p></p><p></p>|<p></p><p>**Números** </p>||

|Encuesta|
| :- |
|Rango Menores de 18|
|Rango entre 18 a 55|
|Rango Mayores de 55|

||||
| :- | :- | :- |
|<p></p><p>**Opinión**</p>|<p></p><p>**Números**</p>||
|<p></p><p>**Estado Civil**</p><p></p><p></p>|<p></p><p>**Cadena de Caracteres** </p>||

**Entidad 2**

|**Atributo**|**Valores posibles**|**Diagrama UML**|
| :-: | :-: | :-: |
|<p></p><p>**Numero Casados**</p>|<p></p><p>**Números**</p>||

|Rango Encuesta|
| :- |
|Total Casados|
|Total Solteros |
|TOTAL|

||||
| :- | :- | :- |
|<p></p><p>**NumeroSolteros**</p><p></p>|<p></p><p>**Números** </p>||
|**Total Calificación Casados**|||










**Relaciones entre entidades. Dibuje las entidades en UML (sin atributos ni métodos) y las relaciones que existan entre ellas.**

|<p></p><p></p><p>![](Aspose.Words.9f47a3a5-b16e-4e07-b6e5-38125d59df9d.001.png)</p><p></p><p>**                                                                                                                   </p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p>|
| - |
||

**Métodos de las entidades. Lea las siguientes descripciones de métodos y escriba su implementación en el lenguaje Python.**

**Método 1**

<table><tr><th valign="top"><b>Clase</b></th><th valign="top"><b>RangoEncuesta</b></th><th rowspan="5" valign="top"></th></tr>
<tr><td valign="top">Nombre</td><td valign="top">darNumeroCasados</td></tr>
<tr><td valign="top">Parámetros</td><td valign="top">Ninguno.</td></tr>
<tr><td valign="top">Retorno</td><td valign="top">El número de personas casadas que respondieron la encuesta, en el rango de edad de la clase.</td></tr>
<tr><td valign="top">Descripción</td><td valign="top">Retorna el número de personas casadas que respondieron la encuesta, en el rango de edad de la clase.</td></tr>
</table>

**Método 2**

<table><tr><th valign="top"><b>Clase</b></th><th valign="top"><b>RangoEncuesta</b></th><th rowspan="5" valign="top"></th></tr>
<tr><td valign="top">Nombre</td><td valign="top">darTotalOpinionCasados</td></tr>
<tr><td valign="top">Parámetros</td><td valign="top">Ninguno.</td></tr>
<tr><td valign="top">Retorno</td><td valign="top">La suma de todas las opiniones de los encuestados casados en el rango de edad de la clase.</td></tr>
<tr><td valign="top">Descripción</td><td valign="top">Retorna la suma de todas las opiniones de los encuestados casados en el rango de edad de la clase.</td></tr>
</table>

**Método 3**

<table><tr><th valign="top"><b>Clase</b></th><th valign="top"><b>RangoEncuesta</b></th><th rowspan="5" valign="top"></th></tr>
<tr><td valign="top">Nombre</td><td valign="top">darPromedio</td></tr>
<tr><td valign="top">Parámetros</td><td valign="top">Ninguno.</td></tr>
<tr><td valign="top">Retorno</td><td valign="top">El promedio de la encuesta en el rango de edad de la clase.</td></tr>
<tr><td valign="top">Descripción</td><td valign="top">Retorna el promedio de la encuesta en el rango de edad de la clase. Para esto suma todas las opiniones y divide por el número total de encuestados.</td></tr>
</table>

**Método 4**

<table><tr><th valign="top"><b>Clase</b></th><th valign="top"><b>Rango Encuesta</b></th><th rowspan="5" valign="top"></th></tr>
<tr><td valign="top">Nombre</td><td valign="top">agregarOpinionCasado</td></tr>
<tr><td valign="top">Parámetros</td><td valign="top">Opinión del encuestado.</td></tr>
<tr><td valign="top">Retorno</td><td valign="top">Ninguno.</td></tr>
<tr><td valign="top">Descripción</td><td valign="top"><p>Añade la opinión de una persona casada en el rango de edad que representa la clase.</p><p></p><p></p><p></p></td></tr>
</table>

**Método 5**

<table><tr><th valign="top"><b>Clase</b></th><th valign="top"><b>RangoEncuesta</b></th><th rowspan="5" valign="top"></th></tr>
<tr><td valign="top">Nombre</td><td valign="top">darPromedioCasados</td></tr>
<tr><td valign="top">Parámetros</td><td valign="top">Ninguno.</td></tr>
<tr><td valign="top">Retorno</td><td valign="top">El promedio de la encuesta en el rango de edad de la clase considerando sólo los casados.</td></tr>
<tr><td valign="top">Descripción</td><td valign="top">Retorna el promedio de la encuesta en el rango de edad de la clase. Para esto suma todas las opiniones de los casados y divide por el número total de ellos.</td></tr>
</table>

**Método 6**

<table><tr><th valign="top"><b>Clase</b></th><th valign="top"><b>Encuesta</b></th><th rowspan="5" valign="top"></th></tr>
<tr><td valign="top">Nombre</td><td valign="top">agregarOpinionRango1Casado</td></tr>
<tr><td valign="top">Parámetros</td><td valign="top">Opinión del encuestado.</td></tr>
<tr><td valign="top">Retorno</td><td valign="top">Ninguno.</td></tr>
<tr><td valign="top">Descripción</td><td valign="top"><p>Añade la opinión de una persona casada en el rango de edad 1 de la encuesta.</p><p></p><p></p></td></tr>
</table>
**Método 7**

<table><tr><th valign="top"><b>Clase</b></th><th valign="top"><b>Encuesta</b></th><th rowspan="5" valign="top"></th></tr>
<tr><td valign="top">Nombre</td><td valign="top">agregarOpinionRango2Soltero</td></tr>
<tr><td valign="top">Parámetros</td><td valign="top">(1) estado civil, (2) opinión.</td></tr>
<tr><td valign="top">Retorno</td><td valign="top">Ninguno.</td></tr>
<tr><td valign="top">Descripción</td><td valign="top"><p>Añade la opinión de una persona soltera en el rango de edad 2 de la encuesta.</p><p></p><p></p><p></p></td></tr>
</table>

**Método 8**

<table><tr><th valign="top"><b>Clase</b></th><th valign="top"><b>Encuesta</b></th><th rowspan="5" valign="top"></th></tr>
<tr><td valign="top">Nombre</td><td valign="top">darPromedio</td></tr>
<tr><td valign="top">Parámetros</td><td valign="top">Ninguno.</td></tr>
<tr><td valign="top">Retorno</td><td valign="top">El promedio de la encuesta en todos los rangos de edad.</td></tr>
<tr><td valign="top">Descripción</td><td valign="top">Retorna el promedio de la encuesta en todos los rangos de edad. Para esto suma todas las opiniones y divide por el número total de encuestados.</td></tr>
</table>

**Método 9**

<table><tr><th valign="top"><b>Clase</b></th><th valign="top"><b>Encuesta</b></th><th rowspan="5" valign="top"></th></tr>
<tr><td valign="top">Nombre</td><td valign="top">darPromedioCasados</td></tr>
<tr><td valign="top">Parámetros</td><td valign="top">Ninguno.</td></tr>
<tr><td valign="top">Retorno</td><td valign="top">El promedio de la encuesta en todos los rangos de edad de la clase, considerando sólo los casados.</td></tr>
<tr><td valign="top">Descripción</td><td valign="top">Retorna el promedio de la encuesta en todos los rangos de edad. Para esto suma todas las opiniones de los casados y divide por el número total de ellos.</td></tr>
</table>

