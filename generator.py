from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.6,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

def generator_func(tone,input_story):
    prompt=PromptTemplate(
        input_variables=["tone","input_story"],
        template="Rewrite the following story in {tone} style:\n{input_story}\n. NOTE: you must include the context of original story and add more details to it."
        )
    chain=LLMChain(llm=llm,prompt=prompt)
    return chain.run(tone=tone,input_story=input_story)