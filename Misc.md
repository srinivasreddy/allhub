####  TODO
### Design Notes.

I am documenting the use cases for `allhub` library, all the API functions return
either a dictionary or list of dictionaries. As usual lists can be accessed with index,
or iterated and the dictionaries can be accessed with dot notation like Object.property
or Object["property"].

I wanted `allhub` to give property access like Javascript does.


```
from allhub import AllHub
allhub = AllHub("srinivasreddy", "xxxxxxxxxxxxx", password="xxxxxxxx")
events = allhub.public_events()
for event in events:
    print(event.created_at)
```


```
from allhub import AllHub, Response
allhub = AllHub("srinivasreddy", "xxxxxxxxxxxxx", password="xxxxxxxx")
events = allhub.public_events()
new_events = allhub.public_events(**{"If-None-Match": user.response.etag})
new_events = allhub.public_events(**{"If-Modified-Since": user.response.last_modified})

```

```
from allhub import AllHub, Response, Iterator
allhub = AllHub("srinivasreddy", "xxxxxxxxxxxxx", password="xxxxxxxx")
events = allhub.public_events()
for events in Iterator(allhub.public_events, user, page=1, per_page=100):
    print(event)
    
```
### Notes on development


1. I have skipped https://developer.github.com/v3/activity/events/types/ and is to be implemented yet.
