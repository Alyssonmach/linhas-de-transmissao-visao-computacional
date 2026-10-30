# Fontes e arquivos compactados

Os arquivos originais das bases não são versionados neste repositório. Consulte as páginas de origem para obter os dados e verifique as respectivas licenças e condições de uso:

- [TTPLA Dataset](https://github.com/R3ab/ttpla_dataset)
- [STN PLAD](https://github.com/andreluizbvs/PLAD)
- [COT SAT](https://universe.roboflow.com/cao-the-ktpc-udrjd/cot-sat-txqdh)
- [DT COT SAT CT](https://universe.roboflow.com/bdpc-ai-gd2/dt-cot-sat-ct)
- [Daychongset110](https://universe.roboflow.com/khpcdoituonggd2/daychongset110)
- [CSAT CT](https://universe.roboflow.com/qbpcluoi110gd1/csat_ct)
- [Base Detection](https://universe.roboflow.com/shandong-university-zvicd/base-detection-zyh6x)
- [110 NHANDIEN COTSAT](https://universe.roboflow.com/tthpc/110_nhandien_cotsat)
- [Tower Joint](https://universe.roboflow.com/yuyang-li/tower_jointv1)
- [Transmission System](https://universe.roboflow.com/power-tower/transimission-system)

## Extração

Coloque os arquivos `.zip` nesta pasta e use a função `unzip_file(zip_path, extract_to)` definida em [`descompactar.py`](descompactar.py). Informe o caminho do arquivo e o diretório de destino, por exemplo:

```python
from descompactar import unzip_file

unzip_file("caminho/para/base.zip", "../datasets-descompactados/nome-da-base")
```

O script fornece a função de extração; ele não escolhe automaticamente o arquivo nem o destino.
