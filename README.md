# Agent Based Modeling for meme propagation in a social network

### Prerequisites
* First, set up a virtual environment with a recent Python version. We tested this application only on version `3.11.1`, but others should work.
* Install all necessary 3rd-party requirements with `pip install -r requirements.txt`.

### Usage instructions
To run the simulation as shown in our paper, simply execute `python main.py`.

### Additional configuration
Simulation parameters are set in the `Config` class in `config.py`. To run the simulation with different parameters than set as default, re-use the code snippets in `main.py:main()` with your custom `Config` object.
By default, our simulation runs based off a SIR model. However, in `models.py`, we do have the groundwork for other simulation model types, namely *Cascades* and *Forest Fire*. These can be substituted in with moderate additional configuration.