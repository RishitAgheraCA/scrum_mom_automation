
import os
os.environ["OPENAI_API_KEY"] = "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"

from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate

# Setting up the template and chain
demo_template = '''
context = ({context_data}).
From the context, extract information to answer the following questions. Provide ONLY the answers in a concise technical format, separated by commas, without any other words or punctuation:
1. What is the completed task?
2. What task is in progress?
3. How many days are needed to complete the ongoing task?
4. What challenges or issues have been encountered?

Answer Format: [completed task],[ongoing task],[number of days],[challenges/issues]
'''

prompt = PromptTemplate(
    input_variables=['context_data'],
    template=demo_template
)

llm = OpenAI(temperature=0.7)
chain1 = LLMChain(llm=llm, prompt=prompt)

def identifySingleTask(context_data):
    return chain1.run(context_data)

def identifyTasks(names_and_contexts):
    # Dictionary to store results
    results = {}

    # Iterate through the names_and_contexts dictionary and call identifySingleTask
    for name, context in names_and_contexts.items():
        result = identifySingleTask(context)
        results[name] = result

    return results
