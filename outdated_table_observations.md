# !!!Outdated due to change in task

# Observations of oddities in tables

The following oddities were observed in the given tables, and might need to be
fixed in some way.

## Absence monthly

- _join01 and _join02 contains a lot of duplicate data
  - Especially since they are constructed from employee initials and Cal_YearMonth
- Absence of zero could be inferred from missing data?

## Absence period

- One row for each date on sick leave, showing the total length of the sickleave
and start and end of leave

## dp Employee

- Probably not necessary to keep one for each row for each month
- Lots of duplicated data, keep separate table for those?
- Lots of calculated data on age (some duplicates), maybe just store date it is calculated from?
- Careers har både tom og not assigned
- JA1 og JA2 er mutuelt eksklusive?
- Hires = Hires_external?
- Terminations = Terminations_external?
- Duplication: Terminations_external = Terminations_external_involuntary + Terminations_external_voluntary
- Incorrect data: Age_group__ some employees set as other when they belong in group 50+
- Incorrect values/naming: Age_Group has categories 30+, 30-, and 30-50.
  - Should be 50+, 30-, and 30-50
    - Data matches this already
  - If last two problems fixed, Age_Group__ and Age_Group are equal
- GroupInt er altid tom
- Somthing very wrong in rounded years
- 18 employees with age in years above 120

## Hierachy

- Probably don't need all levels?

## Ultimate calendar table

- Fiscal month/quarter/year equal to month/quater/year
- Offsets can be calculated from current date, their date.
- Month/quarter/year to date?
- Duplication: Rep{Month/Year}Offset = {Month/Year}Offset
- MonthYearNum + MonthYear + MonthYearLong
- WeekdayNum + Weekday + WeekendWeekend
- WeekSequenceNumber + CurWeekOffset