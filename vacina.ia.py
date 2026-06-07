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
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='titulo-ia'>🧬 OLEGARIO TECHBIO IA // Centro de Biointeligência</h1>", unsafe_allow_html=True)
st.write("Plataforma de computação avançada para cruzamento de patógenos e síntese automatizada de imunizantes.")
st.write("---")

# --- BANCO DE DADOS INTERNO DE PATÓGENOS ---
banco_dados_virus = {
    "Influenza H5N1 Mutada": {"tipo": "RNA fita simples", "proteina_alvo": "Hemaglutinina H5", "base_dados": "NCBI-GenBank #4412"},
    "Sars-CoV-3 (Variante Ômicron-X)": {"tipo": "RNA envelopado", "proteina_alvo": "Spike Glycoprotein S1", "base_dados": "GISAID ID-9982"},
    "Superbactéria KPC-26": {"tipo": "Plasmídeo bacteriano", "proteina_alvo": "Carbapenemase KPC", "base_dados": "UniProtKB #P621"},
    "Novo Patógeno Desconhecido (Amostra X)": {"tipo": "Desconhecido (Sequenciando...)", "proteina_alvo": "Glicoproteína de Membrana", "base_dados": "Análise Isolada Local"}
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
    
    botao_gerar = st.button("🚀 INICIAR SÍNTESE COMPUTACIONAL", use_container_width=True)

with col2:
    st.subheader("2. Terminal de Processamento da IA")
    
    if botao_gerar:
        status_texto = st.empty()
        progresso_barra = st.progress(0)
        
        status_texto.markdown("🔍 **[FASE 1]** Olegario TechBio IA acessando banco estrutural e mapeando capsídeo...")
        for i in range(1, 35):
            time.sleep(0.04)
            progresso_barra.progress(i)
            
        status_texto.markdown("💻 **[FASE 2]** Cruzando informações genéticas... Simulando encaixe químico no receptor celular...")
        for i in range(35, 75):
            time.sleep(0.05)
            progresso_barra.progress(i)
            
        status_texto.markdown("🧪 **[FASE 3]** Modelando fórmula de estabilização e finalizando imunizante...")
        for i in range(75, 101):
            time.sleep(0.03)
            progresso_barra.progress(i)
            
        status_texto.success("✨ PROCESSO CONCLUÍDO COM SUCESSO PELA OLEGARIO TECHBIO IA!")
        
        st.markdown("<div class='status-box'><h3>📋 Relatório Técnico da Vacina Desenvolvida</h3></div>", unsafe_allow_html=True)
        st.write(" ")
        
        # Gera dados aleatórios na hora para simular a resposta da IA
        eficacia = round(random.uniform(94.1, 99.2), 2)
        mutacao_res = random.randint(88, 99)
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric(label="Eficácia Projetada (In Vitro)", value=f"{eficacia}%", delta="+1.5% vs Placebo")
        with m2:
            st.metric(label="Estabilidade Molecular", value="99.67%", delta="Estável")
        with m3:
            st.metric(label="Resistência a Mutações", value=f"{mutacao_res}%", delta="Alta Cobertura")
            
        st.write("### 🧪 Estrutura do Imunizante:")
        st.success(f"""
        * **Tipo Final:** Vacina de {tecnologia_vacina} direcionada contra a proteína *{banco_dados_virus[doenca_selecionada]['proteina_alvo']}*.
        * **Adjuvante Utilizado:** Fosfato de Alumínio Estabilizado com Nanopartículas.
        * **Código de lote gerado:** `OLG-{random.randint(1000,9999)}-{tecnologia_vacina[:4].upper()}`
        * *Imunizante pronto para simulações de testes biológicos de Fase I.*
        """)
        st.balloons()
        
    else:
        st.info("Aguardando comando... Clique no botão à esquerda para acionar os motores da IA e cruzar os dados.")
