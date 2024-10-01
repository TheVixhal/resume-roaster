from crewai import Task
from textwrap import dedent

class Roast:

    def task1(self, agent, cleaned_data):
        return Task(
            description=dedent(f"""
            Resume: {cleaned_data}
            //This is the resume of a person, write a funny, brutal and uncensored very disrespectful roast for them. if given data doesn't seems like resume then tell me to upload resume and give me at least 300 words response and in proper text. also add emoji in resume and see your response should directly mention the person by you whoese resume it is
            """),
            expected_output="This is the resume of a person, write a funny, brutal and uncensored very disrespectful roast for them. if given data doesn't seems like resume then tell me to upload resume and give me at least 300 words response and in proper text. also add emoji in resume and see your response should directly mention the person by you whoese resume it is",
            agent=agent
        )

    

