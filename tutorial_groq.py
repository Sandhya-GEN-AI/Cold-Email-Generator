from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os


load_dotenv()

api_key =os.getenv("GROQ_API_KEY")


llm = ChatGroq(
    
    model="llama-3.3-70b-versatile",
    temperature = 0,

)

response =llm.invoke("The first person land on moon was....")
print(response.content)