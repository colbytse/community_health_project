#There are 13 data files
 
CH83M.CSV        (1973-5 mainland mortality variables)
CH83PRU.CSV      (1983 mainland plasma, red blood cell and urine variables)
CH83DG.CSV       (1983 mainland diet and geographic variables)
CH83Q.CSV        (1983 mainland questionnaire variables)

CH89M.CSV        (1986-8 mainland mortality variables)
CH89PRU.CSV      (1989 mainland plasma, red blood cell and urine variables)
CH89DG.CSV       (1989 mainland diet and geographic variables)
CH89Q.CSV        (1989 mainland questionnaire variables)

CH93PRU.CSV      (1993 mainland plasma, red blood cell and urine variables)
CH93Q.CSV        (1993 mainland questionnaire variables)

CHTAIM.CSV       (1986-8 Taiwan mortality variables)
CHTAIPRU.CSV     (1989 Taiwan plasma, red blood cell and urine variables)
CHTAIQ.CSV       (1989 Taiwan questionnaire variables)
 
Values are comma-separated and missing values are denoted by a decimal point.
 
The first record in each file lists the keywords for variables included in that file.
In each file, for each county there are 9 records in total:
 
Male xiang 1
Male xiang 2
Male xiang code 3 (=mean of xiang 1 and xiang 2 or county value)
Female xiang 1
Female xiang 2
Female xiang code 3
Total xiang 1     where Total (sex code T) =mean of male and female
Total xiang 2
Total xiang code 3
 
For consistency of format all 9 records are included even where a record consists of all missing values (e.g. mortality values are available only at the county level, so xiang-specific values are all missing)
 
A text file, CHNAME.TXT, provides a description of each variable, referenced by the keywords shown in the first record of each data file.