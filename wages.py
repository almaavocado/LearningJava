# Calculate an hourly worker's weekly wage based on hourly rate and hours worked.
# Use constant variables to set thesholds for various payment options.
HOURS_FULLTIME = 40
HOURS_OVERTIME = 60
RATE_OVERTIME = 1.5
RATE_SUPER_OVERTIME = 2.0

hours = float(input("How many hours did you work this week? "))
rate = float(input("How much are you paid per hour? $"))

if hours <= HOURS_FULLTIME:
    # This person gets their rate times their hours.
    earned = hours * rate
elif hours <= HOURS_OVERTIME:
    # This person gets their rate times 40 hours, plus 150% of their rate times
    # the number of hours worked in excess of 40.
    overtime = hours - HOURS_FULLTIME
    earned = rate * HOURS_FULLTIME + (rate * RATE_OVERTIME) * overtime
else:
    # This person worked more than 60 hours. They get their rate times 40 hours,
    # plus 150% of their rate times 20 hours, plus 200% of their rate times the
    # number of hours in excess of 60.
    super_overtime = hours - HOURS_OVERTIME
    earned = rate * HOURS_FULLTIME \
        + (rate * RATE_OVERTIME) * (HOURS_OVERTIME - HOURS_FULLTIME) \
        + (rate * RATE_SUPER_OVERTIME) * super_overtime

print("You earned ${0:.2f}".format(earned))
# This statement creates a formatted string. The {:0.2f} is replaced by the value
# of the variable "earned". The 0.2f says to create a decimal number with exactly
# two decimal points.

# Lessons:
#   {:0.2f} formatting strings
