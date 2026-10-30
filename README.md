# Análise de Linhas de Transmissão com Visão Computacional

Estudo exploratório sobre como técnicas de visão computacional podem apoiar a análise de estruturas de transmissão de energia a partir de imagens e vídeos.

O repositório reúne experimentos com detecção, segmentação e rastreamento de torres, além de etapas de análise e organização de conjuntos de imagens. A investigação observa como a composição dos dados, as transformações aplicadas às imagens e as condições de captura influenciam o comportamento dos modelos.

## Escopo da investigação

- Analisar conjuntos públicos de imagens de torres e componentes de linhas de transmissão.
- Organizar e refinar dados para experimentos de detecção e segmentação.
- Comparar quatro cenários experimentais baseados em YOLOv8.
- Explorar o rastreamento de estruturas em sequências de vídeo.
- Inspecionar resultados em imagens e vídeos de teste.

## Organização do repositório

| Caminho | Conteúdo |
| --- | --- |
| [`deteccao-segmentacao-torres/organizacao-dados/`](deteccao-segmentacao-torres/organizacao-dados/) | Análise de bases, aquisição, descompactação e refinamento dos dados. |
| [`deteccao-segmentacao-torres/yolov8-torres/deteccao-segmentacao/`](deteccao-segmentacao-torres/yolov8-torres/deteccao-segmentacao/) | Notebooks e registros dos quatro cenários de treinamento. |
| [`deteccao-segmentacao-torres/yolov8-torres/rastreamento/`](deteccao-segmentacao-torres/yolov8-torres/rastreamento/) | Experimentos de rastreamento com BoT-SORT, ByteTrack e DeepSORT. |
| [`deteccao-segmentacao-torres/yolov8-torres/conjunto-teste/`](deteccao-segmentacao-torres/yolov8-torres/conjunto-teste/) | Orientações sobre amostras de imagens e vídeos usados na avaliação. |
| [`deteccao-segmentacao-torres/yolov8-torres/inferencia.py`](deteccao-segmentacao-torres/yolov8-torres/inferencia.py) | Script para configurar inferência em imagem ou vídeo com um modelo treinado. |

## Percurso sugerido

1. Consulte a [análise dos conjuntos de imagens](deteccao-segmentacao-torres/organizacao-dados/analise-datasets/README.md) e as fontes dos dados.
2. Leia como os dados são [organizados e refinados](deteccao-segmentacao-torres/organizacao-dados/README.md).
3. Compare os [cenários experimentais](deteccao-segmentacao-torres/yolov8-torres/deteccao-segmentacao/README.md) e seus registros.
4. Explore os experimentos de [rastreamento](deteccao-segmentacao-torres/yolov8-torres/rastreamento/README.md) e as orientações para os dados de teste.

## Dados e execução

Os conjuntos de imagens originais, vídeos, pesos treinados e outros arquivos volumosos não são versionados integralmente. Consulte os READMEs de cada etapa para encontrar as fontes e instruções; as regras de exclusão estão em [`.gitignore`](.gitignore).

Os experimentos estão registrados em notebooks e scripts, mas o repositório não define um ambiente único de execução. Dependências, credenciais de serviços de dados e recursos de GPU podem variar entre os cadernos. Antes de executar um experimento, confira suas células de configuração e os caminhos de entrada.

Os notebooks que baixam conjuntos pelo Roboflow leem a credencial da variável de ambiente `ROBOFLOW_API_KEY`. Configure-a localmente antes da execução; não inclua chaves no código ou no histórico do repositório.
