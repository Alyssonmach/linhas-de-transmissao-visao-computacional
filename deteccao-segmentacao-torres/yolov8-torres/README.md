# Experimentos com YOLOv8

Este diretório reúne os notebooks de treinamento, as avaliações por cenário e o script de inferência para imagens e vídeos.

- [`deteccao-segmentacao/`](deteccao-segmentacao/): quatro configurações experimentais e seus registros.
- [`rastreamento/`](rastreamento/): exploração de algoritmos para acompanhar detecções em vídeo.
- [`conjunto-teste/`](conjunto-teste/): descrição das amostras locais usadas na inspeção dos resultados.
- [`inferencia.py`](inferencia.py): configuração de modelo, entrada, confiança, dispositivo e rastreador.

O script de inferência espera os pesos e os arquivos de entrada em caminhos configurados no próprio código. Esses artefatos não são incluídos necessariamente no repositório.
