import requests
from bs4 import BeautifulSoup
import json


def scrape_training_data(competency_id):
    url = f"https://training.gov.au/Training/Details/{competency_id}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve data for ID: {competency_id}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    releases = []
    release_history_table = soup.find('table', summary="Table listing the release history of this unit of competency")
    if release_history_table:
        rows = release_history_table.find_all('tr')
        for row in rows[1:]:
            cols = row.find_all('td')
            if len(cols) == 2:
                release_version = cols[0].get_text(strip=True)
                release_date = cols[1].get_text(strip=True)
                link_tag = cols[0].find('a')
                link = f"https://training.gov.au{link_tag['href']}" if link_tag else None
                releases.append({
                    "version": release_version,
                    "release_date": release_date,
                    "link": link
                })
    application_heading = soup.find('h2', string='Application')

    if application_heading:
        table = application_heading.find_next('table', class_='ait-table')
        if table:
            application_content = table.get_text(separator='\n', strip=True)  

    elements_and_criteria = []
    elements_section = soup.find('h2', string='Elements and Performance Criteria')
    if elements_section:
        table = elements_section.find_next('table', {'class': 'ait-table'})
        if table:
            rows = table.find_all('tr')
            current_element = None
            current_element_criteria = []

            for row in rows:
                cols = row.find_all('td')
                if len(cols) == 4:
                    element_no = cols[0].get_text(strip=True)
                    element_title = cols[1].get_text(strip=True)
                    criteria_no = cols[2].get_text(strip=True)
                    criteria_desc = cols[3].get_text(strip=True)

                    if element_no:
                        if current_element:
                            elements_and_criteria.append({
                                "element": current_element,
                                "criteria": current_element_criteria
                            })
                        current_element = {
                            "number": element_no,
                            "title": element_title
                        }
                        current_element_criteria = []

                    current_element_criteria.append({
                        "number": criteria_no,
                        "description": criteria_desc
                    })

            if current_element:
                elements_and_criteria.append({
                    "element": current_element,
                    "criteria": current_element_criteria
                })


    sections = {}
    target_sections = ["Knowledge Evidence", "Performance Evidence"]

    for section in target_sections:
        h2_tag = soup.find('h2', string=section)
        if h2_tag:
            table_tag = h2_tag.find_next('table', class_='ait-table')
            if table_tag:
                ul_tags = table_tag.find_all('ul')
                sections[section] = extract_nested_list_items(ul_tags)

    sections['Performance Evidence'] = update_ke(sections.get('Performance Evidence', []), "")
    sections['Knowledge Evidence'] = update_ke(sections.get('Knowledge Evidence', []), "")

    return {
        "competency_id": competency_id,
        "title": soup.find('h2').get_text(strip=True),
         
        "releases": releases,
        "elements_and_performance_criteria": elements_and_criteria,
        
        "performance_evidence": sections.get("Performance Evidence", []),
        "knowledge_evidence": sections.get("Knowledge Evidence", []),
        "application": application_content
    }


def extract_nested_list_items(ul_tags):
    items = []
    current_list = None

    for ul in ul_tags:
        list_class = ul.get('class', [None])[0]
        list_items = ul.find_all('li', recursive=False)
        if list_class == 'ait13':
            # Complete the previous main list item before starting a new one
            if current_list:
                items.append(current_list)
            current_list = {
                "evidence": None,
                "sublist": []
            }

            for li in list_items[:-1]:
                items.append({
                    "evidence": li.get_text(strip=True),
                    "sublist": []
                })
            current_list['evidence'] = list_items[-1].get_text(strip=True)

        elif list_class == 'ait14' and current_list:
            sublist_items = []

            for li in list_items:
                sublist_items.append({
                    "evidence": li.get_text(strip=True),
                    "sublist": []
                })
            current_list["sublist"].extend(sublist_items)

        elif list_class == 'ait31016' and current_list and current_list["sublist"]:
            if current_list["sublist"]:
                last_sublist_item = current_list["sublist"][-1]
                subsublist_items = []

                for li in list_items:
                    subsublist_items.append({
                        "evidence": li.get_text(strip=True)
                    })
                last_sublist_item["sublist"].extend(subsublist_items)
        print(current_list)

    if current_list:
        items.append(current_list)

    return items


def update_ke(ke, pre=""):
    n=len(ke)
    num=1
    ans=[]
    for i in ke:
        if i.get('sublist',0) and i['sublist']:
            i["sublist"] = update_ke(i["sublist"],pre + str(num) + ".")
        i['number'] = pre + str(num)
        num+=1
        ans.append(i)
    return ans

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    competency_id = input("Enter the competency ID: ")
    data = scrape_training_data(competency_id)

    if data:
        filename = f"{competency_id}_training_data.json"
        save_to_json(data, filename)
        print(f"Data saved to {filename}")

        
