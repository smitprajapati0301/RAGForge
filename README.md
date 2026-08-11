<div align="center">

<h1>🔥 RAGForge</h1>

<h3>Production-Oriented Retrieval-Augmented Generation Platform</h3>

<p>
  <strong>
    Upload Documents → Retrieve Knowledge → Generate Grounded Answers → View Sources
  </strong>
</p>

<br>

<a href="https://github.com/smitprajapati0301/RAGForge">
  <img src="https://img.shields.io/badge/GitHub-RAGForge-181717?style=for-the-badge&logo=github" alt="GitHub">
</a>

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">

<img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">

<img src="https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">

<img src="https://img.shields.io/badge/ChromaDB-Vector_DB-F97316?style=for-the-badge" alt="ChromaDB">

<img src="https://img.shields.io/badge/Groq-LLM-F97316?style=for-the-badge" alt="Groq">

<br><br>

<img src="https://img.shields.io/github/stars/smitprajapati0301/RAGForge?style=flat-square" alt="Stars">

<img src="https://img.shields.io/github/forks/smitprajapati0301/RAGForge?style=flat-square" alt="Forks">

<img src="https://img.shields.io/github/license/smitprajapati0301/RAGForge?style=flat-square" alt="License">

</div>

<hr>

<h2>🧠 About RAGForge</h2>

<p>
  <strong>RAGForge</strong> is an end-to-end
  <strong>Retrieval-Augmented Generation (RAG)</strong> platform designed
  for intelligent document question answering.
</p>

<p>
  The system allows users to upload documents and ask questions about
  their content. Instead of relying only on the internal knowledge of an
  LLM, RAGForge retrieves relevant information from indexed documents and
  provides that information to the LLM as grounded context.
</p>

<p>
  The main goal of this project was not simply to call an LLM API, but to
  understand and implement the individual components that make up a modern
  RAG system.
</p>

<br>

<div align="center">

<table>
<tr>
<td align="center">📄<br><strong>Document</strong></td>
<td>→</td>
<td align="center">✂️<br><strong>Chunking</strong></td>
<td>→</td>
<td align="center">🧮<br><strong>Embeddings</strong></td>
<td>→</td>
<td align="center">🗄️<br><strong>Vector Store</strong></td>
</tr>

<tr>
<td colspan="7" align="center">↓</td>
</tr>

<tr>
<td align="center">🔎<br><strong>Hybrid Retrieval</strong></td>
<td>→</td>
<td align="center">🔀<br><strong>RRF</strong></td>
<td>→</td>
<td align="center">🎯<br><strong>Re-ranking</strong></td>
<td>→</td>
<td align="center">📝<br><strong>Prompt</strong></td>
</tr>

<tr>
<td colspan="7" align="center">↓</td>
</tr>

<tr>
<td colspan="7" align="center">
<strong>🤖 Groq LLM → 💬 Answer + 📌 Citations</strong>
</td>
</tr>
</table>

</div>

<hr>

<h2>✨ Key Features</h2>

<table>
<tr>

<td width="50%" valign="top">

<h3>📚 Document Processing</h3>

<ul>
<li>PDF document ingestion</li>
<li>DOCX document ingestion</li>
<li>TXT document ingestion</li>
<li>Markdown document ingestion</li>
<li>Loader Factory pattern</li>
<li>Recursive text chunking</li>
<li>Chunk overlap</li>
<li>Metadata preservation</li>
</ul>

</td>

<td width="50%" valign="top">

<h3>🔍 Retrieval</h3>

<ul>
<li>Semantic vector search</li>
<li>BM25 keyword retrieval</li>
<li>Hybrid retrieval</li>
<li>Reciprocal Rank Fusion</li>
<li>Cross-Encoder re-ranking</li>
<li>Configurable top-k retrieval</li>
</ul>

</td>

</tr>

<tr>

<td width="50%" valign="top">

<h3>🤖 Generation</h3>

<ul>
<li>Groq API integration</li>
<li>Configurable LLM model</li>
<li>Grounded prompt generation</li>
<li>Context-aware responses</li>
<li>Configurable temperature</li>
<li>Configurable maximum tokens</li>
</ul>

</td>

<td width="50%" valign="top">

<h3>📌 Citations</h3>

<ul>
<li>Application-generated citations</li>
<li>Filename tracking</li>
<li>Page tracking</li>
<li>Chunk tracking</li>
<li>Source-aware responses</li>
<li>Reduced risk of fabricated sources</li>
</ul>

</td>

</tr>

<tr>

<td width="50%" valign="top">

<h3>🧪 Evaluation</h3>

<ul>
<li>RAGAS integration</li>
<li>Faithfulness evaluation</li>
<li>Answer Relevancy evaluation</li>
<li>Context Precision evaluation</li>
<li>Context Recall evaluation</li>
</ul>

</td>

<td width="50%" valign="top">

<h3>🌐 Application</h3>

<ul>
<li>FastAPI REST API</li>
<li>React frontend</li>
<li>Vite development environment</li>
<li>Axios API communication</li>
<li>Document upload interface</li>
<li>Question answering interface</li>
</ul>

</td>

</tr>
</table>

<hr>

<h2>🏗️ System Architecture</h2>

<div align="center">

<table border="1" cellpadding="12" cellspacing="0">

<tr>
<td colspan="3" align="center">
<strong>🖥️ React Frontend</strong><br>
Vite + React + Tailwind CSS
</td>
</tr>

<tr>
<td colspan="3" align="center">↓ Axios / HTTP ↓</td>
</tr>

<tr>
<td colspan="3" align="center">
<strong>⚡ FastAPI Backend</strong><br>
REST API
</td>
</tr>

<tr>

<td width="33%" align="center" valign="top">

<strong>📄 Document Ingestion</strong>

<br><br>

Loader Factory

<br>↓

PDF / DOCX / TXT / Markdown

<br>↓

Text Extraction

<br>↓

Cleaning

<br>↓

Chunking

<br>↓

Embeddings

<br>↓

ChromaDB

</td>

<td width="33%" align="center" valign="top">

<strong>🔎 Query Processing</strong>

<br><br>

User Question

<br>↓

Semantic Retrieval

<br>+

BM25 Retrieval

<br>↓

RRF

<br>↓

Cross-Encoder

<br>↓

Top Relevant Chunks

</td>

<td width="33%" align="center" valign="top">

<strong>🤖 Answer Generation</strong>

<br><br>

Retrieved Context

<br>↓

Citation Builder

<br>↓

Prompt Builder

<br>↓

Groq LLM

<br>↓

Answer

<br>+

Sources

</td>

</tr>

</table>

</div>

<hr>

<h2>🔄 Complete RAG Pipeline</h2>

<h3>1️⃣ Document Ingestion</h3>

<p>
RAGForge supports multiple document formats:
</p>

<table>
<tr>
<td align="center">📕 PDF</td>
<td align="center">📘 DOCX</td>
<td align="center">📄 TXT</td>
<td align="center">📝 Markdown</td>
</tr>
</table>

<p>
A <strong>Loader Factory</strong> identifies the uploaded file type and
selects the appropriate document loader.
</p>

<hr>

<h3>2️⃣ ✂️ Text Chunking</h3>

<p>
Large documents are divided into smaller pieces using
<strong>RecursiveCharacterTextSplitter</strong>.
</p>

<p>
The chunk size and overlap are controlled through:
</p>

<p>
<code>configs/config.yaml</code>
</p>

<p>
Overlapping chunks help preserve contextual information between
neighboring sections of a document.
</p>

<hr>

<h3>3️⃣ 🧮 Embedding Generation</h3>

<p>
Each text chunk is converted into a dense vector representation using:
</p>

<div align="center">

<h3>BAAI/bge-base-en-v1.5</h3>

</div>

<p>
These embeddings capture the semantic meaning of the text and allow
RAGForge to perform vector similarity search.
</p>

<hr>

<h3>4️⃣ 🗄️ Vector Storage</h3>

<p>
RAGForge currently uses <strong>ChromaDB</strong> for persistent vector
storage.
</p>

<p>
The vector database stores:
</p>

<ul>
<li>Chunk IDs</li>
<li>Chunk text</li>
<li>Embeddings</li>
<li>Document metadata</li>
<li>Source information</li>
</ul>

<hr>

<h3>5️⃣ 🔍 Semantic Retrieval</h3>

<p>
The user's question is converted into an embedding and compared with
stored document embeddings.
</p>

<p>
The most semantically similar chunks are returned as candidates.
</p>

<hr>

<h3>6️⃣ 🔤 BM25 Keyword Retrieval</h3>

<p>
RAGForge also performs keyword-based retrieval using
<strong>BM25</strong>.
</p>

<p>
BM25 is useful when exact words, technical terms, names, or phrases are
important to the query.
</p>

<hr>

<h3>7️⃣ 🔀 Hybrid Retrieval</h3>

<p>
Semantic retrieval and BM25 retrieval are combined to improve retrieval
coverage.
</p>

<div align="center">

<table>
<tr>
<td align="center">
<strong>🧠 Semantic Search</strong>
<br>
Meaning-based retrieval
</td>

<td align="center">
<strong>+</strong>
</td>

<td align="center">
<strong>🔤 BM25</strong>
<br>
Keyword-based retrieval
</td>

<td align="center">
<strong>↓</strong>
</td>

<td align="center">
<strong>🔀 Hybrid Results</strong>
</td>
</tr>
</table>

</div>

<hr>

<h3>8️⃣ 🔀 Reciprocal Rank Fusion</h3>

<p>
The rankings produced by semantic retrieval and BM25 are combined using
<strong>Reciprocal Rank Fusion (RRF)</strong>.
</p>

<p>
RRF assigns a score to each result based on its position in the
individual ranking lists and produces a unified ranking.
</p>

<hr>

<h3>9️⃣ 🎯 Cross-Encoder Re-ranking</h3>

<p>
The retrieved candidate chunks are passed to:
</p>

<div align="center">

<strong>cross-encoder/ms-marco-MiniLM-L-6-v2</strong>

</div>

<p>
The Cross-Encoder evaluates the relationship between the user's query
and each candidate chunk.
</p>

<table>
<tr>
<td align="center">
<strong>User Query</strong>
</td>
<td>+</td>
<td align="center">
<strong>Retrieved Chunk</strong>
</td>
<td>→</td>
<td align="center">
<strong>Relevance Score</strong>
</td>
</tr>
</table>

<p>
The candidates are then sorted by their relevance scores and the most
relevant chunks are selected.
</p>

<hr>

<h3>🔟 📌 Citation Generation</h3>

<p>
RAGForge generates citations from the metadata of retrieved chunks
rather than asking the LLM to invent source references.
</p>

<p>
A citation may contain:
</p>

<table>
<tr>
<th>Information</th>
<th>Example</th>
</tr>

<tr>
<td>Source</td>
<td>resume.docx</td>
</tr>

<tr>
<td>Page</td>
<td>2</td>
</tr>

<tr>
<td>Chunk</td>
<td>5</td>
</tr>
</table>

<hr>

<h3>1️⃣1️⃣ 📝 Grounded Prompt Generation</h3>

<p>
The retrieved context and generated citations are inserted into a
structured prompt.
</p>

<p>
The prompt instructs the LLM to use the retrieved information when
generating the answer.
</p>

<hr>

<h3>1️⃣2️⃣ 🤖 LLM Generation</h3>

<p>
RAGForge uses the <strong>Groq API</strong> to generate the final answer.
</p>

<p>
The LLM configuration is controlled through:
</p>

<p>
<code>configs/config.yaml</code>
</p>

<hr>

<h2>🧰 Technology Stack</h2>

<table border="1" cellpadding="10" cellspacing="0">

<tr>
<th>Category</th>
<th>Technology</th>
<th>Purpose</th>
</tr>

<tr>
<td>🐍 Language</td>
<td>Python</td>
<td>Core backend and RAG implementation</td>
</tr>

<tr>
<td>⚡ Backend</td>
<td>FastAPI</td>
<td>REST API</td>
</tr>

<tr>
<td>🖥️ Frontend</td>
<td>React</td>
<td>User interface</td>
</tr>

<tr>
<td>⚙️ Frontend Tooling</td>
<td>Vite</td>
<td>Frontend development and build</td>
</tr>

<tr>
<td>🎨 Styling</td>
<td>Tailwind CSS</td>
<td>Frontend styling</td>
</tr>

<tr>
<td>📡 API Client</td>
<td>Axios</td>
<td>Frontend-backend communication</td>
</tr>

<tr>
<td>📕 PDF Processing</td>
<td>PyMuPDF</td>
<td>PDF text extraction</td>
</tr>

<tr>
<td>📘 DOCX Processing</td>
<td>python-docx</td>
<td>DOCX text extraction</td>
</tr>

<tr>
<td>✂️ Chunking</td>
<td>LangChain Text Splitters</td>
<td>Recursive document chunking</td>
</tr>

<tr>
<td>🧮 Embeddings</td>
<td>Sentence Transformers</td>
<td>Dense vector embeddings</td>
</tr>

<tr>
<td>🧠 Embedding Model</td>
<td>BAAI/bge-base-en-v1.5</td>
<td>Semantic representation</td>
</tr>

<tr>
<td>🗄️ Vector Database</td>
<td>ChromaDB</td>
<td>Vector storage and similarity search</td>
</tr>

<tr>
<td>🔤 Keyword Retrieval</td>
<td>rank-bm25</td>
<td>BM25 retrieval</td>
</tr>

<tr>
<td>🔀 Fusion</td>
<td>RRF</td>
<td>Combining retrieval rankings</td>
</tr>

<tr>
<td>🎯 Re-ranking</td>
<td>Cross-Encoder</td>
<td>Candidate relevance scoring</td>
</tr>

<tr>
<td>🤖 LLM</td>
<td>Groq</td>
<td>Answer generation</td>
</tr>

<tr>
<td>🧪 Evaluation</td>
<td>RAGAS</td>
<td>RAG quality evaluation</td>
</tr>

<tr>
<td>🧪 Testing</td>
<td>pytest</td>
<td>Automated testing</td>
</tr>

<tr>
<td>⚙️ Configuration</td>
<td>YAML</td>
<td>Centralized configuration</td>
</tr>

</table>

<hr>

<h2>📁 Project Structure</h2>

<pre>
RAGForge/
│
├── .github/
│
├── app/
│   ├── api/
│   │   ├── routes/
│   │   └── schemas/
│   │
│   ├── citations/
│   ├── core/
│   ├── embeddings/
│   ├── evaluation/
│   ├── ingestion/
│   ├── llm/
│   ├── preprocessing/
│   ├── prompts/
│   ├── reranking/
│   ├── retrieval/
│   └── vectorstore/
│
├── configs/
│
├── data/
│   └── raw/
│
├── docs/
│
├── evals/
│
├── frontend/
│
├── scripts/
│
├── tests/
│
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
└── requirements.txt
</pre>

<hr>

<h2>⚙️ Configuration</h2>

<p>
RAGForge uses centralized YAML configuration instead of hardcoding
important model and retrieval parameters.
</p>

<p>
<strong>Configuration file:</strong>
<code>configs/config.yaml</code>
</p>

<pre>
embedding:
  model_name: "BAAI/bge-base-en-v1.5"

vector_db:
  provider: "chroma"
  collection_name: "ragforge"
  persist_directory: "./chroma_db"

retrieval:
  top_k: 10

reranking:
  enabled: true
  model_name: "cross-encoder/ms-marco-MiniLM-L-6-v2"

llm:
  provider: "groq"
  model_name: "llama-3.3-70b-versatile"
  temperature: 0.2
  max_tokens: 1024
</pre>

<hr>

<h2>🚀 Installation</h2>

<h3>1. Clone the repository</h3>

<pre>
git clone https://github.com/smitprajapati0301/RAGForge.git
cd RAGForge
</pre>

<h3>2. Create a Python virtual environment</h3>

<pre>
python -m venv .venv
</pre>

<h3>3. Activate the environment</h3>

<p><strong>Windows:</strong></p>

<pre>
.venv\Scripts\activate
</pre>

<h3>4. Install dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>5. Configure environment variables</h3>

<p>
Create a <code>.env</code> file in the project root:
</p>

<pre>
GROQ_API_KEY=your_groq_api_key
</pre>

<p>
<strong>⚠️ Never commit the <code>.env</code> file to GitHub.</strong>
</p>

<hr>

<h2>▶️ Running the Backend</h2>

<p>
From the project root:
</p>

<pre>
uvicorn app.main:app --reload
</pre>

<p>
The backend will be available at:
</p>

<pre>
http://127.0.0.1:8000
</pre>

<h3>Swagger API Documentation</h3>

<pre>
http://127.0.0.1:8000/docs
</pre>

<hr>

<h2>🌐 Running the Frontend</h2>

<pre>
cd frontend
npm install
npm run dev
</pre>

<p>
The frontend will normally be available at:
</p>

<pre>
http://localhost:5173
</pre>

<hr>

<h2>🔌 API Endpoints</h2>

<table border="1" cellpadding="10" cellspacing="0">

<tr>
<th>Method</th>
<th>Endpoint</th>
<th>Purpose</th>
</tr>

<tr>
<td><strong>GET</strong></td>
<td><code>/</code></td>
<td>Application status</td>
</tr>

<tr>
<td><strong>GET</strong></td>
<td><code>/health</code></td>
<td>Backend health check</td>
</tr>

<tr>
<td><strong>POST</strong></td>
<td><code>/documents/upload</code></td>
<td>Upload and index a document</td>
</tr>

<tr>
<td><strong>POST</strong></td>
<td><code>/query</code></td>
<td>Ask a question using the RAG pipeline</td>
</tr>

</table>

<hr>

<h2>📤 Document Upload Flow</h2>

<div align="center">

<table>
<tr>
<td align="center">📄 Upload</td>
<td>→</td>
<td align="center">📖 Load</td>
<td>→</td>
<td align="center">🧹 Clean</td>
<td>→</td>
<td align="center">✂️ Chunk</td>
<td>→</td>
<td align="center">🧮 Embed</td>
<td>→</td>
<td align="center">🗄️ Store</td>
</tr>
</table>

</div>

<hr>

<h2>💬 Query Flow</h2>

<div align="center">

<table>
<tr>
<td align="center">💬 Question</td>
<td>→</td>
<td align="center">🧠 Semantic Search</td>
<td>+</td>
<td align="center">🔤 BM25</td>
</tr>

<tr>
<td colspan="5" align="center">↓</td>
</tr>

<tr>
<td colspan="5" align="center">
🔀 <strong>RRF</strong>
</td>
</tr>

<tr>
<td colspan="5" align="center">↓</td>
</tr>

<tr>
<td colspan="5" align="center">
🎯 <strong>Cross-Encoder Re-ranking</strong>
</td>
</tr>

<tr>
<td colspan="5" align="center">↓</td>
</tr>

<tr>
<td colspan="5" align="center">
📌 <strong>Citations + Context</strong>
</td>
</tr>

<tr>
<td colspan="5" align="center">↓</td>
</tr>

<tr>
<td colspan="5" align="center">
🤖 <strong>Groq LLM</strong>
</td>
</tr>

<tr>
<td colspan="5" align="center">↓</td>
</tr>

<tr>
<td colspan="5" align="center">
💬 <strong>Answer + Sources</strong>
</td>
</tr>

</table>

</div>

<hr>

<h2>🧪 Evaluation</h2>

<p>
RAGForge includes a RAG evaluation pipeline using
<strong>RAGAS</strong>.
</p>

<table border="1" cellpadding="10" cellspacing="0">

<tr>
<th>Metric</th>
<th>What It Measures</th>
</tr>

<tr>
<td><strong>Faithfulness</strong></td>
<td>Whether the generated answer is supported by the retrieved context.</td>
</tr>

<tr>
<td><strong>Answer Relevancy</strong></td>
<td>Whether the generated answer appropriately addresses the question.</td>
</tr>

<tr>
<td><strong>Context Precision</strong></td>
<td>How relevant the retrieved context is to the question.</td>
</tr>

<tr>
<td><strong>Context Recall</strong></td>
<td>Whether the relevant information was successfully retrieved.</td>
</tr>

</table>

<p>
Evaluation datasets are maintained under:
</p>

<pre>
evals/
</pre>

<p>
Evaluation scripts are maintained under:
</p>

<pre>
scripts/
</pre>

<hr>

<h2>📸 Screenshots</h2>

<p>
The RAGForge frontend currently provides:
</p>

<ul>
<li>Document upload</li>
<li>Question input</li>
<li>AI-generated answers</li>
<li>Source citations</li>
<li>Loading states</li>
<li>Error handling</li>
</ul>

<div align="center">

<p>
<strong>📷 Frontend screenshots will be added here.</strong>
</p>

</div>

<hr>

<h2>📊 Current Project Status</h2>

<table border="1" cellpadding="10" cellspacing="0">

<tr>
<th>Component</th>
<th>Status</th>
</tr>

<tr>
<td>Document ingestion</td>
<td>✅ Completed</td>
</tr>

<tr>
<td>PDF support</td>
<td>✅ Completed</td>
</tr>

<tr>
<td>DOCX support</td>
<td>✅ Completed</td>
</tr>

<tr>
<td>TXT support</td>
<td>✅ Completed</td>
</tr>

<tr>
<td>Markdown support</td>
<td>✅ Completed</td>
</tr>

<tr>
<td>Text chunking</td>
<td>✅ Completed</td>
</tr>

<tr>
<td>Embeddings</td>
<td>✅ Completed</td>
</tr>

<tr>
<td>ChromaDB</td>
<td>✅ Completed</td>
</tr>

<tr>
<td>Semantic retrieval</td>
<td>✅ Completed</td>
</tr>

<tr>
<td>BM25 retrieval</td>
<td>✅ Completed</td>
</tr>

<tr>
<td>Hybrid retrieval</td>
<td>✅ Completed</td>
</tr>

<tr>
<td>RRF</td>
<td>✅ Completed</td>
</tr>

<tr>
<td>Cross-Encoder re-ranking</td>
<td>✅ Completed</td>
</tr>

<tr>
<td>Citation generation</td>
<td>✅ Completed</td>
</tr>

<tr>
<td>Groq LLM integration</td>
<td>✅ Completed</td>
</tr>

<tr>
<td>RAGAS evaluation</td>
<td>✅ Implemented</td>
</tr>

<tr>
<td>FastAPI backend</td>
<td>✅ Completed</td>
</tr>

<tr>
<td>React frontend</td>
<td>✅ Completed</td>
</tr>

<tr>
<td>Cloud deployment</td>
<td>⏳ Planned</td>
</tr>

</table>

<hr>

<h2>⚠️ Current Limitations</h2>

<ul>
<li>
The vector database currently uses local persistent ChromaDB storage.
</li>

<li>
Uploaded documents remain available to the retrieval system.
</li>

<li>
Document-level query filtering has not yet been implemented.
</li>

<li>
Authentication has not yet been implemented.
</li>

<li>
Cloud deployment has not yet been configured.
</li>

<li>
Production cloud document storage has not yet been configured.
</li>
</ul>

<hr>

<h2>🗺️ Roadmap</h2>

<table border="1" cellpadding="10" cellspacing="0">

<tr>
<th>Feature</th>
<th>Status</th>
</tr>

<tr>
<td>Document ingestion</td>
<td>✅</td>
</tr>

<tr>
<td>Multiple document formats</td>
<td>✅</td>
</tr>

<tr>
<td>Text preprocessing</td>
<td>✅</td>
</tr>

<tr>
<td>Embeddings</td>
<td>✅</td>
</tr>

<tr>
<td>Vector database</td>
<td>✅</td>
</tr>

<tr>
<td>Semantic retrieval</td>
<td>✅</td>
</tr>

<tr>
<td>BM25 retrieval</td>
<td>✅</td>
</tr>

<tr>
<td>Hybrid retrieval</td>
<td>✅</td>
</tr>

<tr>
<td>RRF</td>
<td>✅</td>
</tr>

<tr>
<td>Cross-Encoder re-ranking</td>
<td>✅</td>
</tr>

<tr>
<td>Grounded generation</td>
<td>✅</td>
</tr>

<tr>
<td>Citations</td>
<td>✅</td>
</tr>

<tr>
<td>RAGAS evaluation</td>
<td>✅</td>
</tr>

<tr>
<td>FastAPI API</td>
<td>✅</td>
</tr>

<tr>
<td>React frontend</td>
<td>✅</td>
</tr>

<tr>
<td>Document-level filtering</td>
<td>🔜 Planned</td>
</tr>

<tr>
<td>Cloud deployment</td>
<td>🔜 Planned</td>
</tr>

<tr>
<td>Cloud document storage</td>
<td>🔜 Planned</td>
</tr>

<tr>
<td>Authentication</td>
<td>🔜 Planned</td>
</tr>

<tr>
<td>Monitoring</td>
<td>🔜 Planned</td>
</tr>

</table>

<hr>

<h2>📚 What I Learned</h2>

<p>
RAGForge was built incrementally to understand the engineering concepts
behind modern Retrieval-Augmented Generation systems.
</p>

<table border="1" cellpadding="10" cellspacing="0">

<tr>
<th>Concept</th>
<th>Learning</th>
</tr>

<tr>
<td>Document Ingestion</td>
<td>How different document formats require different extraction strategies.</td>
</tr>

<tr>
<td>Chunking</td>
<td>How document size and overlap affect retrieval context.</td>
</tr>

<tr>
<td>Embeddings</td>
<td>How text can be represented as numerical vectors for semantic search.</td>
</tr>

<tr>
<td>Vector Databases</td>
<td>How embeddings and metadata can be stored and searched efficiently.</td>
</tr>

<tr>
<td>BM25</td>
<td>How lexical keyword retrieval complements semantic search.</td>
</tr>

<tr>
<td>Hybrid Retrieval</td>
<td>Why combining different retrieval strategies improves coverage.</td>
</tr>

<tr>
<td>RRF</td>
<td>How multiple ranking systems can be combined into a unified ranking.</td>
</tr>

<tr>
<td>Re-ranking</td>
<td>How Cross-Encoders can improve the relevance of retrieved candidates.</td>
</tr>

<tr>
<td>Prompt Grounding</td>
<td>How retrieved context can be provided to an LLM to reduce unsupported answers.</td>
</tr>

<tr>
<td>Citations</td>
<td>How source information can be generated independently of the LLM.</td>
</tr>

<tr>
<td>RAG Evaluation</td>
<td>How RAGAS can be used to evaluate retrieval and generation quality.</td>
</tr>

<tr>
<td>FastAPI</td>
<td>How to expose a RAG pipeline through REST APIs.</td>
</tr>

<tr>
<td>React</td>
<td>How to build an interactive frontend for a RAG application.</td>
</tr>

<tr>
<td>Configuration</td>
<td>How centralized configuration reduces hardcoded values and improves maintainability.</td>
</tr>

</table>

<hr>

<h2>🎯 Project Philosophy</h2>

<div align="center">

<h3>Build → Understand → Test → Evaluate → Improve</h3>

<p>
RAGForge focuses on understanding the complete RAG pipeline rather than
hiding the retrieval process behind a single abstraction.
</p>

<table>
<tr>
<td align="center">
🧠<br>
<strong>Understand</strong>
</td>

<td>→</td>

<td align="center">
🔨<br>
<strong>Implement</strong>
</td>

<td>→</td>

<td align="center">
🧪<br>
<strong>Test</strong>
</td>

<td>→</td>

<td align="center">
📊<br>
<strong>Evaluate</strong>
</td>

<td>→</td>

<td align="center">
🚀<br>
<strong>Improve</strong>
</td>
</tr>
</table>

</div>

<hr>

<h2>🔮 Future Work</h2>

<ul>
<li>Document-level filtering</li>
<li>Document management and deletion</li>
<li>Multiple knowledge bases</li>
<li>Cloud-based vector storage</li>
<li>Cloud document storage</li>
<li>User authentication</li>
<li>Streaming LLM responses</li>
<li>Advanced evaluation dashboard</li>
<li>Retrieval performance monitoring</li>
<li>Production deployment</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>

<div align="center">

<h2>Smit Prajapati</h2>

<p>Computer Science Engineering Student</p>

<a href="https://github.com/smitprajapati0301">

<img src="https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github" alt="GitHub Profile">

</a>

</div>

<hr>

<h2>📄 License</h2>

<p>
This project is licensed under the <strong>MIT License</strong>.
</p>

<hr>

<div align="center">

<h2>⭐ RAGForge</h2>

<p>
<strong>Built to learn. Built to understand. Built to experiment with RAG.</strong>
</p>

<p>
If you find this project useful or interesting, consider giving it a ⭐.
</p>

</div>
