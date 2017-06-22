# udata-explorer

> Query and explore datasets hosted on a [udata][udata] instance.

# Install

```bash
pip install udata-explorer
```

# Overview

Import the `Explorer` and connect to a [udata][udata] API endpoint.

```python
from udata_explorer import Explorer, CSVResource, CSVDetective
explorer = Explorer(endpoint = 'https://data.gouv.fr/api/1/')
```

Query datasets.

```python
results = explorer.get_datasets(q='élections legislatives 2017')
print(results)
[<DataSet>("Elections législatives 1958-2012 by Sciences Po"), <DataSet>("Résultats de l'intégralité des élections depuis 2001 by Ministère de l'Intérieur"), ...]
```

Select the one you want to explore.

```python
dataset = results[0]
print(dataset.resources)
[<ZipResource>("Tous les jeux de données de 1958 à 2012 au format XLS en une archive"), <CSVResource>("Résultats des législatives par circonscription 1958 1er tour (23 novembre 1958)"), ...]
```

Resources can be filtered based on their type. CSV can be cleaned with [CSV Detective][csv-detective] for example.

```python
resource = dataset.get_resources(type = CSVResource).first
data = resource.get_data()
cleaned_data = CSVDetective(data)
```

[Pandas dataframe][dataframe] are awesome to process data.

```
print(data.head())
   Code département département  circonscription  Inscrits  Votants  Exprimés
0               NaN         NaN              NaN       NaN      NaN       NaN
1               1.0         AIN              1.0   67589.0  43001.0   42157.0
2               1.0         AIN              2.0   68089.0  47763.0   46939.0
3               1.0         AIN              3.0   62731.0  43019.0   42109.0
4               2.0       AISNE              1.0   52760.0  43066.0   42025.0
```

# In a Jupyter Notebook

TBD.

[udata]: https://github.com/opendatateam/udata
[csv-detective]: https://github.com/etalab/csv_detective
[dataframe]: pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
