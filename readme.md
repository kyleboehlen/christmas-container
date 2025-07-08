![output-onlinepngtools-5](https://github.com/user-attachments/assets/27756972-4967-4a5e-8038-15b85e6c8d32)

# Christmas Container
This is simply a container with python tooling and boilerplate for participating in Advent of Code
## Usage
You can simply run the docker compose file, develop the files locally as they'll be mounted as a volume, and run the app by calling

`python3 app.py`

from the docker container CLI in `/app`

You'll need to add your input to the correct `./input/{day}.txt` file and write your solution in the corresponding `./scripts/{day}.py file`
