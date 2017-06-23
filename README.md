# udata-explorer

> Query and explore datasets hosted on a [udata][udata] instance.

## Features

Work In Progress. Supported now:

- search datasets (no pagination)
- explorer datasets attributes and resources
- for CSV resources, load data into a Panda dataframe

## Install

```bash
git clone https://github.com/opendatateam/udata-explorer.git
cd udata-explorer
python3 -m venv pyenv
. pyenv/bin/activate
pip install -e .
```

## Example usage

Launch the [example Jupyter notebook](https://github.com/opendatateam/udata-explorer/blob/master/udata-explorer-example.ipynb) to see the tool in action.

```bash
pip install jupyter[notebook]
jupyter-notebook udata-explorer-example.ipynb
```

[udata]: https://github.com/opendatateam/udata
