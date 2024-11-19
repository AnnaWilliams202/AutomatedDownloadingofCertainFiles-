import requests

url = 'https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_station/'


def get_data(stations):
    with open('stations.txt', 'r') as f:
        stations_list = f.readlines()
        for station in stations_list:
            stations_list = station.strip()
    return stations_list

def get_filepath(station):
    filepath = f"{station}.csv.gz"
    return filepath

def construct_url(url, filepath):
    file_url = f"{url}{filepath}"
    print(file_url)
    return file_url


def download_file(fileurl, filepath):
    response = requests.get(fileurl)
    with open(filepath, 'wb') as file:
        file.write(response.content)


station_list = get_data('stations.txt')

for station in station_list:
    filepath = get_filepath(station)
    file_url = construct_url(url, filepath)
    download_file(file_url, filepath)

