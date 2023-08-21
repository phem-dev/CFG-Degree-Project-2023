# for storing any config variables such as API keys, SQL creds etc. To use in other files, ues "from stratobus_challenges_config import [variable_name]"
import requests
from datetime import date

# for Asteroid challenge
today_date = date.today()
today_date_string = str(today_date)
api_key = "nFd7Ku7gaRTV7eeYliSeSsYFVOP4oN7U6J80KbFP"
short_url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today_date}&end_date={today_date}&api_key={api_key}"


# for sentinel satellite imagery challenge
sentinel_url = "https://services.sentinel-hub.com/api/v1/process"
headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer eyJraWQiOiJzaCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI0NTYwN2NmZC05NTA1LTRiNDItOTAzZC0xMTE5ZmE5YzU3MmMiLCJhdWQiOiIwZjYxZDM4NS01YzhiLTQ0ZjktYTE1NC0yYWRmNTFkNTAxNDEiLCJqdGkiOiJhM2Q5Y2NhNy1iY2EzLTQ3NzctODU5Ny0yMTYwNzQ4ZjE3ZjYiLCJleHAiOjE2OTIxMjM4OTIsIm5hbWUiOiJSZWEgQmFydGxldHQgVGFuZG9uIiwiZW1haWwiOiJyZWFidEBob3RtYWlsLmNvLnVrIiwiZ2l2ZW5fbmFtZSI6IlJlYSIsImZhbWlseV9uYW1lIjoiQmFydGxldHQgVGFuZG9uIiwic2lkIjoiMDdmMTI2MmEtYjVkYS00YzZiLWE2NTAtODNjOWQ4MzA2NDc3IiwiZGlkIjoxLCJhaWQiOiJiNmEzNGNiOS1jMjQxLTQ5NDAtODRhNC04ODYzZDI2OGI1MWUiLCJkIjp7IjEiOnsicmEiOnsicmFnIjoxfSwidCI6MTEwMDB9fX0.uXzeEeiUzFL3s9Q6VxPxchQZbOnXEBbsXy4RH-CRNJmuJ4AFYbpnkVU2tdM6qHT2xgsKFraPNiV0W5wvuTCxryTql2PdJdKHACsWyd7NvPiZexi-Zr9ufXZFJ6cw29tf8gvlAbVndHcgUeH6dn3WATOFyscBu80mDbfGd3klRm5ybFqV-ckW1jGac8q-cKEwi5CgU0jmrlTfq_r5WFAjrEwEwLf85q0flFB7tJXFYGf-E4UXuSD-wLG5RdgWBTErMkKTtTh5MFBOLow3KOp26ekzakR3oTbldVrRnGQi5OuO4c0pYxevmtw702Ajnvv9xCHze5LPj_X5tCVgMXmXoA"
}

# request coordinates for different locations:
rejkyavic = {
  "input": {
    "bounds": {
      "bbox": [
        -22.1322,
        64.081428,
        -21.58981,
        64.228717
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
    "height": 318.094,
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