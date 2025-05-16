# pkr-automation-fwk
Framework assist to create a new automation fwk which includes all the basic ingredients needed to run a suite end to end

# api_automation locally

1. Install Python 3.12
   * See the official [Python downloads page](https://www.python.org/downloads/)
   
   * Or install it on OSX using brew: `brew install python@3.12`
   * After installation, confirm `python3 --version` reports Python 3.12 or newer version is installed.
     If not, restart your Terminal application.

2. Clone the repository: `https://github.com/techpkr/pkr-automation-fwk.git'
3. `cd pkr-automation-fwk`
4. Setup Virtual Environment
   * `/opt/homebrew/bin/python3.12 -m venv venv`  or `python3 -m venv venv`
   * `source venv/bin/activate`
   * `pip install --upgrade pip`
   * `pip install -r requirements.txt`
5. Set up the environment variables if added in fwk 
    * `export LOGIN_NAME=""`
    * `export PASSWORD=""`
6. Run script to test it out
   * `pytest` [Modify configs in code as this is just template to get started with]
   * or execute scripts with custom configurations
   * `pytest -k -p -h [custom args] `

7. Added container support [can build , run inside the specified env]
8. For Slack integration create app and create a webhook url [https://api.slack.com/apps ]
9. Added BDD (Gherking syntax) support as well [Given , When , Then]
10. Added cronjob support 