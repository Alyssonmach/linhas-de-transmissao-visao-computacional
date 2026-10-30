# Cenário 3 — aumento de dados intensivo

Este experimento usa a versão 4 do projeto `towers-instance-segmentation-v2`. A preparação do conjunto amplia as transformações geométricas e filtragens em relação ao cenário anterior. As imagens foram normalizadas para 960 × 960 pixels; o notebook define `augment=False` no treinamento porque as transformações foram aplicadas durante a preparação dos dados. O limite configurado é de 150 épocas.

O registro disponível indica que a estratégia mais intensa não trouxe melhora consistente e pode ter prejudicado a representação visual útil ao modelo. Em imagens com torres bem destacadas, as detecções foram descritas como satisfatórias. Consulte o notebook antes de comparar este cenário com os demais.
