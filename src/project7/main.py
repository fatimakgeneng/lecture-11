# Importing the Flow class, start & listen decorators, from a flow file which is in flow model of crewai pagckage

from crewai.flow.flow import Flow, start, listen    # These 3 help in making workflow very easily
import time  # To add fake delay in the workflow

class SimpleFlow(Flow): # Inheriting the Flow class from crewai.flow.flow
    
    @start()           # This is a decorator which is used to start the workflow
    def function1(self):
        print("Step 1...")
        time.sleep(3)

    @listen(function1) # This is a decorator which is used to listen to the previous step
    def function2(self): 
        print("Step 2...")
        time.sleep(3)
    
    @listen(function2)
    def function3(self):
        print("Step 3...")
        time.sleep(3)

def kickoff():
    obj=SimpleFlow()
    obj.kickoff() # this method is inherited from Flow class and it starts the workflow
                    # Has noting to do with the kickoff function defined here