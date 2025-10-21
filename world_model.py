Have an idea to create physical world model (laws of diff kinds of science, rules) that can learn one area or many phyical (environment) areas in a NN model. 

One of the option is to add additional modality to output of a gpt-model.

Examples:

Q: Why can camels survive for long without water?	

A: Camels use the fat in their humps to keep them filled with energy and hydration for long periods of time.

Input for the model is the question.

Output can be a list of words such a Camels, humps, fat, energy, hydration, etc.

But they should be related in such a way so we understand the point what is where.

Q:Alice's parents have three daughters: Amy, Jessy, and what’s the name of the third daughter?

A: The name of the third daughter is Alice

Here when model ouput the answer it can be "hidden knowledge"

List of concepts such as parents -> Amy, Jessy and Alice are the related children.

So, mayne answer can be not "Alice" but the scheme of the family, so the hidden knowledge with what we can work after.

Q: What happens when the sun goes down?	

A: When the sun sets, the evening starts.

Probably here we can output sequence of cocnept with its states, such as locations, light intensity, etc.

Q: WHat is the distance between Sun and Mars

Output can be the scheme with coordinates and conepts

Additional modality can be some kind algorithms learnt in a discrete space of a neural network layers.

It can output a static output or sequence with cocnepts and their attributes, for example concepts with states, one of the options is list of embeddings with states. We can encode embeddings to match with nearest word in a discrete vocab of words, and do same with attributes. But it's unclear how to do this and to do this efficently.

The question is how to create this discrete space layers for different concepts and processes

Their can be sequence and static events, different attributes and world models, such as gravity, moving, or event planet movement which is copmlicated to represent on a simple layers 

I also like this idea

We'll be closer to human-level AI when we have systems that can: - understand the physical world - remember and retrieve appropriately - reason - set sub-goals and plan hierarchically But even once we have systems with such capabilities, it will take a while before we bring them up to human or superhuman level.

but for now I want to train prototype for world models (static or processes world models) which can be used fro planning , cause and effect reasoning , etc

please show me how this can look?

simple dataset mock with

x - text input

y - output structured representation that can be simply added to additiinal modality layer in a gpt model

{

  "concepts": [

    { "name": "camel", "attributes": ["mammal", "desert_adapted"] },

    {

      "name": "hump",

      "attributes": ["fat_storage", "energy_source", "water_source"]

    },

    { "name": "survival", "attributes": ["long_periods", "water_scarcity"] }

  ],

  "relations": [

    { "subject": "camel", "predicate": "has", "object": "hump" },

    { "subject": "hump", "predicate": "stores", "object": "fat" },

    { "subject": "fat", "predicate": "provides", "object": "energy" },

    { "subject": "fat", "predicate": "provides", "object": "hydration" },

    { "subject": "camel", "predicate": "survives", "object": "long_periods" },

    { "subject": "camel", "predicate": "adapts_to", "object": "water_scarcity" }

  ]

}

do you think should i start train model on such data

or to learn this complex thing is un efficient for the start

gpt need to learn transalte hidden state of the input text to

-> extract the relevant concepts, their attributes

-> build the graph with these concepts and also their realtionships

