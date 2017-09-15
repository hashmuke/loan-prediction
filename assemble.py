#!/usr/bin/python
""" A script to assemble all the data files into 2 files one for Acquisition the
    other for Performance.

    Date: 13/09/2017

"""
import os
import settings
import pandas as pd

# data columns were updated when I downloaded the dataset hence there is
# some change on the header list
HEADERS = {
    "Acquisition": [
        "id",
        "channel",
        "seller",
        "interest_rate",
        "balance",
        "loan_term",
        "origination_date",
        "first_payment_date",
        "ltv",
        "cltv",
        "borrower_count",
        "dti",
        "borrower_credit_score",
        "first_time_homebuyer",
        "loan_purpose",
        "property_type",
        "unit_count",
        "occupancy_status",
        "property_state",
        "zip",
        "insurance_percentage",
        "product_type",
        "co_borrower_credit_score",
        "mortgage_insurance_type",
        "relocation_mortgage_indicator"
    ],
    "Performance": [
        "id",
        "reporting_period",
        "servicer_name",
        "interest_rate",
        "balance",
        "loan_age",
        "months_to_maturity",
        "adjusted_remaining_months",
        "maturity_date",
        "msa",
        "delinquency_status",
        "modification_flag",
        "zero_balance_code",
        "zero_balance_date",
        "last_paid_installment_date",
        "foreclosure_date",
        "disposition_date",
        "foreclosure_costs",
        "property_repair_costs",
        "recovery_costs",
        "misc_costs",
        "tax_costs",
        "sale_proceeds",
        "credit_enhancement_proceeds",
        "repurchase_proceeds",
        "other_foreclosure_proceeds",
        "non_interest_bearing_balance",
        "principal_forgiveness_balance",
        "repurchase_make_whole_proceeds",
        "foreclosure_principal_writeoff",
        "serving_activity_indicator"
    ]
}

# keep only the following columns
SELECT = {
    "Acquisition": HEADERS["Acquisition"],
    "Performance": [
        "id",
        "foreclosure_date"
    ]
}


def concatenate(prefix="Acquisition"):
    files = os.listdir(settings.DATA_DIR)

    # after first run input files are removed hence no change on output
    if files:
        output_filename = \
            os.path.join(settings.PROCESSED_DIR, "{}.txt".format(prefix))

        # files are too big hence append each file to the
        # output as you read them
        with open(output_filename, 'a') as out_f:
            is_first_file = True
            for c_file in files:
                if not c_file.startswith(prefix):
                    continue
                input_filename = os.path.join(settings.DATA_DIR, c_file)

                # Load only those required column from the input data-frame
                usecols_index = [HEADERS[prefix].index(x)
                                 for x in SELECT[prefix]]
                data = pd.read_csv(input_filename, sep="|", header=None,
                                   usecols=usecols_index,
                                   names=HEADERS[prefix], index_col=False)

                # write current data frame to a file
                print("Writing data from {} to {} ".format(input_filename,
                                                           output_filename))
                if is_first_file:
                    data.to_csv(out_f, sep="|", header=SELECT[prefix],
                                index=False)
                    is_first_file = False
                else:
                    data.to_csv(out_f, sep="|", header=False, index=False)
                del data


if __name__ == "__main__":
    # concatenate("Acquisition")
    concatenate("Performance")