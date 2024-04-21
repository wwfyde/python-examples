from langchain.prompts import ChatPromptTemplate

prompt = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""

prompt_template = ChatPromptTemplate.from_template(prompt)
print(prompt_template, 'ChatPromptTemplate')
