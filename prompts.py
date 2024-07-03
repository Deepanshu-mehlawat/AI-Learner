prompt1='''I'm going to brief you about our business and what we do so that you can get the context of the business and help in developing the resources required. 

We are based in Australia and started the company in 2019, the aim of the business is to provide best quality curriculum material to the RTOs at affordable price. 

We deal with the VET sector in Australia which is vocational education training and adhere by the guidelines of ASQA and follow AQF standard and other educational bodies in Australia to develop the curriculum material. 

We develop the curriculum material for RTOs and TAFEs for the different training packages available on the training.gov.au website. 

The main audience of the curriculum material who will read the content is VET sector students from different cultural package and different needs who wants to complete the different certificates and get the practical knowledge to implement in the real workplace to secure the job so we make sure that the content and information provided is up to date as per the current industry practices and needs 

We also make sure to use Australian English at all times while developing the material and make sure that the writing context is professional and formal writing to ensure we avoid the blog writing language which is the use of first person, any names of people etc. 

We also make sure that the material developed provided the full form of the abbreviations used for better clarity and provide the example limited only to Australia.'''

prompt2='''Great, now what we do is we get the unit code from the project manager on which we need to work and develop the learner guide and after getting that we get the information from trainign.gov.au. 

As you have limited access to websites, I'll provide you with the information about the unit on which we need to work by accessing it from TGA. 

Here is the unit for you to understand at this stage.
"competency_id": "UEECD0007",
"title": "UEECD0007 - Apply work health and safety regulations, codes and practices in the workplace(Release 1)"

"application": "This unit involves the skills and knowledge required to apply work health and safety (WHS)/occupational health and safety (OHS) regulations and codes of practices in the electrotechnology workplace.\nIt includes applying safe working practices, following workplace procedures for hazard identification and risk control. It also includes electrotechnology worker responsibilities and application for health and safety, risk management and adherence to safety practices as part of electrotechnology work functions when preparing to enter a work area.\nNo licensing, legislative or certification requirements apply to this unit at the time of publication."

"elements_and_performance_criteria": [
        {
            "element": {
                "number": "1",
                "title": "Prepare to enter an electrotechnology workplace"
            },
            "criteria": [
                {
                    "number": "1.1",
                    "description": "Work area access permits are obtained from appropriate person/s in accordance with workplace procedures"
                },
                {
                    "number": "1.2",
                    "description": "Relevant workplace WHS/OHS safety regulations and codes of practices are identified and followed when entering the electrotechnology work area"
                },
                {
                    "number": "1.3",
                    "description": "Safe work methods for controlling risks are obtained, read and applied prior to undertaking work activity in accordance with WHS/OHS workplace procedures"
                },
                {
                    "number": "1.4",
                    "description": "Preparation for electrical and non-electrical isolation is carried out to prevent creation of hazards from loss of machine/system/process control in accordance with WHS/OHS workplace procedures"
                },
                {
                    "number": "1.5",
                    "description": "Tools, equipment and chemicals required for the electrotechnology work are checked for safety and correct functionality in accordance with workplace procedures and regulatory requirements"
                },
                {
                    "number": "1.6",
                    "description": "Personal protective equipment (PPE) is worn appropriate to the electrotechnology work area and in accordance with workplace procedures"
                }
            ]
        }]


"knowledge_evidence": [
        {
            "evidence": "effective verbal and written communication techniques",
            "sublist": [],
            "number": "1"
        },
        {
            "evidence": "electrotechnology work environment, including:",
            "sublist": [
                {
                    "evidence": "appropriate fire extinguisher for a given type of fire",
                    "sublist": [],
                    "number": "2.1"
                },
                {
                    "evidence": "commonly used workplace safety signs",
                    "sublist": [],
                    "number": "2.2"
                },
                {
                    "evidence": "relevant industry standard for safe workplace procedures",
                    "sublist": [],
                    "number": "2.3"
                },
                {
                    "evidence": "risk assessment documentation",
                    "sublist": [],
                    "number": "2.4"
                },
                {
                    "evidence": "typical hazards associated with a range of work environments",
                    "sublist": [],
                    "number": "2.5"
                },
                {
                    "evidence": "use of fire extinguishers",
                    "sublist": [],
                    "number": "2.6"
                },
                {
                    "evidence": "housekeeping and potential hazards in relation to improper housekeeping",
                    "sublist": [],
                    "number": "2.7"
                },
                {
                    "evidence": "workplace procedures used to control the risks associated with workplace hazards",
                    "sublist": [],
                    "number": "2.8"
                }
            ],
            "number": "2"
        }]

At this stage understand the unit only by going through the application and see which kind of people it is more relevant too . just try to understand the structure, dont generate anything just yet'''

prompt3='''great so what we do first before starting the learner guide is map the knowledge evidence with the most relevant performance criteria 
We number the knowledge evidence and refer it as KE and then map with the relevant performance criteria which is referred as PC 
here is an example
"elements_and_performance_criteria": [
        {
            "element": {
                "number": "1",
                "title": "Prepare to enter an electrotechnology workplace"
            },
            "criteria": [
                {
                    "number": "1.1",
                    "description": "Work area access permits are obtained from appropriate person/s in accordance with workplace procedures"
                },
                {
                    "number": "1.2",
                    "description": "Relevant workplace WHS/OHS safety regulations and codes of practices are identified and followed when entering the electrotechnology work area"
                },
                {
                    "number": "1.3",
                    "description": "Safe work methods for controlling risks are obtained, read and applied prior to undertaking work activity in accordance with WHS/OHS workplace procedures"
                },
                {
                    "number": "1.4",
                    "description": "Preparation for electrical and non-electrical isolation is carried out to prevent creation of hazards from loss of machine/system/process control in accordance with WHS/OHS workplace procedures"
                },
                {
                    "number": "1.5",
                    "description": "Tools, equipment and chemicals required for the electrotechnology work are checked for safety and correct functionality in accordance with workplace procedures and regulatory requirements"
                },
                {
                    "number": "1.6",
                    "description": "Personal protective equipment (PPE) is worn appropriate to the electrotechnology work area and in accordance with workplace procedures"
                }
            ]
        },
        {
            "element": {
                "number": "2",
                "title": "Apply safe electrotechnology working practices"
            },
            "criteria": [
                {
                    "number": "2.1",
                    "description": "Risk control work measures are implemented in accordance with WHS/OHS workplace procedures"
                },
                {
                    "number": "2.2",
                    "description": "Procedures for dealing with accidents, fires and emergencies are followed in accordance with workplace procedures, scope of responsibility and capabilities"
                },
                {
                    "number": "2.3",
                    "description": "Safe work methods are applied when working at heights including safe and effective use of safety equipment"
                },
                {
                    "number": "2.4",
                    "description": "Safe work methods are used when undertaking lifting, lowering, pushing, pulling, carrying or otherwise moving, holding or restraining workplace tasks in accordance with relevant code of practice"
                },
                {
                    "number": "2.5",
                    "description": "Safe work methods for removing an electric shock victim from a live electrical situation are demonstrated in accordance with workplace emergency management procedures"
                },
                {
                    "number": "2.6",
                    "description": "Working area is kept clean, neat and tidy in accordance with workplace housekeeping procedures"
                }
            ]
        }]

"knowledge_evidence": [
        {
            "evidence": "effective verbal and written communication techniques",
            "sublist": [],
            "number": "1"
        },
        {
            "evidence": "electrotechnology work environment, including:",
            "sublist": [
                {
                    "evidence": "appropriate fire extinguisher for a given type of fire",
                    "sublist": [],
                    "number": "2.1"
                },
                {
                    "evidence": "commonly used workplace safety signs",
                    "sublist": [],
                    "number": "2.2"
                },
                {
                    "evidence": "relevant industry standard for safe workplace procedures",
                    "sublist": [],
                    "number": "2.3"
                },
                {
                    "evidence": "risk assessment documentation",
                    "sublist": [],
                    "number": "2.4"
                },
                {
                    "evidence": "typical hazards associated with a range of work environments",
                    "sublist": [],
                    "number": "2.5"
                },
                {
                    "evidence": "use of fire extinguishers",
                    "sublist": [],
                    "number": "2.6"
                },
                {
                    "evidence": "housekeeping and potential hazards in relation to improper housekeeping",
                    "sublist": [],
                    "number": "2.7"
                },
                {
                    "evidence": "workplace procedures used to control the risks associated with workplace hazards",
                    "sublist": [],
                    "number": "2.8"
                }
            ],
            "number": "2"
        },
        {
            "evidence": "legal requirements relevant to WHS/OHS in the workplace, including:",
            "sublist": [
                {
                    "evidence": "appropriate personal protective equipment (PPE)",
                    "sublist": [],
                    "number": "3.1"
                },
                {
                    "evidence": "asbestos awareness and reporting hazardous gases, including supervisory requirements and duty of care",
                    "sublist": [],
                    "number": "3.2"
                },
                {
                    "evidence": "difference between hazards and risks",
                    "sublist": [],
                    "number": "3.3"
                },
                {
                    "evidence": "duty holder responsibilities, as specified in WHS/OHS Acts, regulations and codes of practice",
                    "sublist": [],
                    "number": "3.4"
                },
                {
                    "evidence": "employer and employee responsibilities, rights and obligations",
                    "sublist": [],
                    "number": "3.5"
                },
                {
                    "evidence": "general aims and objectives of the relevant state or territory legislation relating to WHS/OHS",
                    "sublist": [],
                    "number": "3.6"
                },
                {
                    "evidence": "hazards that may be present in the electrotechnology workplace, the harm they can cause and how this harm occurs",
                    "sublist": [],
                    "number": "3.7"
                },
                {
                    "evidence": "housekeeping and potential hazards in relation to improper housekeeping",
                    "sublist": [],
                    "number": "3.8"
                },
                {
                    "evidence": "major functions of safety committees and representatives",
                    "sublist": [],
                    "number": "3.9"
                },
                {
                    "evidence": "powers of health and safety inspectors",
                    "sublist": [],
                    "number": "3.10"
                },
                {
                    "evidence": "relevant WHS/OHS regulations, codes and practices",
                    "sublist": [],
                    "number": "3.11"
                },
                {
                    "evidence": "underlying principles of WHS",
                    "sublist": [],
                    "number": "3.12"
                }
            ],
            "number": "3"
        }]


Now that we have the Knowledge Evidence and Performance criteria, we need to map all the KE to the performance criterias that they relate to, in JSON format such that the 

THe output should have a key named Mapping which has an array as value
this array includes objects with performance criteria : it has the performance criteria number and description
the there is mapped knowledge evidence : it has the KE numberand description
finally there is the reason for mapping : it contains reason why we mapped the certain KE for PC.
for example,
{
    "Mappings": [
        {
            "Performance Criterion": "(PC 1.1) Work area access permits are obtained from appropriate person/s in accordance with workplace procedures",
            "Mapped Knowledge Evidence": "(KE 1) effective verbal and written communication techniques",
            "Reason For Mapping": "Obtaining work area access permits requires effective communication with relevant persons to ensure proper authorization and compliance with workplace procedures."
        },
        {
            "Performance Criterion": "(PC 1.2) Relevant workplace WHS/OHS safety regulations and codes of practices are identified and followed when entering the electrotechnology work area",
            "Mapped Knowledge Evidence": "(KE 2) electrotechnology work environment",
            "Reason For Mapping": "Identifying and following WHS/OHS regulations and codes of practice requires knowledge of the electrotechnology work environment, including safety signs, standards, risk documentation, hazards, and fire extinguishers."
        },
        {
            "Performance Criterion": "(PC 1.3) Safe work methods for controlling risks are obtained, read and applied prior to undertaking work activity in accordance with WHS/OHS workplace procedures ",
            "Mapped Knowledge Evidence": "(KE 2.8) workplace procedures used to control the risks associated with workplace hazards ",
            "Reason For Mapping": "Applying safe work methods for controlling risks requires an understanding of workplace procedures used to manage these risks."
        }
]
}
Make sure that we don’t generalise the knowledge evidence and map it with multiple performance criteria, we need to make sure that each and every knowledge evidence is mapped to only one performance criteria 
this here is just a small sample output i want, dont generate anything just yet, i will next give you PC and KE and you need to return just the JSON response in text format, nothing else.'''
#  messages=[
#    {"role": "system", "content": '''I am making a AI learner system, i get course details including performance criterias required for a student to qualify,
#knowledge evidences that contains the topics one needs to learn to clear the performance criterias.
#You have to add related knowledge evidences to the performance criterias i provide in json format. add a key named topics and add the related knowledge evidences to each criteria.
#Make sure that we don’t generalise the knowledge evidence and map it with multiple performance criteria, we need to make sure that each and every knowledge evidence is mapped to only one performance criteria 
#'''},
#    {"role": "user", "content": f"i am giving you the performance criterias, return me formatted json data after adding the topics for each criteria,{data['elements_and_performance_criteria']}, here are the knowledge evidences: {data['knowledge_evidence']}.........also, some evidences have the word 'including' in them....  remove the word 'including' from them.......also return the data not in a code block...i am using API and i want to use the data you sent me directly."}
#  ]


prompt4='''Great now divide the PC as per the example provided: 
1.1 Identify and assess organisational compliance against environmental legislation, regulations and standards
First what we do is identify the main keywords which are in this PC as listed
Organisational compliance
Environmental legislation
Regulations
Standards
Identification of organisational compliance 
Assessing organisational compliance 
Once the keywords are listed then we make the content heading that we want students to learn which in this case is as provided
Organisational compliance 
Importance/Role of organisational compliance
Types of organisational compliance 
Environmental legislation 
Importance of environmental legislation
Examples of environmental legislation
Regulations and standards 
Role of legislation and standards 
Types of legislation and standards applicable to organisation and environment 
Organisational compliance in relation with environmental legislation, regulations and standards
Ways to identify organisational compliance with environmental legislation
Ways to assess organisational compliance in relation with environmental legislation, regulations and standards
KE 1 - Compliance requirements for the work area with reference to legislation, regulations, codes of practice, and workplace procedures that relate to environmental and sustainability issues.
Compliance requirements as per legislation, regulations, codes of practice
Codes of practice
Environmental and sustainability issue
Compliance with environmental and sustainability
Make sure that the knowledge evidence is not kept separate it must be integrated and aligned with the performance criteria heading see the example provided: 
These are points of performance criteria: 
Organisational compliance 
Importance/Role of organisational compliance
Types of organisational compliance (KE1) – reason it is talking about the compliance types and our KE is also talking about compliance requirements
Environmental legislation (KE1) – as our knowledge evidence is also asking about environmental issues and legislation
Importance of environmental legislation
Examples of environmental legislation
Regulations and standards (KE 1) – as the knowledge evidence itself is based on compliance requirements as per regulations and standards
Role of legislation and standards 
Types of legislation and standards applicable to organisation and environment 
Organisational compliance in relation with environmental legislation, regulations and standards
Ways to identify organisational compliance with environmental legislation
Ways to assess organisational compliance in relation with environmental legislation, regulations and standards
Another example 
PC 1.2 Collect data on environmental efficiency in organisational systems and processes
Main keywords
Environmental efficiency 
Organisational systems and processes
Collect data 
Main heading that will be included in the guide: 
Environmental efficiency 
Role/importance of environmental efficiency 
Data collection 
Importance of data collection 
Data Collection Techniques and Tools
Organisational system and processes suitable for environmental efficiency
Types of organisational system and processes for analysing environmental efficiency
Ways to gather data on environmental efficiency
Analyse the data collected on environmental efficiency
Another example: 
1.2 Identify required information for diagnosis activity
This is the KE mapped to this PC 
methods to locate and interpret information required to diagnose and repair air conditioning and HVAC systems, including:
information provided by customers and supervisors
air conditioning and HVAC system manufacturer specifications
Australian automotive code of practice: control of refrigerant gases during manufacture, installation, servicing or de-commissioning of motor vehicle air conditioners
First what we do is identify the main keywords which are in this PC as listed
Diagnosis activity
Identify information 
Main heading that will be included in the guide and relevant KE that will be included with heading: 
Importance of locating information to perform diagnosis activity 
Ways to locate and interpret information (KE1) 
Obtain information provided by customers (KE 1.1)
Refer to manufacturer specifications about the air conditioning and HVAC system (KE1.2)
Refer to Australian code of conducts (KE 1.3)
What we have done here is we mapped the KE itself in the heading of the performance criteria as KE is covering more information about the PC, 
While mapping the KE with the PC headings, we make sure that we don’t copy exact KE in the heading, we need to rephrase it a bit. 
We also need to make sure that we don’t change the wording of elements and PC at all.  
Do you have any question on how to do division of the content? Please don’t generate anything yet, I will provide the PC that I want you to divide.
'''
