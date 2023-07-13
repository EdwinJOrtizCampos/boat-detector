# Detector y clasificador de embarcaciones
Este proyecto se basa en una modificación del modelo YOLOv7, cuyo paper es accesible en [YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors](https://arxiv.org/abs/2207.02696). El repositorio original del proyecto se puede encontrar en [GitHub](https://github.com/WongKinYiu/yolov7). Se aconseja abrir este documento en un visualizador de MarkDown.

Los datos y modelos generados por Qualitas Artificial Intelligence and Science S.A están protegidos mediante propiedad intelectual y su uso, incluido comercial, está restringido.

## ¿Qué es esto?

Este proyecto es un detector y clasificador de embarcaciones capaz de ubicarlas a través de la estimación de sus coordenadas en formato GPS. Está basado concretamente en la arquitectura YOLOv7-E6

## Métricas de YOLOV7-E6 sobre dataset  MS COCO
| Model | Test Size | AP<sup>test</sup> | AP<sub>50</sub><sup>test</sup> | AP<sub>75</sub><sup>test</sup> | batch 1 fps | batch 32 average time |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: |
| [**YOLOv7-E6**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6.pt) | 1280 | **56.0%** | **73.5%** | **61.2%** | 56 *fps* | 12.3 *ms*


## A tener en cuenta
Este trabajo académico utiliza datos protegidos por propiedad intelectual por lo que, aunque se describen las modificaciones realizadas, no se han añadido los modelos de pesos generados. Este documento resume el procedimiento para instalar y ejecutar el modelo. Pero en todo caso se recomienda obedecer a las instrucciones del repositorio de YOLOv7

## Modificaciones del proyecto original

 - fichero detect_position.py: es el fichero usado junto a los procesos de geolocalización y una versión extendida del original (detect.py). En este fichero se obtienen los datos de los navíos detectados en base a sus cajas contenedoras y se mandan, junto a datos obtenidos de cámaras PTZ, a una API que ubica estos barcos en formato GPS. Estas coordenadas son finalmente representadas en un mapa HTML.
 - ficheros "train" y "val", no presentes en el repositorio por propiedad intelectual de Qualitas Artificial Intelligence and Science. Continen los datos usados durante el entrenamiento del modelo final.
 - fichero locate_map: rutina encargada de recibir coordenadas GPS y representarlas en mapas HTML almacenados en "/maps".
 - fichero /scripts/estudiante/select_validation_images.py: selecciona de forma aleatoria 205 imágenes para el *dataset* de validación.
 - fichero /scripts/estudiante/move_train_validation_file.py: script auxiliar para el transporte de ficheros de entrenamiento a sus ubicaciones correspondientes.
 - fichero /scripts/estudiante/count_labels.py: fichero encargado de contar las etiquetas correspondientes a cada clase para balancear el *dataset*.
 - fichero /scripts/estudiante/delete_batch_empty_lines.py: fichero que formatea los ficheros de datos de entrenamiento para ser leídos por rutinas auxiliares.
 - fichero /scripts/estudiante/delete_images_no_annotations.py: fichero que itera sobre datasets a los que se le ha aplicado el modelo básico de YOLOV7, eliminando aquellas imágenes que no poseen barcos en base al fichero anterior mediante la comprobación de sus ficheros de etiquetas. Esto ayuda a hacer una primera filtración / criba del dataset.
 - fichero /scripts/estudiante/delete_images_no_annotations.py: fichero auxiliar que itera sobre datasets a los que se le ha aplicado el modelo básico de YOLOV7, eliminando aquellas imágenes que no poseen barcos en base al fichero anterior. Esto ayuda a hacer una primera filtración / criba del dataset.
 - fichero /scripts/estudiante/delete_undersize.py: fichero que filtra las imágenes de un *dataset* por tamaño, útil para seleccionar las imágenes de mayor calidad.
 - fichero /scripts/estudiante/download_from_browser.py: fichero que utiliza un *web scrapper* para buscar imágenes de barcos industriales en internet.
 - fichero /scripts/estudiante/downscale_640.py: fichero que escala imágenes a 640 x 640 píxeles para poder ejecutar un análisis usando distancia de Fréchet.
 - fichero /scripts/estudiante/extract.py: fichero que extrae todas las imágenes bajo un directorio de forma recursiva y añade un *bytecode* aleatorio para evitar duplicados. Usado para obtener imágenes de un servidor.
 - fichero /scripts/estudiante/format_data_dirs.py: fichero que modifica las rutas a otros ficheros para ser leídas por el explorador de Windows 10.
 - fichero /scripts/estudiante/batchprelabel.py: lleva a cabo un pre etiquetado de un *dataset* arbitrario para localizar imágenes donde existen barcos, que luego son filtradas al *dataset* elaborado en el trabajo.
 - fichero /scripts/estudiante/move_labels.py: fichero que transporta de forma automatizada etiquetas de imágenes ubicadas en otro directorio. Útil para agilizar la preparación de los conjuntos de validación y entrenamiento.
 - fichero /scripts/estudiante/get_originals.py: fichero auxiliar para el traslado de archivos. Dados 3 directorios "A", "B" y "C", se localizan todas las imágenes de "A" y se comprueba si existen en "B". En caso afirmativo, se copian a "C". Útil para trabajar con varios ficheros con muchas imágenes en su interior.
 - fichero geofencing.py: realiza llamadas a la API correspondiente para obtener coordenadas GPS a partir de una ubicación en una imagen (en píxeles).
 
## Instalación
Descargue el repositorio en su equipo local y descargue las dependencias
``` shell
pip install -r requirements.txt
```

## Uso

En vídeo:
``` shell
python detect.py --weights yolov7.pt --conf 0.25 --img-size 640 --source yourvideo.mp4
```

En imagen:
``` shell
python detect.py --weights yolov7.pt --conf 0.25 --img-size 640 --source inference/images/horses.jpg
```

<div align="center">
    <a href="./">
        <img src="./figure/horses_prediction.jpg" width="59%"/>
    </a>
</div>

## Citas y  reconocimientos al autor original

```
@article{wang2022yolov7,
  title={{YOLOv7}: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors},
  author={Wang, Chien-Yao and Bochkovskiy, Alexey and Liao, Hong-Yuan Mark},
  journal={arXiv preprint arXiv:2207.02696},
  year={2022}
}
```

```
@article{wang2022designing,
  title={Designing Network Design Strategies Through Gradient Path Analysis},
  author={Wang, Chien-Yao and Liao, Hong-Yuan Mark and Yeh, I-Hau},
  journal={arXiv preprint arXiv:2211.04800},
  year={2022}
}
```

<details><summary> <b>Expand</b> </summary>

* [https://github.com/AlexeyAB/darknet](https://github.com/AlexeyAB/darknet)
* [https://github.com/WongKinYiu/yolor](https://github.com/WongKinYiu/yolor)
* [https://github.com/WongKinYiu/PyTorch_YOLOv4](https://github.com/WongKinYiu/PyTorch_YOLOv4)
* [https://github.com/WongKinYiu/ScaledYOLOv4](https://github.com/WongKinYiu/ScaledYOLOv4)
* [https://github.com/Megvii-BaseDetection/YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)
* [https://github.com/ultralytics/yolov3](https://github.com/ultralytics/yolov3)
* [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)
* [https://github.com/DingXiaoH/RepVGG](https://github.com/DingXiaoH/RepVGG)
* [https://github.com/JUGGHM/OREPA_CVPR2022](https://github.com/JUGGHM/OREPA_CVPR2022)
* [https://github.com/TexasInstruments/edgeai-yolov5/tree/yolo-pose](https://github.com/TexasInstruments/edgeai-yolov5/tree/yolo-pose)

</details>
