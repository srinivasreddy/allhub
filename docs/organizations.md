## Intro 
Exporting username, password and auth token as environment variables enables us to not to write 
them in code and expose it to outer world.

```bash
export GH_USERNAME="test-github42"
export GH_TOKEN="0499690952877243432fggga3db3a216eb01baba1f72"
export GH_PASSWORD="PWD@78656"
```
## All organizations.

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
## Organizations logged-in username belongs to...

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

## Organizations a username belongs to...
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
