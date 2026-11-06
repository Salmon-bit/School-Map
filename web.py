"""The internet-files fetching module"""
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
    r = requests.get(
        f'https://raw.githubusercontent.com/Salmon-bit/School-Map/refs/heads/{branch}/assets/school_{school}_floor_{floor}.json'
    )

    if r.status_code != 200:
        print(
            'Error getting file via url: ' + \
            f'https://raw.githubusercontent.com/Salmon-bit/School-Map/refs/heads/{branch}/assets/school_{school}_floor_{floor}.json'
        )
        return

    with open(f'assets/school_{school}_floor_{floor}.json', 'w', encoding='UTF-8', newline='') as f:
        f.write(r.text)

# def get_database(branch: str = "work"):
#     """Fetching database from repo
    
#     :param branch: The repo branch function should get file
#     :type branch: str
#     """
#     r = requests.get(
#         f'https://github.com/Salmon-bit/School-Map/raw/refs/heads/{branch}/school_map.db'
#     )

#     if r.status_code != 200:
#         print(
#             'Error getting file via url: ' + \
#             f'https://github.com/Salmon-bit/School-Map/raw/refs/heads/{branch}/school_map.db'
#         )
#         return

#     with open('school_map.db', 'wb') as f:
#         f.write(r.content)


if __name__ == "__main__":
    get_school_floor("2070", 1)