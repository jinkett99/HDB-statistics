Repository Structure:
Repository/
├── README.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   └── ...
├── data/
│   ├── raw/
│   ├── processed/
│   └── ...
├── models/
│   ├── trained_model.pkl
│   ├── model_evaluation_report.txt
│   └── ...
├── notebooks/
│   ├── exploratory_analysis.ipynb
│   ├── model_training.ipynb
│   └── ...
└── .gitignore

Summary: 
- Include functions to call in "src" folder
- Raw datasets should be in "data/raw"
- Output/Processed datasets should be in "data/processed"

Project Brainstorm - Datasets for statistical reasoning

1. sales_cleaned.csv: Generic dataset on HDB sales (1000 records, 2019)
- Variables: 'floor_category', 'yearmon', 'sales_date', 'flat_lease_status', 'floor', 'project_name', 'area_sqft', 'unit_price_psf', 'type_of_sale', 'property_type', 'completion_status', 'postal_district', 'planning_region', 'planning_area'.

2. MedianRentByTownAndFlatType.csv: Median rent information by town & flat-type (12k records, 2005-2022)
- Variables: 'quarter', 'town', 'flat_type', 'median_rent'

3. HDBPropertyInformation.csv: Historical information on developed HDB flats including several indicators, sales & rental information (12k records, 1930-2024)
- Variables: blk_no, street, max_floor_lvl, year_completed, residential, commercial, market_hawker, miscellaneous, multistorey_carpark, precinct_pavilion, bldg_contract_town, total_dwelling_units, 1room_sold, 2room_sold, 3room_sold, 4room_sold, 5room_sold, exec_sold, multigen_sold, studio_apartment_sold, 1room_rental, 2room_rental, 3room_rental, other_room_rental

4. 1_average-household-income_by_flat_type: Average HH income by flat type (24 records, 2000-2023)
- Variables: Year, HDB 1- & 2- Room Flats1/, HDB 3-Room Flats, HDB 4-Room Flats, HDB 5-Room & Executive Flats, Condominiums & Other Apartments, Landed Properties

### NEW (Private Property Market)
5. Private Property Rental Index (2004-2024)

6. Private Property Transactions by (1) Type of sale & (2) Sale status (completed vs uncompleted units)

7. Singapore Condominium Rentals (2018-2022)

8. Singapore Private Property Transactions (2018-2022)

Notes from Prof: 
-	Use-case important. Who are we serving? Locals/foreigners? Foreigners for rental data?
-	Dig deeper!
-	Focus on getting hypothesis, key questions, use-case! 
-	Dataset is rich, we can potentially do a lot of things with it.
-	Exploratory & Statistical analysis instead of predictive modelling! 
-	Evidence-based reasoning with KEY findings. Future work can be prediction (:

Proposals: 
JK: Explore Real Estate Information System (REALIS) datasets
https://www.ura.gov.sg/-/media/Corporate/Property/REALIS/User%20Guide/REALIS_eBrochure.pdf
https://data.gov.sg/datasets?agencies=Urban+Redevelopment+Authority+(URA)&page=1&query=private&resultId=d_8e4c50283fb7052a391dfb746a05c853
- Time-series Database
- Transactions Database
- Rental Database
- Developers' Sales Database
- Project Database
- Stock Database
JK: List out potential underlying reasons that influence prices of private residential properties. Investigate. 

Use-case/Value proposition: 
- Increase in Rental Prices for private housing in SG, affecting Locals, Foreigners (Students & Work Permit Holders etc.)
- Increased demand for private rental properties for different groups? *Research for evidence.
- #RESEARCH: What are the underlying reasons behind the increase in demand (and rental prices) for private residential properties?? Does demand for private rental properties come solely from foreigners, or locals as well.
- Our group intends to integrate REALIS datasets from different databases to answer important questions & to address concerns of our intended users: Locals/Foreigners looking to rent a private property in SG. For example, reasons for rental price increases, considerations before renting a private property in SG (too vague), for real estate agents to understand the market better & to make better propositions etc.

Key Questions (for project direction):
1. Are trends in rental prices closely tied to property sale price?
https://youtu.be/hLhrLxN1C_s?si=6Mnsfp-8lsKrTNnB
*Might want to focus on “in-demand” rental properties like those for couples waiting for BTO, foreigners etc.

2. What categories of private property rentals consist of? Eg. No. Of bedrooms, whole unit rentals etc.
3. What are in-demand types of rental properties in SG?
4. Does economic indicators play a role in affecting rental demand? If so, how?
5. Does type of permits/income trends (of foreigners & locals) have an impact on rental demand?
