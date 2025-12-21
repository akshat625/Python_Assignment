from datetime import datetime, timedelta

original_date = datetime(2020, 3, 22, 10, 0)
new_date = original_date + timedelta(weeks=1, hours=12)

print("Original Date & Time:", original_date)
print("New Date & Time:", new_date)

print("\n------------------------------------------------------------------------------------------------------------------------")

from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

print("\n------------------------------------------------------------------------------------------------------------------------")

import os

cwd = os.getcwd()
print("Current Working Directory:", cwd)

os.mkdir("test")
print("Folder 'test' created")

print("Contents of directory:", os.listdir(cwd))

os.rmdir("test")
print("Folder 'test' removed")

print("\n------------------------------------------------------------------------------------------------------------------------")
import os

os.rename("old_name.txt", "new_name.txt")
print("File renamed successfully")

print("\n------------------------------------------------------------------------------------------------------------------------")

import os

with open("example.txt", "w") as file:
    file.write("Hello Python File Handling")

file_size = os.path.getsize("example.txt")
print("File Size:", file_size, "bytes")

print("\n------------------------------------------------------------------------------------------------------------------------")

from datetime import datetime

date_str = "Feb 25 2020 4:20PM"
dt = datetime.strptime(date_str, "%b %d %Y %I:%M%p")

print(dt)

print("\n------------------------------------------------------------------------------------------------------------------------")

from datetime import datetime, timedelta

date_obj = datetime(2025, 2, 25)
new_date = date_obj - timedelta(days=7)

print("New date:", new_date.date())

print("\n------------------------------------------------------------------------------------------------------------------------")
from datetime import datetime

date_obj = datetime(2020, 2, 25)
formatted_date = date_obj.strftime("%A %d %B %Y")

print(formatted_date)

