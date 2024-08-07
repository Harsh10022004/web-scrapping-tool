from bs4 import BeautifulSoup
import requests

# user_agent = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 10.1; Win64; x64; en-US) AppleWebKit/534.49 (KHTML, like Gecko) Chrome/53.0.1211.186 Safari/533.2 Edge/14.75257'}

user_agent = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0', 
                          'Accept-Language':'en-US,en;q=0.5',
                          'Sec-Fetch-Dest':'document',
                          'Sec-Fetch-Mode':'navigate',
                          'Sec-Fetch-Site':'same-origin',
                          'Sec-Fetch-User':'?1',
                          'Upgrade-Insecure-Requests':'1'
              }

def amazon_scrap(url):
    # url = input("Enter the URL: ")


    html_text = requests.get(url, headers = user_agent).text
    soup = BeautifulSoup(html_text, 'lxml')




    product_name = soup.find('span', class_='a-size-large product-title-word-break').text.replace(' ','')

    product_price = soup.find('span', class_='a-price-whole').text.replace(' ','')

    product_source = "amazon"

    print(f'''PRODUCT NAME : {product_name}''')
    print(f'''PRODUCT PRICING : {product_price}''')
    print(f'''PRODUCT WEBSITE SOURCE : {product_source}''')


def flipkart_scrap(url):

    html_text = requests.get(url, headers = user_agent).text
    soup = BeautifulSoup(html_text, 'lxml')

    product_name = soup.find('span', class_='B_NuCI').text.replace(' ','')
    
    product_price = soup.find('div', class_='_30jeq3 _16Jk6d').text.replace(' ','')

    product_source = "flipkart"

    print(f'''PRODUCT NAME IN URL2 : {product_name}''')
    print(f'''PRODUCT PRICING IN URL2 : {product_price}''')
    print(f'''PRODUCT WEBSITE SOURCE IN URL2 : {product_source}''')


# url_amazon = input("Enter URL of Amazon Product: ")
url_amazon = input("Enter the URL FOR AMAZON: ")
url_flipkart = input("Enter the URL FOR FLIPKART: ")
print("GET THE DETAILS OF PRODUCT FROM WEBSITE 1")
amazon_scrap(url_amazon)
print("--------------------------------------------------------------------------------------------------")
print("GET THE DETAILS OF PRODUCT FROM WEBSITE 2")
flipkart_scrap(url_flipkart)



