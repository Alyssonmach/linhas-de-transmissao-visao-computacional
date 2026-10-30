# Cenário 1 — diversidade de estruturas

Este experimento usa o projeto `towers-instance-segmentation-v1`, versão 4, com imagens de diferentes tipos de torre. O conjunto foi normalizado para 960 × 960 pixels e recebeu transformações geométricas mais leves durante a preparação no Roboflow. No treinamento, o notebook define `augment=False`, usa o modelo YOLOv8x de segmentação e configura até 100 épocas.

O registro experimental menciona redução de falsos positivos e falsos negativos, mas também confusões com estruturas que não correspondem ao padrão de interesse. Consulte o notebook para ver a configuração completa e as inferências associadas.
