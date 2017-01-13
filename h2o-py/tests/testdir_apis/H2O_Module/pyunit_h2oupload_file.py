from __future__ import print_function
from builtins import str
from builtins import range
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import urllib.parse
from h2o.estimators.glm import H2OGeneralizedLinearEstimator

# DISCLAMINER
#
# The main function of API tests is to make sure that changes to the API are captured
# before the customers do.  This is to prevent breaking the customer code.  If the
# changes are necessary, we will have the chance to warn them about the changes.
#
# All API tests should be short and fast to run.  The main purposes of API tests are to
# make sure that the command in its most popular forms run correctly when user types in
# correct input arguments.  Light weight checking will be provided on the command output
# to make sure that we are getting the correct responses.
#
# For exhaustive tests using all possible combination of input arguments, making sure all
# responses of the API commands are correct, or if in error, the correct error messages
# are sent should be done elsewhere.

def h2oupload_file():
    """
    h2o.upload_file(path, destination_frame=None, header=0, sep=None, col_names=None, col_types=None, na_strings=None)
    Note: if you want to change the column names that are going to be different from the ones in your file, you
    must do it after you parse in the file.  Setting header=1 but setting col_names different from the column names
    in the file will result reading in the column names as data.  Since the column names may not be the right column
    type, it will be counted as NAs.

    Testing the h2o.upload_file() command here.

    :return: none if test passes or error message otherwise
    """
    try:
        col_types=['enum','numeric','enum','enum','enum','numeric','numeric','numeric']
        col_headers = ["CAPSULE","AGE","RACE","DPROS","DCAPS","PSA","VOL","GLEASON"]
        hex_key = "training_data.hex"
        training_data = h2o.upload_file(pyunit_utils.locate("smalldata/prostate/prostate_cat.csv"),
                                        destination_frame=hex_key, header=1, sep = ',',
                                        col_names=col_headers, col_types=col_types, na_strings=["NA"])
        pyunit_utils.verify_return_type("h2o.upload_file()", "H2OFrame", training_data.__class__.__name__)
        assert training_data.frame_id == hex_key, "frame_id was not assigned correctly.  h2o.upload_file() is not" \
                                                  " working."
        assert cmp(training_data.col_names, col_headers)==0, "column names are incorrect.  " \
                                                             "h2o.upload_file() not working."
        assert training_data.nrow==380, "number of rows is incorrect.  h2o.upload_file() is not working."
        assert training_data.ncol==8, "number of columns is incorrect.  h2o.upload_file() is not working."
        assert sum(training_data.nacnt())==3, "NA count is incorrect.  h2o.upload_file() is not working."

    except Exception as e:
        assert False, "h2o.upload_file() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oupload_file)
else:
    h2oupload_file()
