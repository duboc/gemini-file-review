import os
import base64

import vertexai
from vertexai.preview.generative_models import GenerativeModel

PROJECT_ID = os.environ.get('GCP_PROJECT', '-')
LOCATION = os.environ.get('GCP_REGION', '-')


with open('user_code.txt', 'r') as f:
    user_code = f.read()

vertexai.init(project=PROJECT_ID, location=LOCATION)
model = GenerativeModel("gemini-1.5-pro-preview-0409")


prompt = f"""
    Consider the following code:
    {user_code}

    Perform automated code review to identify potential inefficiencies and poor coding practices and provide all the answers in markdown format.
    Output:
        If issues found:
	    Path: File name and path. 
            Location: Class and method name(s) where the issue occurs.
            Issue: Description of the inefficiency or poor practice.
            Suggestion: Specific guidance on how to improve the code (consider providing alternative code examples).
            Severity: If possible, indicate the potential impact of the issue (e.g., performance bottleneck, maintainability risk, security vulnerability).
        If no issues found: Output "No Issues".
        
    Output Example: 
        Path: ../src/code/service.file
        Location: class DataProcessor, method load_data
        Issue: Loading entire file into memory at once could be inefficient for large files.
        Suggestion: Consider using a generator or line-by-line processing to reduce memory usage.
        Severity: Medium (depends on your application's expected file sizes)"""


prompt_response = model.generate_content(prompt,
        generation_config={
            "max_output_tokens": 4096,
            "temperature": 0.4,
            "top_p": 1
        },
    )

print(f"Gemini Model response: {prompt_response.text}")
