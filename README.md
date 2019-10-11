### About allhub

`allhub` is a REST API library for Github REST API v3 written in python. Currently, this library is under heavy
development.  Maybe i will cut a release once i am confident that major part of the library covered with tests.


### Features

1. `allhub` is heavily inspired by Javascript, meaning that you can access the properties on JSON
object either object.prop or object["prop"]. I feel the later version is kind of verbose, and I recommend
you use the object.prop.

2. I have seen most of the Github libraries are not covered comprehensively. But this library aims to covers 
all of REST API v3.

3. I have designed this library keeping programmer ergonomics in mind, so that you create only one object
 to access any of the API.


### Examples
```python
from allhub import AllHub
allhub = AllHub(
"username",
"tokenxxxxxxxxxxxxxxx",
"app_tokenxxxxxxxxxxxxxx",
"password"
)
response = allhub.xxxxxxxxx()
```
