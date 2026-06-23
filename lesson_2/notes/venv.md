# Python Virtual Environments (venv)

## What it is
`venv` creates isolated Python environments so each project can have its own dependencies.

## Optional: central location
You can store environments in one place (not required):

`mkdir ~/.venv`

## Creating an environment
Run this inside your project directory:

`python3 -m venv .venv`

## Activating

macOS / Linux:
`source .venv/bin/activate`

Windows:
`.venv\Scripts\activate`

## Installing packages
Once activated, install dependencies locally:

`pip install <package>`

## Leaving the environment
To deactivate:

`deactivate`

## Full Flow

```
# Set up a virtual environment named `env_a` for Python 3.9
python3.9 -m venv ~/.venv/env_a
source ~/.venv/env_a/bin/activate
```

```
python3 -m venv .venv
source .venv/bin/activate
pip install requests
deactivate
```
