
<p align="center">
<img src="https://raw.githubusercontent.com/gusgeek/pyDolar-lib/main/pyapp.png">
  <br>
  Libreria para la toma de cotizaciones del Dolar de Argentina
</p>

# Bienvenido

Este proyecto existe gracias a que es mi primera andanza en Python. Me siento muy orgulloso de compartirlo para que vean cómo se puede experimentar con este increíble lenguaje.
<br><br>
  <p align="center">
  <strong>Tenga presente que este codigo es un experimento</strong>
  <br><br>
    <strong>
      <a href="https://github.com/gusgeek/pyDolar-lib/issues/new"> Ofrecer una Idea </a> | 
      <a href="https://github.com/gusgeek/pyDolar-lib/releases/latest"> Obtenerlo </a>
      <br>
      <a href="https://github.com/gusgeek/phpDolar"> Integrarlo en mi Sistema PHP </a>
    </strong>
  </p>

# Como empiezo
> Es necesario seguir las dependencias que se necesita en requeriments.txt

El funciomaniento es sencillo, simplemente debe de incluir la libreria en su documento

```
  import pyDolarLib as dolar 
```
Con las siguientes funciones, segun la entidad, debera de especificar que tipo de Dolar quiere tomar. Indicando ```buy``` para la compra y ```sell``` para la venta.



* Banco Galicia ```bancoGalicia(buy/sell)```

* Ambito Financiero
  * Dolar Oficial ```afOficial(buy/sell)```
  * Dolar Informal ```afInformal(buy/sell)```
  * Dolar Turista ```afTurista(buy/sell)```
  
* Banco DolarSI ```DolarSI(buy/sell)```

Un ejemplo de implementacion seria
```
  import pyDolarLib as d
  print(d.afOficial('sell'))
```
<br><br>
<p align="center">
    <img src="https://img.shields.io/github/downloads/gusgeek/pyDolar-lib/total">  
    <img src="https://img.shields.io/github/v/release/gusgeek/pyDolar-lib">  
    <img src="https://img.shields.io/github/release-date/gusgeek/pyDolar-lib">  
    <img src="https://img.shields.io/github/languages/code-size/gusgeek/pyDolar-lib">
  <br><br>
  <strong>:pencil2: con :heart:</strong>
</p>
