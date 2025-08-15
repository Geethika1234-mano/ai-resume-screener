from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="AI Resume Screener")

# Allow CORS for local frontend during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class JobDescription(BaseModel):
    title: str
    description: str


@app.get("/")
def read_root():
    """Health check endpoint"""
    return {"message": "API is running"}


# Note: File uploads require the python-multipart package. Since that package may not be
# available in some environments, the resume upload endpoint is disabled in this
# minimal implementation. In a full deployment you can reintroduce an endpoint
# that accepts `UploadFile` and parses resumes.

@app.post("/resumes/upload-placeholder")
async def upload_resume_placeholder():
    """
    Placeholder endpoint for uploading a resume.

    Returns a static message because file uploads are not supported in this environment.
    """
    return {"message": "Resume upload is disabled in this environment"}


@app.post("/jobs")
async def create_job(job: JobDescription):
    """Create a job description entry and return a placeholder ID."""
    # TODO: store job description and compute embeddings
    return {"job_id": 1, "title": job.title, "description": job.description}


@app.get("/jobs/{job_id}/candidates")
def rank_candidates(job_id: int):
    """Return a list of candidate rankings for the given job ID."""
    # TODO: compute similarity between job description and resumes
    return {"job_id": job_id, "candidates": []}


@app.get("/candidates/{candidate_id}")
def get_candidate(candidate_id: int):
    """Return details for a candidate by ID."""
    # TODO: retrieve candidate details and scores
    return {"candidate_id": candidate_id, "info": {}}
