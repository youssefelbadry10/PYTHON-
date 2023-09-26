import requests
from bs4 import BeautifulSoup
import csv

date = input("Please enter a date in the following format MM/DD/YYYY: ")
#I want to get any info about this URL in any date
url = f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}"
page = requests.get(url)

def main(page):
    src = page.content
    # I want to translate this website with Html by using "lxml" parser
    soup = BeautifulSoup(src, "lxml")
    matches_details = []

# I want him to find all divs that have a matchCard as a class
    championships = soup.find_all("div", {'class': 'matchCard'})

    def get_match_info(championship):
        # i want him to find a text of a second header (h2)
        championship_title = championship.find('h2').text.strip()
        all_matches = championship.find_all('li')
        number_of_matches = len(all_matches)

        for i in range(number_of_matches):
            # Get teams names
            team_A = all_matches[i].find('div', {'class': 'teamA'}).text.strip()
            team_B = all_matches[i].find('div', {'class': 'teamB'}).text.strip()

            # Get score
            match_result = all_matches[i].find('div', {'class': 'MResult'}).find_all('span', {'class': 'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"

            # Get match time
            match_time = all_matches[i].find('div', {'class': 'MResult'}).find('span', {'class': 'time'}).text.strip()

            # Add match info to matches_details
            matches_details.append({"نوع البطولة": championship_title, "الفريق الأول": team_A,
                                    "الفريق الثاني": team_B, "ميعاد المباراة": match_time, "النتيجة": score})

    # Apply the function for all championships in the chosen day
    for championship in championships:
        get_match_info(championship)

    # Create a CSV file and insert the match details
    keys = matches_details[0].keys()

    with open('yallakora.csv', 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        print("File created.")

main(page)