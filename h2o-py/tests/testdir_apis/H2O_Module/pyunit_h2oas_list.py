from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import random

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

def h2oas_list():
    """
    h2o.as_list(data, use_pandas=True, header=True)

    Testing the h2o.as_list() command here.  Copied from pyunit_frame_as_list.py

    :return: none if test passes or error message otherwise
    """

    try:
        iris = h2o.import_file(path=pyunit_utils.locate("smalldata/iris/iris_wheader.csv"))

        res1 = h2o.as_list(iris, use_pandas=False)
        return_type = "list"
        pyunit_utils.verify_return_type('h2o.as_list()', "list", res1.__class__.__name__)
        res1 = list(zip(*res1))
        assert abs(float(res1[0][9]) - 4.4) < 1e-10 and abs(float(res1[1][9]) - 2.9) < 1e-10 and \
           abs(float(res1[2][9]) - 1.4) < 1e-10, "incorrect values"
    except Exception as e:
        assert False, "h2o.as_list() command not is working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oas_list)
else:
    h2oas_list()
