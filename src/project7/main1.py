# Now making it a bit complex using litellm
# first install litellm using uv add litellm

import os
from crewai.flow.flow import Flow, start, listen 
from litellm import completion    # Importing the completion function

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

class CityFunFact(Flow):
    

    @start()
    def generate_random_city(self):
        result = completion(
            model="gemini/gemini-1.5-flash",
            api_key=GEMINI_API_KEY,
            messages=[{"content": "Return any random city name from Pakistan", "role": "user"}],
        )
        city = result['choices'][0]['message']['content']
        print(f"====================  {city}  ====================")
        return city  #for sending the city name to the next function   BAD PRACTICE
    

    @listen(generate_random_city)
    def generate_fun_fact(self, city_name):
        result = completion(
            model="gemini/gemini-2.0-flash-exp",
            api_key=GEMINI_API_KEY,
            messages=[{"content": f"Write some fun facts about {city_name}", "role": "user"}],
        )
        fun_fact = result['choices'][0]['message']['content']
        print(fun_fact)
        self.state['fun_fact'] = fun_fact # for sending the fun fact to the next function


    @listen(generate_fun_fact)
    def save_fun_fact(self):
        with open("fun_fact.md", "w") as file:  # For preview of the fun fact.md file press ctrl+shift+v
            file.write(self.state['fun_fact'])
            return self.state['fun_fact'] 


def kickoff():
    obj=CityFunFact()
    result=obj.kickoff() # this method is inherited from the Flow class which is a parent class
    print(result)