print("Detailed report")
cheese_roq_ingridient = "Cheese Roquefort"
cheese_roq_weight = "2.0 kg"
cheese_roq_price = 12.50 * 2
currency = "zl"
cheese_stilton_ingridient = "Cheese Stilton"
cheese_stilton_weight = "1.0 kg"
cheese_stilton_price = 11.24
currency = "zl"
cheese_brie_ingridient = "Cheese Brie"
cheese_brie_weight = "1.0 kg"
cheese_brie_price = 9.30
currency = "zl"
cheese_gauda_ingridient = "Cheese Gauda"
cheese_gauda_weight = "1.0 kg"
cheese_gauda_price = 8.55
currency = "zl"
cheese_edam_ingridient = "Cheese Edam"
cheese_edam_weight = "1.0 kg"
cheese_edam_price = 11.00
currency = "zl"
cheese_parm_ingridient = "Cheese Parmesan"
cheese_parm_weight = "3.5 kg"
cheese_parm_price = 16.50 * 3.5
currency = "zl"
cheese_mozz_ingridient = "Cheese Mozzarella"
cheese_mozzarella_weight = "0.13 kg"
cheese_mozzarella_price = 14.00 * 0.13
currency = "zl"
cheese_slov_ingridient = "Slovak sheep's milk cheese"
cheese_slovak_weight = "0.22 kg"
cheese_slovak_price = 122.32 * 0.22
currency = "zl"
mint_ingridient = "Mint"
mint_weight = "0.2 kg"
mint_price = 20
currency = "zl"
detailed_report = f"{cheese_roq_ingridient} = {cheese_roq_weight}, {cheese_roq_price} {currency},                                 {cheese_stilton_ingridient} = {cheese_stilton_weight} {cheese_stilton_price} {currency},                                   {cheese_brie_ingridient} = {cheese_brie_weight}, {cheese_brie_price} {currency},                                       {cheese_gauda_ingridient} = {cheese_gauda_weight}, {cheese_gauda_price} {currency},                                     {cheese_edam_ingridient} = {cheese_edam_weight}, {cheese_edam_price} {currency},                                      {cheese_parm_ingridient} = {cheese_parm_weight}, {cheese_parm_price} {currency},                                 {cheese_mozz_ingridient} = {cheese_mozzarella_weight}, {cheese_mozzarella_price} {currency},                               {cheese_slov_ingridient} = {cheese_slovak_weight}, {cheese_slovak_price} {currency},                   {mint_ingridient} = {mint_weight}, {mint_price} {currency}"
print(detailed_report)
print("Total_cost")
print(cheese_roq_price + cheese_stilton_price + cheese_brie_price + cheese_gauda_price + cheese_edam_price + cheese_parm_price + cheese_mozzarella_price + cheese_slovak_price)