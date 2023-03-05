from .usecases import summarize
import sys

input_file, interviewee = sys.argv[1], sys.argv[2]
f = open(file=input_file, mode='r')
text = f.read()
f.close()
result = summarize(text=text, interviewee_name='Jason')
print(result)