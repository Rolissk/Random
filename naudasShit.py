import random, sys, vardata 

def cashOut():
    print('---------')
    while True:
        print('You currently have ' + str(vardata.balance) + ' available.')
        moneyOut = input('How much would you like to cash out? (write a decimal number)')
        if moneyOut.isalpha():
            print('Sorry, that is not a number.')
        elif moneyOut > str(vardata.balance):
            print('Sorry, you do not have that much money.')
            break
        elif moneyOut <= str(vardata.balance):
            vardata.balance = vardata.balance - int(moneyOut)
            print('Thank you for your cash out!')
            print('You have ' + str(vardata.balance) + ' money left.')
            break

def shopMenu():
    print('---------')
    print('Welcome to the prize shop!\n Here you can exchange your money for a prize!')
    shopIzvele = input('If you want to see prizes - (p), or press enter to quit!')
    if shopIzvele == 'p':
        while True:
            for k, v in vardata.shopItems.items():
                print( k +' - '+str(v))
            shopIzvele = input('Would you like to purchase any of the items? (y) or (n)')
            if shopIzvele == 'n':
                break
            elif shopIzvele == 'y':
                koPirkt = input('Which item would you like to purchase? (write the name of the item)\n')
                if koPirkt == 'bear':
                    print('Bear costs 20 coins')
                    pirktIzvele = input('Would you like to buy it? (y) or (n)')
                    if pirktIzvele == 'y':
                        vardata.balance = vardata.balance - 20
                        vardata.shopItems['bear'] = vardata.shopItems['bear'] - 1
                        vardata.inventoryItems.setdefault('bear', 0)
                        if 'bear' in vardata.inventoryItems.keys():
                            vardata.inventoryItems['bear'] += 1
                    else:
                        break
                elif koPirkt == 'bow and arrow':
                    print('Bow and arrow costs 30 coins')
                    pirktIzvele = input('Would you like to buy it? (y) or (n)')
                    if pirktIzvele == 'y':
                        vardata.balance = vardata.balance - 30
                        vardata.shopItems['bow and arrow'] = vardata.shopItems['bow and arrow'] - 1
                        vardata.inventoryItems.setdefault('bow and arrow', 0)
                        if 'bow and arrow' in vardata.inventoryItems.keys():
                            vardata.inventoryItems['bow and arrow'] += 1
                    else:
                        break
                elif koPirkt == 'toy car':
                    print('Toy car costs 50 coins')
                    pirktIzvele = input('Would you like to buy it? (y) or (n)')
                    if pirktIzvele == 'y':
                        vardata.balance = vardata.balance - 20
                        vardata.shopItems['toy car'] = vardata.shopItems['toy car'] - 1
                        vardata.inventoryItems.setdefault('toy car', 0)
                        if 'toy car' in vardata.inventoryItems.keys():
                            vardata.inventoryItems['toy car'] += 1
                    else:
                        break
                

def inventory():
    print('---------\nInventory:')
    for k, v in vardata.inventoryItems.items():
        print(str(v) + ' ' + str(k))
    print('---------')