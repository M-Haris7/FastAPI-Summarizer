# File Summarizer

File Summarizer is a web application that allows users to upload documents and receive summarized versions using a locally deployed Language Model. The backend is built with FastAPI, the frontend with React, and BART is used as the LLM model for document summarization.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)

## Features
- Upload documents for summarization
- Get concise summaries using BART model
- FastAPI backend for efficient processing
- React frontend for a smooth user experience

## Technologies Used
### Frontend
- React
- Babel
- Webpack
- TailwindCSS

### Backend
- FastAPI
- Uvicorn
- Pydantic
- PyTorch
- Transformers (BART model)

## Installation
### Frontend
1. Clone the repository:
    ```bash
    git clone https://github.com/M-Haris7/FastAPI-Summarizer.git
    cd filesummarizer/frontend
    ```

2. Install the dependencies:
    ```bash
    npm install
    ```

3. Start the development server:
    ```bash
    npm start
    ```

4. To build for production:
    ```bash
    npm run build
    ```

### Backend
1. Navigate to the backend directory:
    ```bash
    cd filesummarizer/backend
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install fastapi uvicorn pydantic torch transformers
    ```

4. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

## Usage
1. Start the backend server as described in the installation steps.
2. Start the frontend development server as described in the installation steps.
3. Open your browser and navigate to `http://localhost:8080` to use the application.
4. Upload a document and get a summarized version.
