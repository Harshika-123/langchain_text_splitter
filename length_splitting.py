from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('dl-curriculum.pdf')


docs=loader.load()
splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,#10-20 % of overlaping is a good number for overlapping
    separator=''
)
result=splitter.split_documents(docs)
print(result[0].page_content)