# Roteiro para Vídeo de Demonstração - Projeto Fase 6 FIAP

## Duração: até 5 minutos

---

## 0. Introdução (30 segundos)

**Fala:**
"Olá! Neste vídeo vou demonstrar o projeto da Fase 6 do curso de IA da FIAP. Este projeto consiste na implementação de um sistema de visão computacional utilizando o modelo YOLO para detecção de objetos."

**Mostrar na tela:** Tela inicial mostrando a página do GitHub do projeto (`farm-tech-solutions-v6/README.md`)

**Fala:**
"Aqui está o repositório do projeto. No arquivo README.md, contém todas as instruções necessárias para executar o projeto e obter os resultados. As boas práticas de versionamento com Git foram seguidas, e todo o processo está devidamente commitado."

---

## 1. Contextualização do Projeto (30 segundos)

**Fala:**
"Neste projeto, desenvolvemos um sistema de visão computacional utilizando o modelo YOLO para detectar dois objetos distintos: gatos e cachorros. A solução demonstra o potencial e a acurácia desta tecnologia através de treinamentos com diferentes configurações."

**Mostrar na tela:**

- Seção "Entregas do Projeto" do README
- Destacar as informações sobre a Entrega 1

---

## 2. Estrutura do Dataset (45 segundos)

**Fala:**
"Para treinar o modelo, organizei um dataset contendo 80 imagens, sendo 40 de gatos e 40 de cachorros. Estas imagens foram distribuídas da seguinte forma: 80% para treinamento, 10% para validação e 10% para testes, mantendo o equilíbrio entre as classes. Todas as imagens foram rotuladas utilizando a ferramenta Make Sense IA."

**Mostrar na tela:**

- Estrutura de pastas do dataset
- `farm-tech-solutions-v6/data`
- Arquivo de configuração do dataset
- `farm-tech-solutions-v6/data/dataset.yaml`
- Algumas imagens de exemplo de cada categoria com suas anotações

---

## 3. Implementação e Treinamento (60 segundos)

**Fala:**
"Para implementar a solução, desenvolvi um script Python que utiliza o modelo YOLOv5. Este script realiza o download e configuração do repositório YOLOv5, prepara o ambiente de treinamento, e executa o treinamento do modelo com os parâmetros definidos. Realizei dois treinamentos com diferentes configurações: um com 30 épocas e outro com 60 épocas, ambos com batch size de 16.

Para facilitar a comparação, o script possui uma opção `--compare` que automaticamente treina os dois modelos (30 e 60 épocas) e gera um relatório comparativo, possibilitando uma análise direta dos resultados."

**Mostrar na tela:**

- Script Python principal
- `farm-tech-solutions-v6/notebooks/GabrielRibeiro_rm560173_pbl_fase6.py`
- Notebook Jupyter
- `farm-tech-solutions-v6/notebooks/GabrielRibeiro_rm560173_pbl_fase6.ipynb`
- Comandos de execução do script:
- `python notebooks/GabrielRibeiro_rm560173_pbl_fase6.py --epochs 30 --batch-size 16`
- `python notebooks/GabrielRibeiro_rm560173_pbl_fase6.py --compare`

---

## 4. Análise de Resultados (75 segundos)

**Fala:**
"Após o treinamento, realizei uma análise comparativa detalhada entre os modelos treinados com 30 e 60 épocas. Os resultados mostraram que o modelo com 30 épocas teve um desempenho significativamente melhor, com um mAP@0.5 de 0,21 contra 0,12 do modelo com 60 épocas. A precisão do modelo de 30 épocas foi de 0,28, superior aos 0,10 do modelo com 60 épocas. Observei que o treinamento estendido até 60 épocas resultou em overfitting, onde o modelo se especializou demais nos dados de treinamento, perdendo capacidade de generalização."

**Mostrar na tela:**

- Resultados da análise comparativa
- `farm-tech-solutions-v6/results/comparison/analysis_summary.md`
- Gráficos de comparação de métricas
- `farm-tech-solutions-v6/results/comparison/analysis_output/` (gráficos relevantes)
- Matrizes de confusão dos dois modelos

---

## 5. Demonstração do Modelo em Ação (45 segundos)

**Fala:**
"Agora, vou mostrar o modelo em ação. Utilizando o modelo treinado com 30 épocas, realizei testes em imagens que não foram utilizadas durante o treinamento. Como podemos observar, o modelo é capaz de detectar e classificar corretamente os objetos, demonstrando sua eficácia na tarefa de visão computacional."

**Mostrar na tela:**

- Execução do script de teste
- Exemplos de imagens processadas pelo modelo
- `farm-tech-solutions-v6/results/comparison/val_best_20250429_112355/` (resultados de validação)

---

## 6. Conclusões e Recomendações (30 segundos)

**Fala:**
"Com base nos resultados obtidos, concluímos que o modelo treinado com 30 épocas apresenta o melhor desempenho para esta aplicação. Recomendamos a implementação de técnicas de aumento de dados e regularização para melhorar ainda mais a robustez do modelo em trabalhos futuros. Além disso, a implementação de parada antecipada baseada em métricas de validação pode otimizar o tempo de treinamento."

**Mostrar na tela:**

- Recomendações baseadas na análise de resultados
- Seção de conclusões do relatório

---

## 7. Encerramento (30 segundos)

**Fala:**
"Este projeto demonstra o potencial da visão computacional utilizando o modelo YOLO para detecção de objetos. Os resultados obtidos mostram que é possível obter bons desempenhos mesmo com conjuntos de dados relativamente pequenos, desde que o treinamento seja realizado de forma adequada. Todo o código e documentação estão disponíveis no repositório GitHub do nosso grupo. Obrigado pela atenção!"

**Mostrar na tela:**

- Página do GitHub do projeto
- `farm-tech-solutions-v6/README.md`
- Destaque para as tecnologias utilizadas
