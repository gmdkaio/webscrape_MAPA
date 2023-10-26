import chromedriver_autoinstaller, urllib3, time
from selenium import webdriver
from links_array import links
from bs4 import BeautifulSoup


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

data_list = []

def scrape_page(scrap_url):
  data_dict = {}

  # Acess the page with selenium and ignore ssl
  chromedriver_autoinstaller.install()
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument("--ignore-certificate-errors")
  chrome_options.add_argument("--ignore-ssl-errors")
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(scrap_url)
  time.sleep(3)
  page_source = driver.page_source
  driver.quit()

  # Get page w/ bs4
  soup = BeautifulSoup(page_source, 'html.parser')

  # Data gathering

  # SIF
  sif_tag = soup.find('input', {'name': 'nr_sif'})
  sif_value = sif_tag['value'] if sif_tag else None

  if sif_value:
    data_dict['SIF'] = sif_value
  else: 
    sif_value = None


  # Processo
  processo_tag = soup.find('input', {'name': 'nr_processo'})
  processo_value = processo_tag['value'] if processo_tag else None

  if processo_value:
    data_dict['Processo'] = processo_value
  else:
    processo_value = None


  # Razão
  razao_tag = soup.find('input', {'name': 'nm_razao_social'})
  razao_value = razao_tag['value'] if razao_tag else None

  if razao_value:
    data_dict['Razão Social'] = razao_value
  else:
    razao_value = None

  # Fantasia
  fantasia_tag = soup.find('input', {'name': 'nm_fantasia'})
  fantasia_value = fantasia_tag['value'] if fantasia_tag else None

  if fantasia_value:
    data_dict['Fantasia'] = fantasia_value
  else:
    fantasia_value = None

  # Situação
  situacao_tag = soup.find('input', {'name': 'nm_razao_social'})
  situacao_value = situacao_tag['value'] if situacao_tag else None

  if situacao_value:
    data_dict['Situação'] = situacao_value
  else:
    situacao_value = None

  # CNPJ
  cnpj_tag = soup.find('input', {'name': 'nr_cnpj'})
  cnpj_value = cnpj_tag['value'] if cnpj_tag else None

  if cnpj_value:
    data_dict['CNPJ'] = cnpj_value
  else:
    cnpj_value = None


  # Data Reserva
  dtReserva_tag = soup.find('input', {'name': 'dt_reserva'})
  dtReserva_value = dtReserva_tag['value'] if dtReserva_tag else None

  if dtReserva_value:
    data_dict['Data Reserva'] = dtReserva_value
  else:
    dtReserva_value = None

  # Data registro
  dtRegistro_tag = soup.find('input', {'name': 'dt_registro'})
  dtRegistro_value = dtRegistro_tag['value'] if dtRegistro_tag else None

  if dtRegistro_value:
    data_dict['Data Registro'] = dtRegistro_value
  else:
    dtRegistro_value = None

  # Logradouro 
  logradouro_tag = soup.find('input', {'name': 'tx_logradouro'})
  logradouro_value = logradouro_tag['value'] if logradouro_tag else None

  if logradouro_value:
    data_dict['Logradouro'] = logradouro_value
  else:     
    logradouro_value = None


  # Bairro
  bairro_tag = soup.find('input', {'name': 'nm_bairro'})
  bairro_value = bairro_tag['value'] if bairro_tag else None

  if bairro_value:
    data_dict['Bairro'] = bairro_value
  else: 
    bairro_value = None


  # Cidade
  cidade_tag = soup.find('input', {'name': 'nm_municipio'})
  cidade_value = cidade_tag['value'] if cidade_tag else None

  if cidade_value:
    data_dict['Cidade'] = cidade_value
  else:
    cidade_value = None


  # Cep
  cep_tag = soup.find('input', {'name': 'nr_cep'})
  cep_value = cep_tag['value'] if cep_tag else None

  if cep_value:
    data_dict['CEP'] = cep_value
  else:
    cep_value = None


  # Estado
  estado_tag = soup.find('input', {'name': 'sg_uf'})
  estado_value = estado_tag['value'] if estado_tag else None

  if estado_value: 
    data_dict['Estado'] = estado_value
  else:  
    estado_value = None

  # Telefone
  telefone_tag = soup.find('input', {'name': 'nr_telefone'})
  telefone_value = telefone_tag['value'] if telefone_tag else None

  if telefone_value:
    data_dict['Telefone'] = telefone_value
  else:
    telefone_value = None

  # Fax
  fax_tag = soup.find('input', {'name': 'nr_fax'})
  fax_value = fax_tag['value'] if fax_tag else None

  if fax_value:
    data_dict['Fax'] = fax_value
  else:
    fax_value = None


  # Email
  email_tag = soup.find_all('a', href=lambda x: x and x.startswith('mailto:'))
  email_value = email_tag[0].get_text().strip() if email_tag else None

  if email_value:
    data_dict['Email'] = email_value
  else: 
    email_value = None


  # Site
  site_tag = soup.find('input', {'name': 'tx_site'})
  site_value = site_tag['value'] if site_tag else None

  if site_value:
    data_dict['Site'] = site_value
  else:
    site_value = None


  # Area de produção
  area_tags = soup.find_all('input', {'name': 'nm_area'})
  area_values = []

  for tag in area_tags:
      area_value = tag.get('value', None)
      if area_value:
          area_values.append(area_value)

  if area_values:
      area_values_str = ', '.join(area_values)
      data_dict['Descricao'] = area_values_str
  else:
      area_value = None


  # Descrição
  descricao_tags = soup.find_all('input', {'name': 'ds_classe_estab'})
  descricao_values = []

  for tag in descricao_tags:
      descricao_value = tag.get('value', None)
      if descricao_value:
          descricao_values.append(descricao_value)

  if descricao_values:
      descricao_values_str = ', '.join(descricao_values)
      data_dict['Descricao'] = descricao_values_str
  else:
      descricao_value = None

  data_list.append(data_dict)


for url in links:
  scrape_page(url)



    

