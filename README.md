# Jumo-Coding-Question

## Situation

Every two months a text file is given from the accounting department
detailing all the loans given out on the networks.
This needs to be a validated against the internal systems by the tuple
of (Network, Product, Month).

## Project

Given the below CSV from the accounting department, this package
calculates the aggregate of loans by the tuple of
(Network, Product, Month) with the total currency amounts and counts
and outputs into a CSV file Output.csv

## Loans.csv

```
MSISDN,Network,Date,Product,Amount
27729554427,'Network 1','12-Mar-2016','Loan Product 1',1000.00
27722342551,'Network 2','16-Mar-2016','Loan Product 1',1122.00
27725544272,'Network 3','17-Mar-2016','Loan Product 2',2084.00
27725326345,'Network 1','18-Mar-2016','Loan Product 2',3098.00
27729234533,'Network 2','01-Apr-2016','Loan Product 1',5671.00
27723453455,'Network 3','12-Apr-2016','Loan Product 3',1928.00
27725678534,'Network 2','15-Apr-2016','Loan Product 3',1747.00
27729554427,'Network 1','16-Apr-2016','Loan Product 2',1801.00
```

## Assumptions

* The csv file to be provided is consistent ie have same number of columns and
  have same type of data.

* The dates in the csv file to be provided are only for two months.

## Running the Project

### Requirements

- Git
- Python3

### Download the Project

Clone the repository into a directory of your own choice.

`git clone https://github.com/SamwelOpiyo/Jumo-Coding-Question.git`

`cd Jumo-Coding-Question`

### Running locally

Run Tests

`python setup.py test`

Install Project

`pip install -e .`

Create logs, input and output directories eg

`mkdir /Jumo/logs/ /Jumo/outputs/ /Jumo/inputs`

Copy input files to input directory

`cp inputs/ /Jumo/inputs/`

Set environment variables

`export LOGS_DIRECTORY="/Jumo/logs/"`

`export INPUTS_DIRECTORY="/Jumo/inputs/"`

`export OUTPUTS_DIRECTORY="/Jumo/outputs/"`

Run project

`jumo_coding_question`

Check the outputs directory to view the csv file generated, Ouput.csv.

For the csv file above, the output data will be:
```
Count,Aggregated Amount,Product,Network,Month
1,1000.0,Loan Product 1,Network 1,Mar
1,1122.0,Loan Product 1,Network 2,Mar
2,5182.0,Loan Product 2,Network 3,Mar
1,5671.0,Loan Product 1,Network 2,Apr
1,1928.0,Loan Product 3,Network 3,Apr
1,1747.0,Loan Product 3,Network 2,Apr
1,1801.0,Loan Product 2,Network 1,Apr
```
