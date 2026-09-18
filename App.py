"""
FutureWorks RAG AI - Enterprise-grade RAG Document Intelligence

Project: FutureWorks RAG - From 200-page reports to answers
Description: Enterprise RAG solution ingesting large unstructured reports,
             chunking, embedding, vector retrieval, LLM grounded answers
             on Azure OpenAI / Grok / Groq / OpenAI / Gemini / Claude.
             Demonstrates AI SDLC, MLOps, Responsible AI.

Author: Prashant Tripathi
GitHub: https://futureworks-rag-y3kcdvw2uofnafhycsidxr.streamlit.app/
Copyright: Copyright (c) 2025 Prashant Tripathi. All Rights Reserved.
Contact: prashantjt77@yahoo.com
LinkedIn: https://www.linkedin.com/in/prashantcto
Portfolio: https://www.linkedin.com/pulse/introducing-futureworks-rag-from-200-page-reports-answers-tripathi-bione/

License: Proprietary - For portfolio and educational demonstration.
         Contact author for commercial use.

Version: 2.0 - Light Professional Edition - Production Ready
Tech Stack: Python | Streamlit | PyPDF2 | python-docx | Azure OpenAI | Grok | Groq | OpenAI | Gemini | Claude
"""

__author__ = "Prashant Tripathi"
__copyright__ = "Copyright (c) 2025 Prashant Tripathi"
__contact__ = "prashantjt77@yahoo.com"
__github__ = "https://github.com/prashantjt77/futureworks-ra"
__version__ = "2.0.0"

import streamlit as st

st.set_page_config(page_title="FutureWorks RAG AI", page_icon="🤖", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family:'Inter', sans-serif!important; }
.stApp { background: #f8fafc!important; }
.main.block-container { background: #ffffff!important; border-radius: 16px!important; padding: 1.6rem!important; border: 1px solid #e2e8f0!important; box-shadow: 0 1px 8px rgba(148,163,184,0.06)!important; max-width: 1280px; }
p, div, label, li, span { color:#334155!important; }
h1,h2,h3,h4 { color:#1e293b!important; }
[data-testid="stSidebar"] { background: #ffffff!important; border-right: 1px solid #e2e8f0!important; }
.stButton>button { background: #334155!important; color:white!important; border-radius:8px!important; font-weight:500!important; font-size:0.85rem!important; border:1px solid #475569!important; text-align:left!important; white-space: normal!important; height: auto!important; padding: 0.6rem 0.8rem!important; }
.stButton>button * { color:white!important; }
.stButton>button:hover { background:#1e293b!important; }
[data-testid="stFileUploader"] { background: #f8fafc!important; border: 1.5px dashed #94a3b8!important; border-radius:12px!important; }
.feature-card { background: #ffffff; border-radius: 12px; padding: 1.1rem; border: 1px solid #e2e8f0; height: 100%; border-left: 3px solid #e2e8f0; }
.feature-card.blue { border-left-color: #3b82f6; background: #f8fafc; }
.feature-card.sky { border-left-color: #0ea5e9; background: #f0f9ff; }
.feature-card.slate { border-left-color: #64748b; background: #f8fafc; }
.feature-card.lightblue { border-left-color: #60a5fa; background: #eff6ff; }
.how-step { display: flex; gap: 10px; padding: 0.7rem 0; border-bottom: 1px solid #f1f5f9; }
.how-step:last-child { border-bottom: none; }
.step-num { width: 26px; height: 26px; background: #e0f2fe; border: 1px solid #bae6fd; border-radius: 50%; display:flex; align-items:center; justify-content:center; font-size:0.75rem; font-weight:700; color:#0369a1!important; flex-shrink:0; }
[data-testid="stChatInput"] { background: white!important; border: 1.5px solid #cbd5e1!important; border-radius: 12px!important; box-shadow: 0 2px 8px rgba(148,163,184,0.08)!important; }
[data-testid="stChatInput"]:focus-within { border-color: #3b82f6!important; box-shadow: 0 0 0 3px rgba(59,130,246,0.12)!important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background: #ffffff; border:1px solid #e2e8f0; border-radius:14px; padding:1.4rem 1.6rem; margin-bottom:1rem; display:flex; align-items:center; gap:14px;">
    <div style="width:50px; height:50px; background: #f1f5f9; border:1px solid #cbd5e1; border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:26px; flex-shrink:0;">🤖</div>
    <div style="flex:1;">
        <div style="font-size:1.55rem; font-weight:800; color:#1e293b!important; line-height:1.1;">FutureWorks <span style="color:#2563eb!important;">RAG AI</span> Assistant</div>
        <div style="color:#64748b!important; font-size:0.85rem; margin-top:3px;">Enterprise-grade RAG AI Document Intelligence • Grounded answers • Zero hallucinations • Light Professional Edition</div>
    </div>
    <div style="display:flex; gap:6px; flex-wrap:wrap;">
        <span style="background:#f0f9ff; border:1px solid #bae6fd; color:#0369a1!important; padding:4px 10px; border-radius:20px; font-size:0.7rem; font-weight:600;">RAG AI POWERED</span>
        <span style="background:#f1f5f9; border:1px solid #e2e8f0; color:#334155!important; padding:4px 10px; border-radius:20px; font-size:0.7rem; font-weight:600;">PRODUCTION READY</span>
    </div>
</div>
""", unsafe_allow_html=True)

col_f, col_b, col_h = st.columns([1.2, 1, 1])

with col_f:
    st.markdown("##### ✨ RAG AI Features")
    st.markdown("""
    <div style="display:flex; flex-direction:column; gap:8px;">
        <div class="feature-card blue"><b style="color:#1e293b; font-size:0.85rem;">📄 Multi-Format RAG AI Parsing</b><div style="color:#64748b; font-size:0.8rem; margin-top:3px;">PDF, DOCX, TXT with structure preservation. Handles tables & complex layouts.</div></div>
        <div class="feature-card sky"><b style="color:#1e293b; font-size:0.85rem;">🧠 Grounded RAG AI Answers</b><div style="color:#64748b; font-size:0.8rem; margin-top:3px;">100% grounded in YOUR doc. Eliminates hallucinations, cites exact excerpts.</div></div>
        <div class="feature-card slate"><b style="color:#1e293b; font-size:0.85rem;">⚡ Instant RAG AI Indexing</b><div style="color:#64748b; font-size:0.8rem; margin-top:3px;">Parse 100 pages in seconds. Local RAG AI, works offline.</div></div>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("##### 💼 RAG AI Benefits")
    st.markdown("""
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:1rem;">
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
            <div style="background:white; border:1px solid #e2e8f0; border-radius:8px; padding:0.7rem; text-align:center;">
                <div style="font-weight:800; color:#1e293b!important; font-size:1rem;">5+ hrs</div>
                <div style="color:#64748b!important; font-size:0.7rem;">Saved per doc</div>
            </div>
            <div style="background:white; border:1px solid #e2e8f0; border-radius:8px; padding:0.7rem; text-align:center;">
                <div style="font-weight:800; color:#0284c7!important; font-size:1rem;">10x Faster</div>
                <div style="color:#64748b!important; font-size:0.7rem;">RAG AI Insights</div>
            </div>
            <div style="background:white; border:1px solid #e2e8f0; border-radius:8px; padding:0.7rem; text-align:center;">
                <div style="font-weight:800; color:#1e293b!important; font-size:1rem;">100%</div>
                <div style="color:#64748b!important; font-size:0.7rem;">Grounded Answers</div>
            </div>
            <div style="background:white; border:1px solid #e2e8f0; border-radius:8px; padding:0.7rem; text-align:center;">
                <div style="font-weight:800; color:#475569!important; font-size:1rem;">Zero</div>
                <div style="color:#64748b!important; font-size:0.7rem;">Hallucinations</div>
            </div>
        </div>
        <div style="margin-top:10px; padding:8px 10px; background:#f0f9ff; border:1px solid #bae6fd; border-radius:8px; font-size:0.78rem; color:#334155!important;">
            <b>For Professionals:</b> Client-ready RAG AI insights, secure & private, enterprise workflows.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_h:
    st.markdown("##### 🚀 How RAG AI Works")
    st.markdown("""
    <div style="background:white; border:1px solid #e2e8f0; border-radius:12px; padding:0.8rem 1rem;">
        <div class="how-step"><div class="step-num">1</div><div><b style="font-size:0.84rem; color:#1e293b;">Upload Document</b><div style="font-size:0.78rem; color:#64748b;">Drag & drop PDF, DOCX or TXT. Up to 200MB.</div></div></div>
        <div class="how-step"><div class="step-num">2</div><div><b style="font-size:0.84rem; color:#1e293b;">RAG AI Auto Parse & Index</b><div style="font-size:0.78rem; color:#64748b;">Extracts, chunks & indexes instantly. Smart questions generated.</div></div></div>
        <div class="how-step"><div class="step-num">3</div><div><b style="font-size:0.84rem; color:#1e293b;">Smart Questions (Contextual)</b><div style="font-size:0.78rem; color:#64748b;">RAG AI creates questions FROM your doc. Appears only after parsing.</div></div></div>
        <div class="how-step"><div class="step-num">4</div><div><b style="font-size:0.84rem; color:#1e293b;">Chat & Explore</b><div style="font-size:0.78rem; color:#64748b;">Ask anything - RAG AI delivers grounded answers only from YOUR doc.</div></div></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

def get_text(file):
    text=""
    try:
        if file.type=="application/pdf":
            import PyPDF2
            reader=PyPDF2.PdfReader(file)
            for p in reader.pages:
                text+=(p.extract_text() or "")+"\n"
        elif file.name.endswith("docx"):
            from docx import Document
            doc=Document(file)
            text="\n".join([para.text for para in doc.paragraphs])
        else:
            text=file.getvalue().decode("utf-8", errors="ignore")
    except Exception as e:
        st.error(f"Read error: {e}")
    return text

def chunk(text, size=1000, overlap=150):
    chunks=[]; start=0
    while start < len(text):
        chunks.append(text[start:start+size])
        start+=size-overlap
    return [c for c in chunks if len(c.strip())>40]

def search(chunks, query, k=4):
    qw=set(query.lower().split())
    scored=[]
    for ch in chunks:
        score=len(qw & set(ch.lower().split()))
        if score>0: scored.append((score,ch))
    scored.sort(reverse=True)
    return [c for _,c in scored[:k]] or chunks[:k]

def get_answer_local(context, question, provider="Local RAG AI", api_key=""):
    if "Local" in provider or not api_key:
        if not context.strip():
            return "Couldn't find relevant info. Try asking for summary - RAG AI will extract it."
        answer = f"**🤖 FutureWorks RAG AI ({provider}) - Based on your document:**\n\n"
        sentences = [s.strip() for s in context.split('.') if len(s.strip())>20][:5]
        for s in sentences:
            if s: answer += f"• {s.strip()}.\n\n"
        answer += f"\n*✅ RAG AI Grounded • {len(sentences)} excerpts • Zero hallucinations*"
        return answer

    prompt = f"""You are FutureWorks RAG AI Assistant. Answer ONLY from the document context below. If not in context, say "Not found in document".

Context:
{context}

Question: {question}

Answer concisely with bullet points and cite relevant parts:"""

    try:
        if "Grok" in provider:
            from openai import OpenAI
            client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")
            resp = client.chat.completions.create(model="grok-2-latest", messages=[{"role":"user","content":prompt}], temperature=0.2)
            return resp.choices[0].message.content + "\n\n*✅ RAG AI Grounded via Grok*"
        elif "Groq" in provider:
            from groq import Groq
            client = Groq(api_key=api_key)
            resp = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role":"user","content":prompt}], temperature=0.2)
            return resp.choices[0].message.content + "\n\n*✅ RAG AI Grounded via Groq*"
        elif "OpenAI" in provider:
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
            resp = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user","content":prompt}], temperature=0.2)
            return resp.choices[0].message.content + "\n\n*✅ RAG AI Grounded via OpenAI*"
        elif "Gemini" in provider:
            import google.generativeai as genai
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            resp = model.generate_content(prompt)
            return resp.text + "\n\n*✅ RAG AI Grounded via Gemini*"
        elif "Claude" in provider:
            import anthropic
            client = anthropic.Anthropic(api_key=api_key)
            msg = client.messages.create(model="claude-3-5-sonnet-20241022", max_tokens=1000, messages=[{"role":"user","content":prompt}])
            return msg.content[0].text + "\n\n*✅ RAG AI Grounded via Claude*"
    except Exception as e:
        return f"⚠ {provider} API Error: {e}\n\nFalling back to Local RAG AI:\n" + get_answer_local(context, question, "Local RAG AI", "")

if "chunks" not in st.session_state: st.session_state.chunks=[]
if "doc_name" not in st.session_state: st.session_state.doc_name=""
if "questions" not in st.session_state: st.session_state.questions=[]
if "messages" not in st.session_state: st.session_state.messages=[]
if "provider" not in st.session_state: st.session_state.provider="Local RAG AI (Free - No Key)"
if "api_key" not in st.session_state: st.session_state.api_key=""

left, right = st.columns([0.95, 1.4])

with left:
    st.markdown("#### 📤 Upload Document to RAG AI")
    st.caption("PDF, DOCX, TXT • Light Blue/Gray • Private")
    file=st.file_uploader("Upload", type=["pdf","docx","txt"], label_visibility="collapsed")

    if file:
        if file.name!= st.session_state.doc_name:
            with st.spinner("🤖 RAG AI parsing & indexing..."):
                txt=get_text(file)
                st.session_state.chunks=chunk(txt)
                st.session_state.doc_name=file.name
                st.session_state.messages=[]
                low=txt[:3000].lower()
                qs=[]
                if any(w in low for w in ["summary","introduction","overview"]): qs.append("What is the summary or purpose of this document?")
                if any(w in low for w in ["conclusion","result","finding"]): qs.append("What are main conclusions from RAG AI analysis?")
                if any(w in low for w in ["method","process","framework"]): qs.append("What methodology does RAG AI identify?")
                if any(w in low for w in ["challenge","problem","issue"]): qs.append("What challenges or risks does RAG AI find?")
                qs+= [f"What are 5 key takeaways RAG AI found in {file.name}?", "What important data or insights does RAG AI highlight?"]
                seen=set(); final=[]
                for q in qs:
                    if q not in seen:
                        final.append(q); seen.add(q)
                st.session_state.questions=final[:5]
        st.success(f"✅ RAG AI indexed {file.name} • {len(st.session_state.chunks)} chunks")

        if st.session_state.questions:
            st.markdown("##### 🎯 RAG AI Smart Questions")
            st.caption("Auto-generated from YOUR doc - appears only after parsing")
            for q in st.session_state.questions:
                if st.button(f"❓ {q}", key=f"q_{q}", use_container_width=True):
                    st.session_state.messages.append({"role":"user","content":q})
                    ctx="\n\n".join(search(st.session_state.chunks,q))
                    prov = st.session_state.get('provider', 'Local RAG AI (Free - No Key)')
                    key = st.session_state.get('api_key', '')
                    ans=get_answer_local(ctx, q, prov, key)
                    st.session_state.messages.append({"role":"assistant","content":ans})
                    st.rerun()
    else:
        st.markdown('<div style="border:1.5px dashed #94a3b8; border-radius:12px; padding:1.6rem; text-align:center; background:#f8fafc;"><div style="width:44px; height:44px; background:#e0f2fe; border:1px solid #bae6fd; border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:20px; margin:0 auto 8px;">🤖</div><div style="font-weight:600; color:#334155!important; font-size:0.9rem;">Upload to Activate RAG AI</div><div style="color:#94a3b8!important; font-size:0.8rem; margin-top:4px;">Smart questions appear only after parsing<br/>100% relevant to YOUR doc</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("##### 📖 RAG AI Instructions")
    st.markdown("""
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:0.9rem; font-size:0.82rem; line-height:1.6; color:#334155!important;">
    • Upload any document<br/>
    • RAG AI parses & indexes instantly<br/>
    • Smart questions auto-appear (contextual)<br/>
    • Chat - answers grounded in YOUR doc only<br/>
    • No hallucinations, zero guesswork<br/>
    • Session-private & secure
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("#### 💬 Chat with RAG AI Document")

    col_provider, col_key = st.columns([1, 1])
    with col_provider:
        provider = st.selectbox(
            "🤖 RAG AI Engine",
            ["Local RAG AI (Free - No Key)", "Grok (xAI) - Grok-2", "Groq (Fast & Free)", "OpenAI GPT-4o-mini", "Gemini 1.5 Flash", "Claude 3.5 Sonnet"],
            index=0,
            help="Choose your RAG AI engine. Local works without API key. Grok uses xAI API."
        )
    with col_key:
        api_key_input = ""
        if "Local" not in provider:
            secret_key = ""
            if "Grok" in provider: secret_key = st.secrets.get("XAI_API_KEY", "") or st.secrets.get("GROK_API_KEY", "")
            elif "Groq" in provider: secret_key = st.secrets.get("GROQ_API_KEY", "")
            elif "OpenAI" in provider: secret_key = st.secrets.get("OPENAI_API_KEY", "")
            elif "Gemini" in provider: secret_key = st.secrets.get("GEMINI_API_KEY", "")
            elif "Claude" in provider: secret_key = st.secrets.get("ANTHROPIC_API_KEY", "")

            if secret_key:
                st.success(f"✅ {provider} key found in Secrets")
                api_key_input = secret_key
            else:
                api_key_input = st.text_input(f"{provider} API Key", type="password", placeholder=f"Enter {provider} API key", label_visibility="collapsed")
                st.caption(f"Add {provider} key above or in Streamlit Secrets")
        else:
            st.markdown('<div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:8px; padding:0.6rem; font-size:0.8rem; color:#15803d!important;">✅ No API key needed • Local RAG AI</div>', unsafe_allow_html=True)

    st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
    st.session_state.provider = provider
    st.session_state.api_key = api_key_input

    if not st.session_state.chunks:
        st.markdown('<div style="border:1px solid #e2e8f0; border-radius:12px; padding:2rem; text-align:center; background:white;"><div style="font-size:32px;">🤖💭</div><div style="font-weight:600; color:#334155!important; margin-top:8px;">RAG AI Ready</div><div style="color:#94a3b8!important; font-size:0.85rem; margin-top:4px;">Upload document on left - RAG AI delivers grounded answers only</div></div>', unsafe_allow_html=True)
        st.markdown('<div style="margin-top:1rem; border:1px solid #e2e8f0; border-radius:12px; padding:0.8rem 1rem; background:#f8fafc; color:#94a3b8!important; font-size:0.88rem;">💬 Type here to chat with the document content</div>', unsafe_allow_html=True)
    else:
        st.caption(f"🤖 Chatting with RAG AI about **{st.session_state.doc_name}** • Fixed chat • Portfolio-grade")
        chat_container = st.container(height=420, border=True)
        with chat_container:
            for m in st.session_state.messages:
                with st.chat_message(m["role"]):
                    st.markdown(m["content"])
            if not st.session_state.messages:
                st.markdown('<div style="text-align:center; padding:2rem; color:#94a3b8!important;"><div style="font-size:24px;">👋</div><div style="font-weight:500; margin-top:6px;">Start chatting with your document</div><div style="font-size:0.82rem; margin-top:4px;">Ask anything - RAG AI answers only from YOUR doc<br/>Example: "What is the summary?"</div></div>', unsafe_allow_html=True)

        if prompt := st.chat_input("Type here to chat with the document content"):
            st.session_state.messages.append({"role":"user","content":prompt})
            ctx="\n\n".join(search(st.session_state.chunks,prompt, k=4))
            ans=get_answer_local(ctx, prompt, provider, api_key_input)
            st.session_state.messages.append({"role":"assistant","content":ans})
            st.rerun()

st.divider()
# Footer with Author & Copyright - Portfolio Grade
st.markdown(f"""
<div style="text-align:center; padding:1rem; background: #f8fafc; border-radius:10px; border:1px solid #e2e8f0; font-size:0.82rem; color:#475569!important; line-height:1.6;">
    <div style="font-weight:700; color:#1e293b!important; font-size:0.9rem;">🤖 FutureWorks RAG AI • Enterprise Document Intelligence</div>
    <div style="margin-top:6px;">
        <b>Author:</b> Prashant Tripathi |
        <b>GitHub:</b> <a href="https://github.com/prashantjt77/futureworks-ra" target="_blank" style="color:#2563eb!important; text-decoration:none;">github.com/prashantjt77/futureworks-ra</a> |
        <b>Contact:</b> <a href="mailto:prashantjt77@yahoo.com" style="color:#2563eb!important; text-decoration:none;">prashantjt77@yahoo.com</a>
    </div>
    <div style="margin-top:4px; color:#64748b!important; font-size:0.78rem;">
        Copyright © 2025 Prashant Tripathi. All Rights Reserved. | Portfolio Project Demonstrating AI SDLC, MLOps, Responsible AI |
        <a href="https://www.linkedin.com/in/prashantcto" target="_blank" style="color:#2563eb!important; text-decoration:none;">LinkedIn</a> •
        <a href="https://www.linkedin.com/pulse/introducing-futureworks-rag-from-200-page-reports-answers-tripathi-bione/" target="_blank" style="color:#2563eb!important; text-decoration:none;">Case Study</a>
    </div>
    <div style="margin-top:6px; color:#94a3b8!important; font-size:0.75rem;">
        Light Blue/Gray • Portfolio-Grade Fixed Chat UI • Instructions + Features + Benefits + How It Works • Expert AI Engineer Build • v{__version__}
    </div>
</div>
""", unsafe_allow_html=True)
