import requests
import json
query = ''' 
   query {
  repository(owner: "Gouranegithub", name: "Hedera_Consensus_Service") {
    owner {
      login
    }
    name
  }
}
'''

headers = {'Authorization':  'Bearer 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', 'Accept': 'application/vnd.github.v3+json'}
url = 'https://api.github.com/graphql'
response = requests.post(url, json={'query': query}, headers= headers)


dataa = json.loads(response.text)
data = dataa['data']

owner_name = data['repository']['owner']['login'] 
repo_name = data['repository']['name']
print(f"Owner: {dataa}")
#print(f"Repository: {repo_name}")


