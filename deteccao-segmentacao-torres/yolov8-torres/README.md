# Detecção e Segmentação das Torres Utilizando a YOLOv8

Nesse diretório está armazenado os arquivos de treinamento e testagem das arquiteturas YOLOv8 para resolver o problema de detecção e segmentação das torres de transmissão. A análise feita para cada um dos cenários está delimitada na documentação do projeto.

O arquivo ```frame-analise.ipynb``` foi um teste desenvolvido para analisar de forma comparativa cada um dos modelos treinados, na qual foi comparado diversos frames dos vídeos de teste para verificação do desempenho dos modelos.

O arquivo ```inferencia.py``` contém um código útil para realizar inferências com os modelos treinados. Nele, é possível configurar o tipo de dispositivo ou mídia de entrada para inferência, e visualizar em tempo real a análise feita pelo algoritmo.