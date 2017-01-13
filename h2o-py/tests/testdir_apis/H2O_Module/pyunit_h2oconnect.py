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

def h2oconnect():
    """
    h2o.connect(server=None, url=None, ip=None, port=None, https=None, verify_ssl_certificates=None, auth=None,
    proxy=None, cluster_id=None, cookies=None, verbose=True)

    Testing the h2o.connect() command here.  I will call this command in the most popular way.  Goal here is not
    to extensively test this command here but rather to make sure it has not changed in a way that it will fail with
    old code version.

    :return: none if test passes or error message otherwise
    """
    ipA = "127.0.0.1"
    portN = "54321"
    urlS = "http://127.0.0.1:54321"
    return_type = "H2OConnection"

    try:
        connect_type=h2o.connect(ip = ipA, port = portN, verbose = True)
        pyunit_utils.verify_return_type("h2o.connect()", return_type, connect_type.__class__.__name__)
    except Exception as e:  # port number may not match.  Make sure the right error message is returned
        assert "Could not establish link to H2O cloud" in e.args[0], "h2o.connect command is not working."

    try:
        connect_type2 = h2o.connect(url=urlS, https=True, verbose = True)     # pass if no connection issue
        pyunit_utils.verify_return_type("h2o.connect()", return_type, connect_type2.__class__.__name__)
    except Exception as e:  # port number may not match.  Make sure the right error message is returned
        assert "Could not establish link to H2O cloud" in e.args[0], "h2o.connect command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oconnect)
else:
    h2oconnect()
