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

def h2oparse_setup():
    """
    h2o.parse_setup(raw_frames, destination_frame=None, header=0, separator=None, column_names=None, column_types=None,
     na_strings=None)

    Testing the h2o.parse_setup() command here.

    :return: none if test passes or error message otherwise
    """
    try:
        col_types=['enum','numeric','enum','enum','enum','numeric','numeric','numeric']
        col_headers = ["CAPSULE","AGE","RACE","DPROS","DCAPS","PSA","VOL","GLEASON"]
        hex_key = "training_data.hex"

        fraw = h2o.import_file(pyunit_utils.locate("smalldata/prostate/prostate_cat.csv"), parse=False)
        setup = h2o.parse_setup(fraw, destination_frame=hex_key, header=1, separator=',', column_names=col_headers,
                                column_types=col_types, na_strings=["NA"])
        pyunit_utils.verify_return_type("h2o.parse_setup()", "H2OResponse", setup.__class__.__name__)
        assert setup["number_columns"]==len(col_headers), "h2o.parse_setup() command is not working."
    except Exception as e:
        assert False, "h2o.parse_setup() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oparse_setup)
else:
    h2oparse_setup()
