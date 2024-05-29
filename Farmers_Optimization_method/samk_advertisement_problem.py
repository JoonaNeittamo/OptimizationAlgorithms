from pulp import *
import time as t

# "VISUALIZE" HOW LONG IT TAKES FOR THE CODE TO COMPLETE
start = t.time()


# CREATE THE OPTIMIZATION METHOD WHICH IN THIS CASE IS FARMERS OPTIMIZATION
lp = LpProblem("Farmers Optimization", LpMaximize)

# DEFINE WHAT THE METHODS ARE AND HOW MANY ADS YOU CAN RUN PER WEEK
TV_spots = LpVariable("TV_spots", 0, 12, cat='Integer')
Newspaper_ads = LpVariable("Newspaper_ads", 0, 5, cat='Integer')
Prime_radio = LpVariable("Prime_radio", 0, 25, cat='Integer')
Afternoon_radio = LpVariable("Afternoon_radio", 0, 20, cat='Integer')

# DEFINE WHAT AUDIENCE REACHED MEANS FOR THE PULP
lp += 5000*TV_spots + 8500*Newspaper_ads + 2400*Prime_radio + 2800*Afternoon_radio, "Total Audience Reached"

# CONSTRAINTS FOR THE MEDIUMS WITH COST PER AD ETC
lp += 800*TV_spots + 925*Newspaper_ads + 290*Prime_radio + 380*Afternoon_radio <= 8000, "Budget"
lp += Prime_radio + Afternoon_radio >= 5, "Min radio spots"
lp += 290*Prime_radio + 380*Afternoon_radio <= 1800, "Radio budget"

# LP.SOLVE IS FUNCTION FROM PULP THAT IS USED TO SOLVE THE SOMETHING THAT YOU WANT (so in this case "lp")
status = lp.solve()

# OPTIMIZATION (which you can ignore) AND THE BEST USE FOR MONEY WITH BUDGET OF 8000
variables = {
    "Optimization status": LpStatus[status],
    "TV Spots": TV_spots.varValue,
    "Newspaper Ads": Newspaper_ads.varValue,
    "Prime Radio Spots": Prime_radio.varValue,
    "Afternoon Radio Spots": Afternoon_radio.varValue,
    "Total Audience Reached": value(lp.objective)
}
for var_name, var_value in variables.items():
    print(f"{var_name}: {var_value}")
end = t.time()
print("TIME:", (end - start))