import json
from openai import OpenAI
from dotenv import load_dotenv
import os
import prompts

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("API_KEY"))

# Define the base system message
base_system_message = '''I am making an AI learner system, I get course details including performance criteria required for a student to qualify,
knowledge evidences that contain the topics one needs to learn to clear the performance criteria.
You have to add related knowledge evidences to the performance criteria I provide in JSON format. Add a key named topics and add the related knowledge evidences to each criterion in form of a list....add just the topic name.'''

messages=[]
mapping=[]

def get_user_prompt(data, custom_prompt=None):
    if custom_prompt:
        return f"i am giving you the performance criteria, return me formatted json performance criteria only after adding the topics for each criteria, here are the performance crietias :{data['elements_and_performance_criteria']}, here are the knowledge evidences: {data['knowledge_evidence']}.........also, some evidences have the word 'including' in them.... remove the word 'including' from them.......also, dont return the data in a code block....i am using API and i want to use the data you sent me directly. {custom_prompt}"
    else:
        return f"i am giving you the performance criteria, return me formatted json data after adding the topics for each criteria, {data['elements_and_performance_criteria']}, here are the knowledge evidences: {data['knowledge_evidence']}.........also, some evidences have the word 'including' in them.... remove the word 'including' from them.......also return the data not in a code block...i am using API and i want to use the data you sent me directly "

def update_training_data(data, custom_prompt=None):
    global messages,mapping
    messages = [
        {"role": "system", "content": prompts.prompt1},
        {"role": "system", "content": prompts.prompt2},
        {"role": "system", "content": prompts.prompt3},
        {"role": "system", "content": f'i am providing you with the performance criteria in json format:\n{data["elements_and_performance_criteria"]}\njust remember it for now, i will provide you with knowledge evidences next'},
        {"role": "system", "content": f'here is the knowledge evidence,\n {data["knowledge_evidence"]}\n remember them and wait for my command to generate mapping'},
        {"role": "system", "content": 'Knowledge evidences are topics one need to learn the performance criterias, we need to map the KEs to PC.'},
    ]

    combined_mappings = []

    # Iterate over each performance criterion and create a completion
    for i in data["elements_and_performance_criteria"]:
        user_message = {"role": "user", "content": f"Now generate the mapping for the given PC and return it in json format not in a code block:{i}\n {custom_prompt}"}
        current_messages = messages + [user_message]

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=current_messages
        )

        response_content = completion.choices[0].message.content
        try:
            mapping_result = json.loads(response_content)
            combined_mappings.extend(mapping_result['Mappings'])
        except json.JSONDecodeError:
            print("Failed to decode JSON from the response:")
            print(response_content)

    # Create a single dictionary with combined mappings
    final_mappings = {"Mappings": combined_mappings}
    mapping = final_mappings
    #with open('combined_mappings.json', 'w') as outfile:
     #   json.dump(final_mappings, outfile, indent=4)
    
    #print("Combined mappings saved to combined_mappings.json")
    
    return final_mappings

def extract_topics_from_evidences(knowledge_evidence, custom_prompt=""):
    global messages
    messages.extend([{"role": "system", "content": prompts.prompt4}])
    try:
        topics = []
        for i in mapping["Mappings"]:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages + [
                    {"role": "user", "content": f'''Divide the criteria including the KE mapped using the mapping generated before and {knowledge_evidence}.
Here is the PC I want you to divide: {i}

Return the PC and subtopics in this JSON format:
{{
    "topics": [
        {{
            "PC": "(PC 3.1) WHS/OHS work completion risk control measures and workplace procedures are followed",
            "subtopics": [
                "WHS/OHS Work Completion Risk Control Measures",
                "Importance of Following Workplace Procedures",
                "Relevance of Legislated Requirements in Work Completion",
                "Ensuring Compliance with Relevant WHS/OHS Legislations",
                "Safety Measures in Completing Work Activities"
            ]
        }}
    ]
}}
Use this just as an example.
'''
                    }]
            )
            topic = eval(completion.choices[0].message.content)
            topics.append(topic["topics"][0])
        return {"topics": topics}

    except Exception as e:
        print(f"Error extracting topics: {str(e)}")

def generate_topic_description(data,topic_name,subtopic_name,custom_prompt=None):
    try:
        messages= [
        {"role": "system", "content": prompts.prompt5},
        {"role": "system", "content": prompts.prompt6},
        {"role": "system", "content": f'''since we need to generate data according to aqf levels, here is a description of all the AQF level:
{prompts.prompt7}
Please remember them'''},
        {"role": "system", "content": f'''{prompts.prompt8}
unit code:{data["competency_id"]}
name : {data["title"]}
application: {data["application"]}

'''},
        {"role": "user", "content": f'''this is the heading for the topic: {topic_name}
you need to describe this subheading while keeping the heading in mind and according to the AQF level i described before
generate just the description for this subheading as text, no need for formatting or anything : {subtopic_name}
{custom_prompt}
'''}
        ]

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        print(f"Error generating topic description: {str(e)}")
        return None
    
    return topics

if (__name__)=="__main__":
    data = []
    with open("UEECD0007_training_data.json","r") as f:
        data = json.load(f)
    heading="(PC 1.1) Work health and safety (WHS)/occupational health and safety (OHS) requirements and workplace procedures for a given work area are obtained and applied"
    sub="Importance of Workplace Procedures"
    print(generate_topic_description(data,heading,sub," "))
    
