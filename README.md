# Full Stack Flask Tutorial

Follows LinkedIn Learning's "Full Stack Web Development with Flask" to create
a Flask project, set up a database system using Flask-MongoEngine, work with
web forms, integrate Flask-Security, and create and test REST APIs using
Postman.

## Getting Set Up

Please see [the setup documentation](SETUP.md) regarding this.

## Folder and File Structure

* [.github/workflows](.github/workflows) - Holds the GitHub Actions files that enables
  CI/CD software workflows
* [.vscode](.vscode) - Holds the Visual Studio Code settings for this project
* [application](application) - Holds the application specific code for this project
* [mongo-setup](mongo-setup) - Holds the files needed to populate our mongodb instance
* [.flake8](.flake8) - Configuration file for the flake8 Python linter
* [.flaskenv](.flaskenv) - Defines some parameters that Flask needs to run
* [.gitignore](.gitignore) - Defines the files/folders to ignore in this repository
* [.markdownlint.rb](.markdownlint.rb) - Configuration file for the pre-commit markdown
  linter
* [.markdownlint.yaml](.markdownlint.rb) - Configuration file for the GitHub Actions
  markdown linter
* [.pre-commit-config.yaml](.pre-commit-config.yaml) - Defines the linting plugins that
  run before any commit. See [SETUP.md](SETUP.md)
* [config.py](config.py) - Defines the configurations for the server
* [LICENSE](LICENSE) - Licensing file
* [main.py](main.py) - Calls the application's entrypoint
* [requirements.txt](requirements.txt) - Pip package requirements for enabling
  developers to contribute. See [SETUP.md](SETUP.md)
* [SETUP.md](SETUP.md) - Setup instructions for contributors
