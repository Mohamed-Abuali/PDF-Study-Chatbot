from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from vectorstore import get_data

model = ChatOllama(
    model="llama3.2"

)

question_template = """
You are an expert teacher with a Phd that can give valibale exams question to student to socre high in their real exam the student will ask about a topic and you give a question with 4 option (MSQ) and the student should asnwer .

the data of subject given : {data}

the asked topic from the student: {question}



"""
answer_template = """
You are an expert teacher with a Phd that can give valibale exams question to student to socre high in their real exam the student will ask about a topic and you give a question with 4 option (MSQ) and the student should asnwer and you tell him if it's right or wrong.

the question that you give as a teacher : {question}

the student answer: {answer}


"""

question_prompt = ChatPromptTemplate.from_template(question_template)
answer_prompt = ChatPromptTemplate.from_template(answer_template)

llm = question_prompt | model
answer_llm = answer_prompt | model

data = get_data()
while True:
    print("------------------------------------------Question----------------------------------------------")
    response = llm.invoke({"data":data,"question":"Ask me a question in the given topic"})
    print(response.content)
    question = response.content
    answer = input("Answer the question or (enter q to quit):")
    if answer == 'q':
        break
    print("------------------------------------------Result----------------------------------------------")
    result = answer_llm.invoke({"question":question,"answer":str(answer)})
    print(result.content)




