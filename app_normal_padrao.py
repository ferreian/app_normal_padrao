import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Distribuição Normal Padrão - Exercícios",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Distribuição Normal Padrão Z ~ N(0,1)")
st.markdown("### Resolução de Exercícios - Cálculo de Probabilidades")

# Função para plotar a distribuição normal com área sombreada usando Plotly
def plot_normal_distribution(lower=-np.inf, upper=np.inf, title="", prob=0):
    # Criar o intervalo x
    x = np.linspace(-4, 4, 1000)
    y = stats.norm.pdf(x, 0, 1)
    
    # Criar figura
    fig = go.Figure()
    
    # Adicionar a curva normal
    fig.add_trace(go.Scatter(
        x=x, 
        y=y,
        mode='lines',
        name='Z ~ N(0,1)',
        line=dict(color='blue', width=3),
        hovertemplate='Z = %{x:.2f}<br>Densidade = %{y:.4f}<extra></extra>'
    ))
    
    # Preparar área sombreada
    if lower == -np.inf:
        x_fill = x[x <= upper]
    elif upper == np.inf:
        x_fill = x[x >= lower]
    else:
        x_fill = x[(x >= lower) & (x <= upper)]
    
    y_fill = stats.norm.pdf(x_fill, 0, 1)
    
    # Adicionar área sombreada
    fig.add_trace(go.Scatter(
        x=x_fill,
        y=y_fill,
        fill='tozeroy',
        mode='none',
        name=f'Área = {prob:.4f}',
        fillcolor='rgba(255, 0, 0, 0.3)',
        hovertemplate='Z = %{x:.2f}<br>Densidade = %{y:.4f}<extra></extra>'
    ))
    
    # Adicionar linhas verticais nos pontos de corte
    if lower != -np.inf:
        fig.add_vline(
            x=lower, 
            line_dash="dash", 
            line_color="green",
            line_width=2,
            annotation_text=f"z = {lower:.2f}",
            annotation_position="bottom"
        )
    
    if upper != np.inf:
        fig.add_vline(
            x=upper, 
            line_dash="dash", 
            line_color="green",
            line_width=2,
            annotation_text=f"z = {upper:.2f}",
            annotation_position="bottom"
        )
    
    # Configurar layout
    fig.update_layout(
        title={
            'text': title,
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16, 'weight': 'bold'}
        },
        xaxis_title='Valores de Z',
        yaxis_title='Densidade de Probabilidade',
        hovermode='x unified',
        showlegend=True,
        width=800,
        height=500,
        template='plotly_white',
        xaxis=dict(
            gridcolor='lightgray',
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='black'
        ),
        yaxis=dict(
            gridcolor='lightgray',
            range=[0, 0.45]
        ),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        )
    )
    
    return fig

# Função para calcular probabilidades
def calcular_prob(tipo, z1=None, z2=None):
    if tipo == "maior":
        prob = 1 - stats.norm.cdf(z1)
        return prob, z1, np.inf
    elif tipo == "menor":
        prob = stats.norm.cdf(z1)
        return prob, -np.inf, z1
    elif tipo == "entre":
        prob = stats.norm.cdf(z2) - stats.norm.cdf(z1)
        return prob, z1, z2
    return 0, 0, 0

# Definir os exercícios
exercicios = {
    "1": {"desc": "P(Z > -1,25)", "tipo": "maior", "z1": -1.25},
    "2": {"desc": "P(-1,5 < Z < 2,53)", "tipo": "entre", "z1": -1.5, "z2": 2.53},
    "3": {"desc": "P(-0,75 < Z < 1)", "tipo": "entre", "z1": -0.75, "z2": 1},
    "4": {"desc": "P(-0,98 < Z < -0,75)", "tipo": "entre", "z1": -0.98, "z2": -0.75},
    "5": {"desc": "P(0,5 < Z < 1)", "tipo": "entre", "z1": 0.5, "z2": 1},
    "6": {"desc": "P(Z < 1,72)", "tipo": "menor", "z1": 1.72},
    "7": {"desc": "P(Z > -1,96)", "tipo": "maior", "z1": -1.96},
    "8": {"desc": "P(-2,02 < Z < -0,52)", "tipo": "entre", "z1": -2.02, "z2": -0.52},
    "9": {"desc": "P(Z < -1,24)", "tipo": "menor", "z1": -1.24},
    "10": {"desc": "P(Z > 1,12)", "tipo": "maior", "z1": 1.12},
    "11": {"desc": "P(-1 < Z < 1)", "tipo": "entre", "z1": -1, "z2": 1},
    "12": {"desc": "P(-2 < Z < 2)", "tipo": "entre", "z1": -2, "z2": 2},
    "13": {"desc": "P(-3 < Z < 3)", "tipo": "entre", "z1": -3, "z2": 3},
}

# Sidebar para navegação
st.sidebar.header("Navegação")
modo = st.sidebar.radio(
    "Escolha o modo:",
    ["Entrada Manual de Dados", "Ver Todos os Exercícios", "Explorar Item Individual"]
)

if modo == "Entrada Manual de Dados":
    st.markdown("---")
    st.subheader("✏️ Entre com seus Dados")
    
    st.markdown("""
    Escolha o tipo de probabilidade que deseja calcular e entre com os valores de Z.
    A aplicação irá gerar automaticamente o gráfico e calcular a probabilidade!
    """)
    
    # Seletor de tipo de probabilidade
    tipo_prob = st.selectbox(
        "Tipo de Probabilidade:",
        ["P(Z > a) - Probabilidade maior que um valor",
         "P(Z < a) - Probabilidade menor que um valor", 
         "P(a < Z < b) - Probabilidade entre dois valores"]
    )
    
    st.markdown("---")
    
    # Inputs baseados no tipo selecionado
    if "maior que" in tipo_prob:
        col1, col2 = st.columns([1, 2])
        with col1:
            z_valor = st.number_input(
                "Valor de Z (a):",
                value=-1.25,
                step=0.01,
                format="%.2f"
            )
        
        # Calcular
        prob, lower, upper = calcular_prob("maior", z_valor)
        
        with col2:
            st.markdown("### Resultado")
            st.success(f"**P(Z > {z_valor:.2f}) = {prob:.4f}**")
            st.info(f"**Percentual: {prob*100:.2f}%**")
        
        # Gráfico
        st.markdown("### 📊 Visualização")
        fig = plot_normal_distribution(lower, upper, f"P(Z > {z_valor:.2f})", prob)
        st.plotly_chart(fig, use_container_width=True)
        
        # Explicação
        with st.expander("📝 Ver Explicação do Cálculo"):
            st.markdown(f"""
            Para calcular **P(Z > {z_valor:.2f})**:
            - Usamos: P(Z > {z_valor:.2f}) = 1 - P(Z ≤ {z_valor:.2f})
            - P(Z ≤ {z_valor:.2f}) = {stats.norm.cdf(z_valor):.4f}
            - P(Z > {z_valor:.2f}) = 1 - {stats.norm.cdf(z_valor):.4f} = **{prob:.4f}**
            
            A área sombreada em vermelho representa a probabilidade calculada.
            """)
    
    elif "menor que" in tipo_prob:
        col1, col2 = st.columns([1, 2])
        with col1:
            z_valor = st.number_input(
                "Valor de Z (a):",
                value=1.72,
                step=0.01,
                format="%.2f"
            )
        
        # Calcular
        prob, lower, upper = calcular_prob("menor", z_valor)
        
        with col2:
            st.markdown("### Resultado")
            st.success(f"**P(Z < {z_valor:.2f}) = {prob:.4f}**")
            st.info(f"**Percentual: {prob*100:.2f}%**")
        
        # Gráfico
        st.markdown("### 📊 Visualização")
        fig = plot_normal_distribution(lower, upper, f"P(Z < {z_valor:.2f})", prob)
        st.plotly_chart(fig, use_container_width=True)
        
        # Explicação
        with st.expander("📝 Ver Explicação do Cálculo"):
            st.markdown(f"""
            Para calcular **P(Z < {z_valor:.2f})**:
            - Usamos diretamente a função de distribuição acumulada (CDF)
            - P(Z < {z_valor:.2f}) = **{prob:.4f}**
            
            A área sombreada em vermelho representa a probabilidade calculada.
            """)
    
    else:  # entre dois valores
        col1, col2 = st.columns(2)
        with col1:
            z_inferior = st.number_input(
                "Valor inferior de Z (a):",
                value=-1.5,
                step=0.01,
                format="%.2f"
            )
        with col2:
            z_superior = st.number_input(
                "Valor superior de Z (b):",
                value=2.53,
                step=0.01,
                format="%.2f"
            )
        
        # Validação
        if z_inferior >= z_superior:
            st.error("⚠️ O valor inferior deve ser menor que o valor superior!")
        else:
            # Calcular
            prob, lower, upper = calcular_prob("entre", z_inferior, z_superior)
            
            # Resultados
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("P(a < Z < b)", f"{prob:.4f}")
            with col2:
                st.metric("Percentual", f"{prob*100:.2f}%")
            with col3:
                st.metric("Complemento", f"{(1-prob):.4f}")
            
            # Gráfico
            st.markdown("### 📊 Visualização")
            fig = plot_normal_distribution(lower, upper, f"P({z_inferior:.2f} < Z < {z_superior:.2f})", prob)
            st.plotly_chart(fig, use_container_width=True)
            
            # Explicação
            with st.expander("📝 Ver Explicação do Cálculo"):
                st.markdown(f"""
                Para calcular **P({z_inferior:.2f} < Z < {z_superior:.2f})**:
                - Usamos: P({z_inferior:.2f} < Z < {z_superior:.2f}) = P(Z < {z_superior:.2f}) - P(Z < {z_inferior:.2f})
                - P(Z < {z_superior:.2f}) = {stats.norm.cdf(z_superior):.4f}
                - P(Z < {z_inferior:.2f}) = {stats.norm.cdf(z_inferior):.4f}
                - P({z_inferior:.2f} < Z < {z_superior:.2f}) = {stats.norm.cdf(z_superior):.4f} - {stats.norm.cdf(z_inferior):.4f} = **{prob:.4f}**
                
                A área sombreada em vermelho representa a probabilidade calculada.
                """)
    
    # Dicas adicionais
    st.markdown("---")
    st.markdown("### 💡 Dicas")
    col1, col2 = st.columns(2)
    with col1:
        st.info("""
        **Valores importantes:**
        - P(-1 < Z < 1) ≈ 68%
        - P(-2 < Z < 2) ≈ 95%
        - P(-3 < Z < 3) ≈ 99.7%
        """)
    with col2:
        st.success("""
        **Interpretação:**
        - Área sombreada = probabilidade
        - Quanto maior a área, maior a chance
        - Total da área sob a curva = 1
        """)

elif modo == "Ver Todos os Exercícios":
    st.markdown("---")
    st.subheader("📋 Resumo de Todos os Exercícios")
    
    # Criar tabela com todos os resultados
    resultados = []
    for num, ex in exercicios.items():
        if ex["tipo"] == "entre":
            prob, lower, upper = calcular_prob(ex["tipo"], ex["z1"], ex["z2"])
        else:
            prob, lower, upper = calcular_prob(ex["tipo"], ex["z1"])
        
        resultados.append({
            "Item": num,
            "Probabilidade": ex["desc"],
            "Resultado": f"{prob:.4f}",
            "Percentual": f"{prob*100:.2f}%"
        })
    
    df = pd.DataFrame(resultados)
    st.dataframe(df, hide_index=True, use_container_width=True)
    
    st.markdown("---")
    st.subheader("📊 Visualizações de Cada Item")
    
    # Mostrar cada exercício em colunas
    for i in range(0, len(exercicios), 2):
        col1, col2 = st.columns(2)
        
        # Coluna 1
        if i < len(exercicios):
            with col1:
                num = str(i + 1)
                ex = exercicios[num]
                
                if ex["tipo"] == "entre":
                    prob, lower, upper = calcular_prob(ex["tipo"], ex["z1"], ex["z2"])
                else:
                    prob, lower, upper = calcular_prob(ex["tipo"], ex["z1"])
                
                st.markdown(f"**Item {num}: {ex['desc']}**")
                fig = plot_normal_distribution(lower, upper, f"Item {num}: {ex['desc']}", prob)
                st.plotly_chart(fig, use_container_width=True)
                st.info(f"**Resposta: {prob:.4f}** ({prob*100:.2f}%)")
        
        # Coluna 2
        if i + 1 < len(exercicios):
            with col2:
                num = str(i + 2)
                ex = exercicios[num]
                
                if ex["tipo"] == "entre":
                    prob, lower, upper = calcular_prob(ex["tipo"], ex["z1"], ex["z2"])
                else:
                    prob, lower, upper = calcular_prob(ex["tipo"], ex["z1"])
                
                st.markdown(f"**Item {num}: {ex['desc']}**")
                fig = plot_normal_distribution(lower, upper, f"Item {num}: {ex['desc']}", prob)
                st.plotly_chart(fig, use_container_width=True)
                st.info(f"**Resposta: {prob:.4f}** ({prob*100:.2f}%)")

else:  # Explorar Item Individual
    st.markdown("---")
    item_selecionado = st.sidebar.selectbox(
        "Selecione o item:",
        options=list(exercicios.keys()),
        format_func=lambda x: f"Item {x}: {exercicios[x]['desc']}"
    )
    
    ex = exercicios[item_selecionado]
    
    st.subheader(f"📌 Item {item_selecionado}: {ex['desc']}")
    
    # Calcular probabilidade
    if ex["tipo"] == "entre":
        prob, lower, upper = calcular_prob(ex["tipo"], ex["z1"], ex["z2"])
    else:
        prob, lower, upper = calcular_prob(ex["tipo"], ex["z1"])
    
    # Criar três colunas
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Probabilidade", f"{prob:.4f}")
    with col2:
        st.metric("Percentual", f"{prob*100:.2f}%")
    with col3:
        st.metric("Complemento", f"{(1-prob):.4f}")
    
    # Mostrar gráfico
    st.markdown("### Visualização Gráfica")
    fig = plot_normal_distribution(lower, upper, f"{ex['desc']}", prob)
    st.plotly_chart(fig, use_container_width=True)
    
    # Explicação detalhada
    st.markdown("### 📝 Explicação do Cálculo")
    
    if ex["tipo"] == "maior":
        st.markdown(f"""
        Para calcular **P(Z > {ex['z1']})**:
        - Usamos: P(Z > {ex['z1']}) = 1 - P(Z ≤ {ex['z1']})
        - P(Z ≤ {ex['z1']}) = {stats.norm.cdf(ex['z1']):.4f}
        - P(Z > {ex['z1']}) = 1 - {stats.norm.cdf(ex['z1']):.4f} = **{prob:.4f}**
        """)
    elif ex["tipo"] == "menor":
        st.markdown(f"""
        Para calcular **P(Z < {ex['z1']})**:
        - Usamos diretamente a função de distribuição acumulada (CDF)
        - P(Z < {ex['z1']}) = **{prob:.4f}**
        """)
    else:  # entre
        st.markdown(f"""
        Para calcular **P({ex['z1']} < Z < {ex['z2']})**:
        - Usamos: P({ex['z1']} < Z < {ex['z2']}) = P(Z < {ex['z2']}) - P(Z < {ex['z1']})
        - P(Z < {ex['z2']}) = {stats.norm.cdf(ex['z2']):.4f}
        - P(Z < {ex['z1']}) = {stats.norm.cdf(ex['z1']):.4f}
        - P({ex['z1']} < Z < {ex['z2']}) = {stats.norm.cdf(ex['z2']):.4f} - {stats.norm.cdf(ex['z1']):.4f} = **{prob:.4f}**
        """)

# Informações adicionais no sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ Sobre")
st.sidebar.info("""
Esta aplicação resolve exercícios de probabilidade usando a distribuição normal padrão Z ~ N(0,1).

**Recursos:**
- Cálculo automático de probabilidades
- Visualização interativa com Plotly
- Área sombreada correspondente à probabilidade
- Explicações detalhadas dos cálculos
- **Exportação fácil de figuras** (PNG, SVG, etc)
""")

st.sidebar.markdown("---")
st.sidebar.success("💡 **Dica:** Passe o mouse sobre o gráfico para ver opções de zoom, pan e **download**!")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📥 Como Salvar Figuras")
st.sidebar.markdown("""
1. Passe o mouse sobre o gráfico
2. Clique no ícone da câmera 📷
3. Escolha o formato desejado
4. A imagem será baixada!
""")
