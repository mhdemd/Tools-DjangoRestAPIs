API's list							
No	Folder	Sub Folder	URLs	Method	Form Data	Auth Type	Function
1	01-Auth	01-token_based_auth	127.0.0.1:8000/api/secret/	GET	-	OAuth 2.0 (Token + Header Prefix=Token)	دسترسی به view خاص با توکن
2	01-Auth	01-token_based_auth	127.0.0.1:8000/api/api-token-auth/	POST	username - password	-	دریافت توکن برای کاربر موردنظر
3	01-Auth	01-token_based_auth	127.0.0.1:8000/api/manager-view/	GET	-	OAuth 2.0 (Token + Header Prefix=Token)	دسترسی به view گروه مدیریت
4	01-Auth	01-token_based_auth	127.0.0.1:8000/api/throttle-check/	GET	-	-	محدودیت گذاری به تعداد درخواست های ناشناس
5	01-Auth	01-token_based_auth	127.0.0.1:8000/api/throttle-check-auth/	GET	-	OAuth 2.0 (Token + Header Prefix=Token)	محدودیت گذاری به تعداد درخواست های احراز هویت شده
6	01-Auth	02-API throttling for class-based views	127.0.0.1:8000/api/register/	GET	username - password	-	محدودیت گذاری به تعداد درخواست های احراز هویت شده برای حالت class-base
![Uploading image.png…]()
