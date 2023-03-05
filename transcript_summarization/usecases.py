import openai
import os
from typing import List

openai.organization = os.getenv("OPENAI_ORG")
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_transcript(text: str, interviewee_name: str, model: str='text-davinci-003'):
    prompt = f"""
    Summarize the following conversation in less than 400 words. 
    The details provided by {interviewee_name} are important.
    {text}
    """
    completion = openai.Completion.create(
        model=model, 
        prompt=prompt, 
        max_tokens=800,
        temperature=0)
    result = completion["choices"][0]['text']
    return result

def summarize_paragraphs(text: str, model: str='text-davinci-003'):
    prompt = f"""
    Summarize the following paragraphs in less than 400 words.
    {text}
    """
    completion = openai.Completion.create(
        model=model,
        prompt=prompt, 
        max_tokens=800,
        temperature=0)
    result = completion["choices"][0]['text']
    return result

def summarize(text: str, interviewee_name: str):
    lines = text.split('\n')
    n = len(lines)
    start = 0
    cur_len = 0
    results = []
    for i in range(n):
        cur_len += len(lines[i])
        if cur_len/4 >= 1600 or i == n-1:
            text = '\n'.join(lines[start:i+1])
            results.append(summarize_transcript('\n'.join(lines[start:i+1]), interviewee_name=interviewee_name))
            start = i+1
            cur_len = 0
    if len(results) > 1:
        summary = summarize_paragraphs('\n'.join(results))
        return summary
    return results[0]
