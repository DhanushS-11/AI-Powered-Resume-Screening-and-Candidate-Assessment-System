<p align="center">
  <img src="https://img.shields.io/badge/Next.js-16-black?style=for-the-badge&logo=next.js&logoColor=white" alt="Next.js" />
  <img src="https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/TailwindCSS-4-38bdf8?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="TailwindCSS" />
  <img src="https://img.shields.io/badge/Ollama-Local_LLM-FF6F00?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama" />
  <img src="https://img.shields.io/badge/TypeScript-5-3178c6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
</p>

<h1 align="center">🧠 HireSense AI</h1>
<h3 align="center">AI-Powered Resume Screening & Candidate Assessment System</h3>

<p align="center">
  <em>Upload a resume. Paste a job description. Get an instant, AI-generated candidate briefing — <br/> complete with a 10-point score, 5-tier fit classification, skill gap analysis, and interview questions.</em>
</p>

<br/>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#%EF%B8%8F-tech-stack">Tech Stack</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-api-reference">API Reference</a> •
  <a href="#-project-structure">Project Structure</a> •
  <a href="#-how-it-works">How It Works</a> •
  <a href="#-license">License</a>
</p>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📄 **PDF Resume Parsing** | Drag-and-drop or click-to-upload PDF resumes with instant text extraction via `pdfplumber` |
| 🧠 **Local LLM Assessment** | Generates professional recruiter-grade candidate analysis using Ollama (`qwen2.5:3b`) — **no API keys, no cloud, fully private** |
| 🎯 **AI Candidate Score** | LLM-generated score on a **10-point scale** based on resume quality, knowledge depth, and job alignment |
| 🏷️ **5-Tier Fit Classification** | Intelligent categorization into one of five hiring tiers (see [Classification System](#-5-tier-fit-classification-system)) |
| 🔍 **Skill Extraction & Gap Analysis** | Automatic extraction of matching skills and identification of missing competencies against the job description |
| 💬 **AI Interview Questions** | Auto-generated targeted interview questions based on detected skill gaps |
| 📊 **Animated Score Gauge** | Dynamic SVG radial gauge with smooth animation and category-specific color gradients |
| 🌙 **Space-Dark Premium UI** | Modern glassmorphism interface with gradient overlays, subtle grid patterns, and micro-animations |
| 🔌 **Offline Fallback** | Graceful degradation when Ollama is offline — provides skill-based assessment without the AI narrative |
| 📋 **Raw Text Preview** | Expandable section to inspect the extracted resume text for verification |

---

## 🏷️ 5-Tier Fit Classification System

The AI evaluates each candidate and assigns one of five fit categories:

| Tier | Classification | Criteria | Color |
|:----:|----------------|----------|:-----:|
| 1 | 🔴 **Not Aligned** | Only some basic skills or no meaningful overlap with role requirements | Rose |
| 2 | 🟠 **Needs Heavy Training** | Lacks more than 40% of core skills but shows potential for growth | Orange |
| 3 | 🟡 **Core Skills Match (Trainable)** | Has 50–70% of core foundational skills; lacks secondary tools where training can bridge the gap | Amber |
| 4 | 🔵 **Strong Fit (Plug-and-Play)** | Possesses 70–90% of required skills; ready to contribute immediately with minimal onboarding | Indigo |
| 5 | 🟢 **Outstanding Expert** | Exceeds role requirements with extensive expert-level alignment across all domains | Emerald |

---

## 🏗 Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    CLIENT (Browser)                     │
│  ┌───────────────────────────────────────────────────┐  │
│  │         Next.js 16 + TailwindCSS 4               │  │
│  │  ┌────────────┬──────────────┬───────────────┐    │  │
│  │  │ Dashboard  │ ScoreGauge   │ Markdown      │    │  │
│  │  │ .tsx       │ .tsx         │ Renderer.tsx  │    │  │
│  │  └──────┬─────┴──────────────┴───────────────┘    │  │
│  └─────────┼─────────────────────────────────────────┘  │
│            │ POST /api/analyze (FormData)                │
│            ▼                                            │
├─────────────────────────────────────────────────────────┤
│                    SERVER (FastAPI)                      │
│  ┌───────────────────────────────────────────────────┐  │
│  │  main.py — CORS, Upload Handling, Response JSON   │  │
│  │  ┌───────────────────────────────────────────┐    │  │
│  │  │  utils/                                   │    │  │
│  │  │  ├── extract_text.py  (pdfplumber)        │    │  │
│  │  │  ├── preprocess.py    (regex cleaning)    │    │  │
│  │  │  ├── skill_extractor.py (keyword match)   │    │  │
│  │  │  └── resume_summary.py (Ollama prompt)    │    │  │
│  │  └───────────────────────────────────────────┘    │  │
│  └──────────────────────┬────────────────────────────┘  │
│                         │ POST /api/generate             │
│                         ▼                                │
│              ┌─────────────────────┐                     │
│              │  Ollama (Local LLM) │                     │
│              │  qwen2.5:3b         │                     │
│              │  localhost:11434     │                     │
│              └─────────────────────┘                     │
└─────────────────────────────────────────────────────────┘
```

---

## ⚙️ Tech Stack

### Frontend
| Technology | Purpose |
|-----------|---------|
| [Next.js 16](https://nextjs.org/) | React framework with App Router, SSR, and Turbopack |
| [TailwindCSS 4](https://tailwindcss.com/) | Utility-first CSS with PostCSS integration |
| [TypeScript 5](https://www.typescriptlang.org/) | Type-safe component development |
| [Lucide React](https://lucide.dev/) | Modern, consistent SVG icon library |
| [Geist Font](https://vercel.com/font) | Premium sans-serif + monospace typography by Vercel |

### Backend
| Technology | Purpose |
|-----------|---------|
| [FastAPI](https://fastapi.tiangolo.com/) | High-performance async Python API server |
| [Uvicorn](https://www.uvicorn.org/) | ASGI server with hot-reload for development |
| [pdfplumber](https://github.com/jsvine/pdfplumber) | Reliable PDF text extraction |
| [NLTK](https://www.nltk.org/) | Natural Language Toolkit for text preprocessing |
| [scikit-learn](https://scikit-learn.org/) | Machine learning utilities (TF-IDF similarity) |

### AI Engine
| Technology | Purpose |
|-----------|---------|
| [Ollama](https://ollama.com/) | Run open-source LLMs locally with zero cloud dependency |
| [Qwen 2.5 3B](https://huggingface.co/Qwen/Qwen2.5-3B) | Lightweight, fast LLM optimized for structured generation |

---

## 🚀 Getting Started

### Prerequisites

| Requirement | Minimum Version |
|-----------|-----------------|
| Python | 3.10+ |
| Node.js | 18+ |
| npm | 9+ |
| Ollama | Latest |

### 1. Clone the Repository

```bash
git clone https://github.com/DhanushS-11/AI-Powered-Resume-Screening-and-Candidate-Assessment-System.git
cd AI-Powered-Resume-Screening-and-Candidate-Assessment-System
```

### 2. Install & Start the LLM (Ollama)

```bash
# Install Ollama from https://ollama.com/download
# Then pull the required model:
ollama pull qwen2.5:3b
```

> **Note:** Ollama must be running in the background on `http://localhost:11434` before starting the backend. You can verify by visiting `http://localhost:11434` in your browser — it should display `"Ollama is running"`.

### 3. Set Up the Backend

```bash
# Navigate to the backend directory
cd backend

# Create a virtual environment (recommended)
python -m venv venv

# Activate the virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r ../requirements.txt

# Start the FastAPI server
python main.py
```

The API server will start at **`http://localhost:8000`** with auto-reload enabled.

### 4. Set Up the Frontend

```bash
# Open a new terminal and navigate to the frontend directory
cd frontend

# Install Node.js dependencies
npm install

# Start the Next.js development server
npm run dev
```

The frontend will start at **`http://localhost:3000`**.

### 5. Open in Browser

Navigate to **[http://localhost:3000](http://localhost:3000)** and start screening resumes! 🎉

---

## 📡 API Reference

### Health Check

```http
GET /api/health
```

**Response:**
```json
{
  "status": "ok",
  "ollama_online": true
}
```

---

### Analyze Resume

```http
POST /api/analyze
Content-Type: multipart/form-data
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `resume` | `File (PDF)` | ✅ | The candidate's resume in PDF format |
| `job_description` | `string` | ✅ | The full job description text |

**Success Response (`200`):**
```json
{
  "success": true,
  "filename": "john_doe_resume.pdf",
  "score": 7.5,
  "category": "Strong Fit (Plug-and-Play)",
  "resume_skills": ["Python", "React", "Docker", "AWS"],
  "missing_skills": ["Kubernetes", "Terraform"],
  "ai_analysis": "## Candidate Summary\nJohn is a ...",
  "resume_text": "Full extracted text from PDF..."
}
```

**Error Responses:**

| Status | Reason |
|--------|--------|
| `400` | Non-PDF file uploaded or empty/scanned PDF |
| `500` | Internal server error during processing |

---

## 📂 Project Structure

```
ResumeScreener/
│
├── 📄 README.md                    # You are here
├── 📄 requirements.txt             # Python dependencies
├── 📄 app.py                       # Legacy Streamlit app (deprecated)
│
├── 🔧 backend/                     # FastAPI Backend Server
│   ├── main.py                     # API endpoints, CORS, request handling
│   ├── data/
│   │   └── skills.txt              # Curated skill keywords database (27 skills)
│   └── utils/
│       ├── extract_text.py         # PDF → plain text (pdfplumber)
│       ├── preprocess.py           # Text normalization (lowercase, regex cleanup)
│       ├── skill_extractor.py      # Keyword-based skill matching engine
│       ├── resume_summary.py       # Ollama LLM prompt template & API call
│       └── similarity.py           # TF-IDF cosine similarity (legacy utility)
│
├── 🎨 frontend/                    # Next.js Frontend Application
│   ├── package.json                # Node.js dependencies & scripts
│   ├── next.config.ts              # Next.js configuration
│   ├── tsconfig.json               # TypeScript configuration
│   ├── postcss.config.mjs          # PostCSS + TailwindCSS pipeline
│   ├── eslint.config.mjs           # ESLint configuration
│   ├── public/                     # Static assets
│   └── src/
│       ├── app/
│       │   ├── layout.tsx          # Root HTML layout (Geist fonts, metadata)
│       │   ├── page.tsx            # Home page with gradient backgrounds
│       │   ├── globals.css         # TailwindCSS imports + CSS variables
│       │   └── favicon.ico         # App icon
│       └── components/
│           ├── Dashboard.tsx       # Main application component (upload, JD input, results)
│           ├── ScoreGauge.tsx      # Animated SVG radial score gauge
│           └── MarkdownRenderer.tsx # LLM response parser with card-based layout
│
├── 📁 data/
│   └── skills.txt                  # Root-level skills reference
│
├── 📁 uploads/                     # Temporary PDF storage (auto-cleaned)
└── 📁 utils/                       # Root-level utility modules (legacy)
```

---

## 🔄 How It Works

The system processes each resume through a **4-stage pipeline**:

### Stage 1 — Text Extraction
The uploaded PDF is parsed using `pdfplumber`, which extracts text from all pages while preserving layout structure. The raw text is used both for skill matching and as context for the LLM.

### Stage 2 — Text Preprocessing
The extracted text is normalized: converted to lowercase, stripped of special characters via regex, and whitespace is consolidated. This creates a clean representation for accurate keyword matching.

### Stage 3 — Skill Extraction & Gap Analysis
Both the resume and job description are scanned against a curated database of **27 technical skills** (located in `data/skills.txt`). The system identifies:
- **Matching skills** — skills present in both resume and JD
- **Missing skills** — skills required by the JD but absent from the resume

### Stage 4 — AI Assessment Generation
All extracted data (resume text, job description, matched skills, and skill gaps) is formatted into a structured prompt and sent to the local Ollama instance running `qwen2.5:3b`. The LLM generates:

| Section | Content |
|---------|---------|
| **Candidate Score** | Numerical rating out of 10 with justification |
| **Fit Classification** | One of 5 hiring tiers based on skill alignment |
| **Candidate Summary** | Brief professional overview |
| **Match Assessment** | Detailed role fit analysis |
| **Key Strengths** | Top competencies and experience highlights |
| **Skill Gaps** | Specific areas needing development |
| **Hiring Recommendation** | Actionable recommendation for hiring managers |
| **Interview Questions** | 5 targeted questions to probe identified gaps |

> The backend parses the score and classification from the LLM's markdown output using regex, while the full narrative is forwarded to the frontend's `MarkdownRenderer` for visual display.

---

## 🎨 UI Design Philosophy

The frontend follows a **"Space-Dark"** design language:

- **Color Palette:** Deep slate backgrounds (`#0B0F19`) with indigo/violet accent gradients
- **Typography:** [Geist](https://vercel.com/font) sans-serif and monospace fonts for a clean, modern feel
- **Glassmorphism:** Cards use `backdrop-blur` with semi-transparent backgrounds
- **Ambient Effects:** Soft gradient orbs and a subtle grid pattern create depth
- **Micro-animations:** Score gauge animates on mount; buttons lift on hover; cards glow on interaction
- **Responsive Layout:** Adapts from single-column mobile to multi-column desktop layouts

---

## 🛡️ Privacy & Security

- **🔒 100% Local Processing** — All AI inference runs on your machine via Ollama. No resume data ever leaves your network.
- **🗑️ Auto-cleanup** — Uploaded PDFs are deleted from the server immediately after processing.
- **🚫 No Telemetry** — Zero external API calls, no analytics, no tracking.

---

## 🤝 Contributing

Contributions are welcome! Here's how to get involved:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  <strong>Built with 💜 by <a href="https://github.com/DhanushS-11">Dhanush S</a></strong>
  <br/>
  <sub>If you found this useful, consider giving it a ⭐ on GitHub!</sub>
</p>