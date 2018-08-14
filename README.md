# AioRESTTrial
A simple API REST test field with aiohttp library, for research purposes 

## Version 0.1

Resources:
- "/" = API Index. Returns all available resource URIs
    - Headers:
        * User
        * Pass
    - Response: JSON with the following:
        * status: int -> Status code from the response
        * resources: Object -> Object with URIs and a descriptive name for everyone of them
- "/user" = User Login. Pretends to create a new user into the system (real user creation incoming in next versions)
    - Headers:
        * User
        * Pass
    - Body: JSON with the following
        * name: string -> User's account
        * pwd: string -> User's account password
    - Response: JSON with the following:
        * status: int -> Status code from the response 

Access:

For now, all requests need to include two headers with the right values in order to grant access. These are
the following:

- User: Dewitt
- Pass: 12345

Pretty simple, eh? We'll work on a better authentication system in next versions
