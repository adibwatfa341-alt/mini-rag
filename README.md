# mini-rag

A Retrieval-Augmented Generation (RAG) question-answering API built with **FastAPI** and **MongoDB**. The project is built step by step, and each step lives on its own branch.

## Status

The work is on the `tut-*` branches. The latest one is **`tut-007`**.

| Branch | Step |
|---|---|
| `tut-001` | Project setup |
| `tut-002` – `tut-005` | FastAPI app, settings, file upload and validation, file processing and chunking |
| `tut-006` | MongoDB with Docker Compose |
| `tut-007` | MongoDB models for projects, assets and chunks, with indexes |

**Next steps:** embeddings, a vector database (Qdrant), and LLM answer generation.

## Stack

Python · FastAPI · Pydantic Settings · LangChain text splitters · PyMuPDF · MongoDB (Motor) · Docker Compose

## Run it

```bash
git checkout tut-007
cd src
pip install -r requirements.txt
cp .env.example .env            # fill in your values
cd ../docker && cp .env.example .env && docker compose up -d   # MongoDB
cd ../src && uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

A Postman collection is in `src/assets/mini-rag-app.postman_collection.json`.

## Project layout (tut-007)

```
src/
  main.py              FastAPI app
  Routes/              API routes and request schemas
  controllers/         upload, processing and project logic
  models/              MongoDB models, schemes and enums
  helpers/config.py    settings from .env
docker/                MongoDB with Docker Compose
```
