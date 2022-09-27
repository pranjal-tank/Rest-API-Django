## SETUP

1. Clone the Repository https://github.com/pranjal-tank/twassignment.git.
2. Install [Docker](https://docs.docker.com/engine/install/) on your system.
3. Redirect to the clone repository on your local machine and run the **Dockerfile** which is in the clone repository to create project image by executing the following command in the terminal:
```
docker build . -t [image name that you want to give]
```

*Eg. docker build . -t api-container*

4. Now with the help of the docker image create and run the docker container by executing the following command:
```
docker run -d -p 8000:8000 [image name]
```

*Eg. docker run -d -p 8000:8000 api-container*

5. Now in your **docker container shell** execute the following command to create table in your database with the help of model schemas in **models.py** file in **api** django application:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
6. now create superuser by executing the following command in your docker container shell:
```
python manage.py createsuperuser
```

## Testing API's

**NOTE: The API's can only be access by the superuser**

To test the API's you can use any fronend application or 3rd party apps or library but here I am using [HTTPie](https://httpie.io/).

- To Install **HTTPie** run the following command in your local machine terminal (make sure **pip** is installed in your local machine):
```
pip install httpie
```

Now to Access the API's the superuser need a access token as all the API's are using JWT Authentication.

- To generate access token using HTTPie run the following command in the terminal:

**I am assuming that the server is running on localhost:8000**
```
http POST http://localhost:8000/gettoken username=[superuser name] password=[superuser password]
```

You will get two token as a JSON response:
1. Access Token (lifetime: 60 minutes)
2. Refresh Token (lifetime: 1 day)

*Eg.*

*Request:*

![get token](https://user-images.githubusercontent.com/78424052/192544714-b7204f8a-68ab-46a1-8996-2e921e770b3b.png)

*Response:*

![get token response](https://user-images.githubusercontent.com/78424052/192544766-a2771174-9679-40f8-a925-4af40eefe332.png)

The refresh Token is use to generate new access token if the old token got expired.

- To generate new token from refresh token run the following command in terminal:
```
http POST http://localhost:8000/refreshtoken refresh=[refresh token]
```

This will return a JSON response with a new assess token.

*Eg.*

*Request:*

![refresh token](https://user-images.githubusercontent.com/78424052/192545802-743900e5-a962-46ef-a3b7-ac7c5d4f64b5.png)

*Response:*

![refresh token response](https://user-images.githubusercontent.com/78424052/192545854-bad2541b-7916-4054-968b-e11d0bd49fa6.png)

- To verify if the access token is expired or not run the following command in your terminal:
```
http POST http://localhost:8000/verifytoken token=[access token]
```

This will return a JSON response about the access token.

*Eg.*

*Request:*

![verify token](https://user-images.githubusercontent.com/78424052/192546550-97d84de3-e8c8-4982-853d-93a27193d233.png)

*Response:*

*If the access token is not expired then it will return a empty JSON response*

![verify token response 1](https://user-images.githubusercontent.com/78424052/192546727-6575b4c7-2a0b-4a85-82f5-108959d790d2.png)

*If the access token is expired then it will return a JSON response that Token is Invalid or Expired*

![verify token response 2](https://user-images.githubusercontent.com/78424052/192548457-4c5e8096-dd6e-4ca8-bfd5-aef445104e36.png)


**Now as we have the access token lets test our API's.**

#### API: Create a Company

To test this API using HTTPie run the following command in the terminal:
```
http -f POST http://localhost:8000/createcompany company_name=[company name] company_ceo=[company CEO] company_address=[company address] inception_date=[inception date in YYYY-MM-DD formate] 'Authorization:Bearer [access token]'
```
This will return a JSON message **Company created**.

*Eg.*

*Request:*

![create company](https://user-images.githubusercontent.com/78424052/192549824-b7daa56d-c4db-4ffa-bc50-9303e4c117cf.png)


*Response:*

![create company response](https://user-images.githubusercontent.com/78424052/192549867-ee4ba4f3-891b-492a-b3e8-92a2b0ab83e6.png)

#### API: Create a Team

To test this API using HTTPie run the following command in the terminal:
```
http POST http://localhost:8000/createteam/[Company id] team_leader=[team leader] 'Authorization:Bearer [access token]'
```

This will return a JSON message **Team created**.

*Eg.*

*Request:*

![create team](https://user-images.githubusercontent.com/78424052/192550468-fe18e3cd-56bb-4d7c-8ea1-557ab01040ef.png)

*Response:*

![create team response](https://user-images.githubusercontent.com/78424052/192550582-4c1fe974-897b-45ab-b6cf-a504bcf38cad.png)

#### API: Get Company object from ID

To test this API using HTTPie run the following command in the terminal:
```
http  GET http://localhost:8000/getcompany/[Company ID] 'Authorization:Bearer [access token]'
```

This will return a JSON response with all the details of the company requested.

*Eg.*

*Request:*

![get company](https://user-images.githubusercontent.com/78424052/192551362-8b7b9d0e-c53d-46ea-9dbe-892a8c1cb80d.png)


*Response:*

![get company response](https://user-images.githubusercontent.com/78424052/192551401-33e8a959-e0b7-4e3b-81fb-a7d59968a398.png)

#### API: Search company by name

To test this API using HTTPie run the following command in the terminal:
```
http  GET http://localhost:8000/searchcompany/[Company name] 'Authorization:Bearer [access token]'
```

This will return a JSON response with all the details of the company searched.

*Eg.*

*Request:*

![search company](https://user-images.githubusercontent.com/78424052/192551963-46248250-f766-4c17-9f30-533e434272ca.png)



*Response:*

![search company response](https://user-images.githubusercontent.com/78424052/192552008-195ba9b9-0f67-4fba-9b01-fe5af44c4d04.png)

#### API: Get All teams

To test this API using HTTPie run the following command in the terminal:
```
http  GET http://localhost:8000/allteam/[Company ID] 'Authorization:Bearer [access token]'
```

This will return a JSON response with all the teams of a company grouped within company object.

*Eg.*

*Request:*

![all team](https://user-images.githubusercontent.com/78424052/192552550-aad9ab24-6a7b-4b61-8874-ec9c1477b926.png)


*Response:*

![all team response](https://user-images.githubusercontent.com/78424052/192552583-d0742b23-50da-40dd-9cdf-d14b0355c454.png)


*Thank you*





