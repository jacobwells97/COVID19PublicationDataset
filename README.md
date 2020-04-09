# COVID19AcademiaDataset
Database of metadata for scholarly articles related to the Coronavirus Disease 2019.

Data is scraped through exported searches of the EBSCOhost search tool, utilizing all of their databases.

A persistent link to the search can be found [here](http://libproxy.temple.edu/login?url=http://search.ebscohost.com/login.aspx?direct=true&db=e000xna&db=e600xww&db=a9h&db=cin20&db=hpi&db=ipa&db=cmedm&db=asn&bquery=(+%26quot%3bcovid-19%26quot%3b+OR+%26quot%3bCOVID-19%26quot%3b+)+OR+%26quot%3b2019-nCoV%26quot%3b+OR+%26quot%3bSevere+acute+respiratory+syndrome+coronavirus+2%26quot%3b+OR+%26quot%3bSARS-CoV-2%26quot%3b+OR+%26quot%3bcoronavirus+disease+2019%26quot%3b+OR+%26quot%3bWuhan+coronavirus%26quot%3b&cli0=RV&clv0=Y&cli1=DT1&clv1=201911-000001&type=1&searchMode=Standard&site=ehost-live&scope=site). This linked worked on a separate browser on 4/9/2020

Search query used was 
( "covid-19" OR "COVID-19" ) OR 
"2019-nCoV" OR 
"Severe acute respiratory syndrome coronavirus 2" OR 
"SARS-CoV-2" OR 
"coronavirus disease 2019" OR 
"Wuhan coronavirus"

Results were limited to Scholarly (Peer Reviewed) Journals with publishing dates on or after November 2019. Databases queried include Academic Search Complete, CINAHL, eBook Academic Collection (EBSCOhost), eBook Clinical Collection (EBSCOhost), Health and Psychosocial Instruments, International Pharmaceutical Abstracts, MEDLINE, and Academic Search Ultimate.

Duplicate DOIs should be automatically removed by EBSCO

Raw XML data is scraped and simple results are plotted:

![COVID-19_Publications_per_Day.png](https://github.com/jakesmells/COVID19AcademiaDataset/blob/master/media/COVID-19_Publications_per_Day.png)
![COVID-19_Total_Publications.png](https://raw.githubusercontent.com/jakesmells/COVID19AcademiaDataset/master/media/COVID-19_Total_Publications.png)

COVID-19 case data is retrieved from [JHU's COVID-19 database](https://github.com/CSSEGISandData/COVID-19):

![Total_Global_Confirmed_COVID-19_Cases.png](https://github.com/jakesmells/COVID19AcademiaDataset/blob/master/media/Total_Global_Confirmed_COVID-19_Cases.png)
![Total_COVID-19_Deaths.png](https://github.com/jakesmells/COVID19AcademiaDataset/blob/master/media/Total_COVID-19_Deaths.png)
