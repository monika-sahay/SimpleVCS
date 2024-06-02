# SimpleVCS

SimpleVCS is a minimalistic version control system implemented in Python, designed to demonstrate the fundamental concepts of version control. It features basic repository initialization, file snapshotting using content-addressable storage, and commit logging.

### Features

- **Repository Initialization:** Create a new version control repository.
- **Committing Changes:** Save the current state of the directory with a commit message.
- **Logging Commits:** View a history of commits with messages and timestamps.

### Usage

#### Initialize a Repository
```sh
python simplevcs.py init /path/to/repo
```

#### Commit Changes
```sh
python simplevcs.py commit /path/to/repo "Initial commit"
```

#### View Commit Logs
```sh
python simplevcs.py log /path/to/repo
```

### Installation

Clone the repository:
```sh
git clone https://github.com/monika-sahay/simplevcs.git
cd simplevcs
```

### License

This project is licensed under the MIT License.

