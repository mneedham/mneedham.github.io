import json
import requests
from datetime import datetime

def get_package_releases(package_name, start_version=None):
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)
    data = response.json()
    releases = data['releases']
    version_dates = {}
    for version, release_info in releases.items():
        if release_info:
            upload_time = release_info[0]['upload_time']
            upload_datetime = datetime.strptime(upload_time, "%Y-%m-%dT%H:%M:%S")
            version_dates[version] = upload_datetime
    sorted_releases = sorted(version_dates.items(), key=lambda x: (date:=x[1]), reverse=False)
    if start_version:
        search_date = next((date for version, date in sorted_releases if version == start_version), None)
    if search_date:
        print(search_date)
        sorted_releases = [release for release in sorted_releases if release[1] >= search_date]
    else:
        print(f"Version {start_version} not found. Ignoring version.")
    return sorted_releases

# Example usage
package_name = 'langchain'
releases = get_package_releases(package_name, "0.0.142")

for version, upload_time in releases:
    print(f"Version: {version}, Upload Time: {upload_time}")
