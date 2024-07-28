import React, { useState } from 'react';
import { Button } from './components/ui/button';

export default function Component() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState('');
  const [sessionId, setSessionId] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) return;
    try {
      const formData = new FormData();
      formData.append('file', file);
      const response = await fetch('http://127.0.0.1:8000/api/upload', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      setSessionId(data.session_id);
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  const handleSummarize = async (e) => {
    e.preventDefault();
    if (!sessionId) return;
    try {
      const formData = new FormData();
      formData.append('session_id', sessionId);
      const response = await fetch('http://127.0.0.1:8000/api/summarize', {
        method: 'POST',
        body: JSON.stringify({ session_id: sessionId })
      });
      const data = await response.json();
      setSummary(data.summary);
    } catch (error) {
      console.error('Error summarizing file:', error);
    }
  };

  

  return (
    <div className="flex flex-col min-h-screen">
      <header className="bg-primary text-primary-foreground py-4 px-6">
        <h1 className="text-2xl font-bold">File Summarizer</h1>
      </header>
      <main className="flex-1 py-8 px-6">
        <form className="max-w-md mx-auto space-y-4">
          <div>
            <label htmlFor="file" className="block mb-2 font-medium text-muted-foreground">
              Select a file to summarize
            </label>
            <div className="flex items-center justify-center w-full">
              <label
                htmlFor="file"
                className="flex items-center justify-center w-full h-32 px-4 transition bg-background border-2 border-muted border-dashed rounded-md cursor-pointer hover:bg-muted hover:border-primary"
              >
                {file ? (
                  <span className="font-medium text-muted-foreground">{file.name}</span>
                ) : (
                  <span className="font-medium text-muted-foreground">Drop file here or click to upload</span>
                )}
                <input id="file" type="file" className="sr-only" onChange={handleFileChange} />
              </label>
            </div>
          </div>
          <div className="flex gap-2">
            <Button onClick={handleUpload} className="flex-1">
              Upload
            </Button>
            <Button onClick={handleSummarize} className="flex-1">
              Summarize
            </Button>
          </div>
        </form>
        {summary && (
          <div className="max-w-3xl mx-auto mt-8">
            <h2 className="text-2xl font-bold mb-4">Summary</h2>
            <div className="prose">{summary}</div>
          </div>
        )}
      </main>
    </div>
  );
}
