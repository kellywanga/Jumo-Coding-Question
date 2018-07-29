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

MSISDN,Network,Date,Product,Amount
27729554427,'Network 1','12-Mar-2016','Loan Product 1',1000.00
27722342551,'Network 2','16-Mar-2016','Loan Product 1',1122.00
27725544272,'Network 3','17-Mar-2016','Loan Product 2',2084.00
27725326345,'Network 1','18-Mar-2016','Loan Product 2',3098.00
27729234533,'Network 2','01-Apr-2016','Loan Product 1',5671.00
27723453455,'Network 3','12-Apr-2016','Loan Product 3',1928.00
27725678534,'Network 2','15-Apr-2016','Loan Product 3',1747.00
27729554427,'Network 1','16-Apr-2016','Loan Product 2',1801.00
