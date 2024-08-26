import os
import requests
from dotenv import load_dotenv

load_dotenv()


# scraping info from linkedin profile
def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = True):
    if mock:
        linkedin_profile_url = (
            "https://gist.githubusercontent.com/Marechka/0cd85ac8d4e8c700ee431e9e347c5642/raw/328f82d26700d6e1d02060c22ad25ac1bcd929d3/john-marty.json"
        )
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoit = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoit,
            params={"url":linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://linkedin.com/in/johnrmarty/"
        ),
    )
