# for storing any config variables such as API keys, SQL creds etc. To use in other files, ues "from stratobus_challenges_config import [variable_name]"
import requests
from datetime import date

# for Asteroid challenge
today_date = date.today()
today_date_string = str(today_date)
api_key = "nFd7Ku7gaRTV7eeYliSeSsYFVOP4oN7U6J80KbFP"
short_url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today_date}&end_date={today_date}&api_key={api_key}"

# for satellite imagery challenge
# url = "https://services.sentinel-hub.com/api/v1/process"
# headers = {
#   "Content-Type": "application/json",
#   "Authorization": "Bearer eyJraWQiOiJzaCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI0NTYwN2NmZC05NTA1LTRiNDItOTAzZC0xMTE5ZmE5YzU3MmMiLCJhdWQiOiIwZjYxZDM4NS01YzhiLTQ0ZjktYTE1NC0yYWRmNTFkNTAxNDEiLCJqdGkiOiIwOTJjZjQ1ZC1hZjExLTRhNTEtYmM5Mi02OTljYzBhYjkwYjEiLCJleHAiOjE2OTE3ODY0NTAsIm5hbWUiOiJSZWEgQmFydGxldHQgVGFuZG9uIiwiZW1haWwiOiJyZWFidEBob3RtYWlsLmNvLnVrIiwiZ2l2ZW5fbmFtZSI6IlJlYSIsImZhbWlseV9uYW1lIjoiQmFydGxldHQgVGFuZG9uIiwic2lkIjoiODBhYmI3NWEtNTI4OS00MGU2LWEyNjItYmEwMTZlNGEwMjRjIiwiZGlkIjoxLCJhaWQiOiJiNmEzNGNiOS1jMjQxLTQ5NDAtODRhNC04ODYzZDI2OGI1MWUiLCJkIjp7IjEiOnsicmEiOnsicmFnIjoxfSwidCI6MTEwMDB9fX0.SSuVIftDemGf3NOAHbxgxsgjQVHGnIcWRV7-eZDd5kxYOdIxhcBUILWGg6ctSRGurkFhHqxn41gMl4h7ncAKOOWbDQ14iziPyG4PZaj20Va_feM1lOhVC7KYTU1QkhMMq9Um3-_iiYH6TOKJVG3gbm9Zk-xS_E85Wby3iU0Vrc5oj9MEN2Sh7q1-QwTeZfvNiquR1iEHXyA7K_HdjQ6Wdou72w-TEMKhTgM3d1MDJahEZRNGqSgqJsJfOm86v6ejYRoL3rBasr6RTx-ztQ5GuR7-y5r4e39IEEfrwEdaKeZQNe5UqKKYH5l_Md8lHbofo4Z6JgFUXEf0Bldptixd_w"
# }
# data = {
#   "input": {
#     "bounds": {
#       "bbox": [
#         12.44693,
#         41.870072,
#         12.541001,
#         41.917096
#       ]
#     },
#     "data": [
#       {
#         "dataFilter": {
#           "timeRange": {
#             "from": "2023-07-11T00:00:00Z",
#             "to": "2023-08-11T23:59:59Z"
#           }
#         },
#         "type": "sentinel-2-l2a"
#       }
#     ]
#   },
#   "output": {
#     "width": 512,
#     "height": 343.697,
#     "responses": [
#       {
#         "identifier": "default",
#         "format": {
#           "type": "image/png"
#         }
#       }
#     ]
#   },
#   "evalscript": "//VERSION=3\n\nfunction setup() {\n  return {\n    input: [\"B02\", \"B03\", \"B04\"],\n    output: { bands: 3 }\n  };\n}\n\nfunction evaluatePixel(sample) {\n  return [2.5 * sample.B04, 2.5 * sample.B03, 2.5 * sample.B02];\n}"
# }
#
# response = requests.post(url, headers=headers, json=data)
