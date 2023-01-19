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
We decided to take all these variables and create a model pipeline that would allow us to define a relationship between the various variables and the mortality rates.  Essentially, we want to answer the question "Can we predict mortality rates based on lifestyle and diet variables?"

&emsp;&emsp;The results of our modeling are not intended to be prescriptive - we are not trying to define the healthiest possible diet or lifestyle.  After all, so many of these variables are not within our control.  However, we believe there is value in trying to understand correlations between diet/lifestyle, and chronic disease/mortality.  The goal of this project would be to create a resource that everybody can use to evaluate their own lifestyle and see where feasible adjustments can be made.  

## Data Information


## Data Cleaning


## Exploratory Data Analysis


## Modeling
### Metrics for Evaluation

### Pipeline for Target Selection


## Results


## Conclusions & Recommendations


## Next Steps