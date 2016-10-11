# sift-nlp
Natural language processing service of the Sift app

## Setup instructions for siftnlp module

### Ensure you have virtualenv installed, which installs pip, on your local machine

#### Ubuntu
`sudo apt-get install virtualenv`
#### RHEL/CentOS
`sudo yum install virtualenv`
#### OSX
`brew install virtualenv`
#### Windows
`Download installer (?)`

### Initiate virtual environment dir, activate it, and go!
```bash
virtualenv venv
source ./venv/bin/activate
make init
```

### Setup.py

Alternatively all these instructions are automated (for \*nix systems) in `setup.sh`. After installing virtualenv as instructed above, run in your `sift-nlp` directory as such:
```bash
chmod +x setup.sh
./setup.sh
```
