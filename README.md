# AI Resume Screener & Job Match Assistant

Welcome to the **AI Resume Screener & Job Match Assistant** project!  This tool uses natural language processing and embeddings to parse resumes, assess candidate qualifications and match them against job descriptions.  With a simple API and optional web interface, you can automate candidate screening and extract meaningful insights from resumes quickly and accurately.

## 🚀 Features

- **Resume Parsing**:  Automatically extract text and structured data from resumes (PDF, DOCX).  The parser normalizes skills, experience and education for downstream analysis.
- **Candidate Scoring**:  Use language model embeddings to measure how well a candidate’s experience aligns with a specific job description.  Scores are normalized and ranked.
- **Job Matching**:  Compare multiple job descriptions against a pool of candidates to find the best fit for each role.
- **FastAPI Endpoints**:  Expose endpoints to upload resumes, submit job descriptions, retrieve candidate rankings and view detailed scores.
- **Vector Store Integration**:  Store resume and job embeddings in Pinecone or Weaviate for efficient similarity searches.
- **Optional Frontend**:  A lightweight React interface to upload resumes and visualize rankings, built with Next.js and Tailwind CSS.

## 🛠 Tech Stack

- ![Python](https://img.shields.io/badge/Python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white) **Python** – core language for the API and ML pipeline
- ![FastAPI](https://img.shields.io/badge/FastAPI-006466?style=for-the-badge&logo=fastapi&logoColor=white) **FastAPI** – high‑performance Python web framework for the API
- ![OpenAI](https://img.shields.io/badge/OpenAI-GPT‑4-4B0082?style=for-the-badge) **OpenAI GPT‑4/Embeddings** – for semantic understanding and scoring
- ![LangChain](https://img.shields.io/badge/LangChain-222222?style=for-the-badge) **LangChain** – utilities for prompt engineering and retrieval‑augmented generation
- ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white) **MongoDB** – stores resume metadata and scores
- ![Pinecone](https://img.shields.io/badge/Pinecone-0033A1?style=for-the-badge) / ![Weaviate](https://img.shields.io/badge/Weaviate-4F46E5?style=for-the-badge) **Vector DB** – stores embeddings and supports similarity search
- ![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black) **React & Next.js** (optional) – for the web UI
- ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) **Docker** – containerizes the application

## 📦 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/Geethika1234-mano/ai-resume-screener.git
   cd ai-resume-screener
   ```
2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. **Configure environment variables**
   Create a `.env` file in the project root and add your API keys:
   ```env
   OPENAI_API_KEY=your_openai_key
   PINECONE_API_KEY=your_pinecone_key   # optional
   MONGODB_URI=your_mongodb_uri
   ```
4. **Run the API**
   ```bash
   uvicorn app.main:app --reload
   ```
5. **(Optional) Run the frontend**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## 📖 Usage

- **Upload a resume**:  Send a POST request to `/resumes/upload` with the resume file.  The server returns a unique ID for the parsed resume.
- **Submit a job description**:  POST to `/jobs` with a title and description.  The API creates a job entry and returns its ID.
- **Rank candidates for a job**:  GET `/jobs/{job_id}/candidates` to receive ranked candidate IDs and scores.
- **Retrieve details**:  GET `/candidates/{candidate_id}` to view a candidate’s extracted information and score breakdown.

Example using `curl`:

```bash
# Upload a resume
curl -X POST -F "file=@resume.pdf" http://localhost:8000/resumes/upload

# Create a job description
curl -X POST -H "Content-Type: application/json" -d '{"title":"Software Engineer","description":"Looking for a Python developer with FastAPI experience"}' http://localhost:8000/jobs

# Get ranked candidates for the job ID
curl http://localhost:8000/jobs/<job_id>/candidates
```

## 🗺 Roadmap

- [ ] Support additional file formats (LinkedIn profiles, plain text)
- [ ] Improve scoring models using fine‑tuned transformers
- [ ] Add authentication and role‑based access
- [ ] Deploy to cloud platforms (AWS/GCP) with CI/CD pipelines
- [ ] Enhance UI with charts and analytics

## 🤝 Contributing

Contributions are welcome!  If you find bugs or have ideas for improvements, please [open an issue](https://github.com/Geethika1234-mano/ai-resume-screener/issues) or submit a pull request.  For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License.  See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by industry best practices for Applicant Tracking Systems (ATS)
- Thanks to the maintainers of FastAPI, LangChain, and the open source community for amazing tools!
