import llama2_impl as l2
import write_results as wr


def super_bowl_qa():
    file_paths = [
        '../materials/super_bowl/Super_Bowl_LVII.pdf',
    ]

    qs = [
        'When was the most recent super bowl?',
        'What was the most recent super bowl called?',
        'Who won the most recent super bowl?',
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

    wr.write_results('super_bowl', results)


def main():
    super_bowl_qa()


if __name__ == '__main__':
    main()
