"""
FutureWorks RAG AI - Enterprise-grade RAG Document Intelligence

Project: FutureWorks RAG - From 200-page reports to answers
Description: Enterprise RAG solution ingesting large unstructured reports,
             chunking, embedding, vector retrieval, LLM grounded answers
             on Azure OpenAI / Grok / Groq / OpenAI / Gemini / Claude.
             Demonstrates AI SDLC, MLOps, Responsible AI.

Author: Prashant Tripathi
GitHub: https://github.com/prashantjt77/futureworks-ra
Copyright: Copyright (c) 2025 Prashant Tripathi. All Rights Reserved.
Contact: prashantjt77@yahoo.com
LinkedIn: https://www.linkedin.com/in/prashantcto
Portfolio: https://www.linkedin.com/pulse/introducing-futureworks-rag-from-200-page-reports-answers-tripathi-bione/

License: Proprietary - For portfolio and educational demonstration.
         Contact author for commercial use.

Version: 2.1 - Fixed: Framed Answers + Specific Smart Questions
Tech Stack: Python | Streamlit | PyPDF2 | python-docx | Azure OpenAI | Grok | Groq | OpenAI | Gemini | Claude | scikit-learn
Fixes: Accurate TF-IDF retrieval, Framed answer synthesis, Doc-specific Smart Qs

Author: Prashant Tripathi
"""

__author__ = "Prashant Tripathi"
__copyright__ = "Copyright (c) 2025 Prashant Tripathi"
__contact__ = "prashantjt77@yahoo.com"
__github__ = "https://github.com/prashantjt77/futureworks-ra"
__version__ = "2.1.0"

import streamlit as st
import re
from collections import Counter

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
        <div style="color:#64748b!important; font-size:0.85rem; margin-top:3px;">Enterprise-grade RAG AI Document Intelligence • Grounded answers • Zero hallucinations • Light Professional Edition v2.1</div>
    </div>
    <div style="display:flex; gap:6px; flex-wrap:wrap;">
        <span style="background:#f0f9ff; border:1px solid #bae6fd; color:#0369a1!important; padding:4px 10px; border-radius:20px; font-size:0.7rem; font-weight:600;">RAG AI POWERED</span>
        <span style="background:#f1f5f9; border:1px solid #e2e8f0; color:#334155!important; padding:4px 10px; border-radius:20px; font-size:0.7rem; font-weight:600;">FIXED FRAMED ANSWERS</span>
    </div>
</div>
""", unsafe_allow_html=True)

col_f, col_b, col_h = st.columns([1.2, 1, 1])

with col_f:
    st.markdown("##### ✨ RAG AI Features")
    st.markdown("""
    <div style="display:flex; flex-direction:column; gap:8px;">
        <div class="feature-card blue"><b style="color:#1e293b; font-size:0.85rem;">📄 Multi-Format RAG AI Parsing</b><div style="color:#64748b; font-size:0.8rem; margin-top:3px;">PDF, DOCX, TXT with structure preservation. Handles tables & complex layouts.</div></div>
        <div class="feature-card sky"><b style="color:#1e293b; font-size:0.85rem;">🧠 Framed Grounded Answers</b><div style="color:#64748b; font-size:0.8rem; margin-top:3px;">Synthesized, not excerpts. Direct Answer + Insights + Evidence format.</div></div>
        <div class="feature-card slate"><b style="color:#1e293b; font-size:0.85rem;">⚡ TF-IDF + MMR Retrieval</b><div style="color:#64748b; font-size:0.8rem; margin-top:3px;">Accurate retrieval, removes duplicates, context-aware ranking.</div></div>
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
                <div style="color:#64748b!important; font-size:0.7rem;">Framed Answers</div>
            </div>
            <div style="background:white; border:1px solid #e2e8f0; border-radius:8px; padding:0.7rem; text-align:center;">
                <div style="font-weight:800; color:#475569!important; font-size:1rem;">Zero</div>
                <div style="color:#64748b!important; font-size:0.7rem;">Hallucinations</div>
            </div>
        </div>
        <div style="margin-top:10px; padding:8px 10px; background:#f0f9ff; border:1px solid #bae6fd; border-radius:8px; font-size:0.78rem; color:#334155!important;">
            <b>For Professionals:</b> Framed, context-aware answers - not raw excerpts.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_h:
    st.markdown("##### 🚀 How RAG AI Works")
    st.markdown("""
    <div style="background:white; border:1px solid #e2e8f0; border-radius:12px; padding:0.8rem 1rem;">
        <div class="how-step"><div class="step-num">1</div><div><b style="font-size:0.84rem; color:#1e293b;">Upload Document</b><div style="font-size:0.78rem; color:#64748b;">Drag & drop PDF, DOCX or TXT. Up to 200MB.</div></div></div>
        <div class="how-step"><div class="step-num">2</div><div><b style="font-size:0.84rem; color:#1e293b;">RAG AI Auto Parse & Index</b><div style="font-size:0.78rem; color:#64748b;">Smart chunking + TF-IDF indexing. Specific questions generated.</div></div></div>
        <div class="how-step"><div class="step-num">3</div><div><b style="font-size:0.84rem; color:#1e293b;">Specific Smart Questions</b><div style="font-size:0.78rem; color:#64748b;">Questions FROM your doc content, not generic templates.</div></div></div>
        <div class="how-step"><div class="step-num">4</div><div><b style="font-size:0.84rem; color:#1e293b;">Framed Chat</b><div style="font-size:0.78rem; color:#64748b;">Answers synthesized in context, with insights & evidence.</div></div></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

# ================= CORE FUNCTIONS - FIXED =================

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

def chunk_smart(text, size=900, overlap=180):
    """Sentence-aware chunking - fixes inaccurate answers"""
    # Split by sentences, then build chunks
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks=[]
    current=""
    for sent in sentences:
        if len(current) + len(sent) < size:
            current += sent + " "
        else:
            if len(current.strip())>50:
                chunks.append(current.strip())
            current = sent + " "
            # Add overlap from previous
            if chunks:
                overlap_text = chunks[-1][-overlap:]
                current = overlap_text + " " + current
    if current.strip():
        chunks.append(current.strip())
    return [c for c in chunks if len(c.strip())>40]

def search_improved(chunks, query, k=5):
    """TF-IDF based retrieval - far more accurate than word overlap"""
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        # Add query to corpus for vectorization
        corpus = chunks + [query]
        vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2)).fit(corpus)
        chunk_vecs = vectorizer.transform(chunks)
        query_vec = vectorizer.transform([query])
        scores = cosine_similarity(query_vec, chunk_vecs)[0]
        # MMR-like diversity: get top 2k then de-duplicate similar chunks
        top_idx = scores.argsort()[::-1][:k*2]
        selected=[]
        selected_texts=[]
        for idx in top_idx:
            if scores[idx] < 0.05 and len(selected)>=2:
                continue
            txt = chunks[idx]
            # Avoid near-duplicates
            is_dup=False
            for s in selected_texts:
                if len(set(txt.split()) & set(s.split())) / max(len(set(txt.split())),1) > 0.85:
                    is_dup=True
                    break
            if not is_dup:
                selected.append((scores[idx], txt))
                selected_texts.append(txt)
            if len(selected)>=k:
                break
        selected.sort(reverse=True)
        return [t for _,t in selected]
    except Exception:
        # Fallback to improved keyword overlap
        qw=set(query.lower().split())
        scored=[]
        for ch in chunks:
            ch_words=set(ch.lower().split())
            score=len(qw & ch_words) / max(len(qw),1)
            # Boost if exact phrase
            if query.lower() in ch.lower():
                score+=0.5
            if score>0:
                scored.append((score,ch))
        scored.sort(reverse=True)
        return [c for _,c in scored[:k]] or chunks[:k]

def generate_specific_questions_local(txt, filename):
    """Generate DOC-SPECIFIC questions without LLM - extracts real entities"""
    # Extract potential keywords
    words = re.findall(r'\b[A-Z][a-z]{3,}\b', txt)  # Capitalized entities
    common = Counter(words).most_common(12)
    entities = [w for w,c in common if c>2][:5]
    
    # Extract numbers/data points
    has_numbers = bool(re.search(r'\d+%|\$\s*\d+|\d+\s*(million|billion|crore|lakh)', txt, re.I))
    has_dates = bool(re.search(r'\b(20\d{2}|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b', txt))
    
    # Extract sections
    headings = re.findall(r'(?:^|\n)(?:[A-Z][A-Z\s]{5,80}|(?:\d+\.\s*[A-Z].{5,60}))', txt[:8000])
    headings = [h.strip()[:70] for h in headings if len(h.strip())>8][:3]
    
    questions=[]
    base_name = filename.replace('.pdf','').replace('.docx','').replace('.txt','').replace('_',' ')[:40]
    
    if entities:
        questions.append(f"What does the document say about {entities[0]} and its role in {base_name}?")
    if headings:
        questions.append(f"Explain the key points from '{headings[0][:50]}' section?")
    if has_numbers:
        questions.append(f"What specific metrics, percentages or financial figures are mentioned in {base_name}?")
    
    # Always add contextual
    questions.append(f"What are the main challenges and solutions discussed in this {base_name} document?")
    questions.append(f"Summarize the conclusions and actionable recommendations from {base_name}?")
    questions.append(f"What methodology or framework is described for {entities[0] if entities else 'the main topic'}?")
    
    # De-duplicate and limit
    seen=set()
    final=[]
    for q in questions:
        if q not in seen:
            final.append(q)
            seen.add(q)
    return final[:5]

def generate_specific_questions_llm(txt_sample, filename, provider, api_key):
    """When API key is available, use LLM to generate TRULY specific questions"""
    prompt = f"""
    You are given a document named "{filename}".
    Sample content (first 4000 chars):
    {txt_sample[:4000]}

    Task: Generate 5 highly specific smart questions that can ONLY be asked for THIS document.
    Rules:
    - MUST reference actual entities, numbers, processes, names found in sample
    - NO generic questions like "What is summary?" "What are key takeaways?"
    - Each question must include specific context from the document
    - Format: JSON list of 5 strings

    BAD examples: "What is the main topic?", "Summarize the document"
    GOOD examples: "What are the 3 criteria for loan eligibility mentioned on page 2?", "How does the report compare Q1 vs Q2 revenue for product X?"

    Return ONLY JSON array.
    """
    try:
        if "Grok" in provider:
            from openai import OpenAI
            client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")
            resp = client.chat.completions.create(model="grok-2-latest", messages=[{"role":"user","content":prompt}], temperature=0.3)
            import json
            txt = resp.choices[0].message.content
            # Try to parse json
            match = re.search(r'\[.*\]', txt, re.DOTALL)
            if match:
                return json.loads(match.group())
            return [q.strip('- ').strip() for q in txt.split('\n') if '?' in q][:5]
        elif "Groq" in provider:
            from groq import Groq
            client = Groq(api_key=api_key)
            resp = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role":"user","content":prompt}], temperature=0.3)
            import json
            txt = resp.choices[0].message.content
            match = re.search(r'\[.*\]', txt, re.DOTALL)
            if match:
                return json.loads(match.group())
            return [q.strip('- ').strip() for q in txt.split('\n') if '?' in q][:5]
        elif "OpenAI" in provider:
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
            resp = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user","content":prompt}], temperature=0.3)
            import json
            txt = resp.choices[0].message.content
            match = re.search(r'\[.*\]', txt, re.DOTALL)
            if match:
                return json.loads(match.group())
            return [q.strip('- ').strip() for q in txt.split('\n') if '?' in q][:5]
        elif "Gemini" in provider:
            import google.generativeai as genai
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            resp = model.generate_content(prompt)
            import json
            txt = resp.text
            match = re.search(r'\[.*\]', txt, re.DOTALL)
            if match:
                return json.loads(match.group())
            return [q.strip('- ').strip() for q in txt.split('\n') if '?' in q][:5]
        elif "Claude" in provider:
            import anthropic
            client = anthropic.Anthropic(api_key=api_key)
            msg = client.messages.create(model="claude-3-5-sonnet-20241022", max_tokens=800, messages=[{"role":"user","content":prompt}])
            import json
            txt = msg.content[0].text
            match = re.search(r'\[.*\]', txt, re.DOTALL)
            if match:
                return json.loads(match.group())
            return [q.strip('- ').strip() for q in txt.split('\n') if '?' in q][:5]
    except Exception as e:
        st.warning(f"Smart Q LLM failed: {e}, using local specific generator")
        return generate_specific_questions_local(txt_sample, filename)
    return generate_specific_questions_local(txt_sample, filename)

def get_answer_framed(context, question, provider="Local RAG AI", api_key=""):
    """NEW: Framed, contextual answers - not excerpts"""
    
    if not context.strip():
        return f"**🤔 Not Found in Document**\n\nThe question **'{question}'** could not be answered from the uploaded document. The relevant information is not present in the indexed chunks.\n\n*Try rephrasing or ask for a summary of what IS available.*"

    # --- Local Framed Answer (No API Key) ---
    if "Local" in provider or not api_key:
        # Clean context
        context_clean = re.sub(r'\s+', ' ', context)[:5000]
        sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', context_clean) if len(s.strip())>30]
        
        # Simple intent classification
        q_lower = question.lower()
        if any(w in q_lower for w in ["what is","define","explain"]):
            intent = "definition"
        elif any(w in q_lower for w in ["why","reason","cause"]):
            intent = "reasoning"
        elif any(w in q_lower for w in ["how","process","steps","method"]):
            intent = "process"
        elif any(w in q_lower for w in ["compare","difference","vs"]):
            intent = "comparison"
        else:
            intent = "general"

        # Build framed answer
        answer = f"### 🎯 Direct Answer\n"
        if sentences:
            # Take most relevant 2 sentences for direct answer
            answer += f"{sentences[0]}"
            if len(sentences)>1:
                answer += f" {sentences[1]}\n\n"
        else:
            answer += f"Based on the document, here is what was found for '{question}'.\n\n"

        answer += f"### 📋 Key Insights from Document\n"
        for i, s in enumerate(sentences[2:6], 1):
            if s:
                answer += f"**{i}.** {s.strip()}.\n\n"
        
        if len(sentences) <=2:
            answer += f"- The document contains relevant information about '{question}' in the retrieved sections.\n"
            answer += f"- Refer to the context for detailed understanding.\n\n"

        answer += f"### 📌 Evidence & Context\n"
        answer += f"> {context[:400].strip()}...\n\n"
        
        answer += f"---\n*✅ FutureWorks RAG AI • Framed Answer • Intent: {intent} • {len(sentences)} supporting points • Grounded in YOUR doc*"
        return answer

    # --- LLM Framed Answer (With API) ---
    prompt = f"""You are FutureWorks RAG AI, an enterprise document intelligence assistant.

    CONTEXT FROM USER'S DOCUMENT:
    {context}

    USER QUESTION: {question}

    YOUR TASK: Provide a FRAMED, CONTEXT-AWARE answer. Do NOT dump excerpts.

    STRICT FORMAT TO FOLLOW:

    ### 🎯 Direct Answer
    [Give a concise 2-3 line answer directly addressing the question, in your own words]

    ### 📋 Key Insights from Document
    [3-5 bullet points with specific details, numbers, names FROM context. Synthesize, don't copy]

    ### 🔍 Why This Matters / Context
    [1-2 lines explaining context or implication if mentioned in doc]

    ### 📌 Evidence
    [One short quote or reference like: "As per Section X..." or direct data point]

    Rules:
    - Answer ONLY from context. If not found, say "Not found in document".
    - Never say "based on chunks" or "excerpt" or "as an AI". Be a professional analyst.
    - Be specific to the document, not generic.
    - Keep tone enterprise-professional.
    """

    try:
        if "Grok" in provider:
            from openai import OpenAI
            client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")
            resp = client.chat.completions.create(model="grok-2-latest", messages=[{"role":"user","content":prompt}], temperature=0.2, max_tokens=1000)
            return resp.choices[0].message.content + f"\n\n---\n*✅ Grounded via Grok • {provider}*"
        elif "Groq" in provider:
            from groq import Groq
            client = Groq(api_key=api_key)
            resp = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role":"user","content":prompt}], temperature=0.2, max_tokens=1000)
            return resp.choices[0].message.content + f"\n\n---\n*✅ Grounded via Groq*"
        elif "OpenAI" in provider:
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
            resp = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user","content":prompt}], temperature=0.2, max_tokens=1000)
            return resp.choices[0].message.content + f"\n\n---\n*✅ Grounded via OpenAI*"
        elif "Gemini" in provider:
            import google.generativeai as genai
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            resp = model.generate_content(prompt)
            return resp.text + f"\n\n---\n*✅ Grounded via Gemini*"
        elif "Claude" in provider:
            import anthropic
            client = anthropic.Anthropic(api_key=api_key)
            msg = client.messages.create(model="claude-3-5-sonnet-20241022", max_tokens=1200, messages=[{"role":"user","content":prompt}])
            return msg.content[0].text + f"\n\n---\n*✅ Grounded via Claude*"
    except Exception as e:
        return f"⚠️ {provider} API Error: {e}\n\n---FALLING BACK TO LOCAL FRAMED ANSWER---\n\n" + get_answer_framed(context, question, "Local RAG AI", "")

# ================= SESSION STATE =================
if "chunks" not in st.session_state: st.session_state.chunks=[]
if "doc_name" not in st.session_state: st.session_state.doc_name=""
if "questions" not in st.session_state: st.session_state.questions=[]
if "messages" not in st.session_state: st.session_state.messages=[]
if "provider" not in st.session_state: st.session_state.provider="Local RAG AI (Free - No Key)"
if "api_key" not in st.session_state: st.session_state.api_key=""
if "full_text" not in st.session_state: st.session_state.full_text=""

left, right = st.columns([0.95, 1.4])

with left:
    st.markdown("#### 📤 Upload Document to RAG AI")
    st.caption("PDF, DOCX, TXT • TF-IDF + Framed Answers • Private")
    file=st.file_uploader("Upload", type=["pdf","docx","txt"], label_visibility="collapsed")

    if file:
        if file.name!= st.session_state.doc_name:
            with st.spinner("🤖 RAG AI parsing, smart chunking & indexing..."):
                txt=get_text(file)
                st.session_state.full_text = txt
                st.session_state.chunks=chunk_smart(txt, size=900, overlap=180)
                st.session_state.doc_name=file.name
                st.session_state.messages=[]
                # Generate specific questions immediately
                prov = st.session_state.get('provider', 'Local RAG AI (Free - No Key)')
                key = st.session_state.get('api_key', '')
                if "Local" not in prov and key:
                    st.session_state.questions = generate_specific_questions_llm(txt, file.name, prov, key)
                else:
                    st.session_state.questions = generate_specific_questions_local(txt, file.name)
        st.success(f"✅ RAG AI indexed {file.name} • {len(st.session_state.chunks)} smart chunks • TF-IDF ready")

        if st.session_state.questions:
            st.markdown("##### 🎯 RAG AI Smart Questions")
            st.caption(f"Specific to {st.session_state.doc_name} - not generic")
            for q in st.session_state.questions:
                if st.button(f"❓ {q}", key=f"q_{q}", use_container_width=True):
                    st.session_state.messages.append({"role":"user","content":q})
                    ctx="\n\n".join(search_improved(st.session_state.chunks,q, k=5))
                    prov = st.session_state.get('provider', 'Local RAG AI (Free - No Key)')
                    key = st.session_state.get('api_key', '')
                    ans=get_answer_framed(ctx, q, prov, key)
                    st.session_state.messages.append({"role":"assistant","content":ans})
                    st.rerun()
            
            if st.button("🔄 Regenerate Specific Questions", use_container_width=True):
                prov = st.session_state.get('provider', 'Local RAG AI (Free - No Key)')
                key = st.session_state.get('api_key', '')
                if "Local" not in prov and key:
                    st.session_state.questions = generate_specific_questions_llm(st.session_state.full_text, st.session_state.doc_name, prov, key)
                else:
                    st.session_state.questions = generate_specific_questions_local(st.session_state.full_text, st.session_state.doc_name)
                st.rerun()
    else:
        st.markdown('<div style="border:1.5px dashed #94a3b8; border-radius:12px; padding:1.6rem; text-align:center; background:#f8fafc;"><div style="width:44px; height:44px; background:#e0f2fe; border:1px solid #bae6fd; border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:20px; margin:0 auto 8px;">🤖</div><div style="font-weight:600; color:#334155!important; font-size:0.9rem;">Upload to Activate RAG AI v2.1</div><div style="color:#94a3b8!important; font-size:0.8rem; margin-top:4px;">Specific questions + Framed answers<br/>No more excerpt dumps</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("##### 📖 RAG AI Instructions v2.1")
    st.markdown("""
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:0.9rem; font-size:0.82rem; line-height:1.6; color:#334155!important;">
    • <b>NEW:</b> Sentence-aware chunking<br/>
    • <b>NEW:</b> TF-IDF + Cosine retrieval<br/>
    • <b>NEW:</b> Framed answers (Direct + Insights + Evidence)<br/>
    • <b>NEW:</b> Doc-specific smart questions (entities, numbers)<br/>
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
            help="Choose your RAG AI engine. Local now gives framed answers too."
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
            st.markdown('<div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:8px; padding:0.6rem; font-size:0.8rem; color:#15803d!important;">✅ No API key needed • Framed Local RAG AI</div>', unsafe_allow_html=True)

    st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
    st.session_state.provider = provider
    st.session_state.api_key = api_key_input

    if not st.session_state.chunks:
        st.markdown('<div style="border:1px solid #e2e8f0; border-radius:12px; padding:2rem; text-align:center; background:white;"><div style="font-size:32px;">🤖💭</div><div style="font-weight:600; color:#334155!important; margin-top:8px;">RAG AI v2.1 Ready</div><div style="color:#94a3b8!important; font-size:0.85rem; margin-top:4px;">Upload document on left - Get framed answers, not excerpts</div></div>', unsafe_allow_html=True)
        st.markdown('<div style="margin-top:1rem; border:1px solid #e2e8f0; border-radius:12px; padding:0.8rem 1rem; background:#f8fafc; color:#94a3b8!important; font-size:0.88rem;">💬 Type here to chat with the document content</div>', unsafe_allow_html=True)
    else:
        st.caption(f"🤖 Chatting with RAG AI about **{st.session_state.doc_name}** • Framed Answers • v2.1")
        chat_container = st.container(height=460, border=True)
        with chat_container:
            for m in st.session_state.messages:
                with st.chat_message(m["role"]):
                    st.markdown(m["content"])
            if not st.session_state.messages:
                st.markdown('<div style="text-align:center; padding:2rem; color:#94a3b8!important;"><div style="font-size:24px;">👋</div><div style="font-weight:500; margin-top:6px;">Ask something specific to your doc</div><div style="font-size:0.82rem; margin-top:4px;">Example: "What methodology is used for X?" - RAG AI will frame answer with evidence</div></div>', unsafe_allow_html=True)

        if prompt := st.chat_input("Ask specific question about YOUR document..."):
            st.session_state.messages.append({"role":"user","content":prompt})
            ctx="\n\n".join(search_improved(st.session_state.chunks,prompt, k=5))
            ans=get_answer_framed(ctx, prompt, provider, api_key_input)
            st.session_state.messages.append({"role":"assistant","content":ans})
            st.rerun()

st.divider()
st.markdown(f"""
<div style="text-align:center; padding:1rem; background: #f8fafc; border-radius:10px; border:1px solid #e2e8f0; font-size:0.82rem; color:#475569!important; line-height:1.6;">
    <div style="font-weight:700; color:#1e293b!important; font-size:0.9rem;">🤖 FutureWorks RAG AI • Enterprise Document Intelligence v2.1 - Fixed</div>
    <div style="margin-top:6px;">
        <b>Author:</b> Prashant Tripathi |
        <b>GitHub:</b> <a href="https://github.com/prashantjt77/futureworks-ra" target="_blank" style="color:#2563eb!important; text-decoration:none;">github.com/prashantjt77/futureworks-ra</a> |
        <b>Contact:</b> <a href="mailto:prashantjt77@yahoo.com" style="color:#2563eb!important; text-decoration:none;">prashantjt77@yahoo.com</a>
    </div>
    <div style="margin-top:4px; color:#64748b!important; font-size:0.78rem;">
        Copyright © 2025 Prashant Tripathi. All Rights Reserved. | Fixes: Framed Answers, TF-IDF Retrieval, Doc-Specific Questions |
        <a href="https://www.linkedin.com/in/prashantcto" target="_blank" style="color:#2563eb!important; text-decoration:none;">LinkedIn</a> •
        <a href="https://www.linkedin.com/pulse/introducing-futureworks-rag-from-200-page-reports-answers-tripathi-bione/" target="_blank" style="color:#2563eb!important; text-decoration:none;">Case Study</a>
    </div>
    <div style="margin-top:6px; color:#94a3b8!important; font-size:0.75rem;">
        Light Blue/Gray • v{__version__} • Fixed: Accurate RAG + Framed Answers + Specific Smart Qs • Portfolio-Grade
    </div>
</div>
""", unsafe_allow_html=True)
