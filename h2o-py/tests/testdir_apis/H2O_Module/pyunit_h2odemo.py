from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o

# DISCLAMINER
#
# The main function of API tests is to make sure that changes to the API are captured
# before the customers do.  This is to prevent breaking the customer code.  If the
# changes are necessary, we will have the chance to warn them about the changes.
#
# All API tests should be short and fast to run.  The main purposes of API tests are to
# make sure that the command in its most popular forms, run correctly when user types in
# correct input arguments.  Light weight checking will be provided on the command output
# to make sure that we are getting the correct responses.
#
# For exhaustive tests using all possible combination of input arguments, making sure all
# responses of the API commands are correct, or if in error, the correct error messages
# are sent should be done elsewhere.

def h2odemo():
    """
    h2o.demo(funcname, interactive=True, echo=True, test=False)[source]

    Testing the h2o.demo() command here.  Copied from pyunit_glm_demo.py

    :return: none if test passes or error message otherwise
    """

    try:
        h2o.demo(funcname="glm", interactive=False, echo=True, test=True)
    except Exception as e:
        assert False, "h2o.demo() command not is working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2odemo)
else:
    h2odemo()
