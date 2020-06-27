# -*- coding: utf-8 -*-

COVID = {
    "covid": "https://brasil.io/dataset/covid19/caso?format=csv",
    "ibge": "https://raw.githubusercontent.com/sandeco/CanalSandeco/master/covid-19/cidades_brasil.csv",
    "recovered": "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-total.csv",
    "geojson": "https://raw.githubusercontent.com/fititnt/gis-dataset-brasil/master/mesorregiao/geojson/mesorregiao.json",
}

ECONOMIC = {
    "dolar": "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='01-01-2019'&@dataFinalCotacao='{}-{}-{}'&$top=10000&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao".format(
        "12", "06", "2020"
    ),
    "ipcaa": "http://api.bcb.gov.br/dados/serie/bcdata.sgs.1635/dados?formato=json",  # 1635
    "inpca": "http://api.bcb.gov.br/dados/serie/bcdata.sgs.1644/dados?formato=json",
    "inpcg": "http://api.bcb.gov.br/dados/serie/bcdata.sgs.188/dados?formato=json",
    "ipcag": "http://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json",
    "inad": "http://api.bcb.gov.br/dados/serie/bcdata.sgs.21084/dados?formato=json",
    "dsoc": "http://api.bcb.gov.br/dados/serie/bcdata.sgs.24369/dados?formato=json",
    "npd": "http://api.bcb.gov.br/dados/serie/bcdata.sgs.24380/dados?formato=json",
    "npo": "http://api.bcb.gov.br/dados/serie/bcdata.sgs.24379/dados?formato=json",
}
