from ollama_impl import OllamaQA

mp = {
    'model': 'llama2',
    'chunk_size': 1000,
    'chunk_overlap': 0,
    'search_type': 'similarity',
    'num_docs': 5,
    'chain_type': "stuff",
}


class Llama2QA:
    def __init__(self, materials):
        self.ollama_qa = OllamaQA(mp['model'],
                                  materials,
                                  mp['chunk_size'],
                                  mp['chunk_overlap'],
                                  mp['search_type'],
                                  mp['num_docs'],
                                  mp['chain_type'])
        self.llm = self.ollama_qa.llm
        self.chain = self.ollama_qa.chain
