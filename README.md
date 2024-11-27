<table>
    <tr>
        <td>API&#39;s list</td>
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
        <td>127.0.0.1:8000/api/secret/</td>
        <td>GET</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>دسترسی به view خاص با توکن</td>
    </tr>
    <tr>
        <td>2</td>
        <td>01-Auth</td>
        <td>01-token_based_auth</td>
        <td>127.0.0.1:8000/api/api-token-auth/</td>
        <td>POST</td>
        <td>username - password</td>
        <td>-</td>
        <td>دریافت توکن برای کاربر موردنظر</td>
    </tr>
    <tr>
        <td>3</td>
        <td>01-Auth</td>
        <td>01-token_based_auth</td>
        <td>127.0.0.1:8000/api/manager-view/</td>
        <td>GET</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>دسترسی به view گروه مدیریت</td>
    </tr>
    <tr>
        <td>4</td>
        <td>01-Auth</td>
        <td>01-token_based_auth</td>
        <td>127.0.0.1:8000/api/throttle-check/</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>محدودیت گذاری به تعداد درخواست های ناشناس</td>
    </tr>
    <tr>
        <td>5</td>
        <td>01-Auth</td>
        <td>01-token_based_auth</td>
        <td>127.0.0.1:8000/api/throttle-check-auth/</td>
        <td>GET</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>محدودیت گذاری به تعداد درخواست های احراز هویت شده</td>
    </tr>
    <tr>
        <td>6</td>
        <td>01-Auth</td>
        <td>02-API throttling for class-based views</td>
        <td>127.0.0.1:8000/api/register/</td>
        <td>GET</td>
        <td>username - password</td>
        <td>-</td>
        <td>محدودیت گذاری به تعداد درخواست های احراز هویت شده برای حالت class-base</td>
    </tr>
    <tr>
        <td>7.1</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>127.0.0.1:8000/auth/users/</td>
        <td>POST</td>
        <td>email - password - re_password</td>
        <td>-</td>
        <td>ثبت نام کاربر جدید</td>
    </tr>
    <tr>
        <td>7.2</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>127.0.0.1:8000/auth/users/</td>
        <td>GET</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>دریافت مشخصات کامل کاربر-کاربران</td>
    </tr>
    <tr>
        <td>8</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>127.0.0.1:8000/auth/token/login/</td>
        <td>POST</td>
        <td>email - password</td>
        <td>-</td>
        <td>ایجاد توکن کاربر</td>
    </tr>
    <tr>
        <td>9</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>127.0.0.1:8000/auth/token/logout/</td>
        <td>POST</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>از بین بردن توکن کاربر</td>
    </tr>
    <tr>
        <td>10</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>127.0.0.1:8000/auth/users/me/</td>
        <td>GET</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>دریافت مشخصات کامل کاربر</td>
    </tr>
    <tr>
        <td>11</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>127.0.0.1:8000/auth/users/me/</td>
        <td>PATCH</td>
        <td>فیلدهایی که میخواهیم تغییر دهیم</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>تغییرات برخی مشخصات فرد</td>
    </tr>
    <tr>
        <td>12</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>127.0.0.1:8000/auth/users/me/</td>
        <td>PUT</td>
        <td>در اصل مقدار جدید  تمام فیلدها باید وارد شود</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>تغییرات تمامی مشخصات فرد</td>
    </tr>
    <tr>
        <td>13</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>127.0.0.1:8000/auth/users/me/</td>
        <td>DELETE</td>
        <td>current_password</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>پاک کردن کاربر</td>
    </tr>
    <tr>
        <td>14</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>127.0.0.1:8000/auth/users/set_email/</td>
        <td>POST</td>
        <td>new_email - current_password</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>تغییر ایمیل کاربر</td>
    </tr>
    <tr>
        <td>15</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>127.0.0.1:8000/auth/users/set_password/</td>
        <td>POST</td>
        <td>new_password - re_new_password - current_password</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>تغییر مستقیم پسورد کاربر</td>
    </tr>
    <tr>
        <td>16</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>127.0.0.1:8000/auth/users/reset_password/</td>
        <td>POST</td>
        <td>email</td>
        <td>-</td>
        <td>ارسال ایمیل بازیابی رمز عبور</td>
    </tr>
    <tr>
        <td>17</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>127.0.0.1:8000/auth/users/reset_password_confirm/</td>
        <td>POST</td>
        <td>uid - token - new_password - re_new_password</td>
        <td>-</td>
        <td>تایید بازیابی رمز عبور توسط ایمیل</td>
    </tr>
    <tr>
        <td>18</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>127.0.0.1:8000/auth/users/activation/</td>
        <td>POST</td>
        <td>uid - token</td>
        <td>-</td>
        <td>فعالسازی حساب کاربری</td>
    </tr>
    <tr>
        <td>19</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>127.0.0.1:8000/auth/users/resend_activation/</td>
        <td>POST</td>
        <td>email</td>
        <td>-</td>
        <td>ارسال مجدد لینک فعالسازی به ایمیل</td>
    </tr>
    <tr>
        <td>20</td>
        <td>01-Auth</td>
        <td>03-Djoser library</td>
        <td>127.0.0.1:8000/api/groups/manager/users/</td>
        <td>POST, DELETE</td>
        <td>-</td>
        <td>OAuth 2.0 (Token + Header Prefix=Token)</td>
        <td>افزودن کاربر به گروه</td>
    </tr>
    <tr>
        <td>21</td>
        <td>01-Auth</td>
        <td>04-JWT(JSON Web Token)</td>
        <td>127.0.0.1:8000/api/token/</td>
        <td>POST</td>
        <td>email - password</td>
        <td>-</td>
        <td>دریافت access و refresh توکن</td>
    </tr>
    <tr>
        <td>22</td>
        <td>01-Auth</td>
        <td>04-JWT(JSON Web Token)</td>
        <td>127.0.0.1:8000/api/secret</td>
        <td>GET</td>
        <td>-</td>
        <td>Bearer Token(Token=token)</td>
        <td>تست کردن access توکن</td>
    </tr>
    <tr>
        <td>23</td>
        <td>01-Auth</td>
        <td>04-JWT(JSON Web Token)</td>
        <td>127.0.0.1:8000/api/token/refresh/</td>
        <td>POST</td>
        <td>refresh</td>
        <td>-</td>
        <td>دریافت مجددaccess token</td>
    </tr>
    <tr>
        <td>24</td>
        <td>01-Auth</td>
        <td>04-JWT(JSON Web Token)</td>
        <td>127.0.0.1:8000/api/token/blacklist/</td>
        <td>POST</td>
        <td>refresh</td>
        <td>-</td>
        <td>قرار دادن refresh token در blacklist</td>
    </tr>
    <tr>
        <td>25</td>
        <td>02-Shop</td>
        <td>01-Simple API</td>
        <td>127.0.0.1:8000/api/products/</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>دریافت تمام محصولات</td>
    </tr>
    <tr>
        <td>26</td>
        <td>02-Shop</td>
        <td>02-Simple DRF</td>
        <td>127.0.0.1:8000/api/products/  ---  127.0.0.1:8000/api/products/{pk}</td>
        <td>GET, POST, PUT,  PATCH, DELETE</td>
        <td>-</td>
        <td>-</td>
        <td>دریافت تمام محصولات با استفاده از route های مختلف</td>
    </tr>
    <tr>
        <td>27</td>
        <td>02-Shop</td>
        <td>03-ViewSet</td>
        <td>127.0.0.1:8000/api/products/  ---  127.0.0.1:8000/api/products/{pk}</td>
        <td>GET, POST, PUT,  PATCH, DELETE</td>
        <td>-</td>
        <td>-</td>
        <td>استفاده از ViewSet در ویو</td>
    </tr>
    <tr>
        <td>28</td>
        <td>02-Shop</td>
        <td>04-(ModelViewSet) (ReadOnlyModelViewSet)</td>
        <td>127.0.0.1:8000/api/products/  ---  127.0.0.1:8000/api/products/{pk}</td>
        <td>GET, POST, PUT,  PATCH, DELETE</td>
        <td>-</td>
        <td>-</td>
        <td>استفاده از ModelViewSet در ویو</td>
    </tr>
    <tr>
        <td>29</td>
        <td>02-Shop</td>
        <td>04-(ModelViewSet) (ReadOnlyModelViewSet)</td>
        <td>127.0.0.1:8000/api/products/  ---  127.0.0.1:8000/api/products/{pk}</td>
        <td>GET(list-retrieve)</td>
        <td>-</td>
        <td>-</td>
        <td>استفاده از ReadOnlyModelViewSet در ویو</td>
    </tr>
    <tr>
        <td>30</td>
        <td>02-Shop</td>
        <td>05-Generic views</td>
        <td>127.0.0.1:8000/api/products/</td>
        <td>GET, POST</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>31</td>
        <td>02-Shop</td>
        <td>05-Generic views</td>
        <td>127.0.0.1:8000/api/products/&lt;int:pk&gt;/</td>
        <td>GET, PUT, PATCH, DELETE</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>32</td>
        <td>02-Shop</td>
        <td>05-Generic views</td>
        <td>127.0.0.1:8000/api/products/create/</td>
        <td>POST</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>33</td>
        <td>02-Shop</td>
        <td>05-Generic views</td>
        <td>127.0.0.1:8000/api/products/&lt;int:pk&gt;/retrieve/</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>34</td>
        <td>02-Shop</td>
        <td>05-Generic views</td>
        <td>127.0.0.1:8000/api/products/&lt;int:pk&gt;/destroy/</td>
        <td>DELETE</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>35</td>
        <td>02-Shop</td>
        <td>05-Generic views</td>
        <td>127.0.0.1:8000/api/products/&lt;int:pk&gt;/update/</td>
        <td>PUT, PATCH</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>36</td>
        <td>02-Shop</td>
        <td>05-Generic views</td>
        <td>127.0.0.1:8000/api/products/&lt;int:pk&gt;/retrieve-update/</td>
        <td>GET, PUT, PATCH</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>37</td>
        <td>02-Shop</td>
        <td>05-Generic views</td>
        <td>127.0.0.1:8000/api/products/&lt;int:pk&gt;/retrieve-destroy/</td>
        <td>GET, DELETE</td>
        <td>-</td>
        <td>-</td>
        <td>با استفاده از احراز هویت انتخابی</td>
    </tr>
    <tr>
        <td>38</td>
        <td>02-Shop</td>
        <td>06-Serialization</td>
        <td>127.0.0.1:8000/api/products/</td>
        <td> GET</td>
        <td>-</td>
        <td>-</td>
        <td>دریافت محصولات با سریالایزر</td>
    </tr>
    <tr>
        <td>39</td>
        <td>02-Shop</td>
        <td>06-Serialization</td>
        <td>127.0.0.1:8000/api/products/&lt;int:id&gt;</td>
        <td> GET</td>
        <td>-</td>
        <td>-</td>
        <td>دریافت محصول با سریالایزر</td>
    </tr>
    <tr>
        <td>40</td>
        <td>02-Shop</td>
        <td>06-Serialization</td>
        <td>127.0.0.1:8000/api/products/</td>
        <td> GET</td>
        <td>-</td>
        <td>-</td>
        <td>دریافت محصولات با سریالایزر مرتبط</td>
    </tr>
    <tr>
        <td>41</td>
        <td>02-Shop</td>
        <td>06-Serialization</td>
        <td>127.0.0.1:8000/api/products/</td>
        <td> GET</td>
        <td>-</td>
        <td>-</td>
        <td>دریافت محصولات با سریالایزر مرتبط</td>
    </tr>
    <tr>
        <td>42</td>
        <td>02-Shop</td>
        <td>06-Serialization</td>
        <td>127.0.0.1:8000/api/products/</td>
        <td> GET</td>
        <td>-</td>
        <td>-</td>
        <td>دریافت محصولات با سریالایزر مرتبط با لینک کتگوری</td>
    </tr>
    <tr>
        <td>43</td>
        <td>02-Shop</td>
        <td>07-Deserializer</td>
        <td>127.0.0.1:8000/api/products/</td>
        <td>POST</td>
        <td>-</td>
        <td>-</td>
        <td>دی سریالایز به کمک post</td>
    </tr>
    <tr>
        <td>44</td>
        <td>02-Shop</td>
        <td>08-Filtering&amp;Searching&amp; ordering</td>
        <td>127.0.0.1:8000/api/products/?category=shows&amp;to_price=25</td>
        <td> GET</td>
        <td>-</td>
        <td>-</td>
        <td>فیلتر کردن بر اساس کتگوری و حد پایین قیمت</td>
    </tr>
    <tr>
        <td>45</td>
        <td>02-Shop</td>
        <td>08-Filtering&amp;Searching&amp; ordering</td>
        <td>127.0.0.1:8000/api/products/?search=t-shirt</td>
        <td> GET</td>
        <td>-</td>
        <td>-</td>
        <td>جستجوکردن بر اساس نام محصول</td>
    </tr>
    <tr>
        <td>46</td>
        <td>02-Shop</td>
        <td>08-Filtering&amp;Searching&amp; ordering</td>
        <td>127.0.0.1:8000/api/products/?ordering=price,inventory,…</td>
        <td> GET</td>
        <td>-</td>
        <td>-</td>
        <td>به ترتیب کردن محصولات</td>
    </tr>
    <tr>
        <td>47</td>
        <td>02-Shop</td>
        <td>09-Validation</td>
        <td>127.0.0.1:8000/api/products/</td>
        <td>POST</td>
        <td>-</td>
        <td>-</td>
        <td>روش اول برای اعتبار سنجی</td>
    </tr>
    <tr>
        <td>48</td>
        <td>02-Shop</td>
        <td>09-Validation</td>
        <td>127.0.0.1:8000/api/products/</td>
        <td>POST</td>
        <td>-</td>
        <td>-</td>
        <td>روش دوم برای اعتبار سنجی</td>
    </tr>
    <tr>
        <td>49</td>
        <td>02-Shop</td>
        <td>09-Validation</td>
        <td>127.0.0.1:8000/api/products/</td>
        <td>POST</td>
        <td>-</td>
        <td>-</td>
        <td>روش سوم برای اعتبار سنجی</td>
    </tr>
    <tr>
        <td>50</td>
        <td>02-Shop</td>
        <td>09-Validation</td>
        <td>127.0.0.1:8000/api/products/</td>
        <td>POST</td>
        <td>-</td>
        <td>-</td>
        <td>روش چهارم برای اعتبار سنجی</td>
    </tr>
    <tr>
        <td>51</td>
        <td>02-Shop</td>
        <td>09-Validation</td>
        <td>127.0.0.1:8000/api/products/</td>
        <td>POST</td>
        <td>-</td>
        <td>-</td>
        <td>اعتبار سنجی برای منحصربفرد بودن</td>
    </tr>
    <tr>
        <td>52</td>
        <td>02-Shop</td>
        <td>09-Validation</td>
        <td>127.0.0.1:8000/api/products/</td>
        <td>POST</td>
        <td>-</td>
        <td>-</td>
        <td>اعتبار سنجی برای منحصربفرد بودن چند فیلد</td>
    </tr>
    <tr>
        <td>53</td>
        <td>02-Shop</td>
        <td>10-Data sanitization</td>
        <td>127.0.0.1:8000/api/products/</td>
        <td>POST</td>
        <td>-</td>
        <td>-</td>
        <td>script injection</td>
    </tr>
    <tr>
        <td>54</td>
        <td>02-Shop</td>
        <td>11-Pagination</td>
        <td>127.0.0.1:8000/api/products?perpage=2&amp;page=2</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>پجینیشن به صورت تابع بیس</td>
    </tr>
    <tr>
        <td>55</td>
        <td>02-Shop</td>
        <td>12-ClassBase Pagination&amp;Filtering</td>
        <td>127.0.0.1:8000/api/products/?ordering=price,inventory,…</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>فیلترینگ برای چند فیلد</td>
    </tr>
    <tr>
        <td>56</td>
        <td>02-Shop</td>
        <td>12-ClassBase Pagination&amp;Filtering</td>
        <td>127.0.0.1:8000/api/products/?ordering=price&amp;page=1</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>ترکیب فیلتر و پجینیشن</td>
    </tr>
    <tr>
        <td>57</td>
        <td>02-Shop</td>
        <td>12-ClassBase Pagination&amp;Filtering</td>
        <td>127.0.0.1:8000/api/products/?page=2&amp;search=shirt</td>
        <td>GET</td>
        <td>-</td>
        <td>-</td>
        <td>ترکیب سرچ و پجینیشن</td>
    </tr>
</table>
