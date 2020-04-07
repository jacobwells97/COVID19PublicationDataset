# COVID19AcademiaDataset
Database of metadata for scholarly articles related to the Coronavirus Disease 2019.

Data is scraped through exported searches of the EBSCOhost search tool, utilizing all of their databases

Search query used was 
( "covid-19" OR "COVID-19" ) OR 
"2019-nCoV" OR 
"Severe acute respiratory syndrome coronavirus 2" OR 
"SARS-CoV-2" OR 
"coronavirus disease 2019" OR 
"Wuhan coronavirus"

Results were limited to Scholarly (Peer Reviewed) Journals with publishing dates on or after November 2019. Databases queried include Academic Search Complete,  Academic Search Ultimate, CINAHL, eBook Clinical Collection (EBSCOhost), Health and Psychosocial Instruments, International Pharmaceutical Abstracts, and MEDLINE.

Duplicate DOIs (will be) removed

For convenience, the raw XML data is scraped using scrapeRawData.ipynb
