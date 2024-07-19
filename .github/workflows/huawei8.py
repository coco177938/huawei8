name: Visit URL and Notify Telegram every 30 minutes

on:
  schedule:
    - cron: "*/60 * * * *"
  workflow_dispatch:

jobs:
  visit-and-notify:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install requests

    - name: Run script
      run: python huawei8.py
