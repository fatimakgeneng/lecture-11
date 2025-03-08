from crewai.flow.flow import Flow, listen, start, router, or_
import random

class RouteFlow(Flow):

    @start()
    def greeting(self):
        print("Hey There!")
        cities = ["karachi", "islamabad", "lahore"]

        select_city = random.choice(cities)
        self.state["city"] = select_city

    @router(greeting)
    def select_city(self):
        

        if self.state["city"] == "karachi":
            return "karachi"
        elif self.state["city"] == "islamabad":
            return "islamabad"
        else:
            return "lahore"

    
    @listen("karachi")
    def karachi1(self):
        print(f"Write some fun facts about {self.state['city']}")
        return f"Write some fun facts about {self.state['city']}"

    @listen("islamabad")
    def islamabad1(self):
        print(f"Write some fun facts about {self.state['city']}")
        return f"Write some fun facts about {self.state['city']}"

    @listen("lahore")
    def lahore1(self):
        print(f"Write some fun facts about {self.state['city']}")    
        return f"Write some fun facts about {self.state['city']}"


def kickoff():
    obj = RouteFlow()
    obj.kickoff()

def plot():
    obj = RouteFlow()
    obj.plot()