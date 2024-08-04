import requests
import random
import datetime

# Define the start and end dates
start_date = datetime.date(2024, 5, 27)
end_date = datetime.date(2024, 6, 1)

# Define the headers and payload template
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarysMYo7JAyPggd8Y6n',
    'Cookie': '_ga=GA1.1.1751846640.1713158117; _ga_PL1FR0T6DN=GS1.1.1717253011.16.1.1717253046.0.0.0; K2P=desktop; REMEMBERME=App.Entity.User%3AdGFuaXNocS5wYXRpZGFyQGthbHZpdW0uY29tbXVuaXR5%3A1717857933%3AuwL6DvgVcRtP3yiZP34BG6dmDEecEJAB00sOWxQ4RRQ~56wHhmaOD_DwK2K9BPRf9jb9gttjsRBGAcl13ABfOmc~; PHPSESSID=3rfi6feii5dsjahb2lpe7mk508',
    'Origin': 'https://worklog.kalvium.community',
    'Referer': 'https://worklog.kalvium.community/en_IN/calendar/',
    'Sec-Ch-Ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'X-Requested-With': 'Kimai-Modal, Kimai',
}

url = 'https://worklog.kalvium.community/en_IN/timesheet/create'

def random_time_within_range(start_hour=9, end_hour=18):
    start = datetime.datetime.strptime(f"{start_hour}:00", "%H:%M")
    end = datetime.datetime.strptime(f"{end_hour}:00", "%H:%M")
    random_start_time = start + datetime.timedelta(minutes=random.randint(0, (end - start).seconds // 60))
    random_end_time = random_start_time + datetime.timedelta(hours=6)
    return random_start_time.strftime("%I:%M %p"), random_end_time.strftime("%I:%M %p")

current_date = start_date
while current_date <= end_date:
    if current_date.weekday() < 5:  # Exclude Saturdays and Sundays
        begin_time, end_time = random_time_within_range()
        payload = {
            'timesheet_edit_form[begin_date]': current_date.strftime("%d/%m/%Y"),
            'timesheet_edit_form[begin_time]': '11:00',
            'timesheet_edit_form[duration]': '6',
            'timesheet_edit_form[end_time]': '17:00',
            'timesheet_edit_form[customer]': '13',
            'timesheet_edit_form[project]': '24',
            'timesheet_edit_form[activity]': '48',
            'timesheet_edit_form[description]': '',
            'timesheet_edit_form[_token]': 'd910cd10fea82937267832d94.-PWThWuVWJSXJUqLzuugJwAOE5IotQSitXvy8KcUS3Q.iYXL9yf_FcbIXSPoq5LSTW83XKcdh06agEKDv91nJU3IxeHCO8MOuch2LQ'
        }
        response = requests.post(url, headers=headers, data=payload)
        print(f"Posted entry for {current_date} from {begin_time} to {end_time}: Status {response.status_code}")
    current_date += datetime.timedelta(days=1)
