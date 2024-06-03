import requests
import os
import zipfile


download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip"
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
]


def main(uris: list, direct: str) -> None:

    # Creating "Downloads" directory if it doesn't exist
    if not os.path.exists(os.path.expanduser(direct)):
        os.makedirs(os.path.expanduser(direct))

    # Iterating over URI's list for downloading zip files with some implementations
    for uri in uris:
        response = requests.get(uri, params={'downloadformat': 'zip'})
        try:
            response.raise_for_status()
        except Exception as e:
            print(f'Exception occuried: {e}')
            continue
        
        # Defining a filename using split method
        filename = uri.split('/')[-1]
        zip_path = os.path.join(os.path.expanduser(direct), filename)

        # Creating zip file and writing the content
        with open(zip_path, mode='wb') as file:
            file.write(response.content)

        # Creating csv file and unpacking zip file content there
        with zipfile.ZipFile(zip_path, mode='r') as zip_ref:
            zip_ref.extractall(os.path.expanduser(direct))

        # Removing zip file
        os.remove(zip_path)
        

if __name__ == "__main__":
    main(download_uris, direct='./downloads')
