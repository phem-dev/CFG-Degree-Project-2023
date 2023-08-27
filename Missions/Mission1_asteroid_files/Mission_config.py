# for storing any config variables such as API keys, SQL creds etc. To use in other files, ues "from stratobus_challenges_config import [variable_name]"
import requests
from datetime import date

# for Asteroid challenge
today_date = date.today()
today_date_string = str(today_date)
api_key = "nFd7Ku7gaRTV7eeYliSeSsYFVOP4oN7U6J80KbFP"
short_url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today_date}&end_date={today_date}&api_key={api_key}"

# for satellite imagery challenge
sentinel_url = "https://services.sentinel-hub.com/api/v1/process"
headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer eyJraWQiOiJzaCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI0NTYwN2NmZC05NTA1LTRiNDItOTAzZC0xMTE5ZmE5YzU3MmMiLCJhdWQiOiIwZjYxZDM4NS01YzhiLTQ0ZjktYTE1NC0yYWRmNTFkNTAxNDEiLCJqdGkiOiIwN2QzZmI2My01OThkLTQ5MjQtODI3Zi1iYzY0NTg3ZWY3NGUiLCJleHAiOjE2OTI2NzA4MjUsIm5hbWUiOiJSZWEgQmFydGxldHQgVGFuZG9uIiwiZW1haWwiOiJyZWFidEBob3RtYWlsLmNvLnVrIiwiZ2l2ZW5fbmFtZSI6IlJlYSIsImZhbWlseV9uYW1lIjoiQmFydGxldHQgVGFuZG9uIiwic2lkIjoiZmJlNmRkOGUtNzZkYi00YmU3LWEyZDQtZjQxZmU5NzhjMDJlIiwiZGlkIjoxLCJhaWQiOiJiNmEzNGNiOS1jMjQxLTQ5NDAtODRhNC04ODYzZDI2OGI1MWUiLCJkIjp7IjEiOnsicmEiOnsicmFnIjoxfSwidCI6MTEwMDB9fX0.jsPyTvPsMo96Sn0IsnAm9OXxp1eLXwXcAdFZxX8oMmyd7zYvZybmDCdetyme1oubFtE_jwcTgNoGmzJ_eyZl-fiarRGcNkmLBN1Hp4TsURVhs1QXFXWVbKfJeoNfDXg6k_W920Hqmwsyj6aql11mUTOb2MtOso16Sg5zN9X6hx3IzvduyHI5fdJJMcwGjcHUMaDZBtejw1bbmuD_Bt4644iSYb33mSzBs91hbw3r7TQq9UwKxeAMLNT5zorHMsmQBSP1nefAMoF5jU2YGKG0Z6YGY7lUXL26HEWXNOXZv6E0AJZmBM2RWF4DEbNPug0vvrlgJlpFD_DKQ3hCXIk8Mg"
}



# request coordinates for different locations:
rejkyavic = {
  "input": {
    "bounds": {
      "bbox": [
        -22.43226,
        63.975785,
        -21.328762,
        64.227737
      ]
    },
    "data": [
      {
        "dataFilter": {
          "timeRange": {
            "from": "2023-07-21T00:00:00Z",
            "to": "2023-08-21T23:59:59Z"
          }
        },
        "type": "sentinel-2-l2a"
      }
    ]
  },
  "output": {
    "width": 512,
    "height": 266.443,
    "responses": [
      {
        "identifier": "default",
        "format": {
          "type": "image/jpeg"
        }
      }
    ]
  },
  "evalscript": "//VERSION=3\n\nfunction setup() {\n  return {\n    input: [\"B02\", \"B03\", \"B04\"],\n    output: { bands: 3 }\n  };\n}\n\nfunction evaluatePixel(sample) {\n  return [2.5 * sample.B04, 2.5 * sample.B03, 2.5 * sample.B02];\n}"
}

lima = {
  "input": {
    "bounds": {
      "bbox": [
        -77.375587,
        -12.299286,
        -76.712361,
        -11.904467
      ]
    },
    "data": [
      {
        "dataFilter": {
          "timeRange": {
            "from": "2023-07-15T00:00:00Z",
            "to": "2023-08-15T23:59:59Z"
          }
        },
        "type": "sentinel-2-l2a"
      }
    ]
  },
  "output": {
    "width": 512,
    "height": 311.493,
    "responses": [
      {
        "identifier": "default",
        "format": {
          "type": "image/jpeg"
        }
      }
    ]
  },
  "evalscript": "//VERSION=3\n\nfunction setup() {\n  return {\n    input: [\"B02\", \"B03\", \"B04\"],\n    output: { bands: 3 }\n  };\n}\n\nfunction evaluatePixel(sample) {\n  return [2.5 * sample.B04, 2.5 * sample.B03, 2.5 * sample.B02];\n}"
}

beijing = {
  "input": {
    "bounds": {
      "bbox": [
        115.798083,
        39.605997,
        117.146506,
        40.200229
      ]
    },
    "data": [
      {
        "dataFilter": {
          "timeRange": {
            "from": "2023-07-15T00:00:00Z",
            "to": "2023-08-15T23:59:59Z"
          }
        },
        "type": "sentinel-2-l2a"
      }
    ]
  },
  "output": {
    "width": 1139.463,
    "height": 651.766,
    "responses": [
      {
        "identifier": "default",
        "format": {
          "type": "image/jpeg"
        }
      }
    ]
  },
  "evalscript": "//VERSION=3\n\nfunction setup() {\n  return {\n    input: [\"B02\", \"B03\", \"B04\"],\n    output: { bands: 3 }\n  };\n}\n\nfunction evaluatePixel(sample) {\n  return [2.5 * sample.B04, 2.5 * sample.B03, 2.5 * sample.B02];\n}"
}


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
