import requests
import json
query = ''' 


 query {
  repository(owner: "mchelali", name: "Analyse-et-traitement-d-Image") {
    defaultBranchRef {
      target {
        ... on Commit {
            oid
            committedDate
            author{
              name
              email
            }
            message 
          
        }
      }
    }
    
    pullRequests(first :3) {
       edges {
        node {
          number
          title
          createdAt
          updatedAt
          author {
            login
          }
          reviews(first: 3){
            edges{
              node{
                author{
                login
                }
                body
              }
            }
          }
        }
      }
       
    }
    
   primaryLanguage { name } 
   
    collaborators(affiliation: ALL, first: 10) {
        
        edges {
          node {
            login
          }
        }
      }
      
  }
}

'''

headers = {'Authorization':  'Bearer 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', 'Accept': 'application/vnd.github.v3+json'}
url = 'https://api.github.com/graphql'
response = requests.post(url, json={'query': query}, headers= headers)


dataa = json.loads(response.text)
data = dataa['data']
print(f"the Data returned is: {data}")

#the commit informations
commit_oid = data['repository']['defaultBranchRef']['target']['oid']
commit_date = data['repository']['defaultBranchRef']['target']['committedDate']
commit_author_name = data['repository']['defaultBranchRef']['target']['author']['name']
commit_author_email = data['repository']['defaultBranchRef']['target']['author']['email']
commit_message = data['repository']['defaultBranchRef']['target']['message']



#language utilisé
language = data['repository']['primaryLanguage']['name']



print('the oid of the commit is:'+commit_oid+"\n")
print('the date of the commit is:'+commit_date+"\n")
print('the author of the commit is:'+commit_author_name +'and his email is'+commit_author_email+"\n")
print('the message in the commit is:'+commit_message+"\n")








# #pullrequests informations

# pullRequests_number = data['repository']['pullRequests']['edges']['node']['number']
# pullRequests_title = data['repository']['pullRequests']['edges']['node']['title']
# pullRequests_createdAt = data['repository']['pullRequests']['edges']['node']['createdAt']
# pullRequests_updatedAt = data['repository']['pullRequests']['edges']['node']['updatedAt']
# pullRequests_author = data['repository']['pullRequests']['edges']['node']['author']['login']

# #reviews of the pullrequest
# pullRequests_reviews_author = data['repository']['pullRequests']['edges']['node']['reviews']['edges']['node']['author']['login']
# pullRequests_reviews_body = data['repository']['pullRequests']['edges']['node']['reviews']['edges']['node']['body']

# #collaborators
# collaborators = data['repository']['collaborators']['edges']['node']['login']