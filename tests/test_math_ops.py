name: Python Automation Pipeline

# What triggers this pipeline?
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

# What actions should it take?
jobs:
  run-tests:
    runs-on: ubuntu-latest # Uses a fresh Linux server hosted by GitHub

    steps:
    - name: Pull code from GitHub repository
      uses: actions/checkout@v4

    - name: Install Python on the server
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install pytest dependency
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Execute pytest validation
      env:
        PYTHONPATH: .
      run: |
        pytest
