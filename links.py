import urllib3, csv, requests
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

fst_url = "https://extranet.agricultura.gov.br/sigsif_cons/!ap_estabelec_nacional_cons"
scd_url = "https://extranet.agricultura.gov.br/sigsif_cons/!ap_estabelec_nacional_lista"
post_data = {'nr_sif': '','nm_razao_social':'','nr_cnpj':'','nm_sort':'nr_sif','script_body':'onload=','p_tipo_consulta':''}
numero_proximo = 15
csv_filename = 'links_csv.csv'

session = requests.Session()

response=requests.get(fst_url, verify=False)
array_links = []


if response.status_code == 200:
    # Analisar o conteúdo da página com o Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')
    cookies = session.cookies

# print('Entrou na pagina')

post_response = session.post(scd_url, data=post_data, verify=False)

while True:
    if post_response.status_code == 200:
        
        post_soup = BeautifulSoup(post_response.text, 'html.parser')
        links = post_soup.find_all('a') 
        
        #Coleta os valores dos botões de proximo e anteior e o value da função do botao proximo para jogar no link da proxima pagina na requisição
        next_button = post_soup.find('input', {'name':'proximo'})
        back_button = post_soup.find('input', {'value':'Anterior'})
        print ('--------------início da página -------------')
        print(numero_proximo)

    # define os dados para enviar na proxima requisição Post
        post_list_data = {'nr_cnpj': '','nm_razao_social':'','nr_sif':'','nm_sort':'nr_sif','p_tipo_consulta':'','p_linha_inicial':numero_proximo}
    
        
    #coleta todos os links da pagina e joga para uma array
        for link in links:
            relative_path = link.get('href')
            link_url = f'https://extranet.agricultura.gov.br/sigsif_cons/{relative_path}'
            
            if link_url not in array_links:             
                print(link_url)
                array_links.append(link_url)

        if next_button is not None:
            post_response = session.post(scd_url, post_list_data, verify=False)
            numero_proximo += 15
            
        else:
            break
        print(numero_proximo)
        print('----------------------FIM DA PAGINA----------------------------')
    else:
        print('falha em acessar a segunda pagina')


with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Links para os cadastros'])

    for link in array_links:
        csv_writer.writerow([link])

print('arquivos baixados com sucesso')