# Emarsys SQL assignment
- Please find the queries for the SQL assignments in the ./sql/query subdirectory.
- You will also find the corresponding guidance beside the scripts in ./sql/sql_readme.md

# Emarsys Due Date Calculator assignment

### Implementing CalculateDueDate method
<br>• Input: Takes the submit date/time and turnaround time.
<br>• Output: Returns the date/time when the issue is resolved.

### Rules
<br>• Working hours are from 9AM to 5PM on every working day, Monday to Friday.
<br>• Holidays should be ignored (e.g. A holiday on a Thursday is considered as a
working day. A working Saturday counts as a non-working day.).
<br>• The turnaround time is defined in working hours (e.g. 2 days equal 16 hours).
If a problem was reported at 2:12PM on Tuesday and the turnaround time is
16 hours, then it is due by 2:12PM on Thursday.
<br>• A problem can only be reported during working hours. (e.g. All submit date
values are set between 9AM to 5PM.)
<br>• Do not use any third-party libraries for date/time calculations (e.g. Moment.js,
Carbon, Joda, etc.) or hidden functionalities of the built-in methods.

### Optional
<br>• Including automated tests to your solution is a plus.
<br>• Test-driven (TDD) solutions are especially welcome.
<br>• Clean Code (by Robert. C. Martin) makes us happy.