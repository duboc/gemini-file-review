# gemini-file-review
This Python code snippet demonstrates automated code review using Google's Gemini language model. It loads user code from a file, initializes the Gemini model, and generates a markdown-formatted report highlighting potential inefficiencies and poor coding practices. The report includes the location of the issue, a description, a suggestion for improvement, and the severity of the issue. If no issues are found, the code outputs "No Issues."

I'm using [1filellm](https://github.com/jimmc414/1filellm) to generate a single text file from the [Hipster Shop](https://github.com/GoogleCloudPlatform/microservices-demo) demo, the output of the repo is stored in a file named **user_code.txt**.

The code snippet is designed to be used in a serverless environment, such as Cloud Functions or App Engine. It handles HTTP requests and uses Google Cloud Logging for logging purposes.

To use the code snippet, you need to have a Gemini model deployed in Vertex AI and set the **GCP_PROJECT** and **GCP_REGION** environment variables accordingly. You also need to provide your user code in a file named **user_code.txt**.

```
export GCP_PROJECT=gemini-file-review
export GCP_REGION=us-central1
```


Once you have set up the environment and provided the user code, you can run the code snippet to generate a code review report. The report will be printed to the console.

```
python3 code_review.py
```
