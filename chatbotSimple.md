## Required imports -( install python 3.10 )
1. load_dotenv
2. HuggingFaceHub
3. LLMChain
4. PromptTemplate

# load vaules from .env File 
`load_dotenv()`

## specify the Model you want to use
`model_id = "gpt2-medium"`

## define your model with appropriate values
`con_model = HuggingFaceHub(repo_id=model_id, model_kwargs={"temperature":0.8, "max_new_tokens":200})`

## create your prompt template
```
prompt = PromptTemplate(
    input_variables=["question"],
    template="You are a Amirican telling the storey about India and its culture: {question}"
)
```
## create the chain using LLMChain 
This is the one responcible to perform action
`chain = LLMChain(prompt=prompt, llm=con_model, verbose=True)`

## run the chain to get results
```
res = chain.run(str)
print(res)
```
