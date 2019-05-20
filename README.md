## TLDR
Simple cli/sdk for making http requests to a paropt-service.

## Setup
1. Create a virtual environment with python 3.7, activate the env
2. `pip install requests`
3. `git clone git@github.com:macintoshpie/paropt-service-sdk.git`

## Usage
API wrappers are located in `service.py`. `runner.py` provides a simple cli/example for using the wrappers.
Use flag `-h` for help and info about flags you can use.
```bash
./runner.py -h
```
Here's an example for making calls to a paropt-service at `https://myservice.com:8080`. Currently the service doesn't use API tokens, so you just have to use your browser to login and grab the session cookie it gives you.
```
./runner.py --experiment ./experiments/s3_example.yaml \
            --optimizer ./optimizers/bayesopt.yaml \
            --maxwait 10 \
            --cookie <session_cookie> \
            --domain myservice.com
```

## Examples
See `/experiments` and `/optimizers` for example files use. These are intended to be *examples* for you to modify to fit your needs. Do not expect them to work by default.
