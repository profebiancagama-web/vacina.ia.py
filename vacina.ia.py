import streamlit as st
import time
import random

# --- CONFIGURAÇÃO DA TELA ---
st.set_page_config(page_title="Olegario TechBio IA", page_icon="🧬", layout="wide")

# CSS para deixar o visual ultra profissional e futurista (Estilo Dark Mode)
st.markdown(
    """
    <style>
    .reportview-container { background: #0e1117; }
    .stMetric { background-color: #1e293b; padding: 15px; border-radius: 10px; border: 1px solid #10b981; }
    .titulo-ia { font-family: 'Courier New', monospace; color: #10b981; font-weight: bold; }
    .status-box { padding: 20px; background-color: #111827; border-radius: 8px; border-left: 5px solid #10b981; }
    .obs-box { padding: 15px; background-color: #1e1b4b; border-radius: 8px; border-left: 5px solid #6366f1; margin-top: 15px; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='titulo-ia'>🧬 OLEGARIO TECHBIO IA // Centro de Biointeligência</h1>", unsafe_allow_html=True)
st.write("Plataforma de computação avançada para cruzamento de patógenos e síntese automatizada de imunizantes.")
st.write("---")

# --- BANCO DE DADOS INTERNO DE PATÓGENOS (Com o novo vírus ácido) ---
banco_dados_virus = {
    "Vírus Acidófilo Gástrico VAG-26": {
        "tipo": "Encapsulado de Alta Resistência", 
        "proteina_alvo": "Enzima de Ativação por Prótons (H+)", 
        "base_dados": "Isolamento Recente #0026",
        "mecanismo": "Se alimenta do meio ácido estomacal. Quanto mais ácido o pH, mais rápido ele se replica e se fortalece. A neutralização da acidez destrói seu capsídeo lipídico."
    },
    "Influenza H5N1 Mutada": {
        "tipo": "RNA fita simples", 
        "proteina_alvo": "Hemaglutinina H5", 
        "base_dados": "NCBI-GenBank #4412",
        "mecanismo": "Transmissão respiratória com mutação na espícula de ligação."
    },
    "Sars-CoV-3 (Variante Ômicron-X)": {
        "tipo": "RNA envelopado", 
        "proteina_alvo": "Spike Glycoprotein S1", 
        "base_dados": "GISAID ID-9982",
        "mecanismo": "Alta taxa de evasão imune em receptores ACE2."
    }
}

# --- PAINEL LATERAL DE PARÂMETROS ---
st.sidebar.header("🔬 Parâmetros do Laboratório")
tecnologia_vacina = st.sidebar.selectbox("Plataforma Tecnológica:", ["RNA Mensageiro (mRNA)", "Vetor Viral Não-Replicante", "Subunidade Proteica Recombinante", "Vírus Inativado"])
foco_anticorpos = st.sidebar.slider("Nível de Rigor de Afinidade Molecular:", 80, 100, 95)

# --- CORPO PRINCIPAL ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("1. Seleção do Patógeno")
    doenca_selecionada = st.selectbox("Escolha a doença/cepa para análise:", list(banco_dados_virus.keys()))
    
    st.write("### 📂 Dados Cruzados (Banco Interno):")
    st.info(f"""
    * **Classificação:** {banco_dados_virus[doenca_selecionada]['tipo']}
    * **Alvo de Neutralização:** {banco_dados_virus[doenca_selecionada]['proteina_alvo']}
    * **Registro no Banco Geral:** {banco_dados_virus[doenca_selecionada]['base_dados']}
    """)
    
    # Exibe o aviso especial se o vírus ácido for selecionado
    if doenca_selecionada == "Vírus Acidófilo Gástrico VAG-26":
        st.warning(f"⚠️ **Mecanismo Patogênico:** {banco_dados_virus[doenca_selecionada]['mecanismo']}")
    
    botao_gerar = st.button("🚀 INICIAR SÍNTESE COMPUTACIONAL", use_container_width=True)

with col2:
    st.subheader("2. Terminal de Processamento da IA")
    
    if botao_gerar:
        status_texto = st.empty()
        progresso_barra = st.progress(0)
        
        status_texto.markdown("🔍 **[FASE 1]** Olegario TechBio IA acessando banco estrutural e isolando fita do patógeno...")
        for i in range(1, 35):
            time.sleep(0.04)
            progresso_barra.progress(i)
            
        status_texto.markdown("💻 **[FASE 2]** Calculando índice de pH... Simulando a neutralização do ambiente ácido...")
        for i in range(35, 75):
            time.sleep(0.05)
            progresso_barra.progress(i)
            
        status_texto.markdown("🧪 **[FASE 3]** Injetando agentes alcalinos e gerando fórmula estabilizada do imunizante...")
        for i in range(75, 101):
            time.sleep(0.03)
            progresso_barra.progress(i)
            
        status_texto.success("✨ SÍNTESE CONCLUÍDA COM SUCESSO PELA OLEGARIO TECHBIO IA!")
        
        st.markdown("<div class='status-box'><h3>📋 Relatório Técnico do Imunizante Desenvolvido</h3></div>", unsafe_allow_html=True)
        st.write(" ")
        
        # Métricas científicas
        eficacia = round(random.uniform(96.5, 99.8), 2) if doenca_selecionada == "Vírus Acidófilo Gástrico VAG-26" else round(random.uniform(94.1, 98.2), 2)
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric(label="Eficácia de Neutralização", value=f"{eficacia}%", delta="+2.1% Estabilidade")
        with m2:
            st.metric(label="Índice de Alcalinização", value="pH 7.4 (Neutro)", delta="Alvo Destruído")
        with m3:
            st.metric(label="Código do Lote", value=f"OLG-{random.randint(1000,9999)}", delta="Aprovado")
            
        st.write("### 🧪 Estrutura Molecular do Imunizante:")
        
        # Se for o nosso vírus gástrico, exibe a estrutura com os compostos corretos
        if doenca_selecionada == "Vírus Acidófilo Gástrico VAG-26":
            st.success(f"""
            * **Base Ativa Primária:** Bicarbonato de Potássio [KHCO₃] *(Agente bloqueador de prótons)*
            * **Co-Adjuvante Patenteado:** Complexo Bio-Alcalino Alkilox-9
            * **Mecanismo de Ação:** O complexo quebra a barreira ácida protetora do vírus, cortando sua fonte de energia e desintegrando a estrutura viral instantaneamente.
            """)
        else:
            st.success(f"""
            * **Tipo Final:** Vacina de {tecnologia_vacina} direcionada contra *{banco_dados_virus[doenca_selecionada]['proteina_alvo']}*.
            * **Adjuvante Geral:** Fosfato de Alumínio Nanoparticulado.
            """)
            
        # --- OBSERVAÇÃO CRÍTICA DE TESTE EM LABORATÓRIO (MUDANÇA DE COR) ---
        st.markdown(
            """
            <div class='obs-box'>
                <h4>🔬 DIRETRIZ DE VERIFICAÇÃO CLÍNICA (VALIDAÇÃO DE SUCESSO)</h4>
                <p><strong>Protocolo de Teste Visual:</strong> Insira a amostra do patógeno no tubo de ensaio reativo. 
                Se o líquido estiver originalmente <b>VERMELHO</b> (indicando alta acidez e infecção ativa) e, 
                após a adição das estruturas do imunizante, o líquido mudar de cor mudando o pH, significa que 
                a <b>vacina obteve sucesso absoluto</b> na neutralização celular.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        st.balloons()
        
    else:
        st.info("🔬 Sistema pronto. Selecione o patógeno e clique no botão para iniciar os cruzamentos genéticos.")
