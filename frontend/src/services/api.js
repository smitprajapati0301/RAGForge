import axios from "axios";

/*
 * Base URL of the RAGForge FastAPI backend.
 *
 * During local development:
 * React → http://localhost:5173
 * FastAPI → http://127.0.0.1:8000
 */
const API_BASE_URL = "http://127.0.0.1:8000";

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 120000,
});

/**
 * Check whether the RAGForge backend is healthy.
 */
export async function checkHealth() {
  const response = await api.get("/health");

  return response.data;
}

/**
 * Upload a document to RAGForge.
 *
 * Supports:
 * PDF
 * DOCX
 * TXT
 * Markdown
 */
export async function uploadDocument(file) {
  const formData = new FormData();

  formData.append("file", file);

  const response = await api.post(
    "/documents/upload",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
}

/**
 * Send a question to the RAG pipeline.
 */
export async function askQuestion(question) {
  const response = await api.post(
    "/query",
    {
      question,
    }
  );

  return response.data;
}