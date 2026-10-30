# Cenário 4 — versão 5 do conjunto

Este experimento usa a versão 5 do projeto `towers-instance-segmentation-v2` e normaliza as imagens para 960 × 960 pixels. O registro qualitativo descreve a preparação do conjunto como uma comparação sem aumento de dados. No entanto, o notebook define `augment=True` durante o treinamento, além de `pretrained=True` e `dropout=0.15`; portanto, não é uma configuração sem aumento de dados em todas as etapas. O limite configurado é de 150 épocas.

As observações registradas apontam desempenho aceitável em algumas situações, mais falsos positivos em vídeos e sinais de sobreajuste aos dados de treinamento. Consulte o notebook e confirme a configuração da versão 5 do conjunto antes de interpretar a comparação.
