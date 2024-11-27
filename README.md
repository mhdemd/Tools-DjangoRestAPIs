<table>
    <tr>
        <td>API's list</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
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
        <td>Access to a specific view with a token</td>
    </tr>
    <tr>
        <td>2</td>
        <td>01-Auth</td>
        <td>01-token_based_auth</td>
        <td>/api/api-token-auth/</td>
        <td>POST</td>
        <td>username - password</td>
        <td>-</td>
        <td>Receive token for the specified user</td>
    </tr>
    <tr>
        <td>3</td>
        <td>01-Auth</td>
        <td>01-token_based_auth</td>
        <td>/api/manager-view/</td>
        <td>GET</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Access to the management group view</td>
    </tr>
    <tr>
        <td>4</td>
        <td>01-Auth</td>
        <td>01-token_based_auth</td>
        <td>/api/throttle-check/</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>Rate limiting for anonymous requests</td>
    </tr>
    <tr>
        <td>5</td>
        <td>01-Auth</td>
        <td>01-token_based_auth</td>
        <td>/api/throttle-check-auth/</td>
        <td>GET</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Rate limiting for authenticated requests</td>
    </tr>
    <tr>
        <td>6</td>
        <td>01-Auth</td>
        <td>02-API throttling for class-based views</td>
        <td>/api/register/</td>
        <td>GET</td>
        <td>username - password</td>
        <td>-</td>
        <td>Rate limiting for authenticated requests in class-based views</td>
    </tr>
    <tr>
        <td>7.1</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/users/</td>
        <td>POST</td>
        <td>email - password - re_password</td>
        <td>-</td>
        <td>Register a new user</td>
    </tr>
    <tr>
        <td>7.2</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/users/</td>
        <td>GET</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Retrieve full user details</td>
    </tr>
    <tr>
        <td>8</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/token/login/</td>
        <td>POST</td>
        <td>email - password</td>
        <td>-</td>
        <td>Create a user token</td>
    </tr>
    <tr>
        <td>9</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/token/logout/</td>
        <td>POST</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Remove user token</td>
    </tr>
    <tr>
        <td>10</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/users/me/</td>
        <td>GET</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Retrieve full user profile</td>
    </tr>
    <tr>
        <td>11</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/users/me/</td>
        <td>PATCH</td>
        <td>Fields to be updated</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Modify some user profile details</td>
    </tr>
    <tr>
        <td>12</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/users/me/</td>
        <td>PUT</td>
        <td>All fields need to be submitted with new values</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Modify all user profile details</td>
    </tr>
    <tr>
        <td>13</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>/auth/users/me/</td>
        <td>DELETE</td>
        <td>current_password</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>Delete user account</td>
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
        <!-- Data for this row continues -->
    </tr>
</table>
