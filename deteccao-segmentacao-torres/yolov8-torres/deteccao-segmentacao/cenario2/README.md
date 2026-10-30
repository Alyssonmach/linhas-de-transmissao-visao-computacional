# Cenário 2 — seleção de estruturas e imagens próximas

Este experimento usa a versão 3 do projeto `towers-instance-segmentation-v2` e restringe o conjunto a tipos de torre mais comuns no contexto brasileiro. Para compensar a seleção, foram incluídas mais imagens capturadas de perto. O conjunto foi normalizado para 960 × 960 pixels; no treinamento, `augment=False` e o limite configurado é de 150 épocas.

As anotações do experimento relatam menos falsos positivos após a seleção dos dados e a inclusão de vistas próximas. Essa observação é qualitativa; consulte o notebook para as configurações e amostras avaliadas.
