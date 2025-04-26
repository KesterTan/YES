# YES
This contains: 
- HTML files that create the [ERD diagram](https://yes-rouge-zeta.vercel.app/) hosted using Vercel.
- A series of scripts which would generate mock data, process and transfer data from a CSV to another so that it can be imported to Airtable. For more information, refer to the [documentation](https://docs.google.com/document/d/1y1g4TY9T2DpEGHrZiUBwMD4rqYo6wuWVB4_pVjbkZRU/edit?usp=sharing).

## Index.html and entityRelationship.html — To generate ERD diagram
Vercel currently reads from `Index.html`. Editing this file would change the ERD diagram on the [site](https://yes-rouge-zeta.vercel.app/). 

## Generate.py — To generate mock CSVs
- Run `pip3 install faker`
- Run `python3 generate.py`

## Transfer.py — To import data from any CSV to Airtable format
Note that if the Airtable schema changes, you would need to change the fields in nodeDataArray for the script to work.

To import a script:
1. Rename the CSV you would like to import to "master.csv" and put it in the root directory of this folder.
2. Create a directory named "test", all JSON files would be created there. Note that a JSON file would be created for each table in nodeDataArray.
3. Run `python3 transfer.py`
