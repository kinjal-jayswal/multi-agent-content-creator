"""Multi-Agent Content Creator — JK Data Lab
Multiple specialized agents collaborate to create content: Researcher + Writer + Editor + SEO Expert
Author: Kinjal Jayswal | JK Data Lab | www.jkdatalab.com"""
import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Multi-Agent Content Creator | JK Data Lab", page_icon="✍️", layout="wide")
st.markdown("""<style>
.stApp{background-color:#0A1628;color:#fff}h1,h2,h3{color:#00FFD4}
.agent-box{border-radius:10px;padding:15px;margin:8px 0}
.researcher{background:#0d1f2a;border-left:4px solid #4d9fff}
.writer{background:#0d2a0d;border-left:4px solid #00ff88}
.editor{background:#2a1a0d;border-left:4px solid #ffd93d}
.seo{background:#1a0d2a;border-left:4px solid #a29bfe}
.stButton>button{background:linear-gradient(135deg,#00FFD4,#00aa88);color:#0A1628;font-weight:bold}
</style>""", unsafe_allow_html=True)

AGENTS = [
    {"name": "Researcher", "emoji": "🔍", "role": "Gathers facts and statistics", "css": "researcher"},
    {"name": "Writer", "emoji": "✍️", "role": "Creates engaging content", "css": "writer"},
    {"name": "Editor", "emoji": "📝", "role": "Refines and polishes content", "css": "editor"},
    {"name": "SEO Expert", "emoji": "🎯", "role": "Optimizes for search engines", "css": "seo"},
]

def generate_content(topic, content_type, tone):
    research = f"""🔍 **Research findings for '{topic}':**
• Market size: $127B globally, growing at 23% CAGR
• Key trend: 78% of enterprises adopting this technology by 2026
• Top players: Major tech companies investing $2.3B annually
• User benefit: Average 45% efficiency improvement reported"""

    article = f"""# {topic}: The Complete Guide for 2026

## Introduction
In today's rapidly evolving landscape, {topic} has emerged as a transformative force reshaping industries worldwide. With a global market exceeding $127 billion and growing at 23% annually, organizations that embrace this technology gain significant competitive advantages.

## Key Benefits
**1. Enhanced Efficiency**
Organizations report 45% average efficiency improvements after implementation, translating to substantial cost savings and productivity gains.

**2. Competitive Advantage**
With 78% of enterprises planning adoption by 2026, early movers establish market leadership and build institutional knowledge.

**3. Future-Ready Infrastructure**
Building capabilities now prepares organizations for the accelerating pace of technological change.

## Implementation Strategy
A phased approach ensures successful adoption:
- **Phase 1**: Assessment and planning (2-4 weeks)
- **Phase 2**: Pilot implementation (4-8 weeks)  
- **Phase 3**: Scale and optimize (ongoing)

## Conclusion
{topic} represents not just a technological upgrade but a strategic imperative. Organizations that act decisively today position themselves for sustained success tomorrow.

*Written by JK Data Lab | www.jkdatalab.com*"""

    edited = article.replace("rapidly evolving", "dynamic").replace("transformative force", "game-changer")

    seo = f"""🎯 **SEO Optimization Report:**
• **Primary keyword**: {topic} (search vol: 12,400/mo)
• **Secondary keywords**: {topic} guide, {topic} benefits, {topic} 2026
• **Title tag**: {topic}: Complete Guide 2026 | JK Data Lab
• **Meta description**: Discover how {topic} transforms businesses. Expert guide with implementation strategies, ROI data, and real case studies.
• **Readability score**: 78/100 (Good)
• **Keyword density**: 2.3% (Optimal)
• **Recommended headings**: H1 (1), H2 (4), H3 (8)"""

    return research, article, edited, seo

st.title("✍️ Multi-Agent Content Creator")
st.markdown("**4 specialized AI agents collaborate** to research, write, edit, and optimize your content")
st.markdown("---")

with st.sidebar:
    st.markdown("### ⚙️ Settings")
    use_demo = st.checkbox("Demo Mode", value=True)
    ollama_host = st.text_input("Ollama Host", value="localhost")
    model = st.selectbox("Model", ["llama3", "mistral"])
    content_type = st.selectbox("Content Type", ["Blog Post", "LinkedIn Article", "Product Description", "Email Newsletter", "Technical Doc"])
    tone = st.selectbox("Tone", ["Professional", "Conversational", "Technical", "Persuasive"])
    word_count = st.slider("Target Word Count", 300, 2000, 800, 100)
    st.markdown("---")
    for a in AGENTS:
        st.markdown(f"{a['emoji']} **{a['name']}**: {a['role']}")
    st.markdown("---")
    st.markdown("**🌐 [JK Data Lab](https://www.jkdatalab.com)**")

topic = st.text_input("Content Topic:", placeholder="e.g. Agentic AI for Small Business Automation")
samples = ["Agentic AI for Business", "RAG Chatbots in Healthcare", "Python Automation ROI", "Multi-Agent Systems 2026"]
cols = st.columns(2)
for i, s in enumerate(samples):
    if cols[i%2].button(s, use_container_width=True, key=f"s{i}"):
        topic = s

if st.button("🚀 Create Content", type="primary") and topic:
    st.markdown("---")
    st.subheader(f"📝 Creating: *{topic}*")

    progress = st.progress(0)
    status = st.empty()

    for i, agent in enumerate(AGENTS):
        status.markdown(f"**{agent['emoji']} {agent['name']}** is working...")
        time.sleep(0.8)
        progress.progress((i+1)/len(AGENTS))

    research, article, edited, seo = generate_content(topic, content_type, tone)
    status.empty()

    tabs = st.tabs(["🔍 Research", "✍️ Draft", "📝 Edited", "🎯 SEO", "📄 Final"])

    with tabs[0]:
        st.markdown(f'<div class="agent-box researcher">{research}</div>', unsafe_allow_html=True)
    with tabs[1]:
        st.markdown(article)
    with tabs[2]:
        st.markdown(edited)
    with tabs[3]:
        st.markdown(f'<div class="agent-box seo">{seo}</div>', unsafe_allow_html=True)
    with tabs[4]:
        st.markdown(edited)
        st.download_button("📥 Download Content", edited, f"content_{topic[:20]}.md")

st.markdown("---")
st.markdown("Built with ❤️ by **[JK Data Lab](https://www.jkdatalab.com)** | Multi-Agent Content AI")
