"""Calculates the exaxt value of any NFT over any period of time!"""

def bought():
    nft_bought = input("How much did you buy your NFT for? (Whole number, no currency symbol): \n")
    if nft_bought.isdigit():
        return int(nft_bought)
    else:
        print("Whole numbers only please, and no currencies. ")
        return bought()

def years():
    nft_years = input("How many years do you plan on holding your NFT for? \n")
    if nft_years.isdigit():
        return int(nft_years)
    else:
        print("Number of years can be integers-only. ")
        return years()

def increase():
    nft_inc = input("Shrewd! What annual % increase do you expect your NFT will increase by? \n")
    if nft_inc.isdigit():
        return int(nft_inc)
    else:
        print("Just a whole number please. ")
        return increase()

def currency():
    nft_curr = input("\nWhat currency did you pay for your NFT with? \n")
    return nft_curr.upper()
    
def calc_increase(a,c):
    decimal_c = 1+(c/100)
    a = (a*decimal_c)
    return a
        
def calc_returns(a,b,c):
    listo = []
    listo.append(a)
    for i in range(b-1):
        a = calc_increase(a,c)
        listo.append(a)
    return listo

def facts(a,d,e):
    print()
    for index, i in enumerate(e):
        print("Your hoped-for investment value in year {}: {:.2f}{}!".format(index+1, i, d))
        print("Your hoped-for profits in year {}: {:.2f}{}!\n".format(index+1,i-a,d))
    print()
    for index, i in enumerate(e):
        print("The ACTUAL value of your NFT in year {}: {:.2f}{}.".format(index+1, i*0,d))
        print("Your ACTUAL profits in year {}: {:.2f}{}\n".format(index+1,((i*0)-a),d))
    print("\nNFTs are, of course, worth NOTHING.\n")
            
def main():
    nft_bought = bought()
    nft_years = years()
    nft_inc = increase()
    nft_curr = currency()
    inc_yield = calc_returns(nft_bought, nft_years, nft_inc)
    facts(nft_bought, nft_curr, inc_yield)

if __name__ == "__main__":
    main()
