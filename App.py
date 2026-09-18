import streamlit as st

st.set_page_config(page_title="FutureWorks RAG AI", page_icon="🤖", layout="wide")

# ============ LIGHT BLUE/GRAY ONLY - MINIMAL ELEGANT ============
st.markdown('''
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family:'Inter', sans-serif !important; }
.stApp { background: #f8fafc !important; }
.main .block-container { background: #ffffff !important; border-radius: 16px !important; padding: 1.8rem !important; border: 1px solid #e2e8f0 !important; box-shadow: 0 1px 6px rgba(148,163,184,0.06) !important; }
p, div, label, li, span { color:#334155 !important; }
h1,h2,h3,h4 { color:#1e293b !important; }
[data-testid="stSidebar"] { background: #ffffff !important; border-right: 1px solid #e2e8f0 !important; }
.stButton>button { background: #334155 !important; color:white !important; border-radius:8px !important; font-weight:600 !important; }
.stButton>button * { color:white !important; }
[data-testid="stFileUploader"] { background: #f8fafc !important; border: 1px dashed #94a3b8 !important; border-radius:12px !important; }

/* Minimal feature cards */
.feature-card { background: #f8fafc; border-radius: 10px; padding: 1rem 1.1rem; border: 1px solid #e2e8f0; }
.benefit-pill { background: white; border:1px solid #e2e8f0; border-radius: 20px; padding: 5px 12px; font-size:0.78rem; color:#475569 !important; display:inline-block; }

/* Chat input placeholder styling */
[data-testid="stChatInput"] { border: 1.5px solid #cbd5e1 !important; border-radius: 12px !important; background: #ffffff !important; }
[data-testid="stChatInput"]:focus-within { border-color: #3b82f6 !important; box-shadow: 0 0 0 3px rgba(59,130,246,0.1) !important; }

/* Text input placeholder */
input::placeholder { color:#94a3b8 !important; font-style: normal !important; }
</style>
''', unsafe_allow_html=True)

# HEADER - MINIMAL WITH ROBOT
st.markdown('''
<div style="background: #ffffff; border:1px solid #e2e8f0; border-radius:14px; padding:1.4rem 1.6rem; margin-bottom:1rem;">
    <div style="display:flex; align-items:center; gap:14px;">
        <div style="width:48px; height:48px; background: #f1f5f9; border:1px solid #cbd5e1; border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:24px;">🤖</div>
        <div>
            <div style="font-size:1.6rem; font-weight:800; color:#1e293b !important; line-height:1.1;">FutureWorks <span style="color:#2563eb !important;">RAG AI</span></div>
            <div style="color:#64748b !important; font-size:0.88rem; margin-top:2px;">Professional RAG AI Document Assistant • Grounded answers from your data</div>
        </div>
    </div>
</div>
''', unsafe_allow_html=True)

# MINIMAL FEATURES & BENEFITS - SINGLE LIGHT ROW
st.markdown('''
<div style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:1rem; align-items:center;">
    <span style="font-size:0.8rem; font-weight:700; color:#334155 !important; margin-right:4px;">RAG AI Features:</span>
    <span class="benefit-pill">📄 PDF/DOCX/TXT</span>
    <span class="benefit-pill">🧠 Grounded Answers</span>
    <span class="benefit-pill">⚡ Instant Parse</span>
    <span class="benefit-pill">🎯 Smart Questions</span>
    <span class="benefit-pill">🔒 Private & Secure</span>
    <span style="margin-left:12px; font-size:0.8rem; font-weight:700; color:#334155 !important;">Benefits:</span>
    <span class="benefit-pill" style="background:#f0f9ff; border-color:#bae6fd; color:#0369a1 !important;">5+ hrs saved</span>
    <span class="benefit-pill" style="background:#f0f9ff; border-color:#bae6fd; color:#0369a1 !important;">100% Grounded</span>
    <span class="benefit-pill" style="background:#f0f9ff; border-color:#bae6fd; color:#0369a1 !important;">Zero Hallucinations</span>
</div>
''', unsafe_allow_html=True)

# SIDEBAR MINIMAL
with st.sidebar:
    st.markdown('<div style="display:flex; align-items:center; gap:8px;"><div style="width:32px; height:32px; background:#f1f5f9; border:1px solid #e2e8f0; border-radius:8px; display:flex; align-items:center; justify-content:center;">🤖</div><div><b style="color:#1e293b;">FutureWorks</b> <b style="color:#2563eb;">RAG AI</b></div></div>', unsafe_allow_html=True)
    st.divider()
    st.markdown("**How RAG AI Works**")
    st.caption("1. Upload doc → 2. RAG AI parses → 3. Smart Qs appear → 4. Chat")
    st.divider()
    st.caption("Light Blue/Gray • Professional • Minimal")

# LOGIC
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

def get_answer_local(context, question):
    if not context.strip():
        return "Couldn't find relevant info. Try asking for summary - RAG AI will extract it."
    answer = f"**🤖 RAG AI - From your document:**\n\n"
    sentences = [s.strip() for s in context.split('.') if len(s.strip())>20][:5]
    for s in sentences:
        if s: answer += f"• {s.strip()}.\n\n"
    answer += f"\n*✅ RAG AI Grounded • {len(sentences)} excerpts*"
    return answer

if "chunks" not in st.session_state: st.session_state.chunks=[]
if "doc_name" not in st.session_state: st.session_state.doc_name=""
if "questions" not in st.session_state: st.session_state.questions=[]
if "messages" not in st.session_state: st.session_state.messages=[]

left, right = st.columns([1,1.25])

with left:
    st.markdown("#### 📤 Upload to RAG AI")
    file=st.file_uploader("Upload", type=["pdf","docx","txt"], label_visibility="collapsed")
    
    if file:
        if file.name != st.session_state.doc_name:
            with st.spinner("🤖 RAG AI parsing..."):
                txt=get_text(file)
                st.session_state.chunks=chunk(txt)
                st.session_state.doc_name=file.name
                st.session_state.messages=[]
                low=txt[:2500].lower()
                qs=[]
                if any(w in low for w in ["summary","introduction"]): qs.append("What is the summary?")
                if any(w in low for w in ["conclusion","result"]): qs.append("What are main conclusions?")
                qs+= [f"5 key takeaways from {file.name}?", "Important data or insights?"]
                seen=set(); final=[]
                for q in qs:
                    if q not in seen:
                        final.append(q); seen.add(q)
                st.session_state.questions=final[:4]
        st.success(f"✅ {file.name} • {len(st.session_state.chunks)} chunks")
        
        if st.session_state.questions:
            st.markdown("**🎯 RAG AI Smart Questions**")
            st.caption("Auto-generated after parsing - from YOUR doc only")
            for q in st.session_state.questions:
                if st.button(f"❓ {q}", key=f"q_{q}", use_container_width=True):
                    st.session_state.messages.append({"role":"user","content":q})
                    ctx="\n\n".join(search(st.session_state.chunks,q))
                    ans=get_answer_local(ctx, q)
                    st.session_state.messages.append({"role":"assistant","content":ans})
                    st.rerun()
    else:
        st.markdown('<div style="border:1px dashed #94a3b8; border-radius:10px; padding:1.5rem; text-align:center; background:#f8fafc;"><div style="font-size:22px;">🤖</div><div style="font-weight:600; color:#334155 !important; font-size:0.9rem; margin-top:6px;">Upload to Activate RAG AI</div><div style="color:#94a3b8 !important; font-size:0.8rem;">Smart Qs appear only after parsing</div></div>', unsafe_allow_html=True)

with right:
    st.markdown("#### 💬 Chat with RAG AI")
    
    if not st.session_state.chunks:
        st.markdown('<div style="border:1px solid #e2e8f0; border-radius:10px; padding:2rem; text-align:center; background:white;"><div style="font-size:32px;">🤖💭</div><div style="font-weight:600; color:#334155 !important; margin-top:8px;">RAG AI Ready</div><div style="color:#94a3b8 !important; font-size:0.85rem;">Upload doc on left to start chatting</div></div>', unsafe_allow_html=True)
        # Placeholder textbox even when no doc - shows sample text
        st.markdown("---")
        st.text_input("Chat box", placeholder="Type here to chat with the document content", disabled=True, label_visibility="collapsed")
    else:
        st.caption(f"Chatting with **{st.session_state.doc_name}**")
        
        for m in st.session_state.messages:
            with st.chat_message(m["role"]):
                st.markdown(m["content"])
        
        # CUSTOM CHAT INPUT WITH PLACEHOLDER "Type here to chat with the document content"
        # This placeholder disappears on click and reappears if empty
        if prompt := st.chat_input("Type here to chat with the document content"):
            st.session_state.messages.append({"role":"user","content":prompt})
            with st.chat_message("user"): st.markdown(prompt)
            with st.chat_message("assistant"):
                with st.spinner("🤖 RAG AI searching..."):
                    ctx="\n\n".join(search(st.session_state.chunks,prompt, k=4))
                    ans=get_answer_local(ctx, prompt)
                    st.markdown(ans)
                    st.session_state.messages.append({"role":"assistant","content":ans})

st.divider()
st.caption("FutureWorks RAG AI • Light Blue/Gray • Minimal • Professional")
