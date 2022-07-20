hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Prices and Cuts
#total price calculation
total_price = 0

for price in prices:
  total_price += price
print(f"Total earnings: {total_price}$")

#calculate ava price 
avarage_price = total_price // len(prices) #sets down result as int not float
print(f"Avarage Haircut Price: {avarage_price}$")

#Creating new_prices with 5 $ cut to each
new_prices = [price - 5 for price in prices]
print(f"New prices: {new_prices}")

#Revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print(f"Total Revenue: {total_revenue}$")

#calculating avg daily revenue
avarage_daily_revenue = total_revenue // 7
print(f"Daily avarage revenue: {avarage_daily_revenue}$")

#Get cuts under 30$
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if prices[i] < 30]
print(cuts_under_30)
