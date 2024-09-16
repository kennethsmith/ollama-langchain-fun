import llama2_impl as l2
import write_results as wr


def trump_harris_qa():
    file_paths = [
        '../materials/harris_trump/2024_United_States_presidential_debates.pdf',
        '../materials/harris_trump/debate-2024-09-10.txt',
        '../materials/harris_trump/NPR - Trump Harris.txt',
        '../materials/harris_trump/fact_check_blurb.txt',
    ]

    qs = [
        'Who won the Trump and Harris debate?',
        'When was the last Trump Harris debate?',
        'Did Trump lie during the debate?',
    ]

    qa = l2.Llama2QA(file_paths)
    chain = qa.chain
    llm = qa.llm
    results = []

    h = []
    for q in qs:
        a = chain.invoke({'query': q, 'chat_history': h})
        h.append((a['query'], a['result']))
        results.append({'query': wr.build_object(a)})

    for q in qs:
        a = llm.invoke(q)
        results.append({'query': {'q': q, 'a': a}})

    wr.write_results('trump_harris', results)


def main():
    trump_harris_qa()


if __name__ == '__main__':
    main()
