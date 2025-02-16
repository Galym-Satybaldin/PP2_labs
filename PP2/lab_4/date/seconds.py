from datetime import datetime

date1 = datetime(2025, 2, 10, 12, 30, 0)  # Example date 1
date2 = datetime(2025, 2, 14, 14, 45, 0)  # Example date 2

difference_in_seconds = abs((date2 - date1).total_seconds())

print(f"Difference in seconds: {difference_in_seconds}")
