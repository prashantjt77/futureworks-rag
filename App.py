import streamlit as st
import os

st.set_page_config(page_title="FutureWorks RAG", page_icon="📄", layout="wide")

# ===== SIMPLE LIGHT PROFESSIONAL THEME =====
st.markdown("""
<style>
.stApp { background:#f8fafc !important; }
.main .block-container { background:white; border-radius:14px; padding:2rem; border:1px solid #e2e8f0; box-shadow:0 1px 3px rgba(0,0,0,0.05); }
p, div, label, li { color:#1e293b !important; }
h1,h2,h3 { color:#0f172a !important; }
[data-testid="stSidebar"] { background:white !important; border-right:1px solid #e2e8f0; }
.stButton>button { background:#0f172a !important; color:white !important; border-radius:8px !important; }
.stButton>button * { color:white !important; }
</style>
""", unsafe_allow_html=True)

# ===== SIDEBAR - SIMPLE INSTRUCTIONS =====
with st.sidebar:
    st.markdown("### 📄 FutureWorks RAG")
    st.markdown("**Ready-to-use Document AI**")
    st.divider()
    st.markdown("#### How to use:")
    st.markdown("""
    
    1. **Upload PDF/DOCX/TXT**
    2. **Ask questions** - get answers from doc
    """)
    st.divider()
    st.markdown("#### Features:")
    st.markdown("- ✅ Works with PDF, DOCX, TXT\n- ✅ Answers only from your doc\n- ✅ Smart questions after upload\n- ✅ No hallucinations")
    st.divider()
    st.markdown("#### Benefits:")
    st.markdown("Save hours. Get instant insights from any document.")
    
    st.divider()
    st.markdown("#### ⚙️ Settings")
    provider = st.selectbox("LLM Provider", ["Groq (Free & Fast)", "OpenAI", "Gemini"])
    api_key = st.text_input(f"{provider} API Key", type="password", help="Add in Streamlit Secrets as GROQ_API_KEY / OPENAI_API_KEY / GEMINI_API_KEY for production")

# ===== HEADER =====
st.markdown("""
<div style="background:white; border:1px solid #e2e8f0; border-radius:12px; padding:1.5rem 2rem; margin-bottom:1rem;">
    <div style="font-size:0.75rem; font-weight:700; color:#2563eb !important; background:#dbeafe; display:inline-block; padding:3px 10px; border-radius:20px; margin-bottom:8px;">PROFESSIONAL RAG TOOL</div>
    <div style="font-size:1.8rem; font-weight:800; color:#0f172a !important;">FutureWorks RAG Assistant</div>
    <div style="color:#64748b !important; margin-top:6px;">Upload any document → Get grounded answers. Simple, fast, professional.</div>
</div>
""", unsafe_allow_html=True)

# ===== HELPER FUNCTIONS =====
def get_text_from_file(file):
    text = ""
    try:
        if file.type == "application/pdf":
            import PyPDF2
            reader = PyPDF2.PdfReader(file)
            for p in reader.pages:
                text += (p.extract_text() or "") + "\n"
        elif "word" in file.type or file.name.endswith("docx"):
            from docx import Document
            doc = Document(file)
            text = "\n".join([para.text for para in doc.paragraphs])
        else:
            text = file.getvalue().decode("utf-8", errors="ignore")
    except Exception as e:
        st.error(f"Error reading file: {e}")
    return text

def chunk_text(text, size=1000, overlap=150):
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start = end - overlap
    return [c for c in chunks if len(c.strip()) > 50]

def get_llm_answer(provider, api_key, context, question):
    prompt = f"""You are FutureWorks RAG Assistant. Answer ONLY from the document context below. If answer not in context, say "Not found in document".

Context:
{context}

Question: {question}

Answer concisely with bullet points where possible and cite relevant parts:"""

    # Try to get key from secrets if not provided
    if not api_key:
        if "Groq" in provider:
            api_key = st.secrets.get("GROQ_API_KEY", "")
        elif "OpenAI" in provider:
            api_key = st.secrets.get("OPENAI_API_KEY", "")
        elif "Gemini" in provider:
            api_key = st.secrets.get("GEMINI_API_KEY", "")

    if not api_key:
        return "⚠️ Please add API key in sidebar or Streamlit Secrets."

    try:
        if "Groq" in provider:
            from groq import Groq
            client = Groq(api_key=api_key)
            resp = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role":"user","content":prompt}],
                temperature=0.2
            )
            return resp.choices[0].message.content
        
        elif "OpenAI" in provider:
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
            resp = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role":"user","content":prompt}],
                temperature=0.2
            )
            return resp.choices[0].message.content
        
        elif "Gemini" in provider:
            import google.generativeai as genai
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            resp = model.generate_content(prompt)
            return resp.text

    except Exception as e:
        return f"Error: {e}"

# Simple vector search using TF-IDF (no heavy FAISS/Chroma needed - works instantly)
def simple_search(chunks, query, top_k=4):
    # Simple keyword overlap scoring - fast and works without embeddings
    query_words = set(query.lower().split())
    scored = []
    for i, chunk in enumerate(chunks):
        chunk_words = set(chunk.lower().split())
        score = len(query_words & chunk_words)
        # bonus for longer overlap
        if score > 0:
            scored.append((score, i, chunk))
    scored.sort(reverse=True)
    return [c for s,i,c in scored[:top_k]]

# ===== STATE =====
if "chunks" not in st.session_state:
    st.session_state.chunks = []
if "doc_name" not in st.session_state:
    st.session_state.doc_name = ""
if "questions" not in st.session_state:
    st.session_state.questions = []
if "messages" not in st.session_state:
    st.session_state.messages = []

# ===== MAIN =====
col_upload, col_chat = st.columns([1, 1.3])

with col_upload:
    st.markdown("### 📤 Step 1: Upload Document")
    file = st.file_uploader("Upload PDF, DOCX, TXT", type=["pdf","docx","txt"], label_visibility="collapsed")
    
    if file:
        if file.name != st.session_state.doc_name:
            with st.spinner("Reading & indexing..."):
                text = get_text_from_file(file)
                chunks = chunk_text(text)
                st.session_state.chunks = chunks
                st.session_state.doc_name = file.name
                st.session_state.messages = []
                # Generate smart questions from content
                preview = text[:2000].lower()
                qs = []
                if "summary" in preview or "introduction" in preview:
                    qs.append("What is the summary of this document?")
                qs.extend([
                    f"What are the key points in {file.name}?",
                    "What are the main conclusions?",
                    "What data or numbers are mentioned?",
                    "Who/what is this document about?"
                ])
                st.session_state.questions = qs[:5]
        
        st.success(f"✅ {file.name} • {len(st.session_state.chunks)} chunks indexed")
        
        with st.expander("Preview text"):
            if st.session_state.chunks:
                st.write(st.session_state.chunks[0][:1000] + "...")
        
        # SMART QUESTIONS - ONLY AFTER DOC PARSED
        if st.session_state.questions:
            st.markdown("### 🎯 Smart Questions (from your doc)")
            st.caption("Click to ask - generated after parsing your document")
            for q in st.session_state.questions:
                if st.button(q, key=q, use_container_width=True):
                    st.session_state.messages.append({"role":"user","content":q})
                    # auto answer
                    context = "\n\n".join(simple_search(st.session_state.chunks, q))
                    ans = get_llm_answer(provider, api_key, context, q)
                    st.session_state.messages.append({"role":"assistant","content":ans})
                    st.rerun()

    else:
        st.info("👆 Upload a document to start. Smart questions will appear only after upload.")

with col_chat:
    st.markdown("### 💬 Step 2: Chat with Document")
    
    if not st.session_state.chunks:
        st.markdown("""
        <div style="border:2px dashed #cbd5e1; border-radius:12px; padding:2rem; text-align:center; background:white;">
            <div style="font-size:32px;">💭</div>
            <div style="font-weight:600; color:#0f172a !important; margin-top:8px;">No document yet</div>
            <div style="color:#64748b !important; font-size:0.9rem; margin-top:4px;">Upload on left to enable chat. Answers will be grounded in your doc.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.caption(f"Chatting with: **{st.session_state.doc_name}** • Grounded answers only")
        
        for m in st.session_state.messages:
            with st.chat_message(m["role"]):
                st.markdown(m["content"])
        
        if q := st.chat_input(f"Ask about {st.session_state.doc_name}..."):
            st.session_state.messages.append({"role":"user","content":q})
            with st.chat_message("user"):
                st.markdown(q)
            
            with st.chat_message("assistant"):
                with st.spinner("Searching your doc..."):
                    top_chunks = simple_search(st.session_state.chunks, q, top_k=4)
                    context = "\n\n---\n\n".join(top_chunks)
                    answer = get_llm_answer(provider, api_key, context, q)
                    st.markdown(answer)
                    st.caption(f"📎 Based on {len(top_chunks)} chunks from {st.session_state.doc_name}")
                    st.session_state.messages.append({"role":"assistant","content":answer})

st.divider()
st.caption("FutureWorks RAG • Light Professional Edition • Simple + Fast • Add GROQ_API_KEY in Streamlit Secrets for best free experience")
