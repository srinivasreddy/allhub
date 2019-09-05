### Design Notes.

I am documenting the use cases for `allhub` library, all the API functions return
either a dictionary or list of dictionaries. As usual lists can be accessed with index,
or iterated and the dictionaries can be accessed with dot notation like Object.property
or Object["property"].

I wanted `allhub` to give property access like Javascript does.


```
from allhub import User
user = User("srinivasreddy", "xxxxxxxxxxxxx", True, "Git@weqwe")
events = user.public_events()
for event in events:
    print(event.created_at)
```


```
from allhub import User, Response
user = User("srinivasreddy", "xxxxxxxxxxxxx", True, "Git@weqwe")
events = user.public_events()
new_events = user.public_events(**{"If-None-Match": user.response.etag})
new_events = user.public_events(**{"If-Modified-Since": user.response.last_modified})

```
