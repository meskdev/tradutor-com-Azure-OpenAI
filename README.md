# Tradutor de Artigos com Azure OpenAI

Este projeto é um tradutor automático de textos extraídos de páginas web, utilizando o serviço Azure OpenAI e a biblioteca LangChain. Basta informar a URL de um artigo e o idioma desejado, e o script retorna a tradução em formato Markdown.

## Funcionalidades

- Extração automática do texto principal de qualquer página web.
- Tradução do conteúdo para o idioma desejado usando modelos avançados do Azure OpenAI.
- Fácil configuração por variáveis de ambiente.

## Como usar

1. **Clone o repositório e instale as dependências:**
   ```
   pip install -r requirements.txt
   ```

2. **Configure o arquivo `.env` com suas credenciais do Azure OpenAI:**
   ```
   AZURE_OPENAI_KEY=SuaChaveAqui
   AZURE_ENDPOINT=https://seurecurso.openai.azure.com/
   AZURE_DEPLOYMENT_NAME=nome-do-seu-deployment
   ```

3. **Execute o script:**
   ```
   python tradutor.py
   ```

## Exemplo de uso

O script já vem configurado para traduzir o conteúdo da página de letras de música do Linkin Park. Basta rodar e conferir o resultado no terminal.

## Requisitos

- Python 3.8+
- Conta e recurso do Azure OpenAI com um deployment ativo

## Créditos

Desenvolvido para fins educacionais, utilizando:
- [LangChain](https://github.com/langchain-ai/langchain)
- [Azure OpenAI](https://learn.microsoft.com/azure/cognitive-services/openai/overview)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

---
