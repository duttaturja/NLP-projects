#getting the ollama model and langchain dependencies
from langchain_ollama.llms import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

#function to generate pet names
def generate_pet_name(animal_type, pet_color, names_amount):
    model = OllamaLLM(model="llama3.2:1b") #Ollama model to generate pet names
    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color', 'names_amount'],
        template="I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me {names_amount} cool names for my pet."
    ) #prompt to generate pet names with input variables
    name_chain = LLMChain(
        llm=model,
        prompt=prompt_template_name,
        output_key="pet_name",
    ) #chain to generate pet names through prompt and Ollama model

    #generating pet name from the chain
    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color, 'names_amount': names_amount})
    return response #returning the pet names

if __name__ == "__main__":
    print(generate_pet_name("Dog", "Black", 5))
