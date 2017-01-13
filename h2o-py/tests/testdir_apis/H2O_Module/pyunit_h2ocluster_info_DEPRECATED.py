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
# make sure that the command in its most popular forms run correctly when user types in
# correct input arguments.  Light weight checking will be provided on the command output
# to make sure that we are getting the correct responses.
#
# For exhaustive tests using all possible combination of input arguments, making sure all
# responses of the API commands are correct, or if in error, the correct error messages
# are sent should be done elsewhere.

def h2ocluster_info():
    """
    h2o.cluster_info()
    Deprecated, use h2o.cluster().show_status().

    Testing the h2o.cluster_info() command here.

    :return: none if test passes or error message otherwise
    """
    try:
        h2o.cluster_info()    # no return type
    except Exception as e:
        assert False, "h2o.cluster_info() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2ocluster_info)
else:
    h2ocluster_info()
