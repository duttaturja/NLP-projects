from langchain_ollama.llms import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def generate_pet_name(animal_type, pet_color):
    model = OllamaLLM(model="llama3.2:1b")
    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet."
    )
    name_chain = LLMChain(
        llm=model,
        prompt=prompt_template_name,
        output_key="pet_name",
    )
    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})
    return response
