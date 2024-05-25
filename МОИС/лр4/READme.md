#  Take umbrella agent

Is an agent that generates recommendation to take umbrella or not depending on weather in the city, associates with the original relation "nrel_recommendation_for_user"

**Action class:**

`action_get_recommendation`


**Parameters:**

1. `linkAddr` -- sc-link with user message text;
2. `dialogAddr` -- dialog node, an element of `concept_dialogue`.

Also there is the `author` of the message.

**Workflow:**

* The agent connects to the selected API service and receives weather data in degrees and information about rain/sun, identifying the author
of the action as the user, and the city in which the user is located as the user's location;
* Then the necessary construction is generated to call the agent of non-atomic action interpretation. An example of this construction is shown below.

<img src="../interpretation.png"></img>

* The agent waits until the interpretation agent finishes its work. Then searches for the set of rules that should have been generated during the interpretation
agent's work and uses it to generate relation between the user and object from a set of recommendations, which includes to_take_umbrella_recommendation and
not_to_take_umbrella_recommendation.

### Example

Example of an input structure:

<img src="../input.png"></img>

Example of an output structure:

<img src="../output.png"></img>

### Result

Possible result codes:
 
* `SC_RESULT_OK` - need to take umbrella;
* `SC_RESULT_ERROR`- there is no need in umbrella.
