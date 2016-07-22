# Traducción al castellano de oTree

## Puedes ver el funcionamiento de oTree en esta demo en inglés
http://demo.otree.org/

## Página oficial
http://www.otree.org/

## Repositorio oficial
https://github.com/oTree-org/otree-core

## Sobre este proyecto

Los juegos íntegramente están programados en inglés. Las instrucciones han sido traducidas al castelleno y pueden descargarlas.
Mencionar que han sido elaboradas para el centro de investigación CSIC-CCHS (http://cchs.csic.es/) pero su uso es totalmente libre y compartido.
Los juegos pueden contener pequeñas erratas de traducción, así que ruego por favor revisar las traducciones en caso de su uso. ***No soy programador***
así que he procurado no modificar el código original y limitarme a incluir códigos méramente indicativos para que las instrucciones de los
juegos quedaran más claras.

## FALLOS SOLUCIONADOS

* **Subasta Vickrey**: las pregutnas para entender el juego no correspondían con su solución.
* **Dilema del Voluntario**: las pregutnas para entender el juego no correspondían con su solución.
* **Dilema del viajero**: {{Constants.reward}} estaba intercambiado erroenamente con {{Constants.pemalty}} en las instrucciones. No afectaba ya que constants.reward y constants.penalty eran el mismo valor. en Resultados modificado.
* * **Stag Hunt Game**: haciendo el juego a personas cercanas he descubierto que puede generar animadversión el hecho de obligar a realizar elecciones sobre cazar animales. He descrito en el juego un escenario totalmente imaginario manteniendo claras las eleciones posibles para evitar moral triggers en el juego que puedan alterar las decisiones. 

## FALLOS NO SOLUCIONADOS

* **Generales**: no sé cómo cambiar al castellano como el temporizador, el texto de espera en ResultsWaitPage, botones de "Next", botones de "Yes/No", las variables de cantidades que incluyen points y el mensaje de agradecimiento al final de cada experimento. Imagino que estará en alguna libreria. Por favor, si se corrige el botón "Next" modifique global/Introduccition para quitar la frase "Por favor, pulse "Next" para avanzar".
* **Survey**: no sé cómo programar la lista de países en castellano.
* **Dilema del prisionero**: en la fase de resultado "Usted eligió defect y el otro participante eligió cooperate.".
* **Juego Agente-Principal**: es muy complicado el juego para que si quiera puedan saber que están haciendo los participantes. Hay que explicarlo mejor.
* **Matching Pennies**: puntos en resultados y botón next en inglés.
* **Traveler Dilemmma**: puntos en resultados y botón next en inglés.
* **Barganing Game**: puntos en resultados y botón next en inglés.
* **Common value auction**: puntos de apuesta y botón next en inglés.
* **Stackelberg competition**: puntos en resultados y botón next en inglés.
* **Bertrand competition**: puntos en resultados y botón next en inglés.

## Instalar oTree original: Guía rápida

Corra los siguientes comandos:

```
pip install --upgrade otree-core
otree startproject oTree
otree resetdb
otree runserver
```

Puede descargar este repositorio y superponer la carpeta original o ejecutar "otree runserver" desde este repositorio descargado.

## Contacto

Si existe algún fallo que pueda corregir o tiene alguna duda por favor escríbame e intentaré ayudar en la medida que pueda: pipegalera@gmail.com


## Contribuidores del proyecto original de oTree

* Gregor Muellegger (http://gremu.net/, https://github.com/gregmuellegger)
* Juan B. Cabral (http://jbcabral.org/, https://github.com/leliel12)
* Bertrand Bordage (https://github.com/BertrandBordage)
* Alexander Schepanovski (https://github.com/Suor/)
* Alexander Sandukovskiy
* Som Datye

# Más información y guía del programa

http://otree.readthedocs.org

# Status

![RTD Badge](https://readthedocs.org/projects/otree/badge/?version=latest)
