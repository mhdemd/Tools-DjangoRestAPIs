class OuterClass:
    def __init__(self):
        self.inner_instance = self.InnerClass()

    class InnerClass:
        inner_attribute = "Inner attribute value"

# ایجاد یک نمونه از کلاس اصلی
outer_obj = OuterClass()
# دسترسی به ویژگی‌ها و اتریبیوت‌های کلاس داخلی از طریق نمونه کلاس اصلی
print(outer_obj.inner_instance.inner_attribute)  # خروجی: Inner attribute value
