<p align="left">
  <a href="https://limit-handling.herokuapp.com/doc">
    <img alt="badge: API documentation" src="https://img.shields.io/badge/API-documentation-brightgreen" />
  </a>
  <a href="https://limit-handling.herokuapp.com/">
    <img alt="badge: Service running in production" src="https://img.shields.io/badge/PROD-service-orange" />
  </a>
  <a href="https://kmattv1.github.io/LimitHandling/">
    <img alt="badge: Test coverage 91%" src="https://img.shields.io/badge/Test%20coverage-91%25-blue" />
  </a>
</p>

# Limit handling service based on subscription packages

## This project runs a microservice and a side container for the database
Every component is running on its own docker container.
Setup of the containers is managed in the docker compose file.

### Containers:
* Microservice writen in python

### Test coverage

```shell script
coverage run -m unittest discover
coverage report
covaerage html
coverage xml
```

### Example requests

```shell script
curl -X GET -H "user_name: testUser" https://limit-handling.herokuapp.com/

curl -X GET -H "user_name: testUser" https://limit-handling.herokuapp.com/api/apps

curl -X GET -H "user_name: testUser" https://limit-handling.herokuapp.com/api/app/limit/testApp

curl -X POST -H "Content-Type: application/json" -d '{"orgName": "exampleOrg", "planName": "pub"}' https://limit-handling.herokuapp.com/api/org

curl -X POST -H "Content-Type: application/json" -d '{"userName": "exampleUser", "email": "example@mail.com", "organizationName": "exampleOrg"}' https://limit-handling.herokuapp.com/api/user

curl -X POST -H "user_name: testUser" -H "Content-Type: application/json" -d '{"appName": "examplePublicApp", "isPublic": "true"}' https://limit-handling.herokuapp.com/api/apps

curl -X PUT -H "Content-Type: application/json" -H "user_name: testUser" -d '{"plan": {"PlanName": "Exceptional1", "AllowedConcurrentBuilds": "100", "BuildTimeLimitInMinutes": "1", "MaximumBuildsPerMonth": "2", "MaximumNumberOfTeamMembers": "20", "MaximumNumberOfApps": "1"}}' https://limit-handling.herokuapp.com/api/app/limit/examplePublicApp

curl -X PUT -H "Content-Type: application/json" -H "user_name: testUser" https://limit-handling.herokuapp.com/api/app/migrate/examplePublicApp
```
