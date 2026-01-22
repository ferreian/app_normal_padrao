# 📊 Calculadora de Distribuição Normal Padrão

Aplicação interativa desenvolvida em **Streamlit** para resolver exercícios de probabilidade utilizando a distribuição normal padrão Z ~ N(0,1).

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🎯 Funcionalidades

- ✅ **Entrada Manual de Dados**: Calcule probabilidades personalizadas entrando com seus próprios valores de Z
- ✅ **Visualização Interativa**: Gráficos interativos em Plotly com zoom, pan e hover
- ✅ **Exportação de Figuras**: Salve gráficos em PNG, SVG, JPEG ou WebP com um clique
- ✅ **13 Exercícios Pré-configurados**: Visualize todos os exercícios da lista com soluções completas
- ✅ **Explicações Detalhadas**: Entenda o passo a passo de cada cálculo
- ✅ **Interface Intuitiva**: Design limpo e fácil de usar

## 📸 Tipos de Probabilidade Suportados

A aplicação calcula três tipos de probabilidades:

1. **P(Z > a)** - Probabilidade de Z ser maior que um valor
2. **P(Z < a)** - Probabilidade de Z ser menor que um valor
3. **P(a < Z < b)** - Probabilidade de Z estar entre dois valores

## 🚀 Como Usar

### Instalação

1. **Clone ou baixe os arquivos do projeto**

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Execute a aplicação:**
```bash
streamlit run app_normal_padrao.py
```

4. **Acesse no navegador:**
   - A aplicação abrirá automaticamente em `http://localhost:8501`

### Uso da Aplicação

#### Modo 1: Entrada Manual de Dados
1. Selecione "**Entrada Manual de Dados**" no menu lateral
2. Escolha o tipo de probabilidade desejado
3. Entre com os valores de Z
4. Visualize o gráfico e o resultado instantaneamente!

#### Modo 2: Ver Todos os Exercícios
- Visualize todos os 13 exercícios da lista com gráficos e soluções

#### Modo 3: Explorar Item Individual
- Selecione um exercício específico para ver detalhes completos

### 📥 Como Salvar Figuras

1. Passe o mouse sobre qualquer gráfico
2. Clique no ícone da **câmera 📷** no canto superior direito
3. Escolha o formato desejado (PNG, SVG, JPEG, WebP)
4. A imagem será baixada automaticamente!

## 📋 Exercícios Incluídos

A aplicação resolve os seguintes exercícios:

1. P(Z > -1,25)
2. P(-1,5 < Z < 2,53)
3. P(-0,75 < Z < 1)
4. P(-0,98 < Z < -0,75)
5. P(0,5 < Z < 1)
6. P(Z < 1,72)
7. P(Z > -1,96)
8. P(-2,02 < Z < -0,52)
9. P(Z < -1,24)
10. P(Z > 1,12)
11. P(-1 < Z < 1)
12. P(-2 < Z < 2)
13. P(-3 < Z < 3)

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Streamlit** - Framework para aplicações web interativas
- **Plotly** - Visualizações interativas e exportação de gráficos
- **SciPy** - Cálculos estatísticos da distribuição normal
- **NumPy** - Operações numéricas
- **Pandas** - Manipulação e apresentação de dados

## 📦 Dependências

```
streamlit>=1.28.0
numpy>=1.24.0
plotly>=5.17.0
scipy>=1.11.0
pandas>=2.0.0
```

## 💡 Recursos Interativos

### Gráficos Plotly
- **Zoom**: Arraste para selecionar área
- **Pan**: Mova o gráfico
- **Hover**: Veja valores exatos ao passar o mouse
- **Reset**: Botão para voltar à visualização original
- **Download**: Exporte em vários formatos

### Interface Streamlit
- Navegação por abas no menu lateral
- Inputs numéricos com validação
- Métricas visuais (probabilidade, percentual, complemento)
- Expansores para explicações detalhadas

## 📚 Conceitos Estatísticos

### Distribuição Normal Padrão
- Média (μ) = 0
- Desvio padrão (σ) = 1
- Notação: Z ~ N(0,1)

### Regra Empírica
- **P(-1 < Z < 1) ≈ 68%** - 68% dos dados dentro de 1 desvio padrão
- **P(-2 < Z < 2) ≈ 95%** - 95% dos dados dentro de 2 desvios padrão
- **P(-3 < Z < 3) ≈ 99.7%** - 99.7% dos dados dentro de 3 desvios padrão

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação
- Enviar pull requests

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.

## 👨‍💻 Autor

Desenvolvido para auxiliar no aprendizado de estatística e probabilidade.

## 📞 Suporte

Se encontrar problemas ou tiver dúvidas:
1. Verifique se todas as dependências estão instaladas
2. Certifique-se de estar usando Python 3.8 ou superior
3. Consulte a documentação do Streamlit em https://docs.streamlit.io

## 🎓 Uso Educacional

Esta aplicação foi desenvolvida como ferramenta educacional para:
- Estudantes de estatística
- Professores de probabilidade
- Pesquisadores que trabalham com análise de dados
- Qualquer pessoa interessada em entender a distribuição normal

---

**Desenvolvido com ❤️ usando Python e Streamlit**

*Última atualização: Janeiro 2026*
