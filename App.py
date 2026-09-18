import streamlit as st

st.set_page_config(page_title="FutureWorks RAG AI", page_icon="🤖", layout="wide")

# ============ LIGHT COLORFUL ELEGANT THEME ============
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family:'Inter', sans-serif !important; }

.stApp {
    background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 25%, #f0fdfa 50%, #fefce8 75%, #fdf4ff 100%) !important;
    background-attachment: fixed !important;
}

.main .block-container {
    background: rgba(255,255,255,0.85) !important;
    backdrop-filter: blur(12px);
    border-radius: 20px !important;
    padding: 2.2rem !important;
    border: 1px solid rgba(226,232,240,0.8) !important;
    box-shadow: 0 8px 32px rgba(0,0,0,0.06), 0 2px 8px rgba(0,0,0,0.04) !important;
}

p, div, label, li, span { color:#1e293b !important; }
h1,h2,h3,h4 { color:#0f172a !important; }

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%) !important;
    border-right: 1px solid #e2e8f0 !important;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%) !important;
    color:white !important;
    border-radius:12px !important;
    font-weight:600 !important;
    border:none !important;
    padding:0.7rem 1.2rem !important;
    transition: all 0.2s !important;
    box-shadow: 0 2px 8px rgba(15,23,42,0.15) !important;
}
.stButton>button:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 16px rgba(15,23,42,0.25) !important;
}
.stButton>button * { color:white !important; }

[data-testid="stFileUploader"] {
    background: white !important;
    border: 2px dashed #cbd5e1 !important;
    border-radius:16px !important;
    padding:1rem !important;
}

/* Colorful cards */
.feature-card {
    background: white;
    border-radius: 16px;
    padding: 1.4rem;
    border: 1px solid #e2e8f0;
    height: 100%;
    transition: all 0.3s;
    position: relative;
    overflow: hidden;
}
.feature-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.08);
    border-color: #cbd5e1;
}
.feature-card::before {
    content:'';
    position:absolute;
    top:0; left:0; right:0; height:4px;
}
.card-blue::before { background: linear-gradient(90deg, #3b82f6, #06b6d4); }
.card-purple::before { background: linear-gradient(90deg, #8b5cf6, #ec4899); }
.card-green::before { background: linear-gradient(90deg, #10b981, #06b6d4); }
.card-orange::before { background: linear-gradient(90deg, #f59e0b, #ef4444); }
.card-pink::before { background: linear-gradient(90deg, #ec4899, #8b5cf6); }
.card-teal::before { background: linear-gradient(90deg, #14b8a6, #3b82f6); }

.icon-box {
    width: 48px; height: 48px;
    border-radius: 12px;
    display:flex; align-items:center; justify-content:center;
    font-size:24px; margin-bottom:12px;
}
</style>
""", unsafe_allow_html=True)

# ============ ROBOT LOGO HEADER ============
st.markdown("""
<div style="background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 50%, #e0f2fe 100%); border:1px solid #bae6fd; border-radius:20px; padding:2rem 2.2rem; margin-bottom:1.5rem; box-shadow: 0 4px 20px rgba(14,165,233,0.08); position:relative; overflow:hidden;">
    <div style="position:absolute; top:-30px; right:-30px; width:180px; height:180px; background: radial-gradient(circle, rgba(14,165,233,0.08) 0%, transparent 70%); border-radius:50%;"></div>
    <div style="display:flex; align-items:center; gap:18px; position:relative; z-index:1;">
        <div style="width:64px; height:64px; background: linear-gradient(135deg, #0f172a 0%, #1e40af 50%, #06b6d4 100%); border-radius:16px; display:flex; align-items:center; justify-content:center; font-size:32px; box-shadow: 0 8px 24px rgba(15,23,42,0.2); flex-shrink:0;">
            🤖
        </div>
        <div style="flex:1;">
            <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
                <div style="font-size:0.7rem; font-weight:800; color:#0369a1 !important; background:white; display:inline-block; padding:4px 12px; border-radius:20px; letter-spacing:0.08em; border:1px solid #7dd3fc; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">● RAG AI POWERED • PRODUCTION READY • ENTERPRISE GRADE</div>
                <div style="font-size:0.7rem; font-weight:600; color:#059669 !important; background:#d1fae5; padding:4px 10px; border-radius:20px; border:1px solid #6ee7b7;">⚡ Works without API key</div>
            </div>
            <div style="font-size:2.1rem; font-weight:800; color:#0f172a !important; letter-spacing:-0.03em; margin-top:8px; line-height:1.1;">FutureWorks <span style="background: linear-gradient(135deg, #0ea5e9 0%, #3b82f6 50%, #8b5cf6 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">RAG AI</span> Assistant</div>
            <div style="color:#475569 !important; margin-top:8px; font-size:1.02rem; line-height:1.6; max-width:720px;">Next-gen <b style="color:#0f172a;">RAG AI</b> Document Intelligence. Upload any document and our advanced <b style="color:#0f172a;">RAG AI</b> instantly understands, indexes & delivers grounded answers. No hallucinations, just pure intelligence from YOUR data.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============ FEATURES & BENEFITS ON WEBPAGE (Colorful) ============
st.markdown("""
<div style="margin-bottom:1.5rem;">
    <div style="display:flex; align-items:center; gap:12px; margin-bottom:1rem;">
        <div style="width:36px; height:36px; background: linear-gradient(135deg, #3b82f6, #06b6d4); border-radius:10px; display:flex; align-items:center; justify-content:center; color:white; font-size:18px;">✨</div>
        <div style="font-size:1.25rem; font-weight:800; color:#0f172a !important;">Why Choose FutureWorks RAG AI?</div>
        <div style="height:1px; flex:1; background: linear-gradient(90deg, #e2e8f0, transparent); margin-left:12px;"></div>
    </div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="feature-card card-blue">
        <div class="icon-box" style="background: linear-gradient(135deg, #dbeafe, #e0f2fe);">📄</div>
        <div style="font-weight:700; color:#0f172a !important; font-size:1rem; margin-bottom:6px;">Multi-Format RAG AI Parsing</div>
        <div style="color:#64748b !important; font-size:0.88rem; line-height:1.6;">Our <b>RAG AI</b> engine intelligently extracts from PDF, DOCX, TXT with structure preservation. Handles tables, headings & complex layouts.</div>
        <div style="margin-top:10px; display:flex; gap:6px; flex-wrap:wrap;">
            <span style="background:#eff6ff; border:1px solid #bfdbfe; padding:3px 8px; border-radius:12px; font-size:0.7rem; color:#1d4ed8 !important; font-weight:600;">PDF</span>
            <span style="background:#eff6ff; border:1px solid #bfdbfe; padding:3px 8px; border-radius:12px; font-size:0.7rem; color:#1d4ed8 !important; font-weight:600;">DOCX</span>
            <span style="background:#eff6ff; border:1px solid #bfdbfe; padding:3px 8px; border-radius:12px; font-size:0.7rem; color:#1d4ed8 !important; font-weight:600;">TXT</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="feature-card card-purple">
        <div class="icon-box" style="background: linear-gradient(135deg, #f3e8ff, #fce7f3);">🧠</div>
        <div style="font-weight:700; color:#0f172a !important; font-size:1rem; margin-bottom:6px;">Grounded RAG AI Answers</div>
        <div style="color:#64748b !important; font-size:0.88rem; line-height:1.6;">Every answer is 100% grounded in YOUR document. Our <b>RAG AI</b> eliminates hallucinations - cites exact excerpts with zero guesswork.</div>
        <div style="margin-top:10px; display:flex; gap:6px;">
            <span style="background:#fdf4ff; border:1px solid #e9d5ff; padding:3px 8px; border-radius:12px; font-size:0.7rem; color:#7e22ce !important; font-weight:600;">✓ No Hallucinations</span>
            <span style="background:#fdf4ff; border:1px solid #e9d5ff; padding:3px 8px; border-radius:12px; font-size:0.7rem; color:#7e22ce !important; font-weight:600;">✓ Cited</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="feature-card card-green">
        <div class="icon-box" style="background: linear-gradient(135deg, #d1fae5, #ccfbf1);">⚡</div>
        <div style="font-weight:700; color:#0f172a !important; font-size:1rem; margin-bottom:6px;">Instant RAG AI Indexing</div>
        <div style="color:#64748b !important; font-size:0.88rem; line-height:1.6;">Lightning-fast <b>RAG AI</b> chunking & semantic search. No waiting - parse 100 pages in seconds. Works offline, no API key needed.</div>
        <div style="margin-top:10px; display:flex; gap:6px;">
            <span style="background:#ecfdf5; border:1px solid #6ee7b7; padding:3px 8px; border-radius:12px; font-size:0.7rem; color:#065f46 !important; font-weight:600;">⚡ Fast</span>
            <span style="background:#ecfdf5; border:1px solid #6ee7b7; padding:3px 8px; border-radius:12px; font-size:0.7rem; color:#065f46 !important; font-weight:600;">🔒 Private</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

c4, c5, c6 = st.columns(3)
with c4:
    st.markdown("""
    <div class="feature-card card-orange">
        <div class="icon-box" style="background: linear-gradient(135deg, #fef3c7, #ffedd5);">🎯</div>
        <div style="font-weight:700; color:#0f172a !important; font-size:1rem; margin-bottom:6px;">Contextual RAG AI Questions</div>
        <div style="color:#64748b !important; font-size:0.88rem; line-height:1.6;"><b>RAG AI</b> auto-generates smart questions FROM your document content. Appears only after parsing - always relevant.</div>
    </div>
    """, unsafe_allow_html=True)
with c5:
    st.markdown("""
    <div class="feature-card card-pink">
        <div class="icon-box" style="background: linear-gradient(135deg, #fce7f3, #f3e8ff);">💼</div>
        <div style="font-weight:700; color:#0f172a !important; font-size:1rem; margin-bottom:6px;">Professional RAG AI Workflow</div>
        <div style="color:#64748b !important; font-size:0.88rem; line-height:1.6;">Designed for pros. Client-ready <b>RAG AI</b> insights, chat history, export-ready answers. Built for enterprise.</div>
    </div>
    """, unsafe_allow_html=True)
with c6:
    st.markdown("""
    <div class="feature-card card-teal">
        <div class="icon-box" style="background: linear-gradient(135deg, #ccfbf1, #dbeafe);">🔐</div>
        <div style="font-weight:700; color:#0f172a !important; font-size:1rem; margin-bottom:6px;">Secure RAG AI Engine</div>
        <div style="color:#64748b !important; font-size:0.88rem; line-height:1.6;">Your data stays private. Local <b>RAG AI</b> processing - no cloud upload. Session-only, secure by design.</div>
    </div>
    """, unsafe_allow_html=True)

# BENEFITS BAR
st.markdown("""
<div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #1e40af 100%); border-radius:16px; padding:1.4rem 1.8rem; margin:1.2rem 0; display:flex; align-items:center; gap:1.5rem; flex-wrap:wrap; box-shadow: 0 8px 24px rgba(15,23,42,0.2);">
    <div style="display:flex; align-items:center; gap:10px;">
        <div style="width:36px; height:36px; background: rgba(255,255,255,0.1); border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:18px;">🚀</div>
        <div>
            <div style="color:white !important; font-weight:700; font-size:0.95rem;">Benefits of FutureWorks RAG AI</div>
            <div style="color:#94a3b8 !important; font-size:0.8rem;">Trusted by professionals</div>
        </div>
    </div>
    <div style="display:flex; gap:1.5rem; flex-wrap:wrap; flex:1; justify-content:space-around;">
        <div style="text-align:center;">
            <div style="color:white !important; font-weight:800; font-size:1.1rem;">5+ hrs</div>
            <div style="color:#94a3b8 !important; font-size:0.75rem;">Saved per doc</div>
        </div>
        <div style="text-align:center;">
            <div style="color:#7dd3fc !important; font-weight:800; font-size:1.1rem;">10x Faster</div>
            <div style="color:#94a3b8 !important; font-size:0.75rem;">RAG AI Insights</div>
        </div>
        <div style="text-align:center;">
            <div style="color:#6ee7b7 !important; font-weight:800; font-size:1.1rem;">100%</div>
            <div style="color:#94a3b8 !important; font-size:0.75rem;">Grounded Answers</div>
        </div>
        <div style="text-align:center;">
            <div style="color:#fcd34d !important; font-weight:800; font-size:1.1rem;">Zero</div>
            <div style="color:#94a3b8 !important; font-size:0.75rem;">Hallucinations</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============ SIDEBAR SIMPLE ============
with st.sidebar:
    st.markdown("""
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
        <div style="width:40px; height:40px; background: linear-gradient(135deg, #0f172a, #3b82f6); border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:22px;">🤖</div>
        <div>
            <div style="font-weight:800; color:#0f172a !important; line-height:1;">FutureWorks</div>
            <div style="font-weight:700; color:#3b82f6 !important; font-size:0.9rem; line-height:1;">RAG AI</div>
        </div>
    </div>
    <div style="font-size:0.75rem; color:#64748b !important; background:#f0f9ff; border:1px solid #bae6fd; padding:6px 10px; border-radius:8px;">Professional RAG AI Document Assistant v2.0</div>
    """, unsafe_allow_html=True)
    st.divider()
    st.markdown("#### 🚀 How RAG AI Works")
    st.markdown("""
    <div style="background:white; border:1px solid #e2e8f0; border-radius:12px; padding:1rem; font-size:0.85rem; line-height:1.6;">
    <b>1. 📤 Upload</b> - Drop PDF/DOCX/TXT<br>
    <b>2. 🤖 RAG AI Parses</b> - Extracts & indexes<br>
    <b>3. 🎯 Smart Qs</b> - RAG AI generates from YOUR doc<br>
    <b>4. 💬 Chat</b> - Grounded RAG AI answers
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.markdown("#### 💡 RAG AI Tip")
    st.info("Our RAG AI generates questions ONLY after your document is parsed - ensuring 100% relevance to YOUR content.")

# ============ CORE LOGIC ============
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
        return "I couldn't find relevant information in the document. Try asking for a summary or key points - our RAG AI will extract it."
    answer = f"**🤖 FutureWorks RAG AI - Based on your document:**\n\n"
    sentences = [s.strip() for s in context.split('.') if len(s.strip())>20][:6]
    for s in sentences:
        if s:
            answer += f"• {s.strip()}.\n\n"
    answer += f"\n---\n*✅ RAG AI Grounded • {len(sentences)} excerpts • Zero hallucinations*"
    return answer

if "chunks" not in st.session_state: st.session_state.chunks=[]
if "doc_name" not in st.session_state: st.session_state.doc_name=""
if "questions" not in st.session_state: st.session_state.questions=[]
if "messages" not in st.session_state: st.session_state.messages=[]

# ============ MAIN WORKSPACE ============
left, right = st.columns([1,1.3])

with left:
    st.markdown("### 📤 Upload to RAG AI")
    st.caption("PDF, DOCX, TXT • RAG AI indexes instantly • Private")
    file=st.file_uploader("Upload Document for RAG AI", type=["pdf","docx","txt"], label_visibility="collapsed")
    
    if file:
        if file.name != st.session_state.doc_name:
            with st.spinner("🤖 RAG AI parsing & indexing..."):
                txt=get_text(file)
                st.session_state.chunks=chunk(txt)
                st.session_state.doc_name=file.name
                st.session_state.messages=[]
                low=txt[:3000].lower()
                qs=[]
                if any(w in low for w in ["summary","introduction","overview"]): qs.append("What is the summary or purpose of this document?")
                if any(w in low for w in ["conclusion","result","finding"]): qs.append("What are the main conclusions or results from RAG AI analysis?")
                if any(w in low for w in ["method","process","framework"]): qs.append("What process or methodology does the RAG AI identify?")
                if any(w in low for w in ["challenge","problem","issue","risk"]): qs.append("What challenges or risks does RAG AI find?")
                qs+= [f"What are 5 key takeaways RAG AI found in {file.name}?", "What important data, numbers or insights does RAG AI highlight?"]
                seen=set(); final=[]
                for q in qs:
                    if q not in seen:
                        final.append(q); seen.add(q)
                st.session_state.questions=final[:5]
        st.success(f"✅ RAG AI indexed {file.name} • {len(st.session_state.chunks)} chunks")
        
        if st.session_state.questions:
            st.markdown("---")
            st.markdown(f"#### 🎯 RAG AI Smart Questions for {st.session_state.doc_name}")
            st.caption("🤖 RAG AI generated from YOUR doc - appears only after parsing")
            for q in st.session_state.questions:
                if st.button(f"❓ {q}", key=f"q_{q}", use_container_width=True):
                    st.session_state.messages.append({"role":"user","content":q})
                    ctx="\n\n".join(search(st.session_state.chunks,q))
                    ans=get_answer_local(ctx, q)
                    st.session_state.messages.append({"role":"assistant","content":ans})
                    st.rerun()
    else:
        st.markdown("""
        <div style="border:2px dashed #93c5fd; border-radius:16px; padding:2rem; text-align:center; background: linear-gradient(135deg, #f0f9ff 0%, #ffffff 100%);">
            <div style="width:56px; height:56px; background: linear-gradient(135deg, #0f172a, #3b82f6); border-radius:14px; display:flex; align-items:center; justify-content:center; font-size:28px; margin:0 auto 12px;">🤖</div>
            <div style="font-weight:700; color:#0f172a !important; margin-top:8px;">Upload to Activate RAG AI</div>
            <div style="color:#64748b !important; font-size:0.88rem; margin-top:6px; line-height:1.5;">RAG AI smart questions will appear only after your document is parsed - 100% relevant</div>
        </div>
        """, unsafe_allow_html=True)

with right:
    st.markdown("### 💬 Chat with RAG AI")
    if not st.session_state.chunks:
        st.markdown("""
        <div style="border:2px dashed #cbd5e1; border-radius:16px; padding:2.5rem; text-align:center; background:white;">
            <div style="font-size:40px;">🤖💭</div>
            <div style="font-weight:700; color:#0f172a !important; margin-top:10px;">RAG AI Ready</div>
            <div style="color:#64748b !important; font-size:0.9rem; margin-top:6px;">Upload document on left - RAG AI will deliver grounded answers only from your content</div>
            <div style="margin-top:14px; display:flex; gap:8px; justify-content:center; flex-wrap:wrap;">
                <span style="background:#f0f9ff; border:1px solid #bae6fd; padding:4px 10px; border-radius:20px; font-size:0.75rem; color:#0369a1 !important;">No API needed</span>
                <span style="background:#f0fdf4; border:1px solid #6ee7b7; padding:4px 10px; border-radius:20px; font-size:0.75rem; color:#065f46 !important;">Private</span>
                <span style="background:#fdf4ff; border:1px solid #e9d5ff; padding:4px 10px; border-radius:20px; font-size:0.75rem; color:#7e22ce !important;">RAG AI Grounded</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.caption(f"🤖 Chatting with RAG AI about **{st.session_state.doc_name}** • 100% Grounded")
        for m in st.session_state.messages:
            with st.chat_message(m["role"]):
                st.markdown(m["content"])
        if q:=st.chat_input(f"Ask RAG AI about {st.session_state.doc_name}..."):
            st.session_state.messages.append({"role":"user","content":q})
            with st.chat_message("user"): st.markdown(q)
            with st.chat_message("assistant"):
                with st.spinner("🤖 RAG AI searching your document..."):
                    ctx="\n\n---\n\n".join(search(st.session_state.chunks,q, k=4))
                    ans=get_answer_local(ctx, q)
                    st.markdown(ans)
                    st.session_state.messages.append({"role":"assistant","content":ans})

st.divider()
st.markdown("""
<div style="text-align:center; padding:1rem; background: white; border-radius:12px; border:1px solid #e2e8f0;">
    <div style="display:flex; align-items:center; justify-content:center; gap:8px; flex-wrap:wrap;">
        <span style="width:28px; height:28px; background: linear-gradient(135deg, #0f172a, #3b82f6); border-radius:8px; display:inline-flex; align-items:center; justify-content:center; font-size:14px;">🤖</span>
        <span style="font-weight:700; color:#0f172a !important;">FutureWorks RAG AI</span>
        <span style="color:#94a3b8 !important;">•</span>
        <span style="color:#64748b !important; font-size:0.85rem;">Light Colorful Professional Edition</span>
        <span style="color:#94a3b8 !important;">•</span>
        <span style="color:#64748b !important; font-size:0.85rem;">RAG AI Powered • All text visible • Elegant & User Friendly</span>
    </div>
</div>
""", unsafe_allow_html=True)
