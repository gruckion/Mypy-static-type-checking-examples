This includes a set of reference examples of [mypy](http://mypy-lang.org/examples.html) static type checking
for python.

### Building

To build the project I recommend [Mini Conda](https://docs.conda.io/en/latest/miniconda.html) as it allows you to create isolated environments for managing your packages.

Creating a new environmenet to manage your python packages.
`conda create --name myenv anaconda python=3`

Installing required packages into your new enviorment.
`conda install --nae myenv --yes --file requirements.txt`

For all other packages use
`conda install --name myenv numpy`

Click here for more on managing packages in [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html)

[.gitignore](https://github.com/github/gitignore/blob/master/Python.gitignore)
