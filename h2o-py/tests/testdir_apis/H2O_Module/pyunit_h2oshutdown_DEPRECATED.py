from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import threading


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

def h2oshutdown():
    """
    h2o.shutdown(prompt=False)
    Deprecated, use h2o.cluster().shutdown()

    Testing the h2o.cluster_status() command here.

    :return: none if test passes or error message otherwise
    """
    thread = threading.Thread(target=call_shutdown)
    thread.daemon =True

    try:
        thread.start()
        thread.join(1.0)
    except Exception as e:
        assert False, "h2o.shutdown() command is not working."

def call_shutdown():
    h2o.shutdown(prompt=True)   # call shutdown but do not actually shut anything down.

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oshutdown)
else:
    h2oshutdown()
