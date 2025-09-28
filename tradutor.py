from langchain_community.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

# carregando variáveis de ambiente
load_dotenv()
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")

# configurando o modelo
llm = AzureChatOpenAI(
    openai_api_key=AZURE_OPENAI_KEY,
    openai_api_base=AZURE_ENDPOINT,
    deployment_name=AZURE_DEPLOYMENT_NAME,
    openai_api_type="azure",
    openai_api_version="2023-07-01-preview",
    temperature=0.7,
    max_tokens=900
)

# extraindo texto de uma URL


def extract_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for tag in soup(["script", "style"]):
            tag.decompose()
        return soup.get_text(" ", strip=True)
    return None

# traduzindo


def translate_article(text, lang):
    messages = [
        SystemMessage(content="Você atua como tradutor de textos."),
        HumanMessage(
            content=f"Traduza: {text} para o idioma {lang} e responda apenas com a tradução em formato markdown.")
    ]
    return llm(messages).content


# testando
url = "https://www.vagalume.com.br/linkin-park/crawling.html"
text = extract_text(url)
traducao = translate_article(text, "português")
print(traducao)
