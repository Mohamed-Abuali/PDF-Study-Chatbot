from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from loader import load_pdf

model = ChatOllama(
    model="llama3.2"

)

template = """
You are an expert teacher with a Phd that can give valibale exams question to student to socre high in their real exam the student will ask about a topic and you give a question with 4 option (MSQ) and the student should asnwer .

the data of subject given : {data}

the asked topic from the student: {question}


"""

prompt = ChatPromptTemplate.from_template(template

)

llm = prompt | model


response = llm.invoke({"data":[],"question":"Ask me a question in javascript"})

print(response.content)
print(load_pdf())