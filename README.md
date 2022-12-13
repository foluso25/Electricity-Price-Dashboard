# MA705 Final Project

The final dashboard is deployed on Heroku [here](https://electricity-dash.herokuapp.com/).

## Dashboard Description
The electricity data used in this dashboard is from the U.S Energy 
Information Administration, and it consists of total sales(consumption),
revenues generated, prices and customers of electricity in each 
sector across different states from 2010 - 2021.
The purpose of this dashboard is to visualize how the price of electricity has changed 
overtime across all the states in the United States of America

### Data Sources
The data set was downloaded from the U.S Energy
Information Administration website, the data set consist of the following columns:
- Year, State, Customers, Electricity price, Revenue and Sales

The data was in excel format, and each column in the data set had a sub-column. 
As a result, the columns in the dataset were cleaned appropriately using Pandas,
and the resulting dataframe was stored in the CSV file titled 'mo_final_project' 

- The U.S Energy Information Administration Electricity
data set can be found [here](https://www.eia.gov/electricity/data.php)

### Other Comments
The following includes key definitions of some terms in the dataset:
######
- **Residential Sector** means an energy-consuming sector that consists of living 
quarters for private households. Common uses of energy associated with this
sector include space heating, water heating, air conditioning, lighting, 
refrigeration, cooking, and running a variety of other appliances. 
The residential sector excludes institutional living quarters.

- **Commercial Sector** means an energy-consuming sector that consists of 
service-providing facilities and equipment of businesses; Federal, State,
and local governments; and other private and public organizations, such as religious, social, 
or fraternal groups. The commercial sector includes institutional living quarters. It also includes 
sewage treatment facilities. Common uses of energy associated with this sector include space heating
, water heating, air conditioning, lighting, refrigeration, cooking, and running a wide variety 
of other equipment.
- **Industrial Sector** means an energy-consuming sector that consists of all facilities and equipment 
used for producing, processing, or assembling goods. The industrial sector encompasses the 
following types of activity: manufacturing; agriculture, forestry, fishing and hunting; mining,
including oil and gas extraction; and construction. Overall energy use in this sector is largely 
for process heat and cooling and powering machinery, with lesser amounts used for facility heating, 
air conditioning, and lighting.
- **Transportation Sector** means an energy-consuming sector that consists of all vehicles 
whose primary purpose is transporting people and/or goods from one physical location to another. 
Included are automobiles; trucks; buses; motorcycles; trains, subways, and other rail vehicles; 
aircraft; and ships, barges, and other waterborne vehicles. Vehicles whose primary purpose is not 
transportation (e.g., construction cranes and bulldozers, farming vehicles, and warehouse tractors 
and forklifts) are classified in the sector of their primary use
