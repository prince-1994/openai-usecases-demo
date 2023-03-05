

# RUN SERVER

Set the following env vars: OPENAI_API_KEY, OPENAI_ORG

Run the server : python -m server

Use curl to hit the service : ex. curl -X POST  -F file=@input.txt -F interviewee=Jason http://localhost:3000/summarize/transcript/

# RUN APP

Set the following env vars: OPENAI_API_KEY, OPENAI_ORG

Run the App : python -m transcript_summarization input.txt