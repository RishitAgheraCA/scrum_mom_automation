
import os,json
from CONFIG.config import API
os.environ["OPENAI_API_KEY"] = API

from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate

# Setting up the template and chain
demo_template = '''
context = ({context_data}).
identify name of the persons and their speech from above text and make it in json format.
Answer formate should be like each person name is key and speech is value.
'''

prompt = PromptTemplate(
    input_variables=['context_data'],
    template=demo_template
)

llm = OpenAI(temperature=0.7)
chain1 = LLMChain(llm=llm, prompt=prompt)

def identifySingleTask(context_data):
    return chain1.run(context_data)

def identify_speaker(context):
    # Dictionary to store results
    results = {}

    # Iterate through the names_and_contexts dictionary and call identifySingleTask
    # for name, context in names_and_contexts.items():
    result = identifySingleTask(context)
    results = result
    # print(results)
    # print('typeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee',type(results))
    json_results = json.loads(results)
    # print(json_results)
    return json_results

# context = """Hey everyone, I'm Alex. I've been working in the software development field for about 8 years now.
# Mostly focused on full-stack web development, but lately, I've been diving deep into machine learning and AI. Super
# excited to be here!Hi Alex, I'm Sarah. Nice to meet you! I come from a background in data analysis and visualization.
# I've spent the last few years working with various data mining tools and creating insightful reports for our clients.
# Looking forward to exchanging ideas with you all!Hi Alex, Sarah! I'm Mark. My expertise lies in cybersecurity. I've
# been in the industry for over a decade, specializing in network security and penetration testing. I'm all about
# keeping our digital world safe from threats. Great to be a part of this conversation! """
#
# identifyTasks(context)