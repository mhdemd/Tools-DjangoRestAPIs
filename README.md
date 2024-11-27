# Django APIs Collection

This project is a collection of various APIs for Django projects, including functionalities such as authentication, product management for e-commerce, token management, and more. It is designed to provide developers with ready-to-use API implementations for common Django tasks, all powered by Django Rest Framework (DRF).

## Project Structure

The project consists of several sub-projects, each dedicated to a specific area of functionality. Each sub-project contains a set of APIs implemented using Django Rest Framework.

### Directory Structure:
```plaintext
.
├── 01-Auth
│   ├── 01-token_based_auth
│   ├── 02-API throttling for class-based views
│   ├── 03-Djoser library
│   └── 04-JWT(JSON Web Token)
├── 02-Shop API
│   ├── 01-Simple API
│   ├── 02-Simple DRF
│   ├── 03-ViewSet
│   ├── 04-ModelViewSet (ReadOnlyModelViewSet)
│   ├── 05-Generic views
│   ├── 06-Serialization
│   ├── 07-Deserialization
│   ├── 08-FilteringSearchingOrdering
│   ├── 09-Validation
│   ├── 10-DataSanitization
│   ├── 11-Pagination
    └── 12-ClassBasePaginationFiltering


```



## Requirements

- Python 3.x
- Django 3.x or later
- Django Rest Framework (DRF)
- (Add any other dependencies your project requires)

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/mhdemd/Tools-APIs.git
```

### 2. Navigate to the project directory
```bash
cd path/to/your/application
```

### 3.Create and activate a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Apply migrations
```bash
python manage.py migrate
```

### 6. Run the development server
```bash
python manage.py runserver
```

## Usage
### Available API Endpoints
Once the server is running, you can access the APIs at the following endpoints (example):

- `POST /api/auth/token/` - Obtain a token for authentication
- `GET /api/products/` - List all products
- `POST /api/orders/` - Create a new order

### Authentication (example)
The APIs support multiple authentication methods, including:

- **Token-based authentication**: This method involves generating a token upon successful login and using that token for subsequent requests to access protected resources.
- **Session-based authentication**: This method maintains a user session on the server, allowing authenticated users to make requests as long as the session is active.
- **JWT-based authentication**: JSON Web Tokens (JWT) are used to securely transmit user authentication data, which can be verified without needing to store session data on the server.

For more details on how each authentication method is implemented and examples of their usage, refer to the table below.

**Note**: Further information on additional APIs and their functionalities is provided in the table below.


<table>
    <tr>
        <th colspan="8">API's list</th>
    </tr>
    <tr>
        <td>No</td>
        <td>Folder</td>
        <td>Sub Folder</td>
        <td>URLs</td>
        <td>Method</td>
        <td>Form Data</td>
        <td>Auth Type</td>
        <td>Function</td>
    </tr>
    <tr>
        <td>1</td>
        <td>01-Auth</td>
        <td>01-token_based_auth</td>
        <td>/api/secret/</td>
        <td>GET</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Access to specific view with token</td>
    </tr>
    <tr>
        <td>2</td>
        <td>01-Auth</td>
        <td>01-token_based_auth</td>
        <td>/api/api-token-auth/</td>
        <td>POST</td>
        <td>username - password</td>
        <td>-</td>
        <td>Get token for the specified user</td>
    </tr>
    <tr>
        <td>3</td>
        <td>01-Auth</td>
        <td>01-token_based_auth</td>
        <td>/api/manager-view/</td>
        <td>GET</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Access to manager group view</td>
    </tr>
    <tr>
        <td>4</td>
        <td>01-Auth</td>
        <td>01-token_based_auth</td>
        <td>/api/throttle-check/</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>Limit the number of anonymous requests</td>
    </tr>
    <tr>
        <td>5</td>
        <td>01-Auth</td>
        <td>01-token_based_auth</td>
        <td>/api/throttle-check-auth/</td>
        <td>GET</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Limit the number of authenticated requests</td>
    </tr>
    <tr>
        <td>6</td>
        <td>01-Auth</td>
        <td>02-API throttling for class-based views</td>
        <td>/api/register/</td>
        <td>GET</td>
        <td>username - password</td>
        <td>-</td>
        <td>Limit the number of authenticated requests for class-based views</td>
    </tr>
    <tr>
        <td>7.1</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/users/</td>
        <td>POST</td>
        <td>email - password - re_password</td>
        <td>-</td>
        <td>Register new user</td>
    </tr>
    <tr>
        <td>7.2</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/users/</td>
        <td>GET</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Get complete details of user(s)</td>
    </tr>
    <tr>
        <td>8</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/token/login/</td>
        <td>POST</td>
        <td>email - password</td>
        <td>-</td>
        <td>Create user token</td>
    </tr>
    <tr>
        <td>9</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/token/logout/</td>
        <td>POST</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Destroy user token</td>
    </tr>
    <tr>
        <td>10</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/users/me/</td>
        <td>GET</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Get complete details of the user</td>
    </tr>
    <tr>
        <td>11</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/users/me/</td>
        <td>PATCH</td>
        <td>Fields to be modified</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Update some user details</td>
    </tr>
    <tr>
        <td>12</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/users/me/</td>
        <td>PUT</td>
        <td>All fields must be provided with new values</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Update all user details</td>
    </tr>
    <tr>
        <td>13</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/users/me/</td>
        <td>DELETE</td>
        <td>current_password</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Delete user</td>
    </tr>
    <tr>
        <td>14</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/users/set_email/</td>
        <td>POST</td>
        <td>new_email - current_password</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Change user email</td>
    </tr>
    <tr>
        <td>15</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/users/set_password/</td>
        <td>POST</td>
        <td>new_password - re_new_password - current_password</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Directly change the user's password</td>
    </tr>
    <tr>
        <td>16</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/users/reset_password/</td>
        <td>POST</td>
        <td>email</td>
        <td>-</td>
        <td>Send password reset email</td>
    </tr>
    <tr>
        <td>17</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/users/reset_password_confirm/</td>
        <td>POST</td>
        <td>uid - token - new_password - re_new_password</td>
        <td>-</td>
        <td>Confirm password reset via email</td>
    </tr>
    <tr>
        <td>18</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/users/activation/</td>
        <td>POST</td>
        <td>uid - token</td>
        <td>-</td>
        <td>Activate user account</td>
    </tr>
    <tr>
        <td>19</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/users/resend_activation/</td>
        <td>POST</td>
        <td>email</td>
        <td>-</td>
        <td>Resend activation link to email</td>
    </tr>
    <tr>
        <td>20</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/api/groups/manager/users/</td>
        <td>POST, DELETE</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Add user to group</td>
    </tr>
    <tr>
        <td>21</td>
        <td>01-Auth</td>
        <td>04-JWT(JSON Web Token)</td>
        <td>/api/token/</td>
        <td>POST</td>
        <td>email - password</td>
        <td>-</td>
        <td>Get access and refresh tokens</td>
    </tr>
    <tr>
        <td>22</td>
        <td>01-Auth</td>
        <td>04-JWT(JSON Web Token)</td>
        <td>/api/secret</td>
        <td>GET</td>
        <td>-</td>
        <td>Bearer Token(Token=token)</td>
        <td>Test access token</td>
    </tr>
    <tr>
        <td>23</td>
        <td>01-Auth</td>
        <td>04-JWT(JSON Web Token)</td>
        <td>/api/token/refresh/</td>
        <td>POST</td>
        <td>refresh</td>
        <td>-</td>
        <td>Renew access token</td>
    </tr>
    <tr>
        <td>24</td>
        <td>01-Auth</td>
        <td>04-JWT(JSON Web Token)</td>
        <td>/api/token/blacklist/</td>
        <td>POST</td>
        <td>refresh</td>
        <td>-</td>
        <td>Add refresh token to blacklist</td>
    </tr>
    <tr>
        <td>25</td>
        <td>02-Shop</td>
        <td>01-Simple API</td>
        <td>/api/products/</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>Get all products</td>
    </tr>
    <tr>
        <td>26</td>
        <td>02-Shop</td>
        <td>02-Simple DRF</td>
        <td>/api/products/  ---  /api/products/{pk}</td>
        <td>GET, POST, PUT, PATCH, DELETE</td>
        <td>-</td>
        <td>-</td>
        <td>Get all products using different routes</td>
    </tr>
    <tr>
        <td>27</td>
        <td>02-Shop</td>
        <td>03-ViewSet</td>
        <td>/api/products/  ---  /api/products/{pk}</td>
        <td>GET, POST, PUT, PATCH, DELETE</td>
        <td>-</td>
        <td>-</td>
        <td>Use ViewSet in view</td>
    </tr>
    <tr>
        <td>28</td>
        <td>02-Shop</td>
        <td>04-(ModelViewSet) (ReadOnlyModelViewSet)</td>
        <td>/api/products/  ---  /api/products/{pk}</td>
        <td>GET, POST, PUT, PATCH, DELETE</td>
        <td>-</td>
        <td>-</td>
        <td>Use ModelViewSet in view</td>
    </tr>
    <tr>
        <td>29</td>
        <td>02-Shop</td>
        <td>04-(ModelViewSet) (ReadOnlyModelViewSet)</td>
        <td>/api/products/  ---  /api/products/{pk}</td>
        <td>GET(list-retrieve)</td>
        <td>-</td>
        <td>-</td>
        <td>Use ReadOnlyModelViewSet in view</td>
    </tr>
    <tr>
        <td>30</td>
        <td>02-Shop</td>
        <td>05-Generic views</td>
        <td>/api/products/</td>
        <td>GET, POST</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>31</td>
        <td>02-Shop</td>
        <td>05-Generic views</td>
        <td>/api/products/<int:pk>/</td>
        <td>GET, PUT, PATCH, DELETE</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>32</td>
        <td>02-Shop</td>
        <td>05-Generic views</td>
        <td>/api/products/create/</td>
        <td>POST</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>33</td>
        <td>02-Shop</td>
        <td>05-Generic views</td>
        <td>/api/products/<int:pk>/retrieve/</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>34</td>
        <td>02-Shop</td>
        <td>05-Generic views</td>
        <td>/api/products/<int:pk>/destroy/</td>
        <td>DELETE</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>35</td>
        <td>02-Shop</td>
        <td>05-Generic views</td>
        <td>/api/products/<int:pk>/update/</td>
        <td>PUT, PATCH</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>36</td>
        <td>02-Shop</td>
        <td>05-Generic views</td>
        <td>/api/products/<int:pk>/retrieve-update/</td>
        <td>GET, PUT, PATCH</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>37</td>
        <td>02-Shop</td>
        <td>05-Generic views</td>
        <td>/api/products/<int:pk>/retrieve-destroy/</td>
        <td>GET, DELETE</td>
        <td>-</td>
        <td>-</td>
        <td>with optional authentication</td>
    </tr>
    <tr>
        <td>38</td>
        <td>02-Shop</td>
        <td>06-Serialization</td>
        <td>/api/products/</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>Retrieve products with serializer</td>
    </tr>
    <tr>
        <td>39</td>
        <td>02-Shop</td>
        <td>06-Serialization</td>
        <td>/api/products/<int:id></td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>Retrieve a product with serializer</td>
    </tr>
    <tr>
        <td>40</td>
        <td>02-Shop</td>
        <td>06-Serialization</td>
        <td>/api/products/</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>Retrieve products with related serializer</td>
    </tr>
    <tr>
        <td>41</td>
        <td>02-Shop</td>
        <td>06-Serialization</td>
        <td>/api/products/</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>Retrieve products with related serializer</td>
    </tr>
    <tr>
        <td>42</td>
        <td>02-Shop</td>
        <td>06-Serialization</td>
        <td>/api/products/</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>Retrieve products with serializer linked to category</td>
    </tr>
    <tr>
        <td>43</td>
        <td>02-Shop</td>
        <td>07-Deserializer</td>
        <td>/api/products/</td>
        <td>POST</td>
        <td>-</td>
        <td>-</td>
        <td>Deserialize with post</td>
    </tr>
    <tr>
        <td>44</td>
        <td>02-Shop</td>
        <td>08-Filtering&Searching&ordering</td>
        <td>/api/products/?category=shows&to_price=25</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>Filter by category and lower price limit</td>
    </tr>
    <tr>
        <td>45</td>
        <td>02-Shop</td>
        <td>08-Filtering&Searching&ordering</td>
        <td>/api/products/?search=t-shirt</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>Search by product name</td>
    </tr>
    <tr>
        <td>46</td>
        <td>02-Shop</td>
        <td>08-Filtering & Searching & ordering</td>
        <td>/api/products/?ordering=price,inventory,…</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>Ordering products</td>
    </tr>
    <tr>
        <td>47</td>
        <td>02-Shop</td>
        <td>09-Validation</td>
        <td>/api/products/</td>
        <td>POST</td>
        <td>-</td>
        <td>-</td>
        <td>First method for validation</td>
    </tr>
    <tr>
        <td>48</td>
        <td>02-Shop</td>
        <td>09-Validation</td>
        <td>/api/products/</td>
        <td>POST</td>
        <td>-</td>
        <td>-</td>
        <td>Second method for validation</td>
    </tr>
    <tr>
        <td>49</td>
        <td>02-Shop</td>
        <td>09-Validation</td>
        <td>/api/products/</td>
        <td>POST</td>
        <td>-</td>
        <td>-</td>
        <td>Third method for validation</td>
    </tr>
    <tr>
        <td>50</td>
        <td>02-Shop</td>
        <td>09-Validation</td>
        <td>/api/products/</td>
        <td>POST</td>
        <td>-</td>
        <td>-</td>
        <td>Fourth method for validation</td>
    </tr>
    <tr>
        <td>51</td>
        <td>02-Shop</td>
        <td>09-Validation</td>
        <td>/api/products/</td>
        <td>POST</td>
        <td>-</td>
        <td>-</td>
        <td>Validation for uniqueness</td>
    </tr>
    <tr>
        <td>52</td>
        <td>02-Shop</td>
        <td>09-Validation</td>
        <td>/api/products/</td>
        <td>POST</td>
        <td>-</td>
        <td>-</td>
        <td>Validation for uniqueness of multiple fields</td>
    </tr>
    <tr>
        <td>53</td>
        <td>02-Shop</td>
        <td>10-Data sanitization</td>
        <td>/api/products/</td>
        <td>POST</td>
        <td>-</td>
        <td>-</td>
        <td>Script injection</td>
    </tr>
    <tr>
        <td>54</td>
        <td>02-Shop</td>
        <td>11-Pagination</td>
        <td>/api/products?perpage=2&page=2</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>Pagination as a function-based approach</td>
    </tr>
    <tr>
        <td>55</td>
        <td>02-Shop</td>
        <td>12-ClassBase Pagination & Filtering</td>
        <td>/api/products/?ordering=price,inventory,…</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>Filtering for multiple fields</td>
    </tr>
    <tr>
        <td>56</td>
        <td>02-Shop</td>
        <td>12-ClassBase Pagination & Filtering</td>
        <td>/api/products/?ordering=price&page=1</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>Combination of filter and pagination</td>
    </tr>
    <tr>
        <td>57</td>
        <td>02-Shop</td>
        <td>12-ClassBase Pagination & Filtering</td>
        <td>/api/products/?page=2&search=shirt</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>Combination of search and pagination</td>
    </tr>

</table>

### Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-xyz`).
3. Commit your changes (`git commit -am 'Add feature xyz'`).
4. Push to the branch (`git push origin feature-xyz`).
5. Create a new Pull Request.

6. ### License
This project is licensed under the MIT License.

MIT License

Copyright (c) [2024] [Mehdi Emadi]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit others to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

