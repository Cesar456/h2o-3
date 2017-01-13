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

def h2oget_frame():
    """
    h2o.get_frame(frame_id)

    Testing the h2o.get_frame() command here.

    :return: none if test passes or error message otherwise
    """
    try:
        frame1 = h2o.import_file(pyunit_utils.locate("smalldata/jira/hexdev_29.csv"))
        frame2 = h2o.get_frame(frame1.frame_id)
        pyunit_utils.verify_return_type("h2o.get_frame()", "H2OFrame", frame2.__class__.__name__)
    except Exception as e:
        assert False, "h2o.get_frame() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oget_frame)
else:
    h2oget_frame()
