from langchain_ollama.llms import OllamaLLM 
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
Ton travail est de répondre aux questions qui te sont posées en te basant sur des articles.
Utilise les articles suivants pour répondre de manière détaillée et spécifique à la question posée. 
Si tu ne connais pas la réponse, dis que tu ne sais pas. 

IMPORTANT : Indique toujours les sources de ta réponse à la fin, sous la forme : "Sources : [source1, source2, ...]".
Fais un paragraphe uniforme et des points importants extraits des articles.

Articles pertinents (résumés) : {articles}
Sources des articles : {sources}
Question : {question}
"""

prompt = ChatPromptTemplate.from_template(template)
Chain = prompt | model

while True:
    print("\n\n-------------------------------")
    question = input("Posez votre question (q pour quitter): ")
    question = question + ". N'oublie pas de mentionner les sources."
    print("\n\n")
    if question =="q":
        break

    articles = retriever.invoke(question)
    sources = []
    summarized_articles = []
    for article in articles:
        #print(f"Source:{article.metadata['source']}")
        summary = model.invoke(f"Résume cet article : {article.page_content}")
        summarized_articles.append(summary)
        sources.append(article.metadata["source"])

    result = Chain.invoke({"articles": summarized_articles, "question": question, "sources": sources})
    print(result)