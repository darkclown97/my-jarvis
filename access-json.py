#!/usr/bin/env python3

import os
import sys
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
  print("Please set OPENAI_API_KEY environment variable")
  sys.exit(1)

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=sys.argv[1],
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.2,
  presence_penalty=0
)
print(response.choices[0].text)