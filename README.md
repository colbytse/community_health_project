# Project 4: Lifestyle and Mortality from The China Study


## Executive Summary
&emsp;&emsp;As data scientists, we are constantly looking for ways to better understand the world around us through the lens of data.  How can we make an impact, how can we improve our lives, how can we explain tragedies?  One topic that our group is particularly interested in is health and mortality.  We want to better understand mortality rates and what lifestyle choices impact different causes of death.  There are so many environmental factors that might be bigger indicators, but individual lifestyle decisions regarding diet, habits, location, etc can also be factors.  To look into this question, we turned to The China Study.

&emsp;&emsp;The China Study is a book written by TC Campbell, a nutrional biochemist.  Over the course of 20 years, a team of researchers from Cornell, Oxford, and the Chinese Academy of Preventative Medicine performed a study of random population samples from the 69 rural counties of China.  The study covered an extensive list of lifestyle questions, diet intake records, and even measurements of blood and urine samples.  Each county also provided detailed records on mortality and the different causes of death to correlate the data by county.  From TC Campbell's [Center for Nutrition Studies](https://nutritionstudies.org/the-china-study/), here is a summary of the survey methodology:

>"Sixty five counties in rural China were selected for the study and dietary, lifestyle and disease characteristics were studied. Within each of the 65 counties, 2 villages were selected and 50 families in each were randomly chosen. One adult from each household (half men and half women), 6,500 for the entire survey, participated. Blood, urine and food samples were obtained for later analysis, while questionnaire and 3-day diet information was recorded."

&emsp;&emsp;The goal of this study was to investigate links between nutrition and the development of chronic diseases like cancer, heart disease, and diabetes.  The results of the study led TC Campbell and his son to write *The China Study*, with the primary conclusion that a diet high in animal-based foods, particularly meat and dairy, is associated with a higher risk of chronic diseases, while a diet based on whole, plant-based foods is associated with a lower risk.  He argues that the nutrients in plant-based foods are more beneficial than getting them from supplements.  This book became very popular and increased participation in diets like plant-based, Whole30, raw-foods, and more.

&emsp;&emsp;Over the years, the book has received both praise (from [The New York Times](https://archive.nytimes.com/well.blogs.nytimes.com/2011/01/07/nutrition-advice-from-the-china-study/)) and critique (from [Science-Based Medicine](https://sciencebasedmedicine.org/the-china-study-revisited/), the [American Journal of Clinical Nutrition](https://academic.oup.com/ajcn/article/71/3/850/4729291?login=false), and [other data-drive nutritionists](https://deniseminger.com/the-china-study/)).  However, there has consistently been praise for the data itself and the effort taken to ensure a thorough, diverse, and repetitive dataset.  As data scientists, we wanted to see what knowledge we could glean from this treasure trove of data itself, instead of relying on the analysis of the researchers.  Of course, they have clearly spent much more time on their analysis and with the data overall than we had, but the exercise is useful.  And there have been many papers over the years that use the China study data to form their own conclusions.

&emsp;&emsp;All the original data files were available on the website for the [Center for Nutrition Studies](https://nutritionstudies.org/the-china-study/).  It is split into the results from three survey periods: 1973-1983, 1986-1989, and 1993.  The data is also broken down into the following categories:
* Mortality variables
* Plasma, red blood cell, and urine variables
* Diet and geography variables
* Lifestyle questionnaire variables

&emsp;&emsp;We decided to take all these variables and create a model pipeline that would allow us to define a relationship between the various variables and the mortality rates.  Essentially, we want to answer the question "Can we predict mortality rates based on lifestyle and diet variables?"

&emsp;&emsp;The results of our modeling are not intended to be prescriptive - we are not trying to define the healthiest possible diet or lifestyle.  After all, so many of these variables are not within our control.  However, we believe there is value in trying to understand correlations between diet/lifestyle, and chronic disease/mortality.  The goal of this project would be to create a resource that everybody can use to evaluate their own lifestyle and see where feasible adjustments can be made.  

## Data Information
We collected all the data and methodology research available from the [Center for Nutrition Studies](https://nutritionstudies.org/the-china-study/).  It contains the following items

|File Name|Years|Description|
|---|---|---|
|CH83M.csv|1973-1983|mainland mortality variables|
|CH83DG.csv|1973-1983|mainland diet and geographic variables|
|CH83PRU.csv|1973-1983|mainland plasma, red blood cell and urine variables|
|CH83Q.csv|1973-1983|mainland questionnaire variables|
|CH89M.csv|1986-1989|mainland mortality variables|
|CH89DG.csv|1986-1989|mainland diet and geographic variables|
|CH89PRU.csv|1986-1989|mainland plasma, red blood cell and urine variables|
|CH89Q.csv|1986-1989|mainland questionnaire variables|
|CH93PRU.csv|1993|mainland plasma, red blood cell and urine variables|
|CH93Q.csv|1993|mainland questionnaire variables|
|CHTAIM.csv|1986-1989|Taiwan mortality variables|
|CHTAIPRU.csv|1986-1989|Taiwan plasma, red blood cell and urine variables|
|CHTAIQ.csv|1986-1989|Taiwan questionnaire variables|
|CHNAME.txt|-|all the variable codes and their descriptions|

We decided to focus on the group of datasets from 1986-1989 mainland China for a few reasons.  This iteration included a full set of all four surveys - mortality, diet, blood/urine, and questionnaires.  It also covered additional counties and more individual respondents per county, so the datasets cover a larger sample size.  And finally there were more questions covered in this iteration than in the other ones.

The downloaded data files came with a readme that contained the below information.  We used this explanation to make decisions about filtering by gender and xiang when appropriate:
> The first record in each file lists the keywords for variables included in that file.
> <br>In each file, for each county there are 9 records in total:
> * Male xiang 1
> * Male xiang 2
> * Male xiang code 3 (=mean of xiang 1 and xiang 2 or county value)
> * Female xiang 1
> * Female xiang 2
> * Female xiang code 3
> * Total xiang 1, where Total (sex code T) =mean of male and female
> * Total xiang 2
> * Total xiang code 3
> <br>For consistency of format all 9 records are included even where a record consists of all missing values (e.g. mortality values are available only at the county level, so xiang-specific values are all missing)

The CHNAME.txt file was a valuable reference because it contained the description for each question.  Additional details about each survey and the wording of each question can be found in the the resource papers in the [research](./research) folder.

An example of the code explanations is below.
|Code|Keywords|Description|
|---|---|---|
|M039| BRAINCAc|   mortality BRAIN TUMOUR (MALIGNANT OR NOT) AGE 35-69 (stand. rate/100,000) (ICD9 191, 225.0, 237.5, 239.6)|
|M040| LYMPHOMAc|  mortality LYMPHOMA AND MYELOMA AGE 35-69 (stand. rate/100,000) (ICD9 200-3)|
|M041| LEUKEMIAb|  mortality LEUKAEMIA AGE 0-34 (stand. rate/100,000) (ICD9 204-8)|                                                      
|...|
|D007| %ANPRKCAL|  diet survey PERCENTAGE OF CALORIC INTAKE FROM ANIMAL PROTEIN (for reference man)|                                                                                                                           
|D008| %PLPRKCAL|  diet survey PERCENTAGE OF CALORIC INTAKE FROM PLANT PROTEIN (for reference man)|                                 
|D009| %CARBKCAL|  diet survey PERCENTAGE OF CALORIC INTAKE FROM CARBOHYDRATE (for reference man)|                                   
|...|
|Q065| dWOODNOW|   questionnaire PERCENTAGE USE MAINLY WOOD/STALKS FOR COOKING NOW|                                                  
|Q066| dOTHFNOW|   questionnaire PERCENTAGE USE MAINLY OTHER FUEL FOR COOKING NOW|                                                   
|...|
|Q176| dEGGS|      questionnaire DAYS PER YEAR EAT EGGS|                                                                             
|Q177| dMILK|      questionnaire DAYS PER YEAR CONSUME MILK OR DAIRY PRODUCTS|                                                       
|Q178| dJASMIN-T|  questionnaire PERCENT DRINK JASMINE TEA DAILY|                                                                    
                                                                                                                                             
## Data Cleaning


## Exploratory Data Analysis


## Modeling
### Metrics for Evaluation

### Pipeline for Target Selection


## Results


## Conclusions & Recommendations


## Next Steps