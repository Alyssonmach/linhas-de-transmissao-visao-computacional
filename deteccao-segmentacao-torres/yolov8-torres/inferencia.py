# Algoritmo para Inferência de mídias utilizando os modelos treinados da YOLOv8

# importação dos pacotes úteis
import ultralytics
from ultralytics import YOLO

# importação dos parâmetros do modelo da YOLOv8 treinado
MODEL_REF = 'cenario2/modelo-treinado/best.pt'

# diretório de referência com a imagem ou vídeo para predição
SOURCE = 'conjunto-teste/rastreamento/rastreio-teste1.mp4'
# limite de confiança do objeto para detecção
CONF = 0.25
# salvar o resultado obtido na inferência
SAVE = True
# visualizar o resultado da inferencia em tempo real
SHOW = True
# algoritmo padrão de rastreamento utilizados
TRACKER = 'bytetrack.yaml'
# escolha do dispositivo (CPU ou GPU) para realização da inferência
DEVICE = 0
# otimização da inferência utilizando o recurso de stream
STREAM = True
# escolha entre predição simples com ou sem o algoritmo de rastreamento
MODEL_MODE = 'track'

# realizando a predição no modelo treinado
model = YOLO(MODEL_REF)

# atualizando o nome da classe alvo
model.names[0] = 'Torre'

# seleção do modelo para realização da predição
if MODEL_MODE == 'predict':
	results = model.predict(source = SOURCE, conf = CONF, show = SHOW, 
                      	    device = DEVICE, stream = STREAM, save = SAVE)

# seleção do modelo para realização da predição com rastreamento
if MODEL_MODE == 'track':
	results = model.track(source = SOURCE, conf = CONF, show = SHOW, 
                      	  tracker = TRACKER, device = DEVICE, 
                      	  stream = STREAM, save = SAVE)

# recurso de otimização de inferência                     
if STREAM == True:
	for r in results:
		boxes, masks, probs = r.boxes, r.masks, r.probs