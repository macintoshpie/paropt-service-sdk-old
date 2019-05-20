## TLDR
Simple cli/sdk for making http requests to a paropt-service.

## Setup
1. Create a virtual environment with python 3.7, activate the env
2. `pip install requests`
3. `git clone git@github.com:macintoshpie/paropt-service-sdk.git`
4. Make sure paropt-service is running, see [repo](https://github.com/macintoshpie/paropt-service) for details. If making calls to a prod service, you'll also need to:
    * Login to service in browser (e.g. https://myservice.com/login)
    * Grab session cookie, you'll need it to make auth'd requests

## Usage
API wrappers are located in `service.py`. `runner.py` provides a simple cli/example for using the wrappers.
Use flag `-h` for help and info about flags you can use.
```bash
./runner.py -h
```
Here's an example for making calls to a paropt-service at `https://myexampleservice.com`.
```
./runner.py --experiment ./experiments/s3_example.yaml \
            --optimizer ./optimizers/bayesopt.yaml \
            --maxwait 10 \
            --cookie <session_cookie> \
            --domain myexampleservice.com
```

## Examples
See `/experiments` and `/optimizers` for example files use. These are intended to be *examples* for you to modify to fit your needs. Do not expect them to work by default.
