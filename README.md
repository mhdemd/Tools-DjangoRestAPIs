| API's list |
| ---------- |
| No         | Folder | Sub Folder | URLs | Method | Form Data | Auth Type | Function |
| 1          | 01-Auth | 01-token_based_auth | 127.0.0.1:8000/api/secret/ | GET | \- | OAuth 2.0 (Token + Header Prefix=Token) | دسترسی به view خاص با توکن |
| 2          | 01-Auth | 01-token_based_auth | 127.0.0.1:8000/api/api-token-auth/ | POST | username - password | \- | دریافت توکن برای کاربر موردنظر |
| 3          | 01-Auth | 01-token_based_auth | 127.0.0.1:8000/api/manager-view/ | GET | \- | OAuth 2.0 (Token + Header Prefix=Token) | دسترسی به view گروه مدیریت |
| 4          | 01-Auth | 01-token_based_auth | 127.0.0.1:8000/api/throttle-check/ | GET | \- | \- | محدودیت گذاری به تعداد درخواست های ناشناس |
| 5          | 01-Auth | 01-token_based_auth | 127.0.0.1:8000/api/throttle-check-auth/ | GET | \- | OAuth 2.0 (Token + Header Prefix=Token) | محدودیت گذاری به تعداد درخواست های احراز هویت شده |
| 6          | 01-Auth | 02-API throttling for class-based views | 127.0.0.1:8000/api/register/ | GET | username - password | \- | محدودیت گذاری به تعداد درخواست های احراز هویت شده برای حالت class-base |
| 7.1        | 01-Auth | 03-Djoser library | 127.0.0.1:8000/auth/users/ | POST | email - password - re_password | \- | ثبت نام کاربر جدید |
| 7.2        | 01-Auth | 03-Djoser library | 127.0.0.1:8000/auth/users/ | GET | \- | OAuth 2.0 (Token + Header Prefix=Token) | دریافت مشخصات کامل کاربر-کاربران |
| 8          | 01-Auth | 03-Djoser library | 127.0.0.1:8000/auth/token/login/ | POST | email - password | \- | ایجاد توکن کاربر |
| 9          | 01-Auth | 03-Djoser library | 127.0.0.1:8000/auth/token/logout/ | POST | \- | OAuth 2.0 (Token + Header Prefix=Token) | از بین بردن توکن کاربر |
| 10         | 01-Auth | 03-Djoser library | 127.0.0.1:8000/auth/users/me/ | GET | \- | OAuth 2.0 (Token + Header Prefix=Token) | دریافت مشخصات کامل کاربر |
| 11         | 01-Auth | 03-Djoser library | 127.0.0.1:8000/auth/users/me/ | PATCH | فیلدهایی که میخواهیم تغییر دهیم | OAuth 2.0 (Token + Header Prefix=Token) | تغییرات برخی مشخصات فرد |
| 12         | 01-Auth | 03-Djoser library | 127.0.0.1:8000/auth/users/me/ | PUT | در اصل مقدار جدید  تمام فیلدها باید وارد شود | OAuth 2.0 (Token + Header Prefix=Token) | تغییرات تمامی مشخصات فرد |
| 13         | 01-Auth | 03-Djoser library | 127.0.0.1:8000/auth/users/me/ | DELETE | current_password | OAuth 2.0 (Token + Header Prefix=Token) | پاک کردن کاربر |
| 14         | 01-Auth | 03-Djoser library | 127.0.0.1:8000/auth/users/set_email/ | POST | new_email - current_password | OAuth 2.0 (Token + Header Prefix=Token) | تغییر ایمیل کاربر |
| 15         | 01-Auth | 03-Djoser library | 127.0.0.1:8000/auth/users/set_password/ | POST | new_password - re_new_password - current_password | OAuth 2.0 (Token + Header Prefix=Token) | تغییر مستقیم پسورد کاربر |
| 16         | 01-Auth | 03-Djoser library | 127.0.0.1:8000/auth/users/reset_password/ | POST | email | \- | ارسال ایمیل بازیابی رمز عبور |
| 17         | 01-Auth | 03-Djoser library | 127.0.0.1:8000/auth/users/reset_password_confirm/ | POST | uid - token - new_password - re_new_password | \- | تایید بازیابی رمز عبور توسط ایمیل |
| 18         | 01-Auth | 03-Djoser library | 127.0.0.1:8000/auth/users/activation/ | POST | uid - token | \- | فعالسازی حساب کاربری |
| 19         | 01-Auth | 03-Djoser library | 127.0.0.1:8000/auth/users/resend_activation/ | POST | email | \- | ارسال مجدد لینک فعالسازی به ایمیل |
| 20         | 01-Auth | 03-Djoser library | 127.0.0.1:8000/api/groups/manager/users/ | POST, DELETE | \- | OAuth 2.0 (Token + Header Prefix=Token) | افزودن کاربر به گروه |
| 21         | 01-Auth | 04-JWT(JSON Web Token) | 127.0.0.1:8000/api/token/ | POST | email - password | \- | دریافت access و refresh توکن |
| 22         | 01-Auth | 04-JWT(JSON Web Token) | 127.0.0.1:8000/api/secret | GET | \- | Bearer Token(Token=token) | تست کردن access توکن |
| 23         | 01-Auth | 04-JWT(JSON Web Token) | 127.0.0.1:8000/api/token/refresh/ | POST | refresh | \- | دریافت مجددaccess token |
| 24         | 01-Auth | 04-JWT(JSON Web Token) | 127.0.0.1:8000/api/token/blacklist/ | POST | refresh | \- | قرار دادن refresh token در blacklist |
| 25         | 02-Shop | 01-Simple API | 127.0.0.1:8000/api/products/ | GET | \- | \- | دریافت تمام محصولات |
| 26         | 02-Shop | 02-Simple DRF | 127.0.0.1:8000/api/products/  ---  127.0.0.1:8000/api/products/{pk} | GET, POST, PUT,  PATCH, DELETE | \- | \- | دریافت تمام محصولات با استفاده از route های مختلف |
| 27         | 02-Shop | 03-ViewSet | 127.0.0.1:8000/api/products/  ---  127.0.0.1:8000/api/products/{pk} | GET, POST, PUT,  PATCH, DELETE | \- | \- | استفاده از ViewSet در ویو |
| 28         | 02-Shop | 04-(ModelViewSet) (ReadOnlyModelViewSet) | 127.0.0.1:8000/api/products/  ---  127.0.0.1:8000/api/products/{pk} | GET, POST, PUT,  PATCH, DELETE | \- | \- | استفاده از ModelViewSet در ویو |
| 29         | 02-Shop | 04-(ModelViewSet) (ReadOnlyModelViewSet) | 127.0.0.1:8000/api/products/  ---  127.0.0.1:8000/api/products/{pk} | GET(list-retrieve) | \- | \- | استفاده از ReadOnlyModelViewSet در ویو |
| 30         | 02-Shop | 05-Generic views | 127.0.0.1:8000/api/products/ | GET, POST | \- | \- | \- |
| 31         | 02-Shop | 05-Generic views | 127.0.0.1:8000/api/products/<int:pk>/ | GET, PUT, PATCH, DELETE | \- | \- | \- |
| 32         | 02-Shop | 05-Generic views | 127.0.0.1:8000/api/products/create/ | POST | \- | \- | \- |
| 33         | 02-Shop | 05-Generic views | 127.0.0.1:8000/api/products/<int:pk>/retrieve/ | GET | \- | \- | \- |
| 34         | 02-Shop | 05-Generic views | 127.0.0.1:8000/api/products/<int:pk>/destroy/ | DELETE | \- | \- | \- |
| 35         | 02-Shop | 05-Generic views | 127.0.0.1:8000/api/products/<int:pk>/update/ | PUT, PATCH | \- | \- | \- |
| 36         | 02-Shop | 05-Generic views | 127.0.0.1:8000/api/products/<int:pk>/retrieve-update/ | GET, PUT, PATCH | \- | \- | \- |
| 37         | 02-Shop | 05-Generic views | 127.0.0.1:8000/api/products/<int:pk>/retrieve-destroy/ | GET, DELETE | \- | \- | با استفاده از احراز هویت انتخابی |
| 38         | 02-Shop | 06-Serialization | 127.0.0.1:8000/api/products/ |  GET | \- | \- | دریافت محصولات با سریالایزر |
| 39         | 02-Shop | 06-Serialization | 127.0.0.1:8000/api/products/<int:id> |  GET | \- | \- | دریافت محصول با سریالایزر |
| 40         | 02-Shop | 06-Serialization | 127.0.0.1:8000/api/products/ |  GET | \- | \- | دریافت محصولات با سریالایزر مرتبط |
| 41         | 02-Shop | 06-Serialization | 127.0.0.1:8000/api/products/ |  GET | \- | \- | دریافت محصولات با سریالایزر مرتبط |
| 42         | 02-Shop | 06-Serialization | 127.0.0.1:8000/api/products/ |  GET | \- | \- | دریافت محصولات با سریالایزر مرتبط با لینک کتگوری |
| 43         | 02-Shop | 07-Deserializer | 127.0.0.1:8000/api/products/ | POST | \- | \- | دی سریالایز به کمک post |
| 44         | 02-Shop | 08-Filtering&Searching& ordering | 127.0.0.1:8000/api/products/?category=shows&to_price=25 |  GET | \- | \- | فیلتر کردن بر اساس کتگوری و حد پایین قیمت |
| 45         | 02-Shop | 08-Filtering&Searching& ordering | 127.0.0.1:8000/api/products/?search=t-shirt |  GET | \- | \- | جستجوکردن بر اساس نام محصول |
| 46         | 02-Shop | 08-Filtering&Searching& ordering | 127.0.0.1:8000/api/products/?ordering=price,inventory,… |  GET | \- | \- | به ترتیب کردن محصولات |
| 47         | 02-Shop | 09-Validation | 127.0.0.1:8000/api/products/ | POST | \- | \- | روش اول برای اعتبار سنجی |
| 48         | 02-Shop | 09-Validation | 127.0.0.1:8000/api/products/ | POST | \- | \- | روش دوم برای اعتبار سنجی |
| 49         | 02-Shop | 09-Validation | 127.0.0.1:8000/api/products/ | POST | \- | \- | روش سوم برای اعتبار سنجی |
| 50         | 02-Shop | 09-Validation | 127.0.0.1:8000/api/products/ | POST | \- | \- | روش چهارم برای اعتبار سنجی |
| 51         | 02-Shop | 09-Validation | 127.0.0.1:8000/api/products/ | POST | \- | \- | اعتبار سنجی برای منحصربفرد بودن |
| 52         | 02-Shop | 09-Validation | 127.0.0.1:8000/api/products/ | POST | \- | \- | اعتبار سنجی برای منحصربفرد بودن چند فیلد |
| 53         | 02-Shop | 10-Data sanitization | 127.0.0.1:8000/api/products/ | POST | \- | \- | script injection |
| 54         | 02-Shop | 11-Pagination | 127.0.0.1:8000/api/products?perpage=2&page=2 | \- | \- | \- | پجینیشن به صورت تابع بیس |
| 55         | 02-Shop | 12-ClassBase Pagination&Filtering | 127.0.0.1:8000/api/products/?ordering=price,inventory,… | GET | \- | \- | فیلترینگ برای چند فیلد |
| 56         | 02-Shop | 12-ClassBase Pagination&Filtering | 127.0.0.1:8000/api/products/?ordering=price&page=1 | GET | \- | \- | ترکیب فیلتر و پجینیشن |
| 57         | 02-Shop | 12-ClassBase Pagination&Filtering | 127.0.0.1:8000/api/products/?page=2&search=shirt | GET | \- | \- | ترکیب سرچ و پجینیشن |
