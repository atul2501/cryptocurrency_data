api=' ' #get this api from coingecho
final=pd.DataFrame()

for j in range(1,172):
    response=requests.get(f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page={j}&sparkline=false&x_cg_demo_api_key={api}').json()

    high_24h=[]
    name=[]
    current_price=[]
    market_cap_rank=[]
    low_24h=[]
    total_supply=[]
    circulating_supply=[]
    fully_diluted_valuation=[]
    
    for i in response:
        name.append(i['name'])
        current_price.append(round(i['current_price'],8))
        market_cap_rank.append(i['market_cap_rank'])
        high_24h.append(i['high_24h'])
        low_24h.append(i['low_24h'])
        circulating_supply.append(i['circulating_supply'])
        total_supply.append(i['total_supply'])
        fully_diluted_valuation.append(i['fully_diluted_valuation'])
    
        d={'market_cap_rank':market_cap_rank,'name':name,'current_price':current_price,'high_24h':high_24h,'low_24h':low_24h,'total_supply':total_supply,'circulating_supply':circulating_supply,'fully_diluted_valuation':fully_diluted_valuation}
        df=pd.DataFrame(d)

        final.drop_duplicates(subset=['market_cap_rank', 'name'], inplace=True)
    

        #final = pd.concat([final, df], ignore_index=True)
        final=pd.concat([final,df],ignore_index=True)
        
    
