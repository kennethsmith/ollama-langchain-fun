import datetime
import os
import json


def build_object(a):
    r = {
        'query': a['query'],
        'result': a['result'],
        'chat_history': [],
        'source_documents': [],
    }

    for h in a['chat_history']:
        r['chat_history'].append(
            {
                'query': h[0],
                'result': h[1],
            }
        )

    for d in a['source_documents']:
        r['source_documents'].append(
            {
                'index': a["source_documents"].index(d),
                'type': d.type,
                'source': d.metadata['source'],
                'page_content': d.page_content,
            }
        )

    return r


def write_results(context, results):
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    cwd = './results/' + ts
    file = cwd + '/' + context + '.json'
    os.mkdir(cwd)

    with open(file, 'w') as outfile:
        json.dump(results, outfile, indent=2)
