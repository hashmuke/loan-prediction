# Machine learning on Fannie Mae

This is a continuation from a machine learning work demonstrated by Vik
Paruchuri [here](https://www.dataquest.io/blog/data-science-portfolio-machine-learning/).
The task require the use of Fannie Mae dataset for training a machine learning
algorithm to predict the performance of a given loan after purchased by Fannie
Mae. The original work can be downloaded from his
[github account](https://github.com/dataquestio/loan-prediction). Due to the
limitation on my computer memory as well as an update on the dataset structure,
I have made the following changes to the original procedure provided by Vik.

## 1. Further reduction on memory demand

The notion of reducing memory demand was discuss throughout the work of Vik, yet
it wasn't complete. Some of the Performance data file are as big as 2GB and most
of the fields in this file are not used for this application. Hence the idea of
loading every field and then extracting the required fields in `assemble.py` is
unnecesary when panda can do the extraction while loading the the data using
`usecols` argument.

An other improvement is avoiding accumulation of data-frames in a list while
loading data from multiple sources in `assemble.py`. In stead, after each
reading the result can be writen to the file without waiting for the subsequent
input files. The improvement from this may not be as important as the previous
suggestion yet it makes sense.

## 2. Update related to change in the dataset

It has been more than a year since the original post. Now the structure for
Fannie Mae dataset is updated with new fields both in Acquisition and
Performance files. This can be seen from the
[layout file](https://loanperformancedata.fanniemae.com/lppub-docs/lppub_file_layout.pdf).
At the time of doing this test the new columns are as follow;

*Acquisition files:*
Append the following two field types to `HEADER` list

    24. mortgage_insurance_type
    25. relocation_mortgage_indicator

*Performance files:*
Add the following three fields to `HEADER` list in the right order

    8. adjusted_remaining_months
    29. repurchase_make_whole_proceeds
    30. foreclosure_principal_writeoff
    31. serving_activity_indicator

These new fields in Performance files are among excluded columns, however the
one Acquisition files can play part in the Machine learning training. This will
require changing the categorical data type under `relocation_mortgage_indicator`
using `annotate.py`. Just add  the field name into column iteration list of
`annotate` method.

## 3. Demonstrating Effect of change in procedure