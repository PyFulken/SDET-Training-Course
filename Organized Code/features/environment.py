"""
BEHAVE HOOKS:
They work much like XSetUp / XTeardown
They are functions that are called to be run before/after step/scenario/etc

Variables created during the steps can be accessed by the AFTER_X functions via the context.varname way.
Simmilarly, steps can access variables created by BEFORE_X functions via the context.varname.

before_step(context, step), after_step(context, step)
    These run before and after every step.

before_scenario(context, scenario), after_scenario(context, scenario)
    These run before and after each scenario is run.

before_feature(context, feature), after_feature(context, feature)
    These run before and after each feature file is exercised.

before_tag(context, tag), after_tag(context, tag)
    These run before and after a section tagged with the given name. They are invoked for each tag encountered in the order they’re found in the feature file.

before_all(context), after_all(context)
    These run before and after the whole shooting match. 

"""

def after_feature(context, scenario):
    print("------------------------------------------------------------------------------------------------------------------------------")
    print(f"The payload created during the scenario was {context.payload}")
    print("------------------------------------------------------------------------------------------------------------------------------")