# Sprint 0 Review: Project Setup & Backend Foundation

## Sprint Goal

Build a clean, runnable, and documented FastAPI backend foundation for AI Crypto Copilot.

By the end of Sprint 0, the project should have:

- A GitHub repository with a clear README
- A basic FastAPI backend application
- A health check endpoint
- An organized backend folder structure
- Project dependency management with `requirements.txt`
- A `.gitignore` file for local and cache files
- Basic FastAPI project metadata
- Setup instructions in the README
- A Sprint 0 development record in `docs/sprint-0.md`
- A first release version, `v0.0.1`

## Completed Work So Far

### Task 0.1: Initialize GitHub Repository

I initialized the AI Crypto Copilot project, wrote the first README, created two commits, configured my Git identity, and pushed the project to GitHub.

I learned that I must pay close attention to spelling because typos can make code fail or make commit messages look unprofessional.

### Task 0.2: Create FastAPI Backend Entrypoint

I created a Python virtual environment, installed FastAPI and Uvicorn, saved the project dependencies in `requirements.txt`, and created the first backend entrypoint in `backend/main.py`.

I added two API endpoints:

- `GET /`
- `GET /health`

I started the local development server with Uvicorn and confirmed that the API returned the correct response in the browser.

#### Problems I Encountered

- I needed to understand the difference between a local development server and a deployed production server.
- I learned that Uvicorn is the server program that runs a FastAPI application.
- I saw a `404 Not Found` error for `favicon.ico` and learned that it is normal because the project does not have a browser icon yet.
- My first `git push` failed with an `Empty reply from server` network error, but retrying `git push` worked.

#### What I Learned

- FastAPI is a Python framework for building APIs.
- Uvicorn runs the FastAPI app as a local server.
- `requirements.txt` records the Python packages needed by the project.
- `.gitignore` prevents files like `.venv` and cache files from being uploaded to GitHub.
- `git push` uploads local commits to GitHub.

### Task 0.3: Organize Backend API Routes

I refactored the backend project structure and moved the health check endpoint into a separate API router.

I created:

- `backend/api/__init__.py`
- `backend/api/health.py`
- `backend/core/__init__.py`

I updated `backend/main.py` to include the health router with `app.include_router()`.

I tested:

- `GET /`
- `GET /health`
- `/docs`

#### Problems I Encountered

- I noticed that one previous commit message had a typo.
- I used interactive rebase to reword the commit message.
- After rewriting Git history, my local branch diverged from `origin/main`.
- I used `git push --force-with-lease` to safely update the GitHub history.

#### What I Learned

- `APIRouter` helps organize API endpoints into separate files.
- `__init__.py` helps Python treat a folder as a package.
- Refactor means improving code structure without changing behavior.
- Reword means changing the text of a commit message.
- `--force-with-lease` is a safer way to force push rewritten Git history.

### Task 0.4: Add FastAPI Project Metadata

I added project metadata to the FastAPI application.

The API documentation now shows:

- Title: `AI Crypto Copilot API`
- Description: `Backend API for AI Crypto Copilot.`
- Version: `0.0.1`

#### What I Learned

- Metadata means information that describes the project itself.
- FastAPI can automatically show project metadata in the `/docs` page.
- API version numbers help describe the current stage of the backend.

### Task 0.5: Update README Setup Instructions

I updated the README with setup instructions so another developer can clone the repository, create a virtual environment, install dependencies, run the backend server, and open the API documentation.

#### What I Learned

- `README.md` is the public entry point for a GitHub project.
- Setup instructions help other developers run the project locally.
- `Preview` shows the rendered Markdown result, while `Source` shows the editable Markdown text.

## Sprint 0 Progress

### Completed

- Task 0.1: Initialize GitHub repository
- Task 0.2: Create FastAPI backend entrypoint
- Task 0.3: Organize backend API routes
- Task 0.4: Add FastAPI project metadata
- Task 0.5: Update README setup instructions
- Task 0.6: Create Sprint 0 documentation

### Remaining

- Task 0.7: Prepare Sprint 0 release `v0.0.1`
