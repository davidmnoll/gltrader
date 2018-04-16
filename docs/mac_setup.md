### *in progress*


## Setup Instructions For Mac

* Requires Python >=3.6

#### 1: CD into desired directory

    cd /path/to/project/dir

#### 2: Clone github repository & enter username and password

    git clone https://github.com/davidmnoll/gltrader


#### 3: CD into repository directory

    cd gltrader

#### 4a: If pip & virtualenv installed skip to 5, else install/upgrade pip:

    python -m pip install --upgrade pip wheel setuptools

#### 4b: Then install virtualenv

    python -m pip install virtualenv


#### 5: Set up Virtual Environment:

    python3 -m venv venv

#### 6: Activate Virtual Environment

    venv/bin/activate

#### 7: Install requirements

    pip install -r requirements.txt

#### 8: Install Kivy Dependencies *https://kivy.org/docs/installation/installation-osx.html*

    pip install Cython==0.27.2

    pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew

#### 9: Install Kivy

    pip install https://github.com/kivy/kivy/archive/master.zip

#### 10: Add keys to config.json

*Copy config-sample.json file to config.json, open in text editor, and replace keys with bittrex API keys*


## To Run:

#### 1: CD into base directory of install

    cd /path/to/project/dir/gltrader

#### 2: Activate venv

    source venv/bin/activate

#### 3: Run Module

    python -m gltrader

## To Run Tests:

#### 1: CD into base directory of install

    cd /path/to/project/dir/gltrader

#### 2: Activate venv

    source venv/bin/activate

#### 3: Run test command

    nosetests
