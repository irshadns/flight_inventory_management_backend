# flight_inventory_management_backend
Technical Assessment from Sastaticket.pk for the job role of Junior Backend Developer.

**Assessment Task**

You are required a build a simple flight inventory management backend where users can come search flights on the platform. The backend will be created using Django Framework and will consist of 3 models
(User) , (Flight), and  (Airport). and a foreign key to Flight as departure_airport and arrival_airport (one to many).


***User model:***

The user model will be extended from the AbstractUser and we will be adding additional property to it (mobile_number)

***Flight Model will consist of following fields:***
- origin
- destination
- flight number
- departure date time
- arrival date time
- base fare
- tax

***Airport model will have following feilds:***
- iata code (string unique representation of airport)
- city (string city name)

We just need to add following airport data for the testing

```
{city: "Karachi", iata_code: "KHI"}
{city: "Islambad", iata_code: "ISB"}
{city: "Lahore", iata_code: "LHE"}
```

**Sample flight data (flights for coming week)**

KHI-LHE/LHE-KHI Day1(dates accordingly) tax is 1000 Rs base fare is 7000Rs
KHI-ISB/ISB-KHI Day2(dates accordingly) tax is 1500 Rs base fare is 9000Rs
We just need 2-3 days sample flight data (one flight each day)

***Django Admin Panel:*** 
* CRUD for Airport model
* CRUD for Flight model
* CRUD for User model

***The following endpoints are required in the Backend API:***
* User Signup
* User Login (JWT authentication class to be use)
* Flight Search (Public) - Flights with out prices are visible on this
* Flight Search with prices are available once user hit the same endpoint with login


***Objectives:***
* **Setup your codebase using Django Cookiecutter**
* Setup Git, make the initial commit
* Push to Github (create a public repo). For rest of the tasks, we will branch from master and work on a feature branch.
* Create feature branch, checkout.
* Configure user model and authentication. Commit. Bonus: Use semantic commits
* Configure flight model and its Public search API. Commit.
* Configure login authentication and modify search API to return prices for logged in users. Commit.
* Bonus: document all endpoints using Postman.


***Points to note:***
* Please ensure you make an initial git commit and then commit your work after each objective!
* Make sure you are using Pythonic code and best practices.



First please discuss all the requirements related to test and clear all queries/confusions first, Once you start you have 2/2.5 hours to complete this test.
