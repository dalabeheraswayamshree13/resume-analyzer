# AI Resume Analyzer

This project is a simple AI-based Resume Analyzer built using Python, Flask, and scikit-learn. The application allows users to upload a resume in PDF format and compare it with a job description to calculate a match score.

## Features

- Upload resume in PDF format
- Enter job description
- Analyze resume similarity with job description
- Display match percentage score

## Technologies Used

- Python
- Flask
- scikit-learn
- PyPDF2
- HTML

## Project Structure

resume-analyzer
│
├── app.py
└── templates
     └── index.html

## How to Run

1. Install required libraries

python -m pip install flask scikit-learn PyPDF2

2. Run the application

python app.py

3. Open browser

http://127.0.0.1:5000

## Output

The application calculates the similarity between the resume and the job description and displays a match percentage.
