import requests
import pandas as pd
import re
import sys


def main(url: str) -> None:

    page_response = requests.get(url)
    page_response.raise_for_status()
    page_content = page_response.text

    # Finding the file which was updated in 2024-01-19 10:22, having size 7.4M and getting name of this file
    filename = re.search(r'".*\.csv"', 
                         re.findall(r'.*2024-01-19 10:22.*7\.4M.*', page_content)[0]
                         ).group().replace('"', '')

    # Compiling a URL to download the file
    file_url = f'{url}{filename}'

    file_response = requests.get(file_url)
    file_response.raise_for_status()

    # Writing file on disk
    with open(filename, mode='wb') as f:
        f.write(file_response.content)
    
    # Creating pandas dataframe with column data type transformation
    df = pd.read_csv(filename,
                     converters={'HourlyDryBulbTemperature':
                                 lambda x: float(x.strip('s')) if x.endswith('s') else float(x) if x != '' else 0}
                     )
    
    # Defining indexes of rows with max value by column
    rows_idx = df['HourlyDryBulbTemperature'].idxmax()
    sys.stdout.write(str(df.loc[rows_idx]))


if __name__ == "__main__":
    main(url='https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/')
