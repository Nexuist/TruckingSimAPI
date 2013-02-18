TruckingSimAPI
==============

Python port of the TruckingSim.com API. Made in about one hour on February 17, 2013.


##Getting Started

First, import the API into your Python file:
   ```python
   import TruckingSimAPI
   ```
Then, instantiate the API with your API key (you can get that from [here](http://truckingsim.com/api)):
   ```python
   api = TruckingSimAPI("xxxxxx")
   ```
Now you can use the API.

##Searching for Data

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

##Miscellaneous data

The TruckingSim API provides access to all city, contract, and cargo. This data can be accessed with the `fetchInfo()` function. `fetchInfo()` accepts one argument: type. Type can be `contracts`, `cargo`, or `cities`.

##Calculating Distances

The TruckingSim API has one extra function, `fetchDistance()`. `fetchDistance()` accepts two parameters: `from` and `to`. These parameters can contain wildcards (*).

##Handling Data

All functions return a string encoded in JSON which you can then manipulate to get the information you want.
