# Reproducible failure injection.
def service_failure_fixture(name):
    scenarios={"none":frozenset(),"budget":frozenset({"verify-budget"}),"schedule":frozenset({"schedule-setup"})}
    if name not in scenarios: raise ValueError("unknown fixture")
    return scenarios[name]