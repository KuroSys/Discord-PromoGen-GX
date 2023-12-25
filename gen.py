import requests
import json
import time

def make_web_request(url, headers, data):
    try:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:

            response_json = response.json()

            token_value = response_json.get("token", "")

            url_string = f"[+] https://discord.com/billing/partner-promotions/1180231712274387115/{token_value}"
            print(url_string)
            
            with open('promos.txt', 'a') as file:
                file.write(url_string + '\n')

        else:
            print(f"Error: {response.status_code} - {response.reason}")
            print("Response content:")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_url = 'https://api.discord.gx.games/v1/direct-fulfillment'

    request_headers = {
        'authority': 'api.discord.gx.games',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.opera.com',
        'referer': 'https://www.opera.com/',
        'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
    }

    request_data = {'partnerUserId': 'fbeea3c4969d6f3ba5a060c97f38830007394d06f37f704daeaa8e63b8c90734'}

while True:
    make_web_request(target_url, request_headers, request_data)