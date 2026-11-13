"""The internet-files fetching module"""
import os
import requests


def get_school_floor(school: str, floor: int, branch: str = "main"):
    """Fetching database from repo
    
    :param school: The name of the school
    :type school: str
    :param floor: The number of floor
    :type floor: int
    :param branch: The repo branch function should get file
    :type branch: str
    """
    try:
        r = requests.get(
            f'https://raw.githubusercontent.com/Salmon-bit/School-Map/refs/heads/{branch}/assets/school_{school}_floor_{floor}.json',
            # pylint: disable=line-too-long
            timeout=10
        )
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        return

    if r.status_code != 200:
        print(
            'Error getting file via url: ' + \
            f'https://raw.githubusercontent.com/Salmon-bit/School-Map/refs/heads/{branch}/assets/school_{school}_floor_{floor}.json'
            # pylint: disable=line-too-long
        )
        return
    os.makedirs('assets', exist_ok=True)
    with open(f'assets/school_{school}_floor_{floor}.json', 'w', encoding='UTF-8', newline='') as f:
        f.write(r.text)


def get_available_schools(branch: str = "main"):
    """Fetching schools from repo

    :param branch: The repo branch function should get file
    :type branch: str"""
    try:
        r = requests.get(
            url=f'https://raw.githubusercontent.com/Salmon-bit/School-Map/refs/heads/{branch}/assets/schools.txt',
            # pylint: disable=line-too-long
            timeout=10
        )
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        return

    if r.status_code != 200:
        print('Error getting available schools')
        return
    os.makedirs('assets', exist_ok=True)
    with open('assets/schools.txt', 'w', encoding='UTF-8', newline='') as f:
        f.write(r.text)

def get_devs(branch: str = "main"):
    """Fetching devs from repo"""
    try:
        r = requests.get(
            url=f'https://raw.githubusercontent.com/Salmon-bit/School-Map/refs/heads/{branch}\
/assets/devs.txt',
            timeout=10
        )
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        return

    if r.status_code != 200:
        return

    os.makedirs('assets', exist_ok=True)
    with open('assets/devs.txt', 'w', encoding='UTF-8', newline='') as f:
        f.write(r.text)


if __name__ == "__main__":
    get_school_floor("2070", 1)
