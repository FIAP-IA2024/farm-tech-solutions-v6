# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="https://raw.githubusercontent.com/lfusca/templateFiap/main/assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

## 👨‍🎓 Integrantes do Grupo

- RM559800 - [Jonas Felipe dos Santos Lima](https://www.linkedin.com/in/jonas-felipe-dos-santos-lima-b2346811b/)
- RM560173 - [Gabriel Ribeiro](https://www.linkedin.com/in/ribeirogab/)
- RM559926 - [Marcos Trazzini](https://www.linkedin.com/in/mstrazzini/)
- RM559645 - [Edimilson Ribeiro](https://www.linkedin.com/in/edimilson-ribeiro/)

## 👩‍🏫 Professores

### Coordenador(a)

- [André Godoi](https://www.linkedin.com/in/profandregodoi/)

---

## 📌 Entregas do Projeto

O projeto consiste em duas entregas principais:

1. **Entrega 1 - Visão Computacional com YOLO**: Desenvolvimento de um sistema de visão computacional usando o modelo YOLO para detecção de objetos, com treinamento em diferentes quantidades de épocas e análise comparativa de resultados.
2. **Entrega 2 - Comparação de Abordagens**: Implementação de abordagens alternativas (YOLO tradicional e CNN treinada do zero) para comparação de desempenho com a solução da Entrega 1.

---

## 🛠 **Entrega 1 - Visão Computacional com YOLO**

Nesta entrega, desenvolvemos um sistema de visão computacional utilizando YOLO para demonstrar seu potencial e acurácia na detecção de objetos. O projeto simula o trabalho da FarmTech Solutions, uma empresa que expandiu seus serviços de IA para além do agronegócio, incluindo visão computacional.

### 📊 Dataset e Organização

- Dataset organizado com imagens de dois objetos distintos (A e B)
- Total de 80 imagens (40 de cada objeto)
- Distribuição:
  - 80% para treinamento (64 imagens: 32 de cada objeto)
  - 10% para validação (8 imagens: 4 de cada objeto)
  - 10% para teste (8 imagens: 4 de cada objeto)
- Imagens rotuladas usando ferramentas específicas para visão computacional

### 🧠 Treinamento do Modelo

- Utilizamos o modelo YOLO para detecção de objetos
- Realizamos treinamentos com diferentes configurações de épocas: 30 e 60
- Comparamos os resultados de precisão, recall e mAP@0.5
- Análise detalhada de overfitting e desempenho do modelo

### 📈 Análise de Resultados

Os resultados da análise comparativa entre os modelos treinados com 30 e 60 épocas mostraram:

- O modelo com 30 épocas alcançou mAP@0.5 de 0,2105, superando o modelo de 60 épocas (0,1167) em 44,54%
- Precisão: o modelo de 30 épocas (0,2841) superou o de 60 épocas (0,1039) em 63,43%
- Recall: ambos os modelos obtiveram valores idênticos (0,2500)
- O treinamento estendido até 60 épocas resultou em overfitting

A análise completa está disponível no notebook Jupyter e no script Python dedicado à análise de resultados.

Para uma análise detalhada e recomendações técnicas, consulte o [Relatório de Análise Completo](results/comparison/analysis_summary.md). Este documento apresenta uma comparação aprofundada dos modelos, incluindo métricas de desempenho, visualizações das curvas de aprendizado, matrizes de confusão e recomendações específicas para melhorar o treinamento em trabalhos futuros.

---

### 🎥 Demonstração no YouTube

[Link para o vídeo demonstrativo do projeto](https://www.youtube.com/watch?v=seu-video-id)

Neste vídeo de 5 minutos, demonstramos o funcionamento do sistema de visão computacional com YOLO, incluindo o processo de treinamento, validação, teste e análise de resultados.

---

### 📁 Estrutura de Pastas

```
farm-tech-solutions-v6/
├── data/
│   ├── dataset.yaml (configuração do dataset)
│   ├── train/
│   │   ├── images/ (64 imagens)
│   │   └── labels/ (64 arquivos de rótulos)
│   ├── val/
│   │   ├── images/ (8 imagens)
│   │   └── labels/ (8 arquivos de rótulos)
│   └── test/
│       ├── images/ (8 imagens)
│       └── labels/ (8 arquivos de rótulos)
├── notebooks/
│   ├── GabrielRibeiro_rm560173_pbl_fase6.ipynb (notebook principal)
│   ├── GabrielRibeiro_rm560173_pbl_fase6.py (código Python exportado)
│   └── yolov5s.pt (modelo pré-treinado)
├── scripts/
│   ├── results_analysis.py (análise de resultados)
│   └── run_analysis.sh (script para execução da análise)
├── results/
│   ├── analysis/ (diretório para análises gerais)
│   └── comparison/ (resultados comparativos)
│       ├── analysis_output/ (gráficos e visualizações)
│       ├── analysis_summary.md (resumo da análise)
│       ├── comparison_report.md (relatório comparativo)
│       ├── train_e30_bs16_20250429_103607/ (resultados do treino com 30 épocas)
│       ├── train_e60_bs16_20250429_105247/ (resultados do treino com 60 épocas)
│       ├── val_best_20250429_112355/ (validação do modelo de 30 épocas)
│       └── val_best_20250429_112434/ (validação do modelo de 60 épocas)
├── .docs/
│   ├── tasks/ (tarefas do projeto)
│   ├── context.md (contexto do projeto)
│   ├── project.md (detalhes do projeto)
│   └── barema.md (critérios de avaliação)
└── requirements.txt (dependências do projeto)
```

---

### 🔧 Como Executar

#### Configuração Inicial

1. Clone este repositório:

   ```bash
   git clone https://github.com/FIAP-IA2024/farm-tech-solutions-v6.git
   cd farm-tech-solutions-v6
   ```

2. Crie e ative um ambiente virtual Python:

   - **Linux/macOS:**

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - **Windows:**

     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```

3. Instale as dependências Python:

   ```bash
   pip install -r requirements.txt
   ```

#### Executar o Script Python

Para treinar o modelo YOLO:

```bash
python scripts/GabrielRibeiro_rm560173_pbl_fase6.py --epochs 30 --batch-size 16
```

Para executar a análise de resultados:

```bash
bash scripts/run_analysis.sh
```

#### Executar o Jupyter Lab

Para executar o notebook Jupyter:

```bash
jupyter lab
```

Navegue até `notebooks/GabrielRibeiro_rm560173_pbl_fase6.ipynb` para visualizar a análise completa.

---

### 💻 Tecnologias Utilizadas

- **Linguagens de Programação:**
  - Python 3.x

- **Bibliotecas e Frameworks:**
  - PyTorch (framework para aprendizado de máquina)
  - YOLOv5 (detecção de objetos)
  - NumPy (computação numérica)
  - Pandas (análise de dados)
  - Matplotlib e Seaborn (visualização)
  - Jupyter (desenvolvimento interativo)
  
- **Ferramentas:**
  - Git e GitHub (controle de versão)
  - Make Sense IA (rotulação de imagens)
  - Google Colab (ambiente de execução na nuvem)

---

## **Entrega 2 - Comparação de Abordagens**

Na segunda entrega, comparamos diferentes abordagens para visão computacional:

1. **YOLO Customizado** (da Entrega 1)
2. **YOLO Tradicional**
3. **CNN Treinada do Zero**

A análise comparativa considera:

- Facilidade de uso e integração
- Precisão dos modelos
- Tempo de treinamento
- Velocidade de inferência

O notebook completo com a implementação e avaliação crítica está em desenvolvimento.

---

## 📋 Licença

Este projeto segue o modelo de licença da FIAP e está licenciado sob **Attribution 4.0 International**. Para mais informações, consulte o [MODELO GIT FIAP](https://github.com/agodoi/template).
