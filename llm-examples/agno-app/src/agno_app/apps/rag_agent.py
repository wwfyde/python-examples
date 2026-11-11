import asyncio

from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.vectordb.qdrant import Qdrant

from lib import settings

COLLECTION_NAME = "pdf-reader"

vector_db = Qdrant(collection=COLLECTION_NAME, url="http://localhost:6333")

# Create a knowledge base with the PDFs from the data/pdfs directory
knowledge_base = PDFKnowledgeBase(
    path=settings.temp_dir.joinpath("snow_brand_intro.pdf"),
    vector_db=vector_db,
    reader=PDFReader(chunk=True),
)

# Create an agent with the knowledge base
agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
)

if __name__ == "__main__":
    # Comment out after first run
    asyncio.run(knowledge_base.aload(recreate=False))

    # Create and use the agent
    asyncio.run(agent.aprint_response("雪花啤酒2011年销量", markdown=True))
