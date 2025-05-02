def day_of_week(day, month, year):
   
    from datetime import datetime
    
    date = datetime(year, month, day)
    
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
 
    return days[(date.weekday() + 1) % 7]


if __name__ == "__main__":
    
    print(f"Example 1: day=31, month=8, year=2019 => {day_of_week(31, 8, 2019)}")  # Should output "Saturday"
    
    # Example 2
    print(f"Example 2: day=18, month=7, year=1999 => {day_of_week(18, 7, 1999)}")  # Should output "Sunday"
    
    # Example 3
    print(f"Example 3: day=15, month=8, year=1993 => {day_of_week(15, 8, 1993)}")  # Should output "Sunday"
    
    print("Debug: All test cases have been executed.") 