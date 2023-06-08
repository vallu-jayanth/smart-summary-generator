import anvil.server
import scrapetube
from youtube_transcript_api import YouTubeTranscriptApi
import openai
import re

@anvil.server.callable
def get_text_from_url(url):
    regex_1 = 'v\=(.*)'
    regex_2 = '\.be\/(.*)'
    video_id = re.findall(regex_1,str(url))
    if len(video_id)==0:
      video_id = re.findall(regex_2,str(url))
    response = YouTubeTranscriptApi.get_transcript(video_id[0],languages=['en','en-IN'])
    text = ["".join(i['text']) for i in response]
    text = " ".join(text)
    return text
@anvil.server.callable
def get_completion(openai_key,prompt,model="gpt-3.5-turbo"):
    openai.api_key = str(openai_key)
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

@anvil.server.callable
def get_summary(key,text):
      prompt = f"""Your task is to generate a summary\
                for the given text. The output should be\
                formatted as follows:\
                - List all the important topics from the text
                - summary of the whole text
                If you fail to recognize important topics\
                tell i don't know\
                the text is delimitited with backticks\
                text : ```{text}```"""
      return get_completion(key,prompt)