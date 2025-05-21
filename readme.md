![output-onlinepngtools-5](https://github.com/user-attachments/assets/27756972-4967-4a5e-8038-15b85e6c8d32)

# Christmas Container
This is simply a container with python tooling and boilerplate for participating in Advent of Code
## Usage
You can simply run the docker compose file, develop the files locally as they'll be mounted as a volume, and run the app by calling

`python3 app.py`

from the docker container CLI in `/app`

You'll need to add your input to the correct `./input/{day}.txt` file and write your solution in the corresponding `./scripts/{day}.py file`

### Using Friday?

If you're using Friday you can:
- Run a command to clone and instantiate the project for you
- Use your session cookie to import all of your inputs automatically
- Run the application through Friday as a proxy to automatically pass the day instead of inputting it on script start

For more information run
`./friday.sh aoc --help`
