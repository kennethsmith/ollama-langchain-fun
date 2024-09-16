# ollama-langchain-fun

## Notes
In the rags/results/<timestamp>/*.json, the model {'query': {'q': string, 'a': string}} is the QA of the model with no new data loaded.
The pdfs really slow the vectorstore creation down. On my machine it's over 5 minutes to load the debate pdf.

## shell scripts
There are some shell scripts to make life a bit easier, they are intended to run form the directory they are in. Change directory to the directory it is in before executing.
* venv_setup.sh - CAUTION: Deletes ./venv directory and builds a new one with a Python location specified in the script.
* install.sh - Installs all of the packages in the requirements.txt.

## ollama
Running on Ollama:
* https://ollama.com/download (Follow the instructions to install it. Also, brew install ollama)
  * ollama serve (localhost:11434)
  * ollama pull llama2
  * ollama list
    * ollama
      * Usage:
        * ollama [flags]
        * ollama [command]

      * Available Commands:
        * serve       : Start ollama
        * create      : Create a model from a Modelfile
        * show        : Show information for a model
        * run         : Run a model
        * pull        : Pull a model from a registry
        * push        : Push a model to a registry
        * list        : List models
        * ps          : List running models
        * cp          : Copy a model
        * rm          : Remove a model
        * help        : Help about any command

      * Flags:
        * -h, --help      : help for ollama
        * -v, --version   : Show version information

      * Use "ollama [command] --help" for more information about a command.

## langchain
* https://python.langchain.com/v0.1/docs/guides/development/local_llms/

## references
* https://github.com/t-redactyl/simple-rag-document-qa
* https://python.langchain.com/v0.1/docs/guides/development/local_llms/
* https://github.com/ollama/ollama/blob/main/README.md
* https://github.com/ollama/ollama-python
* https://ollama.com/library
* https://python.langchain.com/v0.2/docs/tutorials/rag/
* https://api.python.langchain.com/en/latest/langchain_api_reference.html