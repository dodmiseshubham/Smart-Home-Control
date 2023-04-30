def getCurrentWeather(location):
    print("get weather func...")
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":location}

    headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": "ff95de7d70msh2a84c89cc0f71ffp132c5djsn1c6b82a457c0",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    # print(response.json())
    return response.json()