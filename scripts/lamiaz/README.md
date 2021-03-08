## Property Characteristics EDA: former use, contaminants found

### former_use_keyword_extraction.R
Exploration of the keywords describing former use in the Description History field

### relation_former_use_cntmnt.R
Reuses cleaning from the munging/cleanup.R with a few modifications (correction of dates, different way to calculate Number of Contaminants Found, use of numericals instead of factors)
Adds keyword flag variables to the data, using keywords identified from analysis in former_use_keyword_extraction.R
Relates keyword flag variables to the presence of contaminants and the type of contaminated media, and plots outputs

### What could be added
Identify more keywords, and group them into meaningful categories
More precise categories of former use could correlate more strongly to contamination and other property descriptors.
What to do for properties where all Cntmnt_Fnd columns are NA?