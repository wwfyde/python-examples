import httpx


data = {
    "startTime": "2025-09-15",
    "endTime": "2025-09-21",
    "model": 1,
    "fdIdList": [13, 4, 3, 10, 5, 6, 7, 8, 9, 11],
}
# url = "https://www.adguider.com/sv1/calendar/getCalendarAjax"
url = "https://tophub.today/calendar/events"
data = {"start": "2025-09-01T00:00:00+08:00", "end": "2025-10-13T00:00:00+08:00"}

response = httpx.post(
    url,
    data=data,
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": (
            "Hm_lvt_3b1e939f6e789219d8629de8a519eab9=1757399084,1757400606; "
            "__eoi=ID=d76799a611d8b94f:T=1757474075:RT=1757474075:S=AA-AfjatmJxh5ljhcWQL9QiT0_pm; "
            "itc_center_user=e410nbjzyh9JwSsrgWzH3qvL6XQjL%2B1mhUxH5Y%2BCz7CiDlB%2BW6BikaqD"
        ),
    },
)
# print(response.json())
print(response.status_code)
print(response.text)
