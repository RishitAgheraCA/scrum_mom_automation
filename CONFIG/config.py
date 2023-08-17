OPENAI_API_KEY = "yourapikey"

TRANSCRIPT_FILE = "speechtotext/services/transcriptions/"

SYMBOLS = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Nvidia": "NVDA"
}

COMMAND_WORD = "whisper"

PROMPT_INSTRUCTIONS = "Return the name of the company and the quantity in the text below. " \
    "If the text contains the words 'by', 'buy', or 'bye', return 'buy' for the action. " \
    "If the text contain the words 'sell', 'cell', or 'sale', return 'sell' for the action. " \
    "Return the result in JSON format:"

PROMPT_OUTPUT_FORMAT = """
{
    "action": "",
    "company": "",
    "quantity": 
}
"""


MODEL_OUTPUT = {
    "person1":{"task_completed:":"",
               "blockers":"",
               "deliverables":""},
    "person2": {"task_completed:": "",
                "blockers": "",
                "deliverables": ""},
}
API="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"