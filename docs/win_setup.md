
 *in progress--but should approximately work*

## Setup Instructions For Windows

* Requires Python >=3.6

#### 1: CD into desired directory

    cd C:\\Path\\To\\project\\dir

#### 2a: Clone github repository & enter username and password

    git clone https://github.com/davidmnoll/gltrader


#### 3: CD into repository directory####

    cd gltrader

#### 4a: If pip & virtualenv installed skip to 5, else install/upgrade pip:

    python -m pip install --upgrade pip wheel setuptools

#### 4b: Then install virtualenv

    python -m pip install virtualenv

### 4c: As well as virtualenv wrapper for windows shell

    python -m pip install virtualenvwrapper-powershell

#### 4e: install windows python api wrappers

    python -m pip pywin32 pypiwin32

#### 5: Set up Virtual Environment:

    python3 -m venv venv

#### 6: Activate Virtual Environment

    venv\\Scripts\\activate

#### 7: Install requirements

    python -m pip install -r requirements.txt

#### 8: Install Kivy Dependencies *https://kivy.org/docs/installation/installation-windows.html*

    python -m pip install Cython==0.27.2

    python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew

#### 9: Install Kivy

    python -m pip install kivy

#### 10: Add keys to config.json

*Copy config-sample.json file to config.json, open in text editor, and replace keys with bittrex API keys*


## To Run:

#### 1: CD into base directory of install

    cd C:\\Path\\To\\project\\dir\\gltrader

#### 2: Activate venv

    venv\\Scripts\\activate

#### 3: Run Module

    python -m gltrader

## To Run Tests:

#### 1: CD into base directory of install

    cd C:\\Path\\To\\project\\dir\\gltrader

#### 2: Activate venv

    venv\\Scripts\\activate

#### 3: Run test command

    python -m nosetests
