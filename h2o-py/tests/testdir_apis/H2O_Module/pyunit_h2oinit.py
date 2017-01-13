from __future__ import print_function
from builtins import str
from builtins import range
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

def h2oinit():
    """
    h2o.init(url=None, ip=None, port=None, https=None, insecure=None, username=None, password=None, cluster_id=None,
    cookies=None, proxy=None, start_h2o=True, nthreads=-1, ice_root=None, enable_assertions=True, max_mem_size=None,
    min_mem_size=None, strict_version_check=None, **kwargs)

    Testing the h2o.init() command here.

    :return: none if test passes or error message otherwise
    """
    # call with no arguments
    print("Testing h2o.init() command...")
    try:
        h2o.init()
        print("h2o.init() command works!")
    except Exception as e:  # some errors are okay like version mismatch
        pyunit_utils.verify_return_type("h2o.init()", "H2OConnectionError", e.__class__.__name__)

    try:
        h2o.init(strict_version_check=False)
    except Exception as e:
        assert False, "h2o.init(strict_version_check) command is not working."

    # try to join a cluster and test out various command arguments
    ipS = "127.0.0.1"
    portS = "54321"
    nthread = 2
    max_mem_size=10
    min_mem_size=3
    strict_version_check = False
    start_h2o = False

    try:
        h2o.init(ip=ipS, port=portS, nthreads=nthread, max_mem_size=max_mem_size, min_mem_size=min_mem_size,
                 start_h2o=start_h2o, strict_version_check=strict_version_check)
        print("Command h2o.init(ip=ipS, port=portS, nthreads=nthread, max_mem_size=max_mem_size, "
              "min_mem_size=min_mem_size,start_h2o=start_h2o, strict_version_check=strict_version_check) works!")
    except Exception as e:  # make sure correct error message is received
        assert "H2OConnectionError: Unexpected HTTP error:" in e.args[0], \
            "h2o.init(ip=ipS, port=portS, nthreads=nthread, max_mem_size=max_mem_size, min_mem_size=min_mem_size," \
            "start_h2o=start_h2o, strict_version_check=strict_version_check) command is not working"

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oinit)
else:
    h2oinit()
