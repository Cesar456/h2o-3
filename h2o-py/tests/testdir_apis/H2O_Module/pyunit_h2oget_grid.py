from __future__ import print_function
from builtins import str
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
from h2o.grid.grid_search import H2OGridSearch
from h2o.estimators.gbm import H2OGradientBoostingEstimator

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

def h2oget_grid():
    """
    h2o.get_grid(grid_id)

    Testing the h2o.get_grid() command here.  Copy from pyunit_gbm_random_grid.py

    :return: none if test passes or error message otherwise
    """
    try:
        air_hex = h2o.import_file(path=pyunit_utils.locate("smalldata/airlines/allyears2k_headers.zip"), destination_frame="air.hex")
        myX = ["DayofMonth","DayOfWeek"]

        hyper_parameters = {
            'learn_rate':[0.1,0.2],
            'max_depth':[2,3],
            'ntrees':[5,10]
        }

        search_crit = {'strategy': "RandomDiscrete",
                       'max_models': 5,
                       'seed' : 1234,
                       'stopping_rounds' : 3,
                       'stopping_metric' : "AUTO",
                       'stopping_tolerance': 1e-2
                       }

        air_grid = H2OGridSearch(H2OGradientBoostingEstimator, hyper_params=hyper_parameters, search_criteria=search_crit)
        air_grid.train(x=myX, y="IsDepDelayed", training_frame=air_hex, distribution="bernoulli")

        fetched_grid = h2o.get_grid(str(air_grid.grid_id))
        pyunit_utils.verify_return_type('h2o.get_grid', 'H2OGridSearch', fetched_grid.__class__.__name__)
        assert(len(air_grid.get_grid())==5)
        assert (len(air_grid.get_grid())==len(fetched_grid.get_grid())), "h2o.get_grid() is command not working."
    except Exception as e:
        assert False, "h2o.get_grid() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oget_grid)
else:
    h2oget_grid()
