# Blog

Creating a blog with Libano

To start, create a Virtual Enviroment. The following things must be set up:

- Python:3.8
- Django:3.2

# Linux

## Setting up an virtual enviroment and pip

To create a virtual enviroment in python, install pip:

**Note: If you already setted the virtual enviroment up, go to the last command of this section**

### Debian based distros (Debian, Ubuntu, Mint, Elementary, Pop)

Install pip (Python's package manager).  
On Mint's app manager, search for python3-pip and install it.  
In other distros, or Mint's rerminal, use:

```bash
sudo apt-get install python3-pip
```
***
Now, install virtualenv on pip:

```bash
python3 -m pip install virtualenv
```

With these, create a virtual enviroment with any name in any folder you want, Ex:

```bash
mkdir ./virtualEnviroments 
cd ./virtualEnviroments
python3 -m virtualenv blog # You can change "blog", if you want :D
```

To start the virtual enviroment (You will do this a lot), use:

```bash
source ~/path/to/your/venv/bin/activate
```

After that your terminal will look something like this:

```bash
(blog) user@os-name:~/path/to/repo
```

To finish it, you'll need to install the packages on the "requirements.txt" file with pip:

```bash
python3 -m pip install -r requirements.txt
```
# Running it

On the terminal, using the virtual enviroment, use:

```bash
python3 manage.py runserver
```

Now, on a web browser, you should be able to open the site on localhost's port 8000: *localhost:8000*

**Currently, a blank url will result in an error, to get to somewhere, use /posts or /admin at the end of localhost:8000**
