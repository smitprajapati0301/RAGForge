import { useEffect, useRef, useState } from "react";

import {
  askQuestion,
  checkHealth,
  uploadDocument,
} from "./services/api";

import "./App.css";


function App() {
  // --------------------------------------------------
  // Application state
  // --------------------------------------------------

  const [isOnline, setIsOnline] = useState(false);

  const [selectedFile, setSelectedFile] = useState(null);

  const [uploading, setUploading] = useState(false);

  const [uploadResult, setUploadResult] = useState(null);

  const [question, setQuestion] = useState("");

  const [answer, setAnswer] = useState(null);

  const [asking, setAsking] = useState(false);

  const [error, setError] = useState("");

  const fileInputRef = useRef(null);


  // --------------------------------------------------
  // Check backend health when application starts
  // --------------------------------------------------

  useEffect(() => {
    checkBackend();
  }, []);


  async function checkBackend() {
    try {
      await checkHealth();

      setIsOnline(true);
    } catch {
      setIsOnline(false);
    }
  }


  // --------------------------------------------------
  // File selection
  // --------------------------------------------------

  function handleFileChange(event) {
    const file = event.target.files?.[0];

    if (!file) {
      return;
    }

    setSelectedFile(file);
    setUploadResult(null);
    setError("");
  }


  // --------------------------------------------------
  // Upload document
  // --------------------------------------------------

  async function handleUpload() {
    if (!selectedFile) {
      setError("Please select a document first.");
      return;
    }

    setUploading(true);
    setError("");
    setUploadResult(null);

    try {
      const result = await uploadDocument(
        selectedFile
      );

      setUploadResult(result);

      // Clear selected file after successful upload.
      setSelectedFile(null);

      if (fileInputRef.current) {
        fileInputRef.current.value = "";
      }

    } catch (err) {
      console.error(err);

      setError(
        err.response?.data?.detail ||
        "Document upload failed."
      );

    } finally {
      setUploading(false);
    }
  }


  // --------------------------------------------------
  // Ask question
  // --------------------------------------------------

  async function handleAsk() {
    const trimmedQuestion =
      question.trim();

    if (!trimmedQuestion) {
      setError("Please enter a question.");
      return;
    }

    setAsking(true);
    setError("");
    setAnswer(null);

    try {
      const result = await askQuestion(
        trimmedQuestion
      );

      setAnswer(result);

    } catch (err) {
      console.error(err);

      setError(
        err.response?.data?.detail ||
        "Unable to process the question."
      );

    } finally {
      setAsking(false);
    }
  }


  // --------------------------------------------------
  // Handle Enter key
  // --------------------------------------------------

  function handleQuestionKeyDown(event) {
    if (
      event.key === "Enter" &&
      !event.shiftKey
    ) {
      event.preventDefault();

      handleAsk();
    }
  }


  return (
    <div className="min-h-screen bg-slate-50">


      {/* =================================================
          HEADER
      ================================================= */}

      <header className="border-b border-slate-200 bg-white">

        <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-5">

          <div className="flex items-center gap-3">

            {/* Logo */}
            <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-slate-900 text-lg font-bold text-white">
              R
            </div>

            <div>
              <h1 className="text-xl font-bold text-slate-900">
                RAGForge
              </h1>

              <p className="text-xs text-slate-500">
                Retrieval-Augmented Generation
              </p>
            </div>

          </div>


          {/* Backend status */}
          <div className="flex items-center gap-2 rounded-full border border-slate-200 bg-slate-50 px-4 py-2">

            <span
              className={`h-2.5 w-2.5 rounded-full ${
                isOnline
                  ? "bg-emerald-500"
                  : "bg-red-500"
              }`}
            />

            <span className="text-sm font-medium text-slate-600">
              {isOnline
                ? "API Online"
                : "API Offline"}
            </span>

          </div>

        </div>

      </header>


      {/* =================================================
          MAIN CONTENT
      ================================================= */}

      <main className="mx-auto max-w-5xl px-6 py-12">


        {/* Hero */}

        <section className="mb-10 text-center">

          <div className="mb-4 inline-flex rounded-full border border-slate-200 bg-white px-4 py-2 text-sm text-slate-600 shadow-sm">
            AI-powered document assistant
          </div>

          <h2 className="text-4xl font-bold tracking-tight text-slate-900 md:text-5xl">
            Ask questions from
            <span className="block text-slate-500">
              your documents
            </span>
          </h2>

          <p className="mx-auto mt-5 max-w-2xl text-lg leading-8 text-slate-500">
            Upload a PDF or Word document and
            RAGForge will retrieve relevant
            information, re-rank the results,
            and generate a grounded answer
            with citations.
          </p>

        </section>


        {/* =================================================
            ERROR MESSAGE
        ================================================= */}

        {error && (
          <div className="mb-6 rounded-xl border border-red-200 bg-red-50 px-5 py-4 text-sm text-red-700">
            {error}
          </div>
        )}


        {/* =================================================
            DOCUMENT UPLOAD
        ================================================= */}

        <section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">

          <div className="mb-5">

            <h3 className="text-lg font-semibold text-slate-900">
              Upload a document
            </h3>

            <p className="mt-1 text-sm text-slate-500">
              Supported formats: PDF, DOCX, TXT,
              Markdown
            </p>

          </div>


          {/* Upload area */}

          <div
            onClick={() =>
              fileInputRef.current?.click()
            }
            className="cursor-pointer rounded-xl border-2 border-dashed border-slate-300 bg-slate-50 p-10 text-center transition hover:border-slate-500 hover:bg-slate-100"
          >

            <div className="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-xl bg-white text-2xl shadow-sm">
              📄
            </div>

            <p className="font-medium text-slate-700">
              {selectedFile
                ? selectedFile.name
                : "Choose a document"}
            </p>

            <p className="mt-2 text-sm text-slate-500">
              Click to browse files
            </p>

            <input
              ref={fileInputRef}
              type="file"
              accept=".pdf,.docx,.txt,.md"
              onChange={handleFileChange}
              className="hidden"
            />

          </div>


          {/* Selected file */}

          {selectedFile && (
            <div className="mt-4 flex items-center justify-between rounded-xl bg-slate-50 px-4 py-3">

              <div className="min-w-0">

                <p className="truncate text-sm font-medium text-slate-700">
                  {selectedFile.name}
                </p>

                <p className="text-xs text-slate-500">
                  {(
                    selectedFile.size /
                    1024 /
                    1024
                  ).toFixed(2)}{" "}
                  MB
                </p>

              </div>


              <button
                onClick={handleUpload}
                disabled={uploading}
                className="ml-4 rounded-lg bg-slate-900 px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-slate-700 disabled:cursor-not-allowed disabled:opacity-50"
              >
                {uploading
                  ? "Indexing..."
                  : "Upload & Index"}
              </button>

            </div>
          )}


          {/* Upload result */}

          {uploadResult && (
            <div className="mt-4 rounded-xl border border-emerald-200 bg-emerald-50 p-4">

              <div className="flex items-start gap-3">

                <span className="text-lg">
                  ✓
                </span>

                <div>

                  <p className="font-semibold text-emerald-800">
                    Document indexed successfully
                  </p>

                  <p className="mt-1 text-sm text-emerald-700">
                    {uploadResult.filename}
                    {" · "}
                    {uploadResult.chunks_created}
                    {" chunks created"}
                  </p>

                </div>

              </div>

            </div>
          )}

        </section>


        {/* =================================================
            QUESTION INPUT
        ================================================= */}

        <section className="mt-6 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">

          <div className="mb-5">

            <h3 className="text-lg font-semibold text-slate-900">
              Ask a question
            </h3>

            <p className="mt-1 text-sm text-slate-500">
              RAGForge will search the indexed
              documents before generating an answer.
            </p>

          </div>


          <div className="relative">

            <textarea
              value={question}
              onChange={(event) =>
                setQuestion(event.target.value)
              }
              onKeyDown={
                handleQuestionKeyDown
              }
              placeholder="What would you like to know?"
              rows={4}
              className="w-full resize-none rounded-xl border border-slate-300 bg-slate-50 px-4 py-4 pr-4 text-slate-800 outline-none transition placeholder:text-slate-400 focus:border-slate-500 focus:bg-white"
            />

            <div className="mt-3 flex justify-end">

              <button
                onClick={handleAsk}
                disabled={asking}
                className="rounded-lg bg-slate-900 px-6 py-3 text-sm font-semibold text-white transition hover:bg-slate-700 disabled:cursor-not-allowed disabled:opacity-50"
              >
                {asking
                  ? "Searching..."
                  : "Ask RAGForge →"}
              </button>

            </div>

          </div>

        </section>


        {/* =================================================
            ANSWER
        ================================================= */}

        {answer && (
          <section className="mt-6 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">

            <div className="mb-5">

              <div className="flex items-center gap-2">

                <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-slate-900 text-sm text-white">
                  AI
                </span>

                <h3 className="text-lg font-semibold text-slate-900">
                  Answer
                </h3>

              </div>

            </div>


            <div className="rounded-xl bg-slate-50 p-5">

              <p className="whitespace-pre-wrap text-[15px] leading-7 text-slate-700">
                {answer.answer}
              </p>

            </div>


            {/* =================================================
                SOURCES
            ================================================= */}

            {answer.sources?.length > 0 && (

              <div className="mt-6">

                <h4 className="mb-3 text-sm font-semibold uppercase tracking-wide text-slate-500">
                  Sources
                </h4>

                <div className="space-y-3">

                  {answer.sources.map(
                    (source) => (

                      <div
                        key={source.id}
                        className="rounded-xl border border-slate-200 bg-white p-4"
                      >

                        <div className="flex items-center gap-3">

                          <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-slate-100 text-sm font-semibold text-slate-700">
                            [{source.id}]
                          </span>

                          <div>

                            <p className="text-sm font-semibold text-slate-800">
                              {source.filename}
                            </p>

                            <p className="mt-1 text-xs text-slate-500">

                              {source.page !== null &&
                                `Page ${source.page}`}

                              {source.page !== null &&
                                source.chunk_index !== null &&
                                " · "}

                              {source.chunk_index !== null &&
                                `Chunk ${source.chunk_index}`}

                            </p>

                          </div>

                        </div>

                      </div>

                    )
                  )}

                </div>

              </div>

            )}

          </section>
        )}

      </main>


      {/* =================================================
          FOOTER
      ================================================= */}

      <footer className="border-t border-slate-200 bg-white">

        <div className="mx-auto max-w-6xl px-6 py-6 text-center text-sm text-slate-500">

          RAGForge · Hybrid Retrieval + RRF +
          Cross-Encoder Re-ranking

        </div>

      </footer>

    </div>
  );
}

export default App;