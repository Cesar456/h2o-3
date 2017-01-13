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

def h2oparse_raw():
    """
    h2o.parse_raw(setup, id=None, first_line_is_header=0)

    Testing the h2o.parse_raw() command here.  Don't think the users should be using this one...
    copied from pyunit_hexdev_29_parse_false.py

    :return: none if test passes or error message otherwise
    """
    try:
        fraw = h2o.import_file(pyunit_utils.locate("smalldata/jira/hexdev_29.csv"), parse=False)
        assert isinstance(fraw, list)

        fhex = h2o.parse_raw(h2o.parse_setup(fraw), id='hexdev_29.hex', first_line_is_header=0)
        fhex.summary()
        pyunit_utils.verify_return_type("h2o.parse_raw()", "H2OFrame", fhex.__class__.__name__)
    except Exception as e:
        assert False, "h2o.parse_raw() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oparse_raw)
else:
    h2oparse_raw()
