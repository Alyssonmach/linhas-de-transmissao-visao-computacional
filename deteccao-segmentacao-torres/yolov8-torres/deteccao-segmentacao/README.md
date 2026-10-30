# Cenários de detecção e segmentação

Os notebooks organizam quatro experimentos baseados em YOLOv8. As configurações variam as versões dos conjuntos e as estratégias de aumento de dados; cada pasta contém o caderno e um registro qualitativo dos resultados observados.

| Cenário | Configuração registrada |
| --- | --- |
| [Cenário 1](cenario1/README.md) | Projeto `towers-instance-segmentation-v1`, versão 4; 100 épocas; aumento aplicado na preparação do conjunto e `augment=False` no treinamento. |
| [Cenário 2](cenario2/README.md) | Projeto `towers-instance-segmentation-v2`, versão 3; seleção de estruturas mais comuns no contexto brasileiro e inclusão de imagens próximas; 150 épocas. |
| [Cenário 3](cenario3/README.md) | Projeto `towers-instance-segmentation-v2`, versão 4; aumento mais intenso na preparação do conjunto; `augment=False` no treinamento. |
| [Cenário 4](cenario4/README.md) | Projeto `towers-instance-segmentation-v2`, versão 5; o caderno usa `augment=True` e `pretrained=True`. |

Os registros de cenário 4 descrevem a preparação do conjunto como sem aumento de dados, mas o caderno ativa `augment=True` durante o treinamento. Essa diferença está destacada na documentação do cenário. As observações de desempenho são exploratórias e dependem dos dados, pesos e amostras usados. Pesos e mídias podem estar fora do Git; consulte os notebooks para identificar os arquivos necessários à reprodução.
