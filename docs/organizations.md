## Intro 
Exporting username, password and auth token as environment variables enables us to not to write 
them in the code and expose it to the outer world.

```bash
export GH_USERNAME="test-github42"
export GH_TOKEN="0499690952877243432fggga3db3a216eb01baba1f72"
export GH_PASSWORD="PWD@78656"
```
## All organizations

To retrieve all the organizations on the Github, please use this example.


```python
import os
from allhub import AllHub
client = AllHub(
    username = os.environ.get("GH_USERNAME"),
    auth_token = os.environ.get("GH_TOKEN"),
    password = os.environ.get("GH_PASSWORD")
)
organizations = client.all_organizations()  
```

Output will be in the form of,

```text
{'login': 'triveos',
  'id': 1928,
  'node_id': 'MDEyOk9yZ2FuaXphdGlvbjE5Mjg=',
  'url': 'https://api.github.com/orgs/triveos',
  'repos_url': 'https://api.github.com/orgs/triveos/repos',
  'events_url': 'https://api.github.com/orgs/triveos/events',
  'hooks_url': 'https://api.github.com/orgs/triveos/hooks',
  'issues_url': 'https://api.github.com/orgs/triveos/issues',
  'members_url': 'https://api.github.com/orgs/triveos/members{/member}',
  'public_members_url': 'https://api.github.com/orgs/triveos/public_members{/member}',
  'avatar_url': 'https://avatars2.githubusercontent.com/u/1928?v=4',
  'description': None},

  ....
  ....
  ....

 {'login': 'lincolnloop',
  'id': 1964,
  'node_id': 'MDEyOk9yZ2FuaXphdGlvbjE5NjQ=',
  'url': 'https://api.github.com/orgs/lincolnloop',
  'repos_url': 'https://api.github.com/orgs/lincolnloop/repos',
  'events_url': 'https://api.github.com/orgs/lincolnloop/events',
  'hooks_url': 'https://api.github.com/orgs/lincolnloop/hooks',
  'issues_url': 'https://api.github.com/orgs/lincolnloop/issues',
  'members_url': 'https://api.github.com/orgs/lincolnloop/members{/member}',
  'public_members_url': 'https://api.github.com/orgs/lincolnloop/public_members{/member}',
  'avatar_url': 'https://avatars1.githubusercontent.com/u/1964?v=4',
  'description': 'Makers of high performance web applications.'},
```
## Organizations that logged-in username belongs to

```python
import os
from allhub import AllHub
client = AllHub(
    username = os.environ.get("GH_USERNAME"),
    auth_token = os.environ.get("GH_TOKEN"),
    password = os.environ.get("GH_PASSWORD")
)
user_orgs = client.organizations()
```

## Organizations a username belongs to
```python
import os
from allhub import AllHub
client = AllHub(
    username = os.environ.get("GH_USERNAME"),
    auth_token = os.environ.get("GH_TOKEN"),
    password = os.environ.get("GH_PASSWORD")
)
user_orgs = client.user_organizations('srinivasreddy')
```

## Organization information
```python
import os
from allhub import AllHub
client = AllHub(
    username = os.environ.get("GH_USERNAME"),
    auth_token = os.environ.get("GH_TOKEN"),
    password = os.environ.get("GH_PASSWORD")
)
org = client.get_organization('google')
print(org)
```
outputs to, 
```text
{'login': 'google',
 'id': 1342004,
 'node_id': 'MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=',
 'url': 'https://api.github.com/orgs/google',
 'repos_url': 'https://api.github.com/orgs/google/repos',
 'events_url': 'https://api.github.com/orgs/google/events',
 'hooks_url': 'https://api.github.com/orgs/google/hooks',
 'issues_url': 'https://api.github.com/orgs/google/issues',
 'members_url': 'https://api.github.com/orgs/google/members{/member}',
 'public_members_url': 'https://api.github.com/orgs/google/public_members{/member}',
 'avatar_url': 'https://avatars1.githubusercontent.com/u/1342004?v=4',
 'description': 'Google ❤️ Open Source',
 'name': 'Google',
 'company': None,
 'blog': 'https://opensource.google/',
 'location': None,
 'email': 'opensource@google.com',
 'is_verified': True,
 'has_organization_projects': True,
 'has_repository_projects': True,
 'public_repos': 1689,
 'public_gists': 0,
 'followers': 0,
 'following': 0,
 'html_url': 'https://github.com/google',
 'created_at': '2012-01-18T01:30:18Z',
 'updated_at': '2019-12-19T21:09:14Z',
 'type': 'Organization'}
```
## Blocked Users

To list the blocked users in an organization your oauth token should have `org:admin` privileges, otherwise you receive 404
error.

```python
import os
from allhub import AllHub
client = AllHub(
    username = os.environ.get("GH_USERNAME"),
    auth_token = os.environ.get("GH_TOKEN"),
    password = os.environ.get("GH_PASSWORD")
)
users = client.blocked_users('google')
print(users)
```
```text
{'message': 'Not Found',
 'documentation_url': 'https://developer.github.com/v3/orgs/blocking/#list-blocked-users'}
```

```client.response.status_code``` gives 404.
