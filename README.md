### Introduction

Python port of the TruckingSim.com API. Made in about one hour on February 17, 2013.


### Getting Started

First, import the API into your Python file:
   ```python
   import TruckingSimAPI
   ```
Then, instantiate the API with your API key (you can get that from [here](http://truckingsim.com/api)):
   ```python
   api = TruckingSimAPI("xxxxxx")
   ```
Now you can use the API.

### Searching for Data

You can use the `search()` function to conduct searches on the database. The search function is structured like so:
   ```python
   api.search(type, query)
   ```
Type can be `users`, `routes` or `companies`. Query is a string that can contain a wildcard (*). For `users` and `routes`, query is a username, for companies, it is the name of a company.

> ###A note on wildcards
> A wildcard is used to denote an undefined value. You can use it to carry out broader searches.
> Wildcards can be used before words, like `*con`, or after, like `con*`.
> You can even use them inside words, like `c*n`.

##Working with Company Data

The `fetchCompany()` function can be used to get information about a company, such as its finances or contracts. The function is structured like so:
   ```python
   api.fetchCompany(type, company)
   ```
Type can be one of the following values: `users`, `ads`, `finances`, `contracts`, `routes` or `terminals`. Company must be a full valid company name, no wildcards are allowed.

### Miscellaneous Data

The TruckingSim API provides access to all city, contract, and cargo. This data can be accessed with the `fetchInfo()` function.
   ```python
   api.fetchInfo(type)
   ```
Type can be `contracts`, `cargo`, or `cities`.

### Calculating Distances

There is one extra function, `fetchDistance()`.
  ```python
  api.fetchDistance(from, to)
  ```
`From` and `to` are the name of cities. Wildcards are allowed (*).

### Handling Data

All functions return a string encoded in JSON which you can then manipulate.

### License
```
MIT License

Copyright (c) 2016 Andi Andreas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
