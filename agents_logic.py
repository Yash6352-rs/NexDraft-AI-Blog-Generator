import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate

# Load key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Set Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.7
)

# Research agent
research_agent = PromptTemplate(
    input_variables=["topic"],
    template="""
You're a skilled researcher. Provide a concise summary (under 200 words) on the topic: "{topic}".
Include key facts, tips, or insights. Use bullet points if helpful.
"""
)

research_chain = LLMChain(
    llm=llm,
    prompt=research_agent,
    output_key="research_summary"
)

# Writing agent
writing_agent = PromptTemplate(
    input_variables=["topic", "research_summary"],
    template="""
You are a professional content writer.

Using this research:
{research_summary}

Write a blog post on the topic "{topic}" in under 500 words.
Structure it with an introduction, body, and conclusion. Make it engaging and informative.
"""
)

writing_chain = LLMChain(
    llm=llm,
    prompt=writing_agent,
    output_key="blog_draft"
)

# Review, checking agent
review_agent = PromptTemplate(
    input_variables=["blog_draft"],
    template="""
You are a proofreader and editor.

Review and polish the following blog post. Fix grammar, improve flow, and shorten where possible — without changing the meaning.

Blog Draft:
{blog_draft}

Return the final, polished version:
"""
)

review_chain = LLMChain(
    llm=llm,
    prompt=review_agent,
    output_key="final_blog"
)

# Combine all steps into a single sequential chain

blog_chain = SequentialChain(
    chains=[research_chain, writing_chain, review_chain],
    input_variables=["topic"],
    output_variables=["final_blog"],
    verbose=True
)

def run_blog_creation(topic: str) -> str:
    result = blog_chain.run(topic=topic)
    return result
